# Copyright 2017 Red Hat
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import base64
import hmac
import itertools

from oslo_log import log

from keystone.common import password_hashers
from keystone.common.password_hashers import bcrypt
from keystone.common.password_hashers import pbkdf2
from keystone.common.password_hashers import scrypt
import keystone.conf
from keystone import exception
from keystone.i18n import _

CONF = keystone.conf.CONF
LOG = log.getLogger(__name__)

SUPPORTED_HASHERS: frozenset[type[password_hashers.PasswordHasher]] = (
    frozenset(
        [scrypt.Scrypt, bcrypt.Bcrypt, bcrypt.Bcrypt_sha256, pbkdf2.Sha512]
    )
)

_HASHER_NAME_MAP = {hasher.name: hasher for hasher in SUPPORTED_HASHERS}


# NOTE(notmorgan): Build the list of prefixes. This comprehension builds
# a dictionary where the keys are the prefix (all hashedpasswords are
# '$<ident>$<metadata>$<hash>') so we can do a fast-lookup on the hasher to
# use. If has hasher has multiple ident options it is encoded in the
# .ident_values attribute whereas hashers that have a single option
# ( ) only has the .ident attribute.
# NOTE(noonedeadpunk): Though bcrypt_sha256 does define <ident> as part of
# the metadata, actual indent is represented with a <prefix> instead.
def _get_hash_ident(hashers):
    for hasher in hashers:
        if hasattr(hasher, 'prefix'):
            ident = (getattr(hasher, 'prefix'),)
        elif hasattr(hasher, 'ident_values'):
            ident = getattr(hasher, 'ident_values')
        else:
            ident = (getattr(hasher, 'ident'),)
        yield (hasher, ident)


_HASHER_IDENT_MAP = {
    prefix: module
    for module, prefix in itertools.chain(
        *[
            zip([mod] * len(ident), ident)
            for mod, ident in _get_hash_ident(SUPPORTED_HASHERS)
        ]
    )
}


def _get_hasher_from_ident(hashed):
    try:
        return _HASHER_IDENT_MAP[hashed[0 : hashed.index('$', 1) + 1]]
    except KeyError:
        raise ValueError(
            _('Unsupported password hashing algorithm ident: %s')
            % hashed[0 : hashed.index('$', 1) + 1]
        )


def verify_length_and_trunc_password(password) -> bytes:
    """Verify and truncate the provided password to the max_password_length.

    We also need to check that the configured password hashing algorithm does
    not silently truncate the password.  For example, passlib.hash.bcrypt does
    this:
    https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt.html#security-issues

    """
    # When using bcrypt, we limit the password length to 54 to ensure all
    # bytes are fully mixed. See:
    # https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt.html#security-issues
    BCRYPT_MAX_LENGTH = 72
    if (
        CONF.identity.password_hash_algorithm == 'bcrypt'  # nosec: B105
        and CONF.identity.max_password_length > BCRYPT_MAX_LENGTH
    ):
        msg = (
            "Truncating password to algorithm specific maximum length %d"
            " characters."
        )
        LOG.warning(msg, BCRYPT_MAX_LENGTH)
        max_length = BCRYPT_MAX_LENGTH
    else:
        max_length = CONF.identity.max_password_length

    try:
        password_utf8 = password.encode('utf-8')
        if len(password_utf8) > max_length:
            if CONF.strict_password_check:
                raise exception.PasswordVerificationError(size=max_length)
            else:
                msg = "Truncating user password to %d characters."
                LOG.warning(msg, max_length)
                return password_utf8[:max_length]
        else:
            return password_utf8
    except AttributeError:
        raise exception.ValidationError(attribute='string', target='password')


def check_password(password: str, hashed: str) -> bool:
    """Check that a plaintext password matches hashed.

    hashpw returns the salt value concatenated with the actual hash value.
    It extracts the actual salt if this value is then passed as the salt.

    """
    if password is None or hashed is None:
        return False
    password_utf8 = verify_length_and_trunc_password(password)
    hasher = _get_hasher_from_ident(hashed)
    return hasher.verify(password_utf8, hashed)


def hash_user_password(user):
    """Hash a user dict's password without modifying the passed-in dict."""
    password = user.get('password')
    if password is None:
        return user

    return dict(user, password=hash_password(password))


def hash_password(password: str) -> str:
    """Hash a password. Harder."""
    params = {}
    password_utf8 = verify_length_and_trunc_password(password)
    conf_hasher = CONF.identity.password_hash_algorithm
    hasher = _HASHER_NAME_MAP.get(conf_hasher)

    if hasher is None:
        raise RuntimeError(
            _('Password Hash Algorithm %s not found')
            % CONF.identity.password_hash_algorithm
        )

    if CONF.identity.password_hash_rounds:
        params['rounds'] = CONF.identity.password_hash_rounds
    if hasher is scrypt.Scrypt:
        params["n"] = 16
        if CONF.identity.scrypt_block_size:
            params["r"] = CONF.identity.scrypt_block_size
        if CONF.identity.scrypt_parallelism:
            params["p"] = CONF.identity.scrypt_parallelism
        if CONF.identity.salt_bytesize:
            params["salt_size"] = CONF.identity.salt_bytesize
        return scrypt.Scrypt.hash(password_utf8, **params)
    elif hasher is bcrypt.Bcrypt:
        return bcrypt.Bcrypt.hash(password_utf8, **params)
    elif hasher is bcrypt.Bcrypt_sha256:
        return bcrypt.Bcrypt_sha256.hash(password_utf8, **params)
    elif hasher is pbkdf2.Sha512:
        if CONF.identity.salt_bytesize:
            params["salt_size"] = CONF.identity.salt_bytesize
        return pbkdf2.Sha512.hash(password_utf8, **params)
    else:
        raise RuntimeError(
            _('Password Hash Algorithm %s not implemented')
            % CONF.identity.password_hash_algorithm
        )


def generate_partial_password_hash(password: str, salt: str) -> str:
    """Generates partial password hash for reporting purposes.

    The generated password hash is base64 encoded, and `max_chars` of it are
    returned.
    """
    secret_key = CONF.security_compliance.invalid_password_hash_secret_key
    if secret_key is None:
        raise RuntimeError(_('Secret Key value has to be provided'))

    hash_function = CONF.security_compliance.invalid_password_hash_function

    salted = hmac.digest(
        key=bytes(salt, "utf-8"),
        msg=bytes(password, "utf-8"),
        digest=hash_function,
    )

    peppered = hmac.digest(
        key=bytes(secret_key, "utf-8"), msg=salted, digest=hash_function
    )

    # encode to utilize more characters to reduce collisions when further
    # truncating
    encoded = base64.b64encode(peppered).decode("utf-8").rstrip("=")

    max_chars = CONF.security_compliance.invalid_password_hash_max_chars
    if max_chars is None:
        return encoded
    return encoded[:max_chars]
