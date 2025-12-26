"""
DEPRECATED - Old License Key System  

This file is deprecated. The new license system uses:
- auth/membership.py for license management
- Supabase for server-side validation
- Local encrypted storage (hidden, HWID-bound)
- Stripe for payment processing

The user never sees their license key. It's auto-generated
on purchase, stored encrypted on their PC, and validated
with Supabase on every app launch.

For legacy compatibility, this module provides stub functions.
"""

import warnings


def get_hwid() -> str:
    """Get hardware ID - redirects to new system."""
    from auth.membership import get_hwid as new_get_hwid
    return new_get_hwid()


def validate_key(license_key: str):
    """
    DEPRECATED: Use auth.membership module instead.
    
    Validates a key against Supabase.
    """
    warnings.warn(
        "validate_key is deprecated. Use auth.membership.validate_license_with_supabase() instead.",
        DeprecationWarning,
        stacklevel=2
    )
    
    from auth.membership import validate_license_with_supabase
    
    membership = validate_license_with_supabase(license_key)
    
    if membership and membership.is_active:
        days = membership.days_remaining
        tier = membership.tier.value
        return True, f"Valid - {tier.title()} ({days} days)"
    else:
        return False, "Invalid or expired license"


def quick_validate(license_key: str) -> bool:
    """
    DEPRECATED: Quick validation.
    """
    valid, msg = validate_key(license_key)
    print(f"License: {msg}")
    return valid
