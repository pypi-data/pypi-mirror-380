# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import locale
import bcrypt
import base64
import hashlib
import apr1
import crypt  # deprecated in 3.11 and removed in 3.13.
from hmac import compare_digest as compare_hash

# Reference:    https://httpd.apache.org/docs/2.4/misc/password_encryptions.html
#               https://akkadia.org/drepper/SHA-crypt.txt

# empirical format for htpasswd using apache utils 2.4.41
# md5sum:$apr1$AmfEURVX$U0A7kxYcofNn2J.lptuOn0
# bcrypt:$2y$05$LtdiiELPayMNfwk5PMWA2uOMNAWW9wacCrYgN.lXUR35YEG.kOPWO
# sha:{SHA}C5wmJdwh7wX2rU3fR8XyA4N6oyw=
# crypt:znExVsGU19vAQ
# plain:toto

__all__ = ["FlatFileAuthenticationBackend"]

LOG = logging.getLogger(__name__)

# dummy pw is "testpassword" (used when user not found to avoid timing attacks)
DUMMY_HASH_DATA = "$2y$05$Vhvhbk0SYN3ncn9BSvXEHunzztBWfrwqOpX1D0GhrFvM1TcADpKoO"


class HtpasswdFile(object):
    """
    Custom HtpasswdFile implementation which supports comments
    (lines starting with #).
    """

    def __init__(self, filename):
        self.filename = filename
        self.entries = {}
        self._load_file()

    def _load_file(self):
        """
        Load apache htpasswd formatted file with support for lines starting with "#"
        as comments.  The format is a single line per record as <username>:<hash>

        Records are added to the 'entries' dictionary with the username as the key
        and hash data as the value.
        """
        data = None
        with open(self.filename, "r") as f:
            data = f.readlines()
        for line in data:
            line = line.strip()
            if line.startswith("#"):
                LOG.debug(f"Skip comment {line}")
                continue
            if ":" not in line:
                LOG.debug(f"Malformed entry '{line}'.")
                continue
            username, hash_data = line.split(":", 1)
            self.entries[username] = hash_data

    def check_password(self, username, password):
        encode_local = locale.getpreferredencoding()
        pw = bytes(password, encoding=encode_local)
        if username in self.entries:
            hash_data = self.entries[username]
            if hash_data.startswith("$apr1$"):
                LOG.warning(
                    "%s uses MD5 algorithm to hash the password."
                    "Rehash the password with bcrypt is strongly recommended.",
                    username,
                )
                _, _, salt, md5hash = hash_data.split("$")
                return apr1.hash_apr1(salt, password) == hash_data
            elif hash_data.startswith("$2y$"):
                return bcrypt.checkpw(pw, bytes(hash_data, encoding=encode_local))
            elif hash_data.startswith("{SHA}"):
                LOG.warning(
                    "%s uses deprecated SHA algorithm to hash password."
                    "Rehash the password with bcrypt.",
                    username,
                )
                return bytes(hash_data, encoding=encode_local) == b"{SHA}" + base64.b64encode(
                    hashlib.sha1(pw).digest()
                )
            else:
                # crypt is deprecated and will be dropped in python 3.13.
                LOG.warning(
                    "%s uses deprecated crypt algorithm to hash password."
                    "Rehash the password with bcrypt.",
                    username,
                )
                return compare_hash(crypt.crypt(password, hash_data), hash_data)
        else:
            # User not found. Do a dummy hash to avoid timing attacks.
            _ = bcrypt.checkpw(pw, bytes(DUMMY_HASH_DATA, encoding=encode_local))
            return None


class FlatFileAuthenticationBackend(object):
    """
    Backend which reads authentication information from a local file.

    Entries need to be in a htpasswd file like format. This means entries can be managed with
    the htpasswd utility (https://httpd.apache.org/docs/current/programs/htpasswd.html) which
    ships with Apache HTTP server.
    """

    def __init__(self, file_path):
        """
        :param file_path: Path to the file with authentication information.
        :type file_path: ``str``
        """
        self._file_path = file_path

    def authenticate(self, username, password):
        htpasswd_file = HtpasswdFile(self._file_path)
        result = htpasswd_file.check_password(username, password)

        if result is None:
            LOG.debug('User "%s" doesn\'t exist' % (username))
        elif result is False:
            LOG.debug('Invalid password for user "%s"' % (username))
        elif result is True:
            LOG.debug('Authentication for user "%s" successful' % (username))

        return bool(result)

    def get_user(self, username):
        pass
