"""
Membership API Routes with Supabase + Stripe Integration
Auto-generates keys, stores encrypted locally, validates with server
"""

from flask import Blueprint, request, jsonify
from auth.membership import (
    get_membership_info,
    get_pricing_display,
    has_feature,
    can_modify_humanizer,
    can_regenerate_fingerprint,
    get_stripe_payment,
    get_hwid,
    activate_purchase,
    get_secure_storage,
    validate_license_with_supabase,
    create_license_in_supabase,
    initialize_membership,
    MembershipTier
)

membership_api = Blueprint('membership_api', __name__, url_prefix='/api/membership')


@membership_api.route('/info', methods=['GET'])
def api_membership_info():
    """Get current membership information. Pass ?refresh=1 to force server validation."""
    try:
        from auth.membership import refresh_membership_from_server
        
        # Check if refresh requested
        refresh = request.args.get('refresh', '0') == '1'
        
        if refresh:
            # Force fresh validation from Supabase
            membership = refresh_membership_from_server()
        else:
            membership = get_membership_info()
        
        return jsonify({
            "success": True,
            "membership": membership.to_dict(),
            "hwid": get_hwid()
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


@membership_api.route('/pricing', methods=['GET'])
def api_pricing():
    """Get pricing information for all tiers and durations."""
    try:
        return jsonify({
            "success": True,
            "pricing": get_pricing_display()
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


@membership_api.route('/check_feature', methods=['GET'])
def api_check_feature():
    """Check if current membership has access to a feature."""
    try:
        feature = request.args.get('feature', '')
        if not feature:
            return jsonify({
                "success": False,
                "message": "Feature parameter required"
            }), 400
        
        has_access = has_feature(feature)
        return jsonify({
            "success": True,
            "feature": feature,
            "has_access": has_access,
            "can_modify_humanizer": can_modify_humanizer(),
            "can_regenerate_fingerprint": can_regenerate_fingerprint()
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


@membership_api.route('/create_checkout', methods=['POST'])
def api_create_checkout():
    """
    Create a Stripe checkout session for payment.
    
    Expected JSON body:
    {
        "tier": "regular" or "full_access",
        "duration": "1_day", "1_week", etc.
    }
    """
    try:
        data = request.json or {}
        tier = data.get('tier', '')
        duration = data.get('duration', '')
        
        if not tier or not duration:
            return jsonify({
                "success": False,
                "message": "Tier and duration required"
            }), 400
        
        if tier not in ["regular", "full_access"]:
            return jsonify({
                "success": False,
                "message": "Invalid tier"
            }), 400
        
        valid_durations = ["1_day", "1_week", "2_weeks", "1_month", "3_months", "1_year", "lifetime"]
        if duration not in valid_durations:
            return jsonify({
                "success": False,
                "message": "Invalid duration"
            }), 400
        
        stripe = get_stripe_payment()
        if not stripe.enabled:
            return jsonify({
                "success": False,
                "message": "Payment system not available. Install stripe: pip install stripe"
            }), 503
        
        # Get base URL from request
        base_url = request.host_url.rstrip('/')
        
        result = stripe.create_checkout_session(
            tier=tier,
            duration=duration,
            success_url=f"{base_url}/payment/success?session_id={{CHECKOUT_SESSION_ID}}",
            cancel_url=f"{base_url}/payment/cancel",
            hwid=get_hwid()
        )
        
        if result:
            return jsonify({
                "success": True,
                "checkout_url": result["url"],
                "session_id": result["session_id"]
            })
        else:
            return jsonify({
                "success": False,
                "message": "Failed to create checkout session"
            }), 500
            
    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


@membership_api.route('/webhook', methods=['POST'])
def api_stripe_webhook():
    """
    Handle Stripe webhook events.
    Called by Stripe when payment is completed.
    Auto-generates key in Supabase and stores encrypted locally.
    """
    try:
        payload = request.get_data()
        sig_header = request.headers.get('Stripe-Signature', '')
        
        stripe = get_stripe_payment()
        if not stripe.enabled:
            return jsonify({"error": "Stripe not configured"}), 503
        
        event = stripe.verify_webhook(payload, sig_header)
        if not event:
            return jsonify({"error": "Invalid signature"}), 400
        
        # Handle the event
        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            
            # Get metadata
            metadata = session.get('metadata', {})
            tier = metadata.get('tier')
            duration = metadata.get('duration')
            hwid = metadata.get('hwid')
            
            if tier and duration and hwid:
                # Verify HWID matches current machine
                current_hwid = get_hwid()
                
                if hwid == current_hwid:
                    # Activate the purchase - creates key in Supabase + stores locally
                    license_key = activate_purchase(tier, duration)
                    
                    if license_key:
                        print(f"[Payment] ✓ License activated: {tier} for {duration}")
                    else:
                        print(f"[Payment] ✗ Failed to activate license")
                else:
                    print(f"[Payment] HWID mismatch - purchase on different PC")
        
        elif event['type'] == 'payment_intent.payment_failed':
            error_msg = event['data']['object'].get('last_payment_error', {}).get('message', 'Unknown')
            print(f"[Payment] ✗ Failed: {error_msg}")
        
        return jsonify({"status": "success"}), 200
        
    except Exception as e:
        print(f"[Webhook] Error: {e}")
        return jsonify({"error": str(e)}), 500


@membership_api.route('/activate_purchase', methods=['POST'])
def api_activate_purchase():
    """
    Manually activate a purchase (for testing or manual activation).
    Creates license in Supabase and stores encrypted locally.
    
    Expected JSON body:
    {
        "tier": "regular" or "full_access",
        "duration": "1_month", etc.
    }
    """
    try:
        data = request.json or {}
        tier = data.get('tier', '')
        duration = data.get('duration', '')
        
        if not tier or not duration:
            return jsonify({
                "success": False,
                "message": "Tier and duration required"
            }), 400
        
        # Activate the purchase
        license_key = activate_purchase(tier, duration)
        
        if license_key:
            membership = get_membership_info()
            return jsonify({
                "success": True,
                "message": "License activated successfully",
                "membership": membership.to_dict()
            })
        else:
            return jsonify({
                "success": False,
                "message": "Failed to activate license"
            }), 500
            
    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


@membership_api.route('/refresh', methods=['POST'])
def api_refresh_membership():
    """
    Force refresh membership by re-validating with Supabase.
    """
    try:
        storage = get_secure_storage()
        stored_key = storage.read_and_decrypt()
        
        if stored_key:
            membership = validate_license_with_supabase(stored_key)
            
            if membership:
                return jsonify({
                    "success": True,
                    "membership": membership.to_dict()
                })
            else:
                # Clear invalid license
                storage.clear()
                return jsonify({
                    "success": False,
                    "message": "License expired or invalid"
                }), 401
        else:
            return jsonify({
                "success": False,
                "message": "No license found"
            }), 404
            
    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


@membership_api.route('/hwid', methods=['GET'])
def api_get_hwid():
    """Get the current hardware ID."""
    try:
        return jsonify({
            "success": True,
            "hwid": get_hwid()
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


@membership_api.route('/clear', methods=['POST'])
def api_clear_license():
    """
    Clear stored license (for testing/logout).
    """
    try:
        storage = get_secure_storage()
        storage.clear()
        
        # Reinitialize membership
        initialize_membership()
        
        return jsonify({
            "success": True,
            "message": "License cleared"
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


@membership_api.route('/transfer/generate', methods=['POST'])
def api_generate_transfer():
    """
    Generate a transfer code to move license to a new PC.
    Call this on the OLD PC before moving to new PC.
    """
    try:
        from auth.membership import generate_transfer_code
        
        transfer_code = generate_transfer_code()
        
        if transfer_code:
            return jsonify({
                "success": True,
                "transfer_code": transfer_code,
                "message": f"Transfer code: {transfer_code}\n\nWrite this down! Enter it on your new PC to transfer your license."
            })
        else:
            return jsonify({
                "success": False,
                "message": "Failed to generate transfer code. Make sure you have an active license."
            }), 400
            
    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


@membership_api.route('/transfer/redeem', methods=['POST'])
def api_redeem_transfer():
    """
    Redeem a transfer code on new PC to claim the license.
    
    Expected JSON body:
    {
        "transfer_code": "ABC123"
    }
    """
    try:
        from auth.membership import redeem_transfer_code
        
        data = request.json or {}
        code = data.get('transfer_code', '')
        
        if not code:
            return jsonify({
                "success": False,
                "message": "Transfer code required"
            }), 400
        
        result = redeem_transfer_code(code)
        
        if result.get("success"):
            # Reinitialize membership after successful transfer
            initialize_membership()
            
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500
