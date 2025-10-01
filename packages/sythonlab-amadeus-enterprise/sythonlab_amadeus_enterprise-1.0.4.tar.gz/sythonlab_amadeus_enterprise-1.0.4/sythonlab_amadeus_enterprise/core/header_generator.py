import base64
import hashlib
import os
from datetime import datetime, timezone

from sythonlab_amadeus_enterprise import settings


class AmadeusHeaderGenerator:
    message_id = None
    action = None
    nonce_bytes = None
    nonce = None
    created_at = None
    password_digest = None

    def __init__(self, **kwargs):
        pass

    def generate_message_id(self):
        random_bytes = os.urandom(24)
        b64_encoded = base64.urlsafe_b64encode(random_bytes).decode('ascii')
        clean_b64 = b64_encoded.replace('=', '').replace('_', '-').replace('/', '')
        self.message_id = clean_b64[:43]

    def generate_nonce(self):
        self.nonce_bytes = os.urandom(16)
        self.nonce = base64.b64encode(self.nonce_bytes).decode('utf-8')

    def generate_created_at(self):
        self.created_at = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    def generate_password_digest(self):
        password_bytes = settings.AMADEUS_CONFIG['PASSWORD'].encode('utf-8')
        concatenated = self.nonce_bytes + self.created_at.encode('utf-8') + hashlib.sha1(password_bytes).digest()
        digest = hashlib.sha1(concatenated).digest()
        self.password_digest = base64.b64encode(digest).decode('utf-8')

    def generate_header(self):
        self.generate_message_id()
        self.generate_created_at()
        self.generate_nonce()
        self.generate_password_digest()
