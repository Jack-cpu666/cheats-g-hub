"""
Membership System with Supabase + Local Encrypted Storage
- Auto-generates keys on purchase (user never sees it)
- Stores encrypted key hidden on PC
- Validates against Supabase on every launch
"""

import os
import time
import hashlib
import secrets
import subprocess
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional, List, Dict
import requests

# Try to import cryptography for encryption
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    import base64
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False
    print("[Warning] cryptography not installed. Run: pip install cryptography")


# ============================================
# Supabase Configuration
# ============================================
SUPABASE_URL = "https://tlmlbcjiheckhmczzjtq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRsbWxiY2ppaGVja2htY3p6anRxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2NjI3MjU4MywiZXhwIjoyMDgxODQ4NTgzfQ._73uwkgHadansQQ3yprO4CXL_9J6m1b0ceSUOgxzKIU"
API_URL = f"{SUPABASE_URL}/rest/v1/keys"

SUPABASE_HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}


# ============================================
# Stripe Configuration  
# ============================================
STRIPE_SECRET_KEY = "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"
STRIPE_WEBHOOK_SECRET = "whsec_your_webhook_secret_here"


# ============================================
# Membership Tiers & Features
# ============================================
class MembershipTier(Enum):
    NONE = "none"
    REGULAR = "regular"
    FULL_ACCESS = "full_access"


# Feature definitions per tier
TIER_FEATURES = {
    MembershipTier.NONE: [],
    MembershipTier.REGULAR: [
        "aimbot",
        "humanizer_view",  # Read-only
        "fingerprint_static",  # Static, cannot regenerate
        "web_ui"
    ],
    MembershipTier.FULL_ACCESS: [
        "aimbot",
        "triggerbot",
        "anti_recoil",
        "crosshair_overlay",
        "humanizer",  # Full access - can modify
        "fingerprint",  # Can regenerate
        "advanced_settings",
        "web_ui",
        "priority_support"
    ]
}


# Pricing in cents for Stripe
PRICING = {
    MembershipTier.REGULAR: {
        "1_day": 299,
        "1_week": 50,  # $0.50 for testing (Stripe minimum)
        "2_weeks": 1499,
        "1_month": 2499,
        "3_months": 5999,
        "1_year": 14999,
        "lifetime": 29999
    },
    MembershipTier.FULL_ACCESS: {
        "1_day": 499,
        "1_week": 50,  # $0.50 for testing (Stripe minimum)
        "2_weeks": 2999,
        "1_month": 4999,
        "3_months": 11999,
        "1_year": 29999,
        "lifetime": 49999
    }
}


# Duration to days mapping
DURATION_DAYS = {
    "1_day": 1,
    "1_week": 7,
    "2_weeks": 14,
    "1_month": 30,
    "3_months": 90,
    "1_year": 365,
    "lifetime": 36500  # 100 years
}


@dataclass
class MembershipInfo:
    """Current user's membership information"""
    tier: MembershipTier = MembershipTier.NONE
    features: List[str] = field(default_factory=list)
    expiry_timestamp: int = 0
    days_remaining: int = 0
    is_active: bool = False
    hwid: str = ""
    
    @property
    def can_modify_humanizer(self) -> bool:
        return "humanizer" in self.features
    
    @property
    def can_regenerate_fingerprint(self) -> bool:
        return "fingerprint" in self.features
    
    def to_dict(self) -> dict:
        # Create features dict with boolean values for UI
        feature_flags = {
            "aimbot": "aimbot" in self.features,
            "triggerbot": "triggerbot" in self.features,
            "anti_recoil": "anti_recoil" in self.features,
            "crosshair_overlay": "crosshair_overlay" in self.features,
            "humanizer": "humanizer" in self.features or "humanizer_view" in self.features,
            "fingerprint_randomization": "fingerprint" in self.features or "fingerprint_static" in self.features,
            "advanced_settings": "advanced_settings" in self.features,
            "web_ui": "web_ui" in self.features
        }
        
        # Format tier for display
        tier_display = "Full Access" if self.tier == MembershipTier.FULL_ACCESS else (
            "Regular" if self.tier == MembershipTier.REGULAR else "No License"
        )
        
        return {
            "tier": self.tier.value,
            "tier_display": tier_display,
            "features": feature_flags,
            "features_list": self.features,
            "expiry_timestamp": self.expiry_timestamp,
            "days_remaining": self.days_remaining,
            "is_active": self.is_active,
            "is_lifetime": self.days_remaining > 3650,  # More than 10 years = lifetime
            "can_modify_humanizer": self.can_modify_humanizer,
            "can_regenerate_fingerprint": self.can_regenerate_fingerprint
        }


# ============================================
# Hardware ID
# ============================================
def get_hwid() -> str:
    """Get unique hardware identifier"""
    try:
        result = subprocess.run(
            ['powershell', '-Command', 
             '(Get-CimInstance Win32_ComputerSystemProduct).UUID'],
            capture_output=True, text=True, timeout=5,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        uuid = result.stdout.strip()
        if uuid and uuid != "":
            return hashlib.sha256(uuid.encode()).hexdigest()[:32]
    except:
        pass
    
    # Fallback
    import platform
    return hashlib.sha256((platform.node() + platform.processor()).encode()).hexdigest()[:32]


# ============================================
# Hidden Encrypted Storage with Key Obfuscation
# ============================================

# OBFUSCATED ENCRYPTION KEY COMPONENTS
# These are XOR-encrypted at rest - decrypted at runtime
# Actual key is derived by combining these with HWID
# DO NOT STORE KEYS IN PLAIN TEXT

# Primary key component (XOR encrypted with runtime mask)
_EK_P1 = bytes([0x9f, 0x3b, 0xa8, 0xd2, 0xe5, 0x4c, 0x2d, 0x76, 0xf6, 0xe1, 0xd9, 0xba, 0xd3, 0xa2, 0xe5, 0x3d, 
                0xc8, 0xb7, 0xaa, 0xd1, 0xc9, 0xe2, 0xf3, 0xa4, 0xb5, 0xc6, 0xd7, 0xe8, 0xf9, 0xaa, 0xb1, 0xc2])

# Secondary key component (bit-shifted storage)
_EK_P2 = bytes([0x3c, 0x5d, 0x7e, 0x9f, 0xb0, 0xf2, 0xa4, 0xb6, 0xc8, 0xda, 0xe3, 0xf5, 0xa7, 0xc9, 0xe1, 0xb3, 
                0xd5, 0xf7, 0xa9, 0xcb, 0xe2, 0xb5, 0xd7, 0xf9, 0xa1, 0xc3, 0xe5, 0xb7, 0xd9, 0xfb, 0xa3, 0xc5])

# Tertiary component (reversed nibbles)
_EK_P3 = bytes([0x6a, 0x8b, 0xac, 0x2d, 0x4e, 0x7f, 0xe6, 0xa8, 0xba, 0x2c, 0x4e, 0x6a, 0x8b, 0xfd, 0x2e, 0x4b, 
                0x6d, 0x8f, 0xa0, 0xc2, 0xe4, 0xb6, 0xd8, 0xfa, 0x1c, 0x3e, 0x5a, 0x7c, 0x9e, 0xba, 0xdc, 0xfe])

# XOR mask derived from compile-time constant
_XOR_MASK = bytes([0x17, 0x29, 0x3b, 0x4d, 0x5f, 0x71, 0x83, 0x95, 0xa7, 0xb9, 0xcb, 0xdd, 0xef, 0x11, 0x23, 0x35,
                   0x47, 0x59, 0x6b, 0x7d, 0x8f, 0xa1, 0xb3, 0xc5, 0xd7, 0xe9, 0xfb, 0x0d, 0x1f, 0x31, 0x43, 0x55])


def _deobfuscate_key_component(component: bytes, mask: bytes) -> bytes:
    """Deobfuscate a key component using XOR"""
    return bytes(a ^ b for a, b in zip(component, mask))


def _derive_master_secret() -> bytes:
    """
    Derive the master secret from obfuscated components.
    This is computed at runtime - never stored in plain text.
    """
    # Deobfuscate components
    p1 = _deobfuscate_key_component(_EK_P1, _XOR_MASK)
    p2 = _deobfuscate_key_component(_EK_P2, bytes(reversed(_XOR_MASK)))
    p3 = _deobfuscate_key_component(_EK_P3, bytes((b + 0x33) & 0xFF for b in _XOR_MASK))
    
    # Combine components with rotation
    combined = bytes((a ^ b ^ c) for a, b, c in zip(p1, p2, p3))
    
    # Final hash to normalize length
    return hashlib.sha256(combined).digest()


class SecureStorage:
    """
    Stores encrypted license key in a hidden location on the PC.
    User never sees the key - it's auto-generated and stored encrypted.
    Uses multi-layer key derivation for maximum security.
    """
    
    # Hidden storage locations (Windows)
    STORAGE_LOCATIONS = [
        os.path.join(os.environ.get('APPDATA', ''), '.system_cache'),
        os.path.join(os.environ.get('LOCALAPPDATA', ''), '.runtime_data'),
        os.path.join(os.path.expanduser('~'), '.config', '.cache_data')
    ]
    
    def __init__(self):
        self.hwid = get_hwid()
        self._master_secret = _derive_master_secret()
        self._encryption_key = self._derive_key()
    
    def _derive_key(self) -> Optional[bytes]:
        """
        Derive encryption key from HWID + obfuscated master secret.
        Multi-layer derivation makes reverse engineering very difficult.
        """
        if not CRYPTO_AVAILABLE:
            return None
        
        # Combine HWID with master secret for unique per-machine key
        combined_secret = hashlib.sha512(
            self.hwid.encode() + self._master_secret
        ).digest()
        
        # Use PBKDF2 with high iterations for additional security
        salt = combined_secret[:16]  # First 16 bytes as salt
        password = combined_secret[16:]  # Rest as password
        
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=150000,  # High iteration count
        )
        
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key
    
    def _get_storage_path(self) -> str:
        """Get the storage file path, creating directories if needed"""
        for location in self.STORAGE_LOCATIONS:
            try:
                os.makedirs(location, exist_ok=True)
                # Set hidden attribute on Windows
                if os.name == 'nt':
                    subprocess.run(['attrib', '+h', location], 
                                   capture_output=True, 
                                   creationflags=subprocess.CREATE_NO_WINDOW)
                return os.path.join(location, '.license.dat')
            except:
                continue
        
        # Fallback to temp
        return os.path.join(os.environ.get('TEMP', '/tmp'), '.license.dat')
    
    def _derive_outer_key(self) -> bytes:
        """Derive a second key for outer encryption layer"""
        if not CRYPTO_AVAILABLE:
            return None
        # Different derivation for outer layer
        outer_secret = hashlib.sha512(
            self._master_secret + self.hwid.encode() + b'OUTER_LAYER_V2'
        ).digest()
        
        salt = outer_secret[32:48]
        password = outer_secret[:32]
        
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        return kdf.derive(password)
    
    def _xor_obfuscate(self, data: bytes, key: bytes) -> bytes:
        """XOR obfuscation layer"""
        key_len = len(key)
        return bytes([data[i] ^ key[i % key_len] for i in range(len(data))])
    
    def encrypt_and_store(self, license_key: str) -> bool:
        """
        Triple-layer encryption:
        1. Fernet (AES-128-CBC + HMAC)
        2. AES-256-GCM outer encryption
        3. XOR obfuscation with random padding
        """
        if not CRYPTO_AVAILABLE or not self._encryption_key:
            return False
        
        try:
            from cryptography.hazmat.primitives.ciphers.aead import AESGCM
            
            # Layer 1: Fernet encryption
            fernet = Fernet(self._encryption_key)
            payload = f"{license_key}|{self.hwid}|{int(time.time())}"
            layer1 = fernet.encrypt(payload.encode())
            
            # Layer 2: AES-256-GCM outer encryption
            outer_key = self._derive_outer_key()
            aesgcm = AESGCM(outer_key)
            nonce = secrets.token_bytes(12)  # 96-bit nonce for GCM
            layer2 = aesgcm.encrypt(nonce, layer1, None)
            
            # Layer 3: XOR obfuscation with random padding
            xor_key = secrets.token_bytes(32)
            random_padding = secrets.token_bytes(16)  # Random noise
            combined = random_padding + nonce + layer2
            layer3 = self._xor_obfuscate(combined, xor_key)
            
            # Final format: [magic 2 bytes][xor_key 32 bytes][encrypted data]
            final_data = bytes([0xDE, 0xAD]) + xor_key + layer3
            
            # Store in hidden location
            storage_path = self._get_storage_path()
            with open(storage_path, 'wb') as f:
                f.write(final_data)
            
            # Set hidden attribute
            if os.name == 'nt':
                subprocess.run(['attrib', '+h', storage_path], 
                               capture_output=True,
                               creationflags=subprocess.CREATE_NO_WINDOW)
            
            print(f"[Storage] License stored with triple encryption")
            return True
        except Exception as e:
            print(f"[Storage] Failed to store: {e}")
            return False
    
    def read_and_decrypt(self) -> Optional[str]:
        """
        Decrypt triple-layer encryption
        """
        if not CRYPTO_AVAILABLE or not self._encryption_key:
            return None
        
        storage_path = self._get_storage_path()
        
        if not os.path.exists(storage_path):
            return None
        
        try:
            from cryptography.hazmat.primitives.ciphers.aead import AESGCM
            
            with open(storage_path, 'rb') as f:
                final_data = f.read()
            
            # Check for new format (triple encryption)
            if len(final_data) > 34 and final_data[0:2] == bytes([0xDE, 0xAD]):
                # New triple-encrypted format: [magic 2][xor_key 32][data]
                xor_key = final_data[2:34]
                layer3 = final_data[34:]
                
                # Layer 3: De-XOR
                combined = self._xor_obfuscate(layer3, xor_key)
                
                # Extract components: 16 byte padding + 12 byte nonce + ciphertext
                random_padding = combined[:16]  # Discard
                nonce = combined[16:28]
                layer2 = combined[28:]
                
                # Layer 2: AES-256-GCM decrypt
                outer_key = self._derive_outer_key()
                aesgcm = AESGCM(outer_key)
                layer1 = aesgcm.decrypt(nonce, layer2, None)
                
                # Layer 1: Fernet decrypt
                fernet = Fernet(self._encryption_key)
                decrypted = fernet.decrypt(layer1).decode()
            else:
                # Legacy single-layer format (for backwards compatibility)
                fernet = Fernet(self._encryption_key)
                decrypted = fernet.decrypt(final_data).decode()
            
            parts = decrypted.split('|')
            
            if len(parts) >= 2:
                stored_key = parts[0]
                stored_hwid = parts[1]
                
                # Verify HWID matches
                if stored_hwid == self.hwid:
                    return stored_key
                else:
                    print("[Storage] HWID mismatch - license not valid for this PC")
                    return None
            
            return None
        except Exception as e:
            print(f"[Storage] Failed to read: {e}")
            return None
    
    def clear(self):
        """Clear stored license"""
        try:
            storage_path = self._get_storage_path()
            if os.path.exists(storage_path):
                os.remove(storage_path)
        except:
            pass


# Global storage instance
_secure_storage: Optional[SecureStorage] = None


def get_secure_storage() -> SecureStorage:
    global _secure_storage
    if _secure_storage is None:
        _secure_storage = SecureStorage()
    return _secure_storage


# ============================================
# Supabase License Validation
# ============================================
def generate_license_key() -> str:
    """Generate a new unique license key"""
    chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    parts = []
    for _ in range(4):
        part = ''.join(secrets.choice(chars) for _ in range(4))
        parts.append(part)
    return '-'.join(parts)


def create_license_in_supabase(tier: str, duration: str, hwid: str) -> Optional[str]:
    """
    Create a new license key in Supabase.
    Called after successful payment.
    """
    try:
        # Generate unique key
        license_key = generate_license_key()
        
        # Calculate expiry
        days = DURATION_DAYS.get(duration, 30)
        expiry_ms = int((time.time() + (days * 86400)) * 1000)
        
        # Map tier string to proper value
        tier_value = "full" if tier == "full_access" else "regular"
        
        # Create record in Supabase (matching actual table structure)
        payload = {
            "key": license_key,
            "hwid": hwid,
            "status": "active",
            "expires": expiry_ms,
            "created": int(time.time() * 1000),
            "notes": tier_value  # Store tier in notes column
        }
        
        response = requests.post(
            API_URL,
            headers=SUPABASE_HEADERS,
            json=payload,
            timeout=10
        )
        
        if response.status_code in [200, 201]:
            print(f"[Supabase] License created: {license_key[:8]}...")
            return license_key
        else:
            print(f"[Supabase] Failed to create license: {response.status_code} - {response.text}")
            return None
            
    except Exception as e:
        print(f"[Supabase] Error creating license: {e}")
        return None


def validate_license_with_supabase(license_key: str) -> Optional[MembershipInfo]:
    """
    Validate license key with Supabase server.
    Returns MembershipInfo if valid, None if invalid/expired.
    """
    try:
        hwid = get_hwid()
        
        # Fetch key from Supabase
        response = requests.get(
            f"{API_URL}?key=eq.{license_key}&select=*",
            headers=SUPABASE_HEADERS,
            timeout=10
        )
        
        keys = response.json()
        
        if not keys or len(keys) == 0:
            return None
        
        key_data = keys[0]
        
        # Check status
        if key_data.get("status") == "suspended":
            return None
        
        # Check expiry
        now_ms = int(time.time() * 1000)
        expiry_ms = key_data.get("expires", 0)
        
        if expiry_ms < now_ms:
            return None  # Expired
        
        # Check HWID
        stored_hwid = key_data.get("hwid", "")
        
        if stored_hwid and stored_hwid != hwid:
            return None  # Different PC
        
        # Bind HWID if first use
        if not stored_hwid:
            requests.patch(
                f"{API_URL}?key=eq.{license_key}",
                headers=SUPABASE_HEADERS,
                json={"hwid": hwid},
                timeout=10
            )
        
        # Build membership info (tier is stored in 'notes' column)
        tier_str = key_data.get("notes", "regular")
        tier = MembershipTier.FULL_ACCESS if tier_str == "full" else MembershipTier.REGULAR
        
        days_remaining = (expiry_ms - now_ms) // 86400000
        features = TIER_FEATURES.get(tier, [])
        
        return MembershipInfo(
            tier=tier,
            features=features,
            expiry_timestamp=expiry_ms,
            days_remaining=days_remaining,
            is_active=True,
            hwid=hwid
        )
        
    except Exception as e:
        print(f"[Supabase] Validation error: {e}")
        return None


# ============================================
# Stripe Payment Handler
# ============================================
class StripePayment:
    """Handle Stripe payment integration"""
    
    def __init__(self):
        self.enabled = False
        try:
            import stripe
            stripe.api_key = STRIPE_SECRET_KEY
            self.stripe = stripe
            self.enabled = True
        except ImportError:
            print("[Stripe] Not available. Install: pip install stripe")
    
    def create_checkout_session(self, tier: str, duration: str, 
                                 success_url: str, cancel_url: str, 
                                 hwid: str) -> Optional[dict]:
        """Create Stripe checkout session"""
        if not self.enabled:
            return None
        
        try:
            tier_enum = MembershipTier.FULL_ACCESS if tier == "full_access" else MembershipTier.REGULAR
            price_cents = PRICING[tier_enum].get(duration, 4999)
            
            tier_name = "Full Access" if tier == "full_access" else "Regular"
            duration_name = duration.replace("_", " ").title()
            
            session = self.stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': price_cents,
                        'product_data': {
                            'name': f'{tier_name} - {duration_name}',
                            'description': f'Ascendancy {tier_name} membership for {duration_name}'
                        }
                    },
                    'quantity': 1
                }],
                mode='payment',
                success_url=success_url,
                cancel_url=cancel_url,
                metadata={
                    'tier': tier,
                    'duration': duration,
                    'hwid': hwid
                }
            )
            
            return {
                'session_id': session.id,
                'url': session.url
            }
            
        except Exception as e:
            print(f"[Stripe] Error creating session: {e}")
            return None
    
    def verify_webhook(self, payload: bytes, sig_header: str) -> Optional[dict]:
        """Verify and parse Stripe webhook"""
        if not self.enabled:
            return None
        
        try:
            event = self.stripe.Webhook.construct_event(
                payload, sig_header, STRIPE_WEBHOOK_SECRET
            )
            return event
        except Exception as e:
            print(f"[Stripe] Webhook error: {e}")
            return None


# Global instances
_stripe_payment: Optional[StripePayment] = None
_current_membership: Optional[MembershipInfo] = None


def get_stripe_payment() -> StripePayment:
    global _stripe_payment
    if _stripe_payment is None:
        _stripe_payment = StripePayment()
    return _stripe_payment


# ============================================
# Main Membership Functions
# ============================================
def initialize_membership() -> MembershipInfo:
    """
    Initialize membership on app startup.
    1. Read encrypted key from hidden storage
    2. Validate with Supabase
    3. Return membership info
    """
    global _current_membership
    
    storage = get_secure_storage()
    stored_key = storage.read_and_decrypt()
    
    if stored_key:
        print("[Membership] Found stored license, validating...")
        membership = validate_license_with_supabase(stored_key)
        
        if membership:
            _current_membership = membership
            print(f"[Membership] ✓ {membership.tier.value.title()} - {membership.days_remaining} days remaining")
            return membership
        else:
            print("[Membership] ✗ License invalid or expired")
            storage.clear()
    
    # No valid membership
    _current_membership = MembershipInfo()
    return _current_membership


def activate_purchase(tier: str, duration: str) -> Optional[str]:
    """
    Called after successful Stripe payment.
    Creates license in Supabase and stores encrypted locally.
    Returns the license key (but user never sees it).
    """
    global _current_membership
    
    hwid = get_hwid()
    storage = get_secure_storage()
    
    # Create license in Supabase
    license_key = create_license_in_supabase(tier, duration, hwid)
    
    if not license_key:
        return None
    
    # Store encrypted locally
    if storage.encrypt_and_store(license_key):
        print(f"[Membership] License activated and stored securely")
        
        # Refresh membership
        _current_membership = validate_license_with_supabase(license_key)
        return license_key
    
    return None


def get_membership_info() -> MembershipInfo:
    """Get current membership info"""
    global _current_membership
    
    if _current_membership is None:
        return initialize_membership()
    
    return _current_membership


def refresh_membership_from_server() -> MembershipInfo:
    """Force refresh membership info from Supabase (not cached)"""
    global _current_membership
    
    hwid = get_hwid()
    storage = get_secure_storage()
    license_key = storage.read_and_decrypt()
    
    if license_key:
        # Force fresh validation from Supabase
        _current_membership = validate_license_with_supabase(license_key)
        if _current_membership:
            print(f"[Membership] Refreshed from server: {_current_membership.tier.value}, {_current_membership.days_remaining} days")
            return _current_membership
    
    # No valid license
    _current_membership = MembershipInfo(
        tier=MembershipTier.NONE,
        features=[],
        expiry_timestamp=0,
        days_remaining=0,
        is_active=False,
        hwid=hwid
    )
    return _current_membership


def has_feature(feature: str) -> bool:
    """Check if current membership has a feature"""
    membership = get_membership_info()
    return feature in membership.features


def can_modify_humanizer() -> bool:
    """Check if user can modify humanizer settings"""
    return get_membership_info().can_modify_humanizer


def can_regenerate_fingerprint() -> bool:
    """Check if user can regenerate fingerprint"""
    return get_membership_info().can_regenerate_fingerprint


def get_pricing_display() -> dict:
    """Get pricing for display in UI"""
    return {
        "regular": {k: v/100 for k, v in PRICING[MembershipTier.REGULAR].items()},
        "full_access": {k: v/100 for k, v in PRICING[MembershipTier.FULL_ACCESS].items()}
    }


# ============================================
# License Transfer System
# ============================================

def generate_transfer_code() -> Optional[str]:
    """
    Generate a one-time transfer code for moving license to a new PC.
    The transfer code is stored in Supabase and the current HWID is marked for transfer.
    Returns: 6-character transfer code or None on error
    """
    try:
        storage = SecureStorage()
        license_key = storage.read_and_decrypt()
        
        if not license_key:
            print("[Transfer] No license found to transfer")
            return None
        
        hwid = get_hwid()
        
        # Verify the license exists and belongs to this HWID
        response = requests.get(
            f"{API_URL}?key=eq.{license_key}&hwid=eq.{hwid}",
            headers=SUPABASE_HEADERS,
            timeout=10
        )
        
        if response.status_code != 200 or not response.json():
            print("[Transfer] License not found or doesn't belong to this PC")
            return None
        
        # Generate 6-character transfer code
        chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'  # No confusing chars like 0/O, 1/I
        transfer_code = ''.join(secrets.choice(chars) for _ in range(6))
        
        # Store transfer code in Supabase (in notes field temporarily) and clear HWID
        update_payload = {
            "hwid": f"TRANSFER:{transfer_code}",  # Mark as pending transfer with code
            "notes": response.json()[0].get("notes", "regular")  # Keep tier info
        }
        
        update_response = requests.patch(
            f"{API_URL}?key=eq.{license_key}",
            headers=SUPABASE_HEADERS,
            json=update_payload,
            timeout=10
        )
        
        if update_response.status_code in [200, 204]:
            # Clear local license since it's now pending transfer
            storage.clear()
            print(f"[Transfer] Transfer code generated: {transfer_code}")
            return transfer_code
        else:
            print(f"[Transfer] Failed to create transfer code: {update_response.status_code}")
            return None
            
    except Exception as e:
        print(f"[Transfer] Error generating transfer code: {e}")
        return None


def redeem_transfer_code(transfer_code: str) -> dict:
    """
    Redeem a transfer code on a new PC to claim the license.
    Returns: dict with success status and message
    """
    try:
        transfer_code = transfer_code.upper().strip()
        
        if len(transfer_code) != 6:
            return {"success": False, "message": "Invalid transfer code format"}
        
        new_hwid = get_hwid()
        
        # Find license with this transfer code
        response = requests.get(
            f"{API_URL}?hwid=eq.TRANSFER:{transfer_code}",
            headers=SUPABASE_HEADERS,
            timeout=10
        )
        
        if response.status_code != 200:
            return {"success": False, "message": "Server error"}
        
        data = response.json()
        if not data:
            return {"success": False, "message": "Invalid or expired transfer code"}
        
        key_data = data[0]
        license_key = key_data.get("key")
        
        # Check if license is expired
        expiry_ms = key_data.get("expires", 0)
        now_ms = int(time.time() * 1000)
        if expiry_ms < now_ms:
            return {"success": False, "message": "This license has expired"}
        
        # Bind license to new HWID
        update_payload = {
            "hwid": new_hwid
        }
        
        update_response = requests.patch(
            f"{API_URL}?key=eq.{license_key}",
            headers=SUPABASE_HEADERS,
            json=update_payload,
            timeout=10
        )
        
        if update_response.status_code in [200, 204]:
            # Store license locally on new PC
            storage = SecureStorage()
            storage.encrypt_and_store(license_key)
            
            print(f"[Transfer] License successfully transferred to new PC")
            return {
                "success": True, 
                "message": "License transferred successfully! Restart the application.",
                "license_key": license_key
            }
        else:
            return {"success": False, "message": "Failed to transfer license"}
            
    except Exception as e:
        print(f"[Transfer] Error redeeming transfer code: {e}")
        return {"success": False, "message": f"Error: {str(e)}"}


# Initialize on import
initialize_membership()
