from flask import Flask
from web.routes.main_view import index
from web.routes.api_updates import update_settings
from web.routes.api_stats import get_stats
from web.routes.api_v7 import api_v7
from web.routes.api_membership import membership_api
from web.routes.spotify import spotify_bp

def create_app():
    app = Flask(__name__)
    
    # Secret key for session management (Spotify OAuth)
    app.secret_key = 'ascendancy_v7_secret_key_prod_2025'
    
    # Register V7 API blueprint
    app.register_blueprint(api_v7)
    
    # Register Membership API blueprint
    app.register_blueprint(membership_api)
    
    # Register Spotify blueprint
    app.register_blueprint(spotify_bp)
    
    # Main view
    app.add_url_rule("/", "index", index, methods=["GET"])
    
    # Settings API
    app.add_url_rule("/api/update", "update", update_settings, methods=["POST"])
    app.add_url_rule("/api/stats", "stats", get_stats, methods=["GET"])
    
    # Crosshair API
    from crosshair import get_top_crosshairs
    import json
    def api_get_crosshairs():
        return json.dumps(get_top_crosshairs(50))
    app.add_url_rule("/api/crosshairs", "get_crosshairs", api_get_crosshairs, methods=["GET"])
    
    # Note: Profiles and RCS routes removed - settings now use cookie auto-save
    # RCS is marked as "Coming Soon" in the UI
    
    # Reset Settings API
    def api_reset_settings():
        from core.thread import AimbotTriggerbotThread
        if AimbotTriggerbotThread.INSTANCE:
            AimbotTriggerbotThread.INSTANCE.reset_settings()
            return {"success": "1", "message": "Settings reset to defaults"}
        return {"success": "0", "message": "Thread not initialized"}, 500
        
    app.add_url_rule("/api/reset_settings", "reset_settings", api_reset_settings, methods=["GET", "POST"])
    
    # Regenerate Fingerprint API (call between matches)
    def api_regenerate_fingerprint():
        """
        Regenerate behavioral fingerprints to change the detection signature.
        Should be called between matches for maximum anti-detection.
        Requires Full Access membership to regenerate.
        """
        try:
            # Check membership permission
            from auth.membership import can_regenerate_fingerprint
            if not can_regenerate_fingerprint():
                return {"success": "0", "message": "Full Access membership required to regenerate fingerprint"}, 403
            
            from features.aim.maths import regenerate_fingerprints
            regenerate_fingerprints()
            
            # Get new fingerprint info for display
            from core.mouse_humanizer import get_humanized_controller
            controller = get_humanized_controller()
            
            if controller:
                fp = controller.fingerprint
                return {
                    "success": "1",
                    "message": "Behavioral fingerprint regenerated",
                    "fingerprint": {
                        "speed": round(fp.speed_tendency, 3),
                        "tremor": round(fp.tremor_intensity, 3),
                        "overshoot": round(fp.overshoot_tendency, 3),
                        "reaction_offset_ms": round(fp.reaction_time_offset_ms, 1)
                    }
                }
            else:
                return {"success": "1", "message": "Session profile regenerated (basic mode)"}
        except Exception as e:
            return {"success": "0", "message": f"Error: {str(e)}"}, 500
    
    app.add_url_rule("/api/regenerate_fingerprint", "regenerate_fingerprint", api_regenerate_fingerprint, methods=["POST"])
    
    # Payment Success Page - Activates the purchase
    def payment_success():
        """
        Handle successful Stripe payment.
        Retrieves session data, creates license in Supabase, stores encrypted locally.
        """
        from flask import request
        session_id = request.args.get('session_id', '')
        
        # Try to retrieve session from Stripe and activate
        activation_result = "pending"
        error_message = ""
        
        try:
            import stripe
            stripe.api_key = "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"
            
            if session_id:
                # Retrieve the session from Stripe
                session = stripe.checkout.Session.retrieve(session_id)
                
                if session.payment_status == 'paid':
                    # Get metadata
                    metadata = session.get('metadata', {})
                    tier = metadata.get('tier')
                    duration = metadata.get('duration')
                    
                    if tier and duration:
                        # Activate the purchase
                        from auth.membership import activate_purchase
                        license_key = activate_purchase(tier, duration)
                        
                        if license_key:
                            activation_result = "success"
                        else:
                            activation_result = "failed"
                            error_message = "Failed to create license"
                    else:
                        activation_result = "failed"
                        error_message = "Missing tier or duration"
                else:
                    activation_result = "failed"
                    error_message = "Payment not completed"
        except Exception as e:
            activation_result = "failed"
            error_message = str(e)
        
        if activation_result == "success":
            return f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Payment Successful</title>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
                <style>
                    body {{ font-family: 'Inter', -apple-system, sans-serif; background: #0a0b0e; color: #fff; display: flex; align-items: center; justify-content: center; min-height: 100vh; margin: 0; }}
                    .container {{ text-align: center; padding: 60px; background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(16, 185, 129, 0.05)); border: 2px solid rgba(16, 185, 129, 0.4); border-radius: 32px; max-width: 550px; box-shadow: 0 0 80px rgba(16, 185, 129, 0.2); }}
                    .checkmark {{ width: 100px; height: 100px; border-radius: 50%; background: linear-gradient(135deg, #10b981, #059669); display: flex; align-items: center; justify-content: center; margin: 0 auto 32px; animation: scaleIn 0.5s ease-out; }}
                    .checkmark i {{ font-size: 3rem; color: white; }}
                    @keyframes scaleIn {{ from {{ transform: scale(0); }} to {{ transform: scale(1); }} }}
                    h1 {{ font-size: 2.5rem; color: #10b981; margin-bottom: 16px; font-weight: 700; }}
                    p {{ color: #9ca3af; line-height: 1.7; font-size: 1.1rem; margin-bottom: 8px; }}
                    .redirect {{ margin-top: 32px; padding: 16px 40px; background: linear-gradient(135deg, #10b981, #059669); color: #fff; text-decoration: none; border-radius: 16px; font-weight: 600; font-size: 1.1rem; display: inline-block; transition: all 0.3s; }}
                    .redirect:hover {{ transform: translateY(-3px); box-shadow: 0 10px 30px rgba(16, 185, 129, 0.4); }}
                    .countdown {{ font-size: 0.9rem; color: #6b7280; margin-top: 16px; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="checkmark"><i class="fas fa-check"></i></div>
                    <h1>Welcome Aboard!</h1>
                    <p>Your membership has been activated successfully.</p>
                    <p>All features are now unlocked and ready to use.</p>
                    <a href="/" class="redirect"><i class="fas fa-rocket"></i> Launch Application</a>
                    <p class="countdown">Redirecting in <span id="timer">5</span> seconds...</p>
                </div>
                <script>
                    let seconds = 5;
                    const timer = document.getElementById('timer');
                    setInterval(() => {{
                        seconds--;
                        timer.textContent = seconds;
                        if (seconds <= 0) window.location.href = '/';
                    }}, 1000);
                </script>
            </body>
            </html>
            """
        else:
            return f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Activation Issue</title>
                <style>
                    body {{ font-family: -apple-system, sans-serif; background: #0a0b0e; color: #fff; display: flex; align-items: center; justify-content: center; min-height: 100vh; margin: 0; }}
                    .container {{ text-align: center; padding: 40px; background: linear-gradient(135deg, rgba(251, 191, 36, 0.1), rgba(251, 191, 36, 0.05)); border: 2px solid rgba(251, 191, 36, 0.3); border-radius: 24px; max-width: 500px; }}
                    h1 {{ font-size: 2rem; color: #fbbf24; margin-bottom: 16px; }}
                    p {{ color: #9ca3af; line-height: 1.6; }}
                    .icon {{ font-size: 4rem; margin-bottom: 20px; }}
                    a {{ display: inline-block; margin-top: 24px; padding: 12px 32px; background: linear-gradient(135deg, #fbbf24, #f59e0b); color: #000; text-decoration: none; border-radius: 12px; font-weight: 600; }}
                    .error {{ font-size: 0.8rem; color: #ef4444; margin-top: 16px; font-family: monospace; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="icon">⚠️</div>
                    <h1>Activation Processing</h1>
                    <p>Your payment was received but activation is still processing. This usually resolves within a few minutes.</p>
                    <p>Please try refreshing or contact support if this persists.</p>
                    <div class="error">{error_message}</div>
                    <a href="/">Try Again</a>
                </div>
            </body>
            </html>
            """
    
    app.add_url_rule("/payment/success", "payment_success", payment_success, methods=["GET"])
    
    # Payment Cancel Page
    def payment_cancel():
        """Show cancel page if user cancels Stripe payment"""
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Payment Cancelled</title>
            <style>
                body { font-family: -apple-system, sans-serif; background: #0a0b0e; color: #fff; display: flex; align-items: center; justify-content: center; min-height: 100vh; margin: 0; }
                .container { text-align: center; padding: 40px; background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(239, 68, 68, 0.05)); border: 2px solid rgba(239, 68, 68, 0.3); border-radius: 24px; max-width: 500px; }
                h1 { font-size: 2rem; color: #ef4444; margin-bottom: 16px; }
                p { color: #9ca3af; line-height: 1.6; }
                .icon { font-size: 4rem; margin-bottom: 20px; }
                a { display: inline-block; margin-top: 24px; padding: 12px 32px; background: linear-gradient(135deg, #6366f1, #4f46e5); color: #fff; text-decoration: none; border-radius: 12px; font-weight: 600; }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="icon">❌</div>
                <h1>Payment Cancelled</h1>
                <p>Your payment was cancelled. No charges were made. Feel free to try again whenever you're ready.</p>
                <a href="/">Return to Dashboard</a>
            </div>
        </body>
        </html>
        """
    
    app.add_url_rule("/payment/cancel", "payment_cancel", payment_cancel, methods=["GET"])
    
    # Humanizer Statistics API
    def api_humanizer_stats():
        """Get statistics about the humanization system"""
        try:
            from core.mouse_humanizer import get_humanized_controller
            controller = get_humanized_controller()
            
            if controller:
                stats = controller.get_statistics()
                fp = controller.fingerprint
                return {
                    "success": "1",
                    "stats": stats,
                    "fingerprint": {
                        "speed_tendency": round(fp.speed_tendency, 3),
                        "tremor_intensity": round(fp.tremor_intensity, 3),
                        "overshoot_tendency": round(fp.overshoot_tendency, 3),
                        "curve_tightness": round(fp.curve_tightness, 3),
                        "reaction_offset_ms": round(fp.reaction_time_offset_ms, 1)
                    }
                }
            else:
                return {"success": "1", "stats": {}, "message": "Controller not initialized"}
        except Exception as e:
            return {"success": "0", "message": f"Error: {str(e)}"}, 500
    
    app.add_url_rule("/api/humanizer_stats", "humanizer_stats", api_humanizer_stats, methods=["GET"])
    
    # Update Humanizer Settings API
    def api_update_humanizer_settings():
        """Update humanizer settings from the UI. Requires Full Access membership."""
        from flask import request
        try:
            # Check membership permission
            from auth.membership import can_modify_humanizer
            if not can_modify_humanizer():
                return {"success": "0", "message": "Full Access membership required to modify Humanizer settings"}, 403
            
            from core.humanizer_settings import update_from_ui, get_humanizer_settings
            
            data = request.form.to_dict() if request.form else {}
            if not data and request.json:
                data = request.json
            
            updated_count = 0
            for key, value in data.items():
                if update_from_ui(key, value):
                    updated_count += 1
            
            settings = get_humanizer_settings()
            return {
                "success": "1",
                "message": f"Updated {updated_count} settings",
                "current_settings": settings.to_dict()
            }
        except Exception as e:
            return {"success": "0", "message": f"Error: {str(e)}"}, 500
    
    app.add_url_rule("/api/humanizer_settings", "humanizer_settings", api_update_humanizer_settings, methods=["POST"])
    
    # Get Humanizer Settings API
    def api_get_humanizer_settings():
        """Get current humanizer settings"""
        try:
            from core.humanizer_settings import get_humanizer_settings
            settings = get_humanizer_settings()
            return {
                "success": "1",
                "settings": settings.to_dict()
            }
        except Exception as e:
            return {"success": "0", "message": f"Error: {str(e)}"}, 500
    
    app.add_url_rule("/api/humanizer_settings", "get_humanizer_settings", api_get_humanizer_settings, methods=["GET"])
    
    return app

def start_flask_server():
    app = create_app()
    app.run(host="0.0.0.0", port=5000, use_reloader=False)