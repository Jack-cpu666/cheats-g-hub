"""
Professional Subscription Page Template
Modern, clean design - No license keys, just purchases
"""

LICENSE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ APP_NAME }} - Get Access</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        :root {
            --bg-primary: #0a0b0e;
            --bg-secondary: #12141a;
            --bg-card: #1a1d26;
            --accent-gold: #fbbf24;
            --accent-gold-dark: #f59e0b;
            --accent-purple: #8b5cf6;
            --accent-blue: #3b82f6;
            --accent-green: #10b981;
            --accent-red: #ef4444;
            --text-primary: #ffffff;
            --text-secondary: #9ca3af;
            --text-muted: #6b7280;
            --border-subtle: rgba(255, 255, 255, 0.08);
            --glow-gold: rgba(251, 191, 36, 0.4);
            --glow-purple: rgba(139, 92, 246, 0.4);
        }
        
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--bg-primary);
            min-height: 100vh;
            color: var(--text-primary);
            overflow-x: hidden;
        }
        
        /* Animated Background */
        .bg-effects {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
            overflow: hidden;
            pointer-events: none;
        }
        
        .bg-gradient {
            position: absolute;
            width: 150%;
            height: 150%;
            top: -25%;
            left: -25%;
            background: 
                radial-gradient(ellipse at 20% 20%, rgba(139, 92, 246, 0.15) 0%, transparent 50%),
                radial-gradient(ellipse at 80% 80%, rgba(251, 191, 36, 0.1) 0%, transparent 50%),
                radial-gradient(ellipse at 50% 50%, rgba(59, 130, 246, 0.08) 0%, transparent 70%);
            animation: bgRotate 30s linear infinite;
        }
        
        @keyframes bgRotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
        
        .floating-orb {
            position: absolute;
            border-radius: 50%;
            filter: blur(80px);
            opacity: 0.5;
            animation: float 20s ease-in-out infinite;
        }
        
        .orb-1 {
            width: 400px;
            height: 400px;
            background: linear-gradient(135deg, var(--accent-purple), var(--accent-blue));
            top: 10%;
            left: 5%;
            animation-delay: 0s;
        }
        
        .orb-2 {
            width: 300px;
            height: 300px;
            background: linear-gradient(135deg, var(--accent-gold), var(--accent-red));
            bottom: 10%;
            right: 10%;
            animation-delay: -10s;
        }
        
        .orb-3 {
            width: 200px;
            height: 200px;
            background: linear-gradient(135deg, var(--accent-green), var(--accent-blue));
            top: 50%;
            right: 20%;
            animation-delay: -5s;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0) translateX(0); }
            25% { transform: translateY(-30px) translateX(20px); }
            50% { transform: translateY(20px) translateX(-20px); }
            75% { transform: translateY(-20px) translateX(-30px); }
        }
        
        /* Grid Pattern Overlay */
        .grid-pattern {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
            background-size: 60px 60px;
        }
        
        /* Main Container */
        .container {
            position: relative;
            z-index: 1;
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        
        /* Header */
        .header {
            text-align: center;
            margin-bottom: 60px;
        }
        
        .logo-container {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 100px;
            height: 100px;
            background: linear-gradient(135deg, var(--accent-red), #c53030);
            border-radius: 28px;
            margin-bottom: 24px;
            box-shadow: 
                0 20px 40px rgba(239, 68, 68, 0.3),
                0 0 80px rgba(239, 68, 68, 0.2);
            animation: logoPulse 3s ease-in-out infinite;
        }
        
        @keyframes logoPulse {
            0%, 100% { transform: scale(1); box-shadow: 0 20px 40px rgba(239, 68, 68, 0.3), 0 0 80px rgba(239, 68, 68, 0.2); }
            50% { transform: scale(1.05); box-shadow: 0 25px 50px rgba(239, 68, 68, 0.4), 0 0 100px rgba(239, 68, 68, 0.3); }
        }
        
        .logo-icon {
            font-size: 3rem;
            color: white;
        }
        
        .app-title {
            font-size: 3rem;
            font-weight: 800;
            background: linear-gradient(135deg, #fff 0%, #e0e0e0 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 8px;
            letter-spacing: -0.02em;
        }
        
        .app-subtitle {
            font-size: 1.125rem;
            color: var(--text-secondary);
            font-weight: 400;
        }
        
        .app-subtitle span {
            color: var(--accent-gold);
            font-weight: 600;
        }
        
        /* Tagline */
        .tagline {
            margin-bottom: 50px;
            text-align: center;
        }
        
        .tagline h2 {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 16px;
            background: linear-gradient(135deg, var(--accent-gold), var(--accent-gold-dark));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .tagline p {
            font-size: 1.125rem;
            color: var(--text-secondary);
            max-width: 600px;
            margin: 0 auto;
            line-height: 1.6;
        }
        
        /* Pricing Cards Container */
        .pricing-container {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 32px;
            width: 100%;
            max-width: 900px;
            margin-bottom: 40px;
        }
        
        /* Pricing Card */
        .pricing-card {
            position: relative;
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: 24px;
            padding: 40px;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            overflow: hidden;
        }
        
        .pricing-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, var(--accent-purple), var(--accent-blue));
            opacity: 0;
            transition: opacity 0.3s;
        }
        
        .pricing-card:hover {
            transform: translateY(-8px);
            border-color: rgba(139, 92, 246, 0.3);
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
        }
        
        .pricing-card:hover::before {
            opacity: 1;
        }
        
        .pricing-card.selected {
            border-color: var(--accent-gold);
            box-shadow: 0 0 60px var(--glow-gold);
        }
        
        .pricing-card.selected::before {
            background: linear-gradient(90deg, var(--accent-gold), var(--accent-gold-dark));
            opacity: 1;
        }
        
        /* Premium Card Styling */
        .pricing-card.premium {
            background: linear-gradient(135deg, rgba(251, 191, 36, 0.1), rgba(245, 158, 11, 0.05));
            border-color: rgba(251, 191, 36, 0.3);
        }
        
        .pricing-card.premium::before {
            background: linear-gradient(90deg, var(--accent-gold), var(--accent-gold-dark));
            opacity: 1;
        }
        
        .pricing-card.premium.selected {
            box-shadow: 0 0 80px var(--glow-gold), 0 20px 60px rgba(0, 0, 0, 0.4);
        }
        
        /* Popular Badge */
        .popular-badge {
            position: absolute;
            top: 16px;
            right: 16px;
            background: linear-gradient(135deg, var(--accent-gold), var(--accent-gold-dark));
            color: #000;
            font-size: 0.7rem;
            font-weight: 700;
            padding: 6px 12px;
            border-radius: 20px;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            display: flex;
            align-items: center;
            gap: 4px;
        }
        
        /* Card Content */
        .card-icon {
            font-size: 3rem;
            margin-bottom: 20px;
        }
        
        .card-name {
            font-size: 1.75rem;
            font-weight: 700;
            margin-bottom: 8px;
        }
        
        .pricing-card.premium .card-name {
            background: linear-gradient(135deg, var(--accent-gold), var(--accent-gold-dark));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .card-description {
            font-size: 0.9rem;
            color: var(--text-secondary);
            margin-bottom: 24px;
            line-height: 1.5;
        }
        
        .card-price {
            margin-bottom: 24px;
        }
        
        .price-amount {
            font-size: 3rem;
            font-weight: 800;
            letter-spacing: -0.02em;
        }
        
        .price-period {
            font-size: 1rem;
            color: var(--text-muted);
            margin-left: 4px;
        }
        
        .price-note {
            font-size: 0.8rem;
            color: var(--text-muted);
            margin-top: 4px;
        }
        
        /* Features List */
        .features-list {
            list-style: none;
            margin-bottom: 32px;
        }
        
        .features-list li {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 10px 0;
            font-size: 0.95rem;
            color: var(--text-primary);
        }
        
        .features-list li i {
            font-size: 0.875rem;
            width: 20px;
            text-align: center;
        }
        
        .features-list li i.fa-check {
            color: var(--accent-green);
        }
        
        .features-list li i.fa-times {
            color: var(--text-muted);
        }
        
        .features-list li.disabled {
            color: var(--text-muted);
        }
        
        .feature-badge {
            font-size: 0.65rem;
            font-weight: 600;
            padding: 2px 8px;
            border-radius: 10px;
            background: rgba(251, 191, 36, 0.2);
            color: var(--accent-gold);
            margin-left: 8px;
        }
        
        /* Select Button */
        .select-btn {
            width: 100%;
            padding: 16px 24px;
            border: 2px solid var(--border-subtle);
            border-radius: 14px;
            background: transparent;
            color: var(--text-primary);
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }
        
        .select-btn:hover {
            border-color: var(--accent-purple);
            background: rgba(139, 92, 246, 0.1);
        }
        
        .pricing-card.selected .select-btn {
            background: linear-gradient(135deg, var(--accent-gold), var(--accent-gold-dark));
            border-color: transparent;
            color: #000;
        }
        
        .pricing-card.premium .select-btn {
            background: linear-gradient(135deg, var(--accent-gold), var(--accent-gold-dark));
            border-color: transparent;
            color: #000;
        }
        
        /* Duration Selector */
        .duration-section {
            width: 100%;
            max-width: 500px;
            margin-bottom: 32px;
        }
        
        .duration-label {
            font-size: 0.875rem;
            font-weight: 600;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 12px;
            text-align: center;
        }
        
        .duration-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
        }
        
        .duration-btn {
            padding: 14px 8px;
            background: var(--bg-card);
            border: 1px solid var(--border-subtle);
            border-radius: 12px;
            color: var(--text-secondary);
            font-size: 0.85rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s;
            text-align: center;
        }
        
        .duration-btn:hover {
            border-color: var(--accent-purple);
            color: var(--text-primary);
        }
        
        .duration-btn.selected {
            background: linear-gradient(135deg, var(--accent-purple), var(--accent-blue));
            border-color: transparent;
            color: white;
        }
        
        .duration-btn .price {
            display: block;
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--text-primary);
            margin-top: 4px;
        }
        
        .duration-btn.selected .price {
            color: white;
        }
        
        .duration-btn.best-value {
            position: relative;
        }
        
        .duration-btn.best-value::after {
            content: 'BEST';
            position: absolute;
            top: -8px;
            right: -8px;
            background: var(--accent-green);
            color: white;
            font-size: 0.6rem;
            font-weight: 700;
            padding: 2px 6px;
            border-radius: 6px;
        }
        
        /* Purchase Button */
        .purchase-section {
            width: 100%;
            max-width: 500px;
        }
        
        .purchase-btn {
            width: 100%;
            padding: 20px 32px;
            background: linear-gradient(135deg, var(--accent-green), #059669);
            border: none;
            border-radius: 16px;
            color: white;
            font-size: 1.25rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            box-shadow: 0 10px 40px rgba(16, 185, 129, 0.3);
        }
        
        .purchase-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 50px rgba(16, 185, 129, 0.4);
        }
        
        .purchase-btn:disabled {
            opacity: 0.7;
            cursor: not-allowed;
            transform: none;
        }
        
        .purchase-btn.gold {
            background: linear-gradient(135deg, var(--accent-gold), var(--accent-gold-dark));
            color: #000;
            box-shadow: 0 10px 40px var(--glow-gold);
        }
        
        .purchase-btn.gold:hover {
            box-shadow: 0 15px 50px var(--glow-gold);
        }
        
        /* UUID Display */
        .uuid-display {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            margin-top: 20px;
            padding: 12px 20px;
            background: rgba(0, 0, 0, 0.3);
            border: 1px solid var(--border-subtle);
            border-radius: 12px;
            color: var(--text-muted);
            font-size: 0.8rem;
        }
        
        .uuid-display i {
            color: var(--accent-purple);
            font-size: 1rem;
        }
        
        .uuid-display code {
            font-family: 'SF Mono', 'Consolas', monospace;
            color: var(--text-secondary);
            background: rgba(139, 92, 246, 0.15);
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.75rem;
            letter-spacing: 0.5px;
        }
        
        /* Trust Badges */
        .trust-section {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 32px;
            margin-top: 32px;
            padding-top: 32px;
            border-top: 1px solid var(--border-subtle);
            width: 100%;
            max-width: 600px;
        }
        
        .trust-badge {
            display: flex;
            align-items: center;
            gap: 8px;
            color: var(--text-muted);
            font-size: 0.85rem;
        }
        
        .trust-badge i {
            font-size: 1.1rem;
            color: var(--accent-green);
        }
        
        /* Error/Success Messages */
        .message {
            width: 100%;
            max-width: 500px;
            padding: 16px 20px;
            border-radius: 12px;
            margin-bottom: 24px;
            display: none;
            align-items: center;
            gap: 12px;
            font-size: 0.95rem;
        }
        
        .message.error {
            display: flex;
            background: rgba(239, 68, 68, 0.1);
            border: 1px solid rgba(239, 68, 68, 0.3);
            color: var(--accent-red);
        }
        
        .message.success {
            display: flex;
            background: rgba(16, 185, 129, 0.1);
            border: 1px solid rgba(16, 185, 129, 0.3);
            color: var(--accent-green);
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .pricing-container {
                grid-template-columns: 1fr;
                max-width: 400px;
            }
            
            .duration-grid {
                grid-template-columns: repeat(2, 1fr);
            }
            
            .app-title {
                font-size: 2.25rem;
            }
            
            .tagline h2 {
                font-size: 1.75rem;
            }
            
            .trust-section {
                flex-direction: column;
                gap: 16px;
            }
        }
        
        /* Animations */
        .fade-in {
            animation: fadeIn 0.6s ease-out forwards;
            opacity: 0;
        }
        
        .fade-in-delay-1 { animation-delay: 0.1s; }
        .fade-in-delay-2 { animation-delay: 0.2s; }
        .fade-in-delay-3 { animation-delay: 0.3s; }
        .fade-in-delay-4 { animation-delay: 0.4s; }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>
    <!-- Background Effects -->
    <div class="bg-effects">
        <div class="bg-gradient"></div>
        <div class="floating-orb orb-1"></div>
        <div class="floating-orb orb-2"></div>
        <div class="floating-orb orb-3"></div>
        <div class="grid-pattern"></div>
    </div>
    
    <div class="container">
        <!-- Header -->
        <header class="header fade-in">
            <div class="logo-container">
                <i class="fas fa-crosshairs logo-icon"></i>
            </div>
            <h1 class="app-title">{{ APP_NAME }}</h1>
            <p class="app-subtitle">v{{ APP_VERSION }} • <span>Holiday Edition</span></p>
        </header>
        
        <!-- Tagline -->
        <div class="tagline fade-in fade-in-delay-1">
            <h2>Start Your Valorant Journey With A Bang</h2>
            <p>Dominate every match from day one. Weekly updates, undetected gameplay, legendary results.</p>
        </div>
        
        <!-- Error/Success Messages -->
        <div id="messageBox" class="message"></div>
        
        <!-- Pricing Cards -->
        <div class="pricing-container fade-in fade-in-delay-2">
            <!-- Regular Tier -->
            <div class="pricing-card" id="cardRegular" onclick="selectTier('regular')">
                <div class="card-icon">🎯</div>
                <h3 class="card-name">Regular</h3>
                <p class="card-description">Essential features for getting started with aim training and improvement.</p>
                
                <div class="card-price">
                    <span class="price-amount" id="priceRegular">$24.99</span>
                    <span class="price-period">/month</span>
                </div>
                
                <ul class="features-list">
                    <li><i class="fas fa-check"></i> Aimbot Engine</li>
                    <li><i class="fas fa-check"></i> Humanizer <span class="feature-badge">VIEW ONLY</span></li>
                    <li><i class="fas fa-check"></i> Fingerprint <span class="feature-badge">STATIC</span></li>
                    <li><i class="fas fa-check"></i> Web Dashboard</li>
                    <li class="disabled"><i class="fas fa-times"></i> Triggerbot</li>
                    <li class="disabled"><i class="fas fa-times"></i> Crosshair Overlay</li>
                    <li class="disabled"><i class="fas fa-times"></i> Anti-Recoil</li>
                </ul>
                
                <button class="select-btn">
                    <i class="fas fa-check-circle"></i>
                    Select Plan
                </button>
            </div>
            
            <!-- Full Access Tier -->
            <div class="pricing-card premium selected" id="cardFull" onclick="selectTier('full_access')">
                <div class="popular-badge"><i class="fas fa-crown"></i> MOST POPULAR</div>
                <div class="card-icon">👑</div>
                <h3 class="card-name">Full Access</h3>
                <p class="card-description">Complete toolkit with all features unlocked and full customization control.</p>
                
                <div class="card-price">
                    <span class="price-amount" id="priceFull">$49.99</span>
                    <span class="price-period">/month</span>
                </div>
                
                <ul class="features-list">
                    <li><i class="fas fa-check"></i> Everything in Regular</li>
                    <li><i class="fas fa-check"></i> Triggerbot</li>
                    <li><i class="fas fa-check"></i> Crosshair Overlay</li>
                    <li><i class="fas fa-check"></i> Anti-Recoil System</li>
                    <li><i class="fas fa-check"></i> Modify Humanizer Settings</li>
                    <li><i class="fas fa-check"></i> Regenerate Fingerprint</li>
                    <li><i class="fas fa-check"></i> Priority Support</li>
                </ul>
                
                <button class="select-btn">
                    <i class="fas fa-crown"></i>
                    Select Plan
                </button>
            </div>
        </div>
        
        <!-- Duration Selector -->
        <div class="duration-section fade-in fade-in-delay-3">
            <div class="duration-label">Choose Duration</div>
            <div class="duration-grid">
                <button class="duration-btn" data-duration="1_week" onclick="selectDuration('1_week')">
                    1 Week
                    <span class="price" id="dur_1_week">$19.99</span>
                </button>
                <button class="duration-btn selected" data-duration="1_month" onclick="selectDuration('1_month')">
                    1 Month
                    <span class="price" id="dur_1_month">$49.99</span>
                </button>
                <button class="duration-btn best-value" data-duration="1_year" onclick="selectDuration('1_year')">
                    1 Year
                    <span class="price" id="dur_1_year">$299.99</span>
                </button>
                <button class="duration-btn" data-duration="lifetime" onclick="selectDuration('lifetime')">
                    Lifetime
                    <span class="price" id="dur_lifetime">$499.99</span>
                </button>
            </div>
        </div>
        
        <!-- Purchase Button -->
        <div class="purchase-section fade-in fade-in-delay-4">
            <button class="purchase-btn gold" id="purchaseBtn" onclick="startPurchase()">
                <i class="fas fa-bolt"></i>
                <span id="purchaseBtnText">Get Full Access - $49.99</span>
            </button>
            
            <!-- UUID Display -->
            <div class="uuid-display">
                <i class="fas fa-fingerprint"></i>
                <span>Your Device ID: <code>{{ HWID }}</code></span>
            </div>
        </div>
        
        <!-- Trust Badges -->
        <div class="trust-section fade-in fade-in-delay-4">
            <div class="trust-badge">
                <i class="fas fa-shield-alt"></i>
                Secure Payment
            </div>
            <div class="trust-badge">
                <i class="fas fa-lock"></i>
                Hardware Encrypted
            </div>
            <div class="trust-badge">
                <i class="fas fa-bolt"></i>
                Instant Access
            </div>
        </div>
        
        <!-- Transfer Code Section -->
        <div class="transfer-section fade-in fade-in-delay-4" style="margin-top: 60px; padding: 32px; background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 20px; max-width: 500px; margin-left: auto; margin-right: auto;">
            <div style="text-align: center; margin-bottom: 20px;">
                <i class="fas fa-exchange-alt" style="font-size: 2rem; color: #10b981; margin-bottom: 12px;"></i>
                <h3 style="font-size: 1.25rem; font-weight: 600; color: var(--text-primary);">Transferring from another PC?</h3>
                <p style="color: var(--text-secondary); font-size: 0.9rem; margin-top: 8px;">Enter your transfer code to claim your license</p>
            </div>
            <div style="display: flex; gap: 12px; justify-content: center;">
                <input type="text" id="transferCodeInput" placeholder="ABC123" maxlength="6" 
                       style="width: 160px; padding: 14px 20px; background: rgba(0,0,0,0.4); border: 2px solid rgba(16, 185, 129, 0.4); border-radius: 12px; color: var(--text-primary); text-align: center; font-size: 1.5rem; font-weight: 700; letter-spacing: 6px; text-transform: uppercase; font-family: 'JetBrains Mono', monospace;">
                <button onclick="redeemTransferCode()" 
                        style="padding: 14px 28px; background: linear-gradient(135deg, #10b981, #059669); border: none; border-radius: 12px; color: white; font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 8px; font-size: 1rem; transition: all 0.3s ease;">
                    <i class="fas fa-check"></i> Claim License
                </button>
            </div>
            <div id="transferResult" style="margin-top: 16px; text-align: center; display: none;"></div>
        </div>
    </div>
    
    <script>
        let selectedTier = 'full_access';
        let selectedDuration = '1_month';
        
        const pricing = {
            regular: {
                '1_day': 2.99,
                '1_week': 9.99,
                '2_weeks': 14.99,
                '1_month': 24.99,
                '3_months': 59.99,
                '1_year': 149.99,
                'lifetime': 299.99
            },
            full_access: {
                '1_day': 4.99,
                '1_week': 19.99,
                '2_weeks': 29.99,
                '1_month': 49.99,
                '3_months': 119.99,
                '1_year': 299.99,
                'lifetime': 499.99
            }
        };
        
        function selectTier(tier) {
            selectedTier = tier;
            
            // Update card selection
            document.querySelectorAll('.pricing-card').forEach(card => card.classList.remove('selected'));
            document.getElementById(tier === 'regular' ? 'cardRegular' : 'cardFull').classList.add('selected');
            
            // Update duration prices and button
            updatePrices();
        }
        
        function selectDuration(duration) {
            selectedDuration = duration;
            
            // Update button selection
            document.querySelectorAll('.duration-btn').forEach(btn => btn.classList.remove('selected'));
            document.querySelector(`[data-duration="${duration}"]`).classList.add('selected');
            
            // Update purchase button
            updatePurchaseButton();
        }
        
        function updatePrices() {
            // Update duration buttons with current tier prices
            const tierPricing = pricing[selectedTier];
            
            document.getElementById('dur_1_week').textContent = '$' + tierPricing['1_week'].toFixed(2);
            document.getElementById('dur_1_month').textContent = '$' + tierPricing['1_month'].toFixed(2);
            document.getElementById('dur_1_year').textContent = '$' + tierPricing['1_year'].toFixed(2);
            document.getElementById('dur_lifetime').textContent = '$' + tierPricing['lifetime'].toFixed(2);
            
            updatePurchaseButton();
        }
        
        function updatePurchaseButton() {
            const price = pricing[selectedTier][selectedDuration];
            const tierName = selectedTier === 'full_access' ? 'Full Access' : 'Regular';
            const btn = document.getElementById('purchaseBtn');
            const btnText = document.getElementById('purchaseBtnText');
            
            btnText.textContent = `Get ${tierName} - $${price.toFixed(2)}`;
            
            if (selectedTier === 'full_access') {
                btn.className = 'purchase-btn gold';
            } else {
                btn.className = 'purchase-btn';
            }
        }
        
        async function startPurchase() {
            const btn = document.getElementById('purchaseBtn');
            const messageBox = document.getElementById('messageBox');
            
            btn.disabled = true;
            btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';
            messageBox.className = 'message';
            messageBox.style.display = 'none';
            
            try {
                const response = await fetch('/api/membership/create_checkout', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        tier: selectedTier,
                        duration: selectedDuration
                    })
                });
                
                const data = await response.json();
                
                if (data.success && data.checkout_url) {
                    window.location.href = data.checkout_url;
                } else {
                    showMessage('error', data.message || 'Failed to create checkout. Please try again.');
                    btn.disabled = false;
                    updatePurchaseButton();
                }
            } catch (error) {
                showMessage('error', 'Connection error. Please check your internet and try again.');
                btn.disabled = false;
                updatePurchaseButton();
            }
        }
        
        function showMessage(type, text) {
            const messageBox = document.getElementById('messageBox');
            messageBox.className = `message ${type}`;
            messageBox.innerHTML = `<i class="fas fa-${type === 'error' ? 'exclamation-circle' : 'check-circle'}"></i> ${text}`;
            messageBox.style.display = 'flex';
        }
        
        async function redeemTransferCode() {
            const code = document.getElementById('transferCodeInput').value.trim().toUpperCase();
            const resultDiv = document.getElementById('transferResult');
            
            if (!code || code.length !== 6) {
                resultDiv.style.display = 'block';
                resultDiv.innerHTML = '<span style="color: #f59e0b;"><i class="fas fa-exclamation-triangle"></i> Please enter a valid 6-character code</span>';
                return;
            }
            
            resultDiv.style.display = 'block';
            resultDiv.innerHTML = '<span style="color: var(--text-secondary);"><i class="fas fa-spinner fa-spin"></i> Validating...</span>';
            
            try {
                const response = await fetch('/api/membership/transfer/redeem', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ transfer_code: code })
                });
                
                const data = await response.json();
                
                if (data.success) {
                    resultDiv.innerHTML = '<span style="color: #10b981;"><i class="fas fa-check-circle"></i> ' + (data.message || 'License claimed! Redirecting...') + '</span>';
                    // Redirect to main app after short delay
                    setTimeout(() => {
                        window.location.href = '/';
                    }, 2000);
                } else {
                    resultDiv.innerHTML = '<span style="color: #ef4444;"><i class="fas fa-times-circle"></i> ' + (data.message || 'Invalid transfer code') + '</span>';
                }
            } catch (error) {
                resultDiv.innerHTML = '<span style="color: #ef4444;"><i class="fas fa-times-circle"></i> Connection error. Please try again.</span>';
            }
        }
        
        // Initialize
        updatePrices();
    </script>
</body>
</html>
"""
