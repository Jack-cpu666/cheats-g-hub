# Auto-generated from v6 claude.txt
HTML_TEMPLATE = r"""
<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ APP_NAME }} Control Panel</title>
    <link id="favicon" rel="icon" type="image/png" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAIRlWElmTU0AKgAAAAgABQESAAMAAAABAAEAAAEaAAUAAAABAAAASgEbAAUAAAABAAAAUgEoAAMAAAABAAIAAIdpAAQAAAABAAAAWgAAAAAAAACQAAAAAQAAAJAAAAABAAOgAQADAAAAAQABAACgAgAEAAAAAQAAABCgAwAEAAAAAQAAABAAAAAIMLSbAAAAEXRFWHRTb2Z0d2FyZQBTbmlwYXN0ZV0Xzt0AAAGSSURBVDhPtZNLaxNRFIbP+/fejWcam3QDbZNWYYgUQSgoBURcCLpy70L9F3z6S3wVfAlLuPAlEAoqIC5EVJA2iahpUmM2abLpZt7OOxvxKS4MDDhnvg/nHLh9C8Lg97Xe6et7uTzxt8Ab9f3Xy+q3eVjq7RFrF6m7zUM9Gqs9z4X+L7Z6Wfy0XqDEZnLyfSj9Y+lHPxqW6rQPGpnjciGYs2zcXmMkP2WXI2s23YGFuo/P1M7G7Psb7j0rSYUK9aI1PBolV8rM9VbHx0z0s7n1NfW4w+dtuBPa9q8C7F6V6sHhHqWd3D2u9AQSNe70r2RBiEgRERkE4hBC4KEM7KIIBGTwiEEAhLsjCoJgSCIUgEEAkJIKHEBEJCRJCQ4gIkYZEQhIUQUOJ+CJDGRiQke0FDMiIpIZWUhkZSkjSAhyUUkeYMo7QRP02pSExl51SjW9G2aJ/M5BmtJvAhC0DFN80mUMzHYY4sa0zV1K80uVyyLpdVSNaRiqjBWZcbGgUloSyvjXWJ//85/AB3wD2m8FwH/Bi6tAAAAAElFTkSuQmCC">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    :root {
        /* Christmas Theme Colors */
        --bg-primary: #0b1016; /* Deep Winter Night */
        --bg-secondary: #121820;
        --bg-tertiary: #1a222e;
        --bg-quaternary: #222b3a;
        --bg-glass: rgba(26, 34, 46, 0.85); /* Frosty Glass */
        
        /* Text Colors */
        --text-primary: #f0f4f8; /* Snow White */
        --text-secondary: #b0b8c4; /* Silver */
        --text-tertiary: #6b7a8f;
        --text-accent: #e2e8f0;
        
        /* Christmas Accents */
        --accent-primary: #ff3b3b; /* Santa Red */
        --accent-secondary: #00d66b; /* Mistletoe Green */
        --accent-tertiary: #3b82f6; /* Ice Blue */
        --accent-quaternary: #fbbf24; /* Golden Star */
        --accent-danger: #ef4444; 
        --accent-warning: #f59e0b;
        
        /* Gradients */
        --gradient-primary: linear-gradient(135deg, #ff3b3b 0%, #c53030 100%); /* Candy Cane */
        --gradient-secondary: linear-gradient(135deg, #00d66b 0%, #059669 100%); /* Pine Tree */
        --gradient-success: linear-gradient(135deg, #10B981 0%, #059669 100%);
        --gradient-danger: linear-gradient(135deg, #EF4444 0%, #DC2626 100%);
        --gradient-glass: linear-gradient(135deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0.02) 100%);
        
        /* Spacing */
        --space-1: 0.25rem;
        --space-2: 0.5rem;
        --space-3: 0.75rem;
        --space-4: 1rem;
        --space-5: 1.25rem;
        --space-6: 1.5rem;
        --space-8: 2rem;
        --space-10: 2.5rem;
        --space-12: 3rem;
        --space-16: 4rem;
        
        /* Border Radius */
        --radius-sm: 0.375rem;
        --radius-md: 0.5rem;
        --radius-lg: 0.75rem;
        --radius-xl: 1rem;
        --radius-2xl: 1.5rem;
        
        /* Shadows */
        --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
        --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
        --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
        --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
        --shadow-2xl: 0 25px 50px -12px rgb(0 0 0 / 0.25);
        --shadow-glow: 0 0 20px rgba(255, 59, 59, 0.4); /* Red Glow */
        --shadow-glow-lg: 0 0 40px rgba(255, 59, 59, 0.5); /* Intense Red Glow */
        
        /* Transitions */
        --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
        --transition-normal: 250ms cubic-bezier(0.4, 0, 0.2, 1);
        --transition-slow: 350ms cubic-bezier(0.4, 0, 0.2, 1);
        
        /* Typography */
        --font-sans: 'Space Grotesk', system-ui, -apple-system, sans-serif;
        --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
        
        /* Layout */
        --sidebar-width: 280px;
        --header-height: 72px;
    }

    /* Christmas Lights Animation */
    @keyframes flash-1 { 0%, 100% { opacity: 1; } 50% { opacity: 0.4; } }
    @keyframes flash-2 { 0%, 100% { opacity: 0.4; } 50% { opacity: 1; } }
    @keyframes flash-3 { 0%, 100% { opacity: 0.6; } 50% { opacity: 1; } }
    
    /* Scale In Animation for modals */
    @keyframes scaleIn {
        from { transform: scale(0.8); opacity: 0; }
        to { transform: scale(1); opacity: 1; }
    }

    /* Candy Cane Border */
    .card-header::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 2px;
        background: repeating-linear-gradient(
            45deg,
            var(--accent-primary),
            var(--accent-primary) 10px,
            #ffffff 10px,
            #ffffff 20px
        );
        opacity: 0.6;
    }

    /* Aurora Borealis Animation */
    @keyframes aurora {
        0% { background-position: 50% 50%, 50% 50%; }
        50% { background-position: 100% 0%, 0% 100%; }
        100% { background-position: 50% 50%, 50% 50%; }
    }

    /* Falling Snow Animation */
    @keyframes fall {
        0% { transform: translateY(-100vh) rotate(0deg); opacity: 0; }
        10% { opacity: 0.9; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    
    .snow-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 9999;
        overflow: hidden;
    }
    
    .snowflake {
        position: absolute;
        top: -10px;
        color: #fff;
        opacity: 0.8;
        font-size: 1.2rem;
        animation: fall linear infinite;
        text-shadow: 0 0 5px rgba(255,255,255,0.8);
    }

    html {
        font-family: var(--font-sans);
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }

    body {
        background-color: var(--bg-primary);
        color: var(--text-primary);
        overflow: hidden;
        height: 100vh;
        position: relative;
        
        /* Aurora Borealis Gradients */
        background-image: 
            radial-gradient(circle at top left, rgba(0, 255, 127, 0.15), transparent 60%), /* Spring Green */
            radial-gradient(circle at top right, rgba(138, 43, 226, 0.15), transparent 60%), /* Blue Violet */
            radial-gradient(circle at bottom, rgba(0, 191, 255, 0.1), transparent 70%); /* Deep Sky Blue */
            
        background-size: 200% 200%;
        animation: aurora 15s ease infinite alternate;
    }
    
    /* Frosty Noise Texture Overlay */
    body::after {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.05'/%3E%3C/svg%3E");
        pointer-events: none;
        z-index: 0;
        opacity: 0.4;
    }

    /* Vignette for Frosty Edges */
    .app-container {
        position: relative;
        z-index: 1;
        box-shadow: inset 0 0 150px rgba(0,0,0,0.7); /* Inner shadow for depth */
        height: 100vh;
        width: 100vw;
        display: flex;
    }
    /* Hanging Christmas Lights */
    .light-rope {
        text-align: center;
        white-space: nowrap;
        overflow: hidden;
        position: absolute;
        z-index: 10000; /* Above snow */
        margin: -15px 0 0 0;
        padding: 0;
        pointer-events: none;
        width: 100%;
        display: flex;
        justify-content: space-evenly;
    }

    .light-bulb {
        position: relative;
        display: inline-block;
        background: rgba(0, 255, 127, 0.4);
        width: 14px;
        height: 28px;
        border-radius: 50%;
        margin: 20px 20px;
        z-index: 1;
        transform-origin: 50% -15px;
        animation: swing 3s ease-in-out infinite alternate;
        box-shadow: 0px 5px 20px 2px rgba(0, 255, 127, 0.5);
    }
    
    .light-bulb::before { /* Wire */
        content: "";
        position: absolute;
        background: #222;
        width: 100px;
        height: 2px;
        border-radius: 50%;
        top: -15px;
        left: -50px;
        z-index: -1;
        border-bottom: 2px solid #555;
    }

    .light-bulb:nth-child(2n) {
        background: rgba(0, 255, 255, 0.4);
        box-shadow: 0px 5px 20px 2px rgba(0, 255, 255, 0.5);
        animation-duration: 3.5s;
    }
    .light-bulb:nth-child(3n) {
        background: rgba(255, 0, 255, 0.4);
        box-shadow: 0px 5px 20px 2px rgba(255, 0, 255, 0.5);
        animation-duration: 4s;
    }
    .light-bulb:nth-child(4n) {
        background: rgba(255, 59, 59, 0.4);
        box-shadow: 0px 5px 20px 2px rgba(255, 59, 59, 0.5);
        animation-duration: 4.5s;
    }
    .light-bulb:nth-child(5n) {
        background: rgba(255, 215, 0, 0.4);
        box-shadow: 0px 5px 20px 2px rgba(255, 215, 0, 0.5);
        animation-duration: 5s;
    }

    @keyframes swing {
        0% { transform: rotate(5deg); }
        100% { transform: rotate(-5deg); }
    }

    /* Winter Landscape Footer */
    .winter-footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 15vh;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 320'%3E%3Cpath fill='%23ffffff' fill-opacity='0.1' d='M0,224L48,213.3C96,203,192,181,288,181.3C384,181,480,203,576,224C672,245,768,267,864,261.3C960,256,1056,224,1152,197.3C1248,171,1344,149,1392,138.7L1440,128L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z'%3E%3C/path%3E%3Cpath fill='%23ffffff' fill-opacity='0.05' d='M0,160L48,176C96,192,192,224,288,229.3C384,235,480,213,576,192C672,171,768,149,864,160C960,171,1056,213,1152,224C1248,235,1344,213,1392,202.7L1440,192L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z'%3E%3C/path%3E%3C/svg%3E");
        background-repeat: no-repeat;
        background-position: bottom;
        background-size: cover;
        pointer-events: none;
        z-index: 0;
    }

    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 6px;
        height: 6px;
    }

    ::-webkit-scrollbar-track {
        background: var(--bg-tertiary);
        border-radius: var(--radius-lg);
    }

    ::-webkit-scrollbar-thumb {
        background: var(--gradient-primary);
        border-radius: var(--radius-lg);
    }

    ::-webkit-scrollbar-thumb:hover {
        background: var(--gradient-secondary);
    }

    /* Layout */
    .app-container {
        display: flex;
        height: 100vh;
        overflow: hidden;
    }

    /* Sidebar */
    .sidebar {
        width: var(--sidebar-width);
        background: var(--bg-glass);
        backdrop-filter: blur(20px) saturate(180%);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
        display: flex;
        flex-direction: column;
        position: relative;
        z-index: 50;
    }

    .sidebar::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: var(--gradient-primary);
        z-index: 1;
    }

    .sidebar-header {
        padding: var(--space-8);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        position: relative;
    }

    .logo {
        display: flex;
        align-items: center;
        gap: var(--space-3);
        margin-bottom: var(--space-4);
    }

    .logo-icon {
        width: 40px;
        height: 40px;
        background: var(--gradient-primary);
        border-radius: var(--radius-xl);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.25rem;
        box-shadow: var(--shadow-glow);
        animation: logoFloat 3s ease-in-out infinite;
    }

    @keyframes logoFloat {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-5px) rotate(5deg); }
    }

    .logo-text {
        flex: 1;
    }

    .logo-title {
        font-size: 1.25rem;
        font-weight: 700;
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.2;
    }

    .logo-version {
        font-size: 0.75rem;
        color: var(--text-secondary);
        font-family: var(--font-mono);
        opacity: 0.8;
    }

    /* Navigation */
    .nav {
        flex: 1;
        padding: var(--space-6);
        overflow-y: auto;
    }

    .nav-list {
        list-style: none;
        display: flex;
        flex-direction: column;
        gap: var(--space-2);
    }

    .nav-item {
        position: relative;
    }

    .nav-link {
        display: flex;
        align-items: center;
        gap: var(--space-3);
        padding: var(--space-4);
        color: var(--text-secondary);
        text-decoration: none;
        border-radius: var(--radius-lg);
        transition: all var(--transition-normal);
        position: relative;
        overflow: hidden;
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid transparent;
    }

    .nav-link::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: var(--gradient-glass);
        transition: left var(--transition-normal);
    }

    .nav-link:hover {
        color: var(--text-primary);
        background: rgba(255, 255, 255, 0.05);
        border-color: rgba(99, 102, 241, 0.3);
        transform: translateX(4px);
        box-shadow: var(--shadow-lg);
    }

    .nav-link:hover::before {
        left: 0;
    }

    .nav-link.active {
        color: var(--text-primary);
        background: var(--gradient-primary);
        border-color: var(--accent-primary);
        box-shadow: var(--shadow-glow);
        transform: translateX(4px);
    }

    .nav-icon {
        width: 20px;
        height: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        z-index: 1;
    }

    .nav-text {
        font-weight: 500;
        position: relative;
        z-index: 1;
    }

    /* Anti-Detection Danger Navigation Item */
    .nav-item-danger {
        margin-top: var(--space-4);
        padding-top: var(--space-4);
        border-top: 1px solid rgba(239, 68, 68, 0.3);
    }

    .nav-link-danger {
        background: rgba(239, 68, 68, 0.1) !important;
        border: 1px solid rgba(239, 68, 68, 0.3) !important;
    }

    .nav-link-danger:hover {
        background: rgba(239, 68, 68, 0.2) !important;
        border-color: rgba(239, 68, 68, 0.5) !important;
        box-shadow: 0 0 20px rgba(239, 68, 68, 0.3) !important;
    }

    .nav-link-danger.active {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%) !important;
        box-shadow: 0 0 25px rgba(239, 68, 68, 0.5) !important;
    }

    .nav-badge-danger {
        margin-left: auto;
        color: #ef4444;
        font-size: 0.75rem;
        animation: dangerPulse 2s infinite;
    }

    @keyframes dangerPulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.6; transform: scale(1.1); }
    }

    /* Tooltip Styles for Help Icons */
    .setting-row {
        position: relative;
    }

    .help-tooltip {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 18px;
        height: 18px;
        background: rgba(59, 130, 246, 0.2);
        color: var(--accent-tertiary);
        border-radius: 50%;
        font-size: 0.7rem;
        cursor: help;
        margin-left: var(--space-2);
        position: relative;
        transition: all var(--transition-fast);
    }

    .help-tooltip:hover {
        background: rgba(59, 130, 246, 0.4);
        transform: scale(1.1);
    }

    .help-tooltip .tooltip-content {
        position: absolute;
        bottom: 130%;
        left: 50%;
        transform: translateX(-50%);
        background: var(--bg-quaternary);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: var(--radius-md);
        padding: var(--space-3) var(--space-4);
        width: 280px;
        font-size: 0.8rem;
        color: var(--text-secondary);
        line-height: 1.5;
        box-shadow: var(--shadow-xl);
        opacity: 0;
        visibility: hidden;
        transition: all var(--transition-fast);
        z-index: 1000;
        pointer-events: none;
    }

    .help-tooltip .tooltip-content::after {
        content: '';
        position: absolute;
        top: 100%;
        left: 50%;
        transform: translateX(-50%);
        border: 8px solid transparent;
        border-top-color: var(--bg-quaternary);
    }

    .help-tooltip:hover .tooltip-content {
        opacity: 1;
        visibility: visible;
    }

    /* Anti-Detection Warning Banner */
    .antidetect-warning {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.15) 0%, rgba(220, 38, 38, 0.15) 100%);
        border: 2px solid rgba(239, 68, 68, 0.4);
        border-radius: var(--radius-xl);
        padding: var(--space-6);
        margin-bottom: var(--space-6);
        display: flex;
        align-items: flex-start;
        gap: var(--space-4);
    }

    .antidetect-warning-icon {
        font-size: 2rem;
        color: #ef4444;
        animation: warningShake 2s infinite;
    }

    @keyframes warningShake {
        0%, 100% { transform: rotate(0deg); }
        25% { transform: rotate(-5deg); }
        75% { transform: rotate(5deg); }
    }

    .antidetect-warning-content h3 {
        color: #ef4444;
        font-size: 1.25rem;
        margin-bottom: var(--space-2);
    }

    .antidetect-warning-content p {
        color: var(--text-secondary);
        font-size: 0.9rem;
        line-height: 1.6;
    }

    /* Anti-Detection Cards */
    .antidetect-card {
        background: rgba(239, 68, 68, 0.05);
        border: 1px solid rgba(239, 68, 68, 0.2);
    }

    .antidetect-card .card-header {
        border-bottom-color: rgba(239, 68, 68, 0.2);
    }

    .antidetect-card .card-icon {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
    }

    /* Fingerprint Stats Display */
    .fingerprint-display {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: var(--space-4);
        margin-top: var(--space-4);
        padding: var(--space-4);
        background: rgba(0, 0, 0, 0.2);
        border-radius: var(--radius-lg);
    }

    .fingerprint-stat {
        text-align: center;
        padding: var(--space-3);
    }

    .fingerprint-stat-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--accent-tertiary);
        font-family: var(--font-mono);
    }

    .fingerprint-stat-label {
        font-size: 0.75rem;
        color: var(--text-tertiary);
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* Regenerate Button Special */
    .btn-regenerate {
        background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);
        border: none;
        box-shadow: 0 4px 15px rgba(139, 92, 246, 0.3);
    }

    .btn-regenerate:hover {
        box-shadow: 0 6px 20px rgba(139, 92, 246, 0.5);
        transform: translateY(-2px);
    }

    /* Status Footer */
    .sidebar-footer {
        padding: var(--space-6);
        border-top: 1px solid rgba(255, 255, 255, 0.1);
    }

    .status-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: var(--radius-lg);
        padding: var(--space-4);
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .status-info {
        display: flex;
        align-items: center;
        gap: var(--space-2);
        font-size: 0.875rem;
        font-weight: 500;
    }

    .status-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: var(--accent-danger);
        animation: statusPulse 2s infinite;
    }

    .status-dot.active {
        background: var(--accent-quaternary);
    }

    @keyframes statusPulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.7; transform: scale(1.2); }
    }

    /* Main Content */
    .main-content {
        flex: 1;
        display: flex;
        flex-direction: column;
        overflow: hidden;
    }

    /* Header */
    .header {
        height: var(--header-height);
        background: var(--bg-glass);
        backdrop-filter: blur(20px) saturate(180%);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 var(--space-8);
        position: relative;
        z-index: 40;
    }

    .header::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: var(--gradient-primary);
        opacity: 0.6;
    }

    .stats-grid {
        display: flex;
        gap: var(--space-6);
    }

    .stat-item {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: var(--radius-lg);
        padding: var(--space-4) var(--space-5);
        display: flex;
        align-items: center;
        gap: var(--space-3);
        transition: all var(--transition-normal);
        position: relative;
        overflow: hidden;
    }

    .stat-item::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: var(--gradient-glass);
        transition: left var(--transition-normal);
    }

    .stat-item:hover {
        border-color: rgba(99, 102, 241, 0.3);
        transform: translateY(-2px);
        box-shadow: var(--shadow-lg);
    }

    .stat-item:hover::before {
        left: 0;
    }

    .stat-icon {
        width: 24px;
        height: 24px;
        color: var(--accent-primary);
        position: relative;
        z-index: 1;
    }

    .stat-content {
        position: relative;
        z-index: 1;
    }

    .stat-label {
        font-size: 0.75rem;
        color: var(--text-secondary);
        margin-bottom: var(--space-1);
    }

    .stat-value {
        font-size: 0.875rem;
        font-weight: 600;
        font-family: var(--font-mono);
    }

    .performance-indicator {
        display: inline-flex;
        align-items: center;
        gap: var(--space-1);
        margin-left: var(--space-2);
    }

    .performance-dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: var(--accent-danger);
    }

    .performance-dot.good { background: var(--accent-quaternary); }
    .performance-dot.warning { background: var(--accent-warning); }
    .performance-dot.bad { background: var(--accent-danger); }

    /* Content Area */
    .content-area {
        flex: 1;
        overflow-y: auto;
        padding: var(--space-8);
    }

    .content-section {
        display: none;
        animation: contentSlideIn 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .content-section.active {
        display: block;
    }

    @keyframes contentSlideIn {
        from {
            opacity: 0;
            transform: translateY(20px) scale(0.98);
        }
        to {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }

    /* Cards */
    .card {
        background: var(--bg-glass);
        backdrop-filter: blur(20px) saturate(180%);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: var(--radius-2xl);
        padding: var(--space-8);
        margin-bottom: var(--space-8);
        position: relative;
        overflow: hidden;
    }

    .card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: var(--gradient-primary);
    }

    .card::after {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        background: radial-gradient(circle at top right, rgba(99, 102, 241, 0.05) 0%, transparent 50%);
        pointer-events: none;
    }

    .card-header {
        display: flex;
        align-items: center;
        gap: var(--space-4);
        margin-bottom: var(--space-8);
        position: relative;
        z-index: 1;
    }

    .card-icon {
        width: 48px;
        height: 48px;
        background: var(--gradient-primary);
        border-radius: var(--radius-xl);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.25rem;
        color: white;
        box-shadow: var(--shadow-glow);
    }

    .card-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--text-primary);
    }

    .card-content {
        position: relative;
        z-index: 1;
    }

    /* Form Controls */
    .form-group {
        margin-bottom: var(--space-6);
    }

    .form-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: var(--space-5) 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        transition: all var(--transition-normal);
    }

    .form-row:hover {
        background: rgba(255, 255, 255, 0.02);
        margin: 0 calc(-1 * var(--space-5));
        padding-left: var(--space-5);
        padding-right: var(--space-5);
        border-radius: var(--radius-lg);
    }

    .form-label {
        display: flex;
        align-items: center;
        gap: var(--space-3);
        font-weight: 500;
        color: var(--text-secondary);
        flex: 1;
    }

    .form-label.premium {
        color: var(--accent-primary);
        font-weight: 600;
        position: relative;
    }

    .form-label.premium::after {
        content: '✨';
        margin-left: var(--space-2);
        font-size: 0.875rem;
        animation: sparkle 2s ease-in-out infinite;
    }

    @keyframes sparkle {
        0%, 100% { opacity: 0.6; transform: scale(1) rotate(0deg); }
        50% { opacity: 1; transform: scale(1.2) rotate(180deg); }
    }

    .form-controls {
        display: flex;
        align-items: center;
        gap: var(--space-4);
    }

    /* Toggle Switch */
    .toggle {
        position: relative;
        display: inline-block;
        width: 56px;
        height: 28px;
    }

    .toggle input {
        opacity: 0;
        width: 0;
        height: 0;
    }

    .toggle-slider {
        position: absolute;
        cursor: pointer;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: var(--bg-quaternary);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 28px;
        transition: all var(--transition-normal);
    }

    .toggle-slider:before {
        position: absolute;
        content: "";
        height: 22px;
        width: 22px;
        left: 2px;
        bottom: 2px;
        background: white;
        border-radius: 50%;
        transition: all var(--transition-normal);
        box-shadow: var(--shadow-md);
    }

    input:checked + .toggle-slider {
        background: var(--gradient-primary);
        border-color: var(--accent-primary);
        box-shadow: var(--shadow-glow);
    }

    input:checked + .toggle-slider:before {
        transform: translateX(28px);
        background: white;
        box-shadow: 0 0 15px rgba(99, 102, 241, 0.5);
    }

    /* Range Input */
    .range-control {
        display: flex;
        align-items: center;
        gap: var(--space-4);
    }

    .range-input {
        -webkit-appearance: none;
        appearance: none;
        width: 200px;
        height: 6px;
        background: var(--bg-quaternary);
        border-radius: var(--radius-lg);
        outline: none;
        cursor: pointer;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    .range-input::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 20px;
        height: 20px;
        background: var(--gradient-primary);
        border-radius: 50%;
        cursor: pointer;
        border: 2px solid white;
        box-shadow: var(--shadow-md);
        transition: all var(--transition-fast);
    }

    .range-input::-webkit-slider-thumb:hover {
        transform: scale(1.2);
        box-shadow: var(--shadow-glow);
    }

    .range-input::-moz-range-thumb {
        width: 20px;
        height: 20px;
        background: var(--gradient-primary);
        border-radius: 50%;
        cursor: pointer;
        border: 2px solid white;
        box-shadow: var(--shadow-md);
    }

    .range-output {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-width: 60px;
        height: 32px;
        background: var(--gradient-primary);
        color: white;
        border-radius: var(--radius-lg);
        font-size: 0.875rem;
        font-weight: 600;
        font-family: var(--font-mono);
        box-shadow: var(--shadow-glow);
    }

    /* Select */
    .select {
        position: relative;
        min-width: 160px;
    }

    .select select {
        width: 100%;
        padding: var(--space-3) var(--space-4);
        background: var(--bg-quaternary);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: var(--radius-lg);
        color: var(--text-primary);
        font-size: 0.875rem;
        cursor: pointer;
        appearance: none;
        transition: all var(--transition-normal);
    }

    .select::after {
        content: '';
        position: absolute;
        top: 50%;
        right: var(--space-3);
        transform: translateY(-50%);
        width: 0;
        height: 0;
        border-left: 4px solid transparent;
        border-right: 4px solid transparent;
        border-top: 4px solid var(--text-secondary);
        pointer-events: none;
    }

    .select select:hover,
    .select select:focus {
        border-color: var(--accent-primary);
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
        outline: none;
    }

    /* Input */
    .input {
        padding: var(--space-3) var(--space-4);
        background: var(--bg-quaternary);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: var(--radius-lg);
        color: var(--text-primary);
        font-size: 0.875rem;
        width: 100px;
        text-align: center;
        transition: all var(--transition-normal);
    }

    .input:hover,
    .input:focus {
        border-color: var(--accent-primary);
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
        outline: none;
    }

    /* Christmas 3D Glass Buttons */
    .btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: var(--space-2);
        padding: var(--space-3) var(--space-6);
        background: linear-gradient(135deg, #ff4d4d 0%, #c53030 100%);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-top: 1px solid rgba(255, 255, 255, 0.8);
        border-bottom: 3px solid rgba(139, 0, 0, 0.5);
        border-radius: 9999px; /* Pill shape */
        font-size: 0.95rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1); /* Bouncy spring */
        text-decoration: none;
        position: relative;
        overflow: hidden;
        box-shadow: 
            0 4px 6px rgba(0, 0, 0, 0.2), 
            0 1px 3px rgba(0, 0, 0, 0.1),
            inset 0 2px 4px rgba(255, 255, 255, 0.3);
        text-shadow: 0 1px 2px rgba(0,0,0,0.3);
    }

    .btn:hover {
        transform: translateY(-2px) scale(1.02);
        box-shadow: 
            0 7px 14px rgba(0, 0, 0, 0.25), 
            0 3px 6px rgba(0, 0, 0, 0.15),
            inset 0 2px 4px rgba(255, 255, 255, 0.4),
            0 0 15px rgba(255, 77, 77, 0.6); /* Red Glow */
    }

    .btn:active {
        transform: translateY(1px) scale(0.98);
        box-shadow: inset 0 2px 8px rgba(0,0,0,0.2);
        border-bottom-width: 1px;
    }

    /* Candy Cane Toggles */
    .toggle {
        position: relative;
        display: inline-block;
        width: 60px;
        height: 32px;
        filter: drop-shadow(0 4px 4px rgba(0,0,0,0.3));
    }

    .toggle input {
        opacity: 0;
        width: 0;
        height: 0;
    }

    .toggle-slider {
        position: absolute;
        cursor: pointer;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: #222b3a; /* Dark inactive */
        transition: .4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border-radius: 34px;
        border: 2px solid rgba(255,255,255,0.1);
        overflow: hidden;
    }

    /* Snowball Knob */
    .toggle-slider:before {
        position: absolute;
        content: "";
        height: 24px;
        width: 24px;
        left: 2px;
        bottom: 2px;
        background: radial-gradient(circle at 30% 30%, #ffffff, #e2e8f0);
        transition: .4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border-radius: 50%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.3);
        z-index: 2;
    }

    /* Active State - Candy Cane Stripes */
    input:checked + .toggle-slider {
        background: repeating-linear-gradient(
            45deg,
            #ff3b3b,
            #ff3b3b 10px,
            #ffffff 10px,
            #ffffff 20px
        );
        border-color: #ff3b3b;
        animation: stripe-move 20s linear infinite;
    }

    @keyframes stripe-move {
        from { background-position: 0 0; }
        to { background-position: 500px 0; }
    }

    input:checked + .toggle-slider:before {
        transform: translateX(28px);
        box-shadow: -2px 2px 8px rgba(0,0,0,0.2);
        background: radial-gradient(circle at 30% 30%, #fbbf24, #f59e0b); /* Gold when active */
    }

    /* Hover Glow */
    .toggle:hover .toggle-slider {
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
    }

    .btn.danger {
        background: var(--gradient-danger);
    }

    .btn.warning {
        background: linear-gradient(135deg, var(--accent-warning) 0%, #D97706 100%);
    }

    .btn.small {
        padding: var(--space-2) var(--space-3);
        font-size: 0.75rem;
    }

    /* Tabs */
    .tabs {
        display: flex;
        background: var(--bg-quaternary);
        border-radius: var(--radius-xl);
        padding: var(--space-1);
        margin-bottom: var(--space-8);
        position: relative;
    }

    .tab-button {
        flex: 1;
        padding: var(--space-3) var(--space-5);
        background: transparent;
        border: none;
        color: var(--text-secondary);
        font-weight: 500;
        cursor: pointer;
        border-radius: var(--radius-lg);
        transition: all var(--transition-normal);
        position: relative;
        z-index: 1;
    }

    .tab-button.active {
        color: white;
        background: var(--gradient-primary);
        box-shadow: var(--shadow-md);
    }

    .tab-content {
        display: none;
        animation: tabSlideIn 0.3s ease-out;
    }

    .tab-content.active {
        display: block;
    }

    @keyframes tabSlideIn {
        from {
            opacity: 0;
            transform: translateY(10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* Info Boxes */
    .info-box {
        padding: var(--space-5);
        border-radius: var(--radius-lg);
        margin-top: var(--space-6);
        position: relative;
        overflow: hidden;
        border: 1px solid;
    }

    .info-box.info {
        background: rgba(6, 182, 212, 0.1);
        border-color: rgba(6, 182, 212, 0.3);
        color: #67E8F9;
    }

    .info-box.warning {
        background: rgba(245, 158, 11, 0.1);
        border-color: rgba(245, 158, 11, 0.3);
        color: #FCD34D;
    }

    .info-box.premium {
        background: rgba(99, 102, 241, 0.1);
        border-color: rgba(99, 102, 241, 0.3);
        color: var(--accent-primary);
    }

    /* Keybind Display */
    .keybind-display {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-width: 120px;
        height: 36px;
        background: var(--bg-quaternary);
        border: 2px dashed rgba(255, 255, 255, 0.3);
        border-radius: var(--radius-lg);
        font-family: var(--font-mono);
        font-weight: 600;
        color: var(--text-secondary);
        cursor: pointer;
        transition: all var(--transition-normal);
    }

    .keybind-display.listening {
        border-color: var(--accent-primary);
        color: var(--accent-primary);
        background: rgba(99, 102, 241, 0.1);
        animation: keybindPulse 1s infinite;
    }

    @keyframes keybindPulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.8; transform: scale(1.05); }
    }

    /* Visualizer */
    .visualizer-container {
        display: flex;
        justify-content: center;
        align-items: center;
        background: var(--bg-secondary);
        border: 2px dashed rgba(255, 255, 255, 0.2);
        border-radius: var(--radius-xl);
        padding: var(--space-8);
        margin-top: var(--space-6);
        min-height: 300px;
        position: relative;
        overflow: hidden;
    }

    .visualizer-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at center, rgba(99, 102, 241, 0.1) 0%, transparent 70%);
    }

    #detectionVisualizer {
        background: var(--bg-primary);
        border-radius: var(--radius-lg);
        box-shadow: var(--shadow-xl);
        position: relative;
        z-index: 1;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Chart Container */
    .chart-container {
        height: 240px;
        margin: var(--space-6) 0;
        background: var(--bg-secondary);
        border-radius: var(--radius-xl);
        padding: var(--space-6);
        border: 1px solid rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
    }

    .chart-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at top left, rgba(99, 102, 241, 0.05) 0%, transparent 50%);
    }

    /* RCS Canvas */
    #rcsCanvas {
        background: var(--bg-primary);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: var(--radius-lg);
        cursor: crosshair;
        box-shadow: var(--shadow-xl);
    }

    .rcs-editor {
        display: grid;
        grid-template-columns: 1fr 300px;
        gap: var(--space-8);
        margin-top: var(--space-6);
    }

    .rcs-controls {
        display: flex;
        flex-direction: column;
        gap: var(--space-4);
    }

    /* Lists */
    .list {
        background: var(--bg-secondary);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: var(--radius-lg);
        padding: var(--space-2);
        max-height: 300px;
        overflow-y: auto;
    }

    .list-item {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: var(--space-3) var(--space-4);
        border-radius: var(--radius-md);
        transition: all var(--transition-fast);
    }

    .list-item:hover {
        background: rgba(255, 255, 255, 0.05);
    }

    .list-item-actions {
        display: flex;
        gap: var(--space-2);
    }

    /* Tooltips */
    .tooltip {
        position: relative;
        display: inline-block;
    }

    .tooltip .tooltip-content {
        visibility: hidden;
        position: absolute;
        z-index: 1000;
        bottom: 125%;
        left: 50%;
        transform: translateX(-50%);
        background: var(--bg-primary);
        color: var(--text-primary);
        text-align: center;
        border-radius: var(--radius-lg);
        padding: var(--space-3) var(--space-4);
        font-size: 0.875rem;
        white-space: nowrap;
        opacity: 0;
        transition: all var(--transition-normal);
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: var(--shadow-xl);
        backdrop-filter: blur(20px);
    }

    .tooltip:hover .tooltip-content {
        visibility: visible;
        opacity: 1;
    }

    .tooltip .tooltip-content::after {
        content: "";
        position: absolute;
        top: 100%;
        left: 50%;
        margin-left: -5px;
        border-width: 5px;
        border-style: solid;
        border-color: var(--bg-primary) transparent transparent transparent;
    }

    /* Toast */
    .toast-container {
        position: fixed;
        top: var(--space-6);
        right: var(--space-6);
        z-index: 1000;
        display: flex;
        flex-direction: column;
        gap: var(--space-3);
        pointer-events: none;
    }

    .toast {
        background: var(--bg-primary);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: var(--radius-lg);
        padding: var(--space-4) var(--space-5);
        box-shadow: var(--shadow-xl);
        backdrop-filter: blur(20px);
        display: flex;
        align-items: center;
        gap: var(--space-3);
        opacity: 0;
        transform: translateX(100%) scale(0.9);
        transition: all var(--transition-normal);
        pointer-events: auto;
        cursor: pointer;
        min-width: 300px;
        max-width: 400px;
    }

    .toast.show {
        opacity: 1;
        transform: translateX(0) scale(1);
    }

    .toast.success {
        border-color: var(--accent-quaternary);
        color: var(--accent-quaternary);
    }

    .toast.error {
        border-color: var(--accent-danger);
        color: var(--accent-danger);
    }

    .toast.warning {
        border-color: var(--accent-warning);
        color: var(--accent-warning);
    }

    .toast.info {
        border-color: var(--accent-tertiary);
        color: var(--accent-tertiary);
    }

    .toast:hover {
        transform: translateX(-4px) scale(1.02);
    }

    /* Premium Features */
    .premium-feature {
        position: relative;
    }

    .premium-feature::after {
        content: '✨ PRO';
        position: absolute;
        top: var(--space-2);
        right: var(--space-2);
        background: var(--gradient-primary);
        color: white;
        padding: var(--space-1) var(--space-2);
        border-radius: var(--radius-md);
        font-size: 0.625rem;
        font-weight: 700;
        letter-spacing: 0.5px;
        box-shadow: var(--shadow-glow);
        animation: premiumGlow 3s ease-in-out infinite;
    }

    @keyframes premiumGlow {
        0%, 100% { opacity: 0.8; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.05); }
    }

    /* Responsive */
    @media (max-width: 1024px) {
        .rcs-editor {
            grid-template-columns: 1fr;
        }
        
        .stats-grid {
            flex-wrap: wrap;
            gap: var(--space-4);
        }
    }

    @media (max-width: 768px) {
        .sidebar {
            position: fixed;
            left: -100%;
            top: 0;
            bottom: 0;
            z-index: 100;
            transition: left var(--transition-normal);
        }
        
        .sidebar.open {
            left: 0;
        }
        
        .form-row {
            flex-direction: column;
            align-items: stretch;
            gap: var(--space-4);
        }
        
        .range-control {
            justify-content: space-between;
        }
    }

    /* Loading States */
    .loading {
        position: relative;
        overflow: hidden;
    }

    .loading::after {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        animation: shimmer 2s infinite;
    }

    @keyframes shimmer {
        0% { left: -100%; }
        100% { left: 100%; }
    }

    /* Code/Logs */
    .log-viewer {
        width: 100%;
        height: 400px;
        background: var(--bg-primary);
        color: var(--text-secondary);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: var(--radius-lg);
        padding: var(--space-5);
        font-family: var(--font-mono);
        font-size: 0.875rem;
        white-space: pre-wrap;
        overflow-y: auto;
        resize: vertical;
        line-height: 1.5;
    }

    /* Utilities */
    .flex { display: flex; }
    .items-center { align-items: center; }
    .justify-between { justify-content: space-between; }
    .gap-2 { gap: var(--space-2); }
    .gap-4 { gap: var(--space-4); }
    .mt-4 { margin-top: var(--space-4); }
    .mb-6 { margin-bottom: var(--space-6); }
    .text-sm { font-size: 0.875rem; }
    .font-mono { font-family: var(--font-mono); }
    .font-medium { font-weight: 500; }
    .font-semibold { font-weight: 600; }
    .text-center { text-align: center; }
    /* Crosshair Grid */
    .crosshair-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
        gap: var(--space-4);
        margin-top: var(--space-6);
    }
    
    .crosshair-card {
        background: var(--bg-secondary);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: var(--radius-md);
        padding: var(--space-4);
        cursor: pointer;
        transition: all 0.2s ease;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    
    .crosshair-card:hover {
        transform: translateY(-2px);
        border-color: var(--accent-primary);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
    }
    
    .crosshair-preview-box {
        width: 100%;
        aspect-ratio: 1;
        background: #444 url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='8' height='8' viewBox='0 0 8 8'%3E%3Cg fill='%239C92AC' fill-opacity='0.1'%3E%3Cpath fill-rule='evenodd' d='M0 0h4v4H0V0zm4 4h4v4H4V4z'/%3E%3C/g%3E%3C/svg%3E");
        border-radius: var(--radius-sm);
        margin-bottom: var(--space-3);
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
    }
    
    .crosshair-name {
        font-weight: 600;
        color: var(--text-primary);
        font-size: 0.9rem;
        margin-bottom: var(--space-1);
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        max-width: 100%;
    }

    /* Modal */
    .modal-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.8);
        backdrop-filter: blur(4px);
        z-index: 1000;
        display: none;
        align-items: center;
        justify-content: center;
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .modal-overlay.active {
        display: flex;
        opacity: 1;
    }
    
    .modal-content {
        background: var(--bg-secondary);
        border: 1px solid var(--accent-primary);
        border-radius: var(--radius-lg);
        width: 90%;
        max-width: 500px;
        padding: var(--space-6);
        position: relative;
        transform: scale(0.9);
        transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    }
    
    .modal-overlay.active .modal-content {
        transform: scale(1);
    }
    
    .modal-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: var(--space-4);
    }
    
    .modal-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: var(--text-primary);
    }
    
    .modal-close {
        background: none;
        border: none;
        color: var(--text-tertiary);
        cursor: pointer;
        font-size: 1.5rem;
        transition: color 0.2s;
    }
    
    .modal-close:hover { color: var(--text-primary); }
    
    .preview-large {
        width: 100%;
        height: 250px;
        background: #555 url("https://www.vcrdb.net/bg/1.jpg") center/cover;
        border-radius: var(--radius-md);
        margin-bottom: var(--space-4);
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative; 
    }
    
    .code-box {
        background: rgba(0,0,0,0.3);
        padding: var(--space-3);
        border-radius: var(--radius-md);
        font-family: var(--font-mono);
        color: var(--accent-primary);
        font-size: 0.9rem;
        word-break: break-all;
        border: 1px dashed rgba(255,255,255,0.1);
        margin-bottom: var(--space-4);
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: var(--space-3);
    }
</style>

<script>
    let charts = {};
    const FAVICON_GREEN = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAIRlWElmTU0AKgAAAAgABQESAAMAAAABAAEAAAEaAAUAAAABAAAASgEbAAUAAAABAAAAUgEoAAMAAAABAAIAAIdpAAQAAAABAAAAWgAAAAAAAACQAAAAAQAAAJAAAAABAAOgAQADAAAAAQABAACgAgAEAAAAAQAAABCgAwAEAAAAAQAAABAAAAAIMLSbAAABGklEQVQ4T6WTMW7CQBCGv5tN2JBGywQ2gQkMG5gokBASihChj0ALRFBCRRKEhBoqIBQkIcQGSUEsWLpt1zZtJ2ZndmfuN8kPMAw8D+cNxzPsPwqGaT023y+dARv3LzTTH3L88vsU9GA8pZyvWo9Xq2XVyNfP0ZgYg1Zt7QERq3nKeiF+L5nL5fNDJ9pAKgaBsWkWRZpLhBVnUbH5mBGBIdp7G2Aoa1J1vSgykM223mU/l7XvQnx2PqfdXgOtftXcwkGbjVfXGoA8/g9z085jvxVwKAwOCAHCQAgIBAIIgBAQASkAAkAI8kAEBIKAhBAICEpAEAgICCABSUgACSAgJAKSgAREgIAUEP8HCAsyIiUhFZSCIiglIQhIRRLWIExlIJY2KiEiMpPJq1Fq5o+UmQxZmfSAPyLYGfkAcT3PAAAAAElFTkSuQmCC";
    const FAVICON_RED = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAIRlWElmTU0AKgAAAAgABQESAAMAAAABAAEAAAEaAAUAAAABAAAASgEbAAUAAAABAAAAUgEoAAMAAAABAAIAAIdpAAQAAAABAAAAWgAAAAAAAACQAAAAAQAAAJAAAAABAAOgAQADAAAAAQABAACgAgAEAAAAAQAAABCgAwAEAAAAAQAAABAAAAAIMLSbAAABG0lEQVQ4T6WTMW7CQBCGv5tN2JBGywQ2gQkMG5gokBASihChj0ALRFBCRRKEhBoqIBQkIcQGSUEsWLpt1zZtJ2ZndmfuN8kPMAw8D+cNxzPsPwqGaT023y+dARv3LzTTH3L88vsU9GA8pZyvWo9Xq2XVyNfP0ZgYg1Zt7QERq3nKeiF+L5nL5fNDJ9pAKgaBsWkWRZpLhBVnUbH5mBGBIdp7G2Aoa1J1vSgykM223mU/l7XvQnx2PqfdXgOtftXcwkGbjVfXGoA8/g9z085jvxVwKARuGwhAIBgGABCAICCABSQACQAjyQAQCAYQhCAICEpAEAgICCABSUgACSAgJAKSgAREAICUGP8HCAsyIiUhFZSCIiglIQhIRRLWIExlIJY2KiEiMpPJq1Fq5o+UmQxZmfSAPzM4GfsAZzDPAAAAAElFTkSuQmCC";
    
    // ============================================
    // Cookie-based Settings Auto-Save System
    // Settings are saved to cookies with 30-day expiry
    // Expiry refreshes each time the app runs
    // ============================================
    
    const COOKIE_NAME = 'ascendancy_settings';
    const COOKIE_EXPIRY_DAYS = 30;
    
    // Set a cookie with expiry date
    function setCookie(name, value, days) {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        const expires = "expires=" + date.toUTCString();
        document.cookie = name + "=" + encodeURIComponent(value) + ";" + expires + ";path=/;SameSite=Strict";
    }
    
    // Get a cookie by name
    function getCookie(name) {
        const nameEQ = name + "=";
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let c = cookies[i].trim();
            if (c.indexOf(nameEQ) === 0) {
                return decodeURIComponent(c.substring(nameEQ.length));
            }
        }
        return null;
    }
    
    // Save all settings to cookie
    function saveSettingsToCookie() {
        const form = document.getElementById('settingsForm');
        if (!form) return;
        
        const settings = {};
        const formData = new FormData(form);
        
        // Handle checkboxes properly
        form.querySelectorAll('input[type="checkbox"]').forEach(cb => {
            settings[cb.name] = cb.checked ? '1' : '0';
        });
        
        // Get all other form values
        for (const [key, value] of formData.entries()) {
            if (!key.endsWith('_slider')) { // Skip slider duplicates
                settings[key] = value;
            }
        }
        
        // Save to cookie with 30-day expiry
        setCookie(COOKIE_NAME, JSON.stringify(settings), COOKIE_EXPIRY_DAYS);
        console.log('[AutoSave] Settings saved to cookie (expires in 30 days)');
    }
    
    // Load settings from cookie and apply to form
    function loadSettingsFromCookie() {
        const savedData = getCookie(COOKIE_NAME);
        if (!savedData) {
            console.log('[AutoSave] No saved settings found');
            return false;
        }
        
        try {
            const settings = JSON.parse(savedData);
            const form = document.getElementById('settingsForm');
            if (!form) return false;
            
            let appliedCount = 0;
            
            for (const [key, value] of Object.entries(settings)) {
                const element = form.elements[key];
                if (!element) continue;
                
                if (element.type === 'checkbox') {
                    element.checked = value === '1' || value === 'true';
                    appliedCount++;
                } else if (element.type === 'select-one') {
                    element.value = value;
                    appliedCount++;
                } else if (element.type === 'range' || element.type === 'number' || element.type === 'hidden' || element.type === 'text') {
                    element.value = value;
                    // Trigger input event for range sliders to update display
                    if (element.type === 'range') {
                        element.dispatchEvent(new Event('input', { bubbles: true }));
                    }
                    appliedCount++;
                }
            }
            
            // Refresh the cookie expiry (30 more days from now)
            setCookie(COOKIE_NAME, savedData, COOKIE_EXPIRY_DAYS);
            
            console.log(`[AutoSave] Loaded ${appliedCount} settings from cookie (expiry refreshed)`);
            return true;
        } catch (e) {
            console.error('[AutoSave] Failed to parse saved settings:', e);
            return false;
        }
    }
    
    // Debounce function to avoid too frequent saves
    let saveTimeout = null;
    function debouncedSave() {
        if (saveTimeout) clearTimeout(saveTimeout);
        saveTimeout = setTimeout(() => {
            saveSettingsToCookie();
        }, 500); // Save 500ms after last change
    }

    function parseResponseText(responseText) {
        const data = {};
        if (!responseText) return data;
        
        // Try parsing as JSON first
        try {
            const jsonData = JSON.parse(responseText);
            Object.assign(data, jsonData);
            return data;
        } catch (e) {
            // Not JSON, continue to URLSearchParams
        }

        try {
            const params = new URLSearchParams(responseText);
            for (const [key, value] of params.entries()) {
                data[key] = value;
            }
        } catch(e) { console.error("Could not parse response text", e); }
        return data;
    }

    function autoUpdate(element = null) {
        const form = document.getElementById('settingsForm');
        if (!form) return;
        const formData = new FormData(form);
        form.querySelectorAll('input[type="checkbox"]').forEach(cb => {
            if (!cb.checked) {
                formData.set(cb.name, '0');
            }
        });
        const requestBody = new URLSearchParams(formData).toString();

        fetch('/api/update', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: requestBody
        })
        .then(response => response.text().then(text => ({ok: response.ok, status: response.status, text: text})))
        .then(result => {
            const data = parseResponseText(result.text);
            if (result.ok && data.success === '1') {
                if (data.message) showToast(data.message, "success");
                // Auto-save to cookie after successful update
                debouncedSave();
            } else {
                showToast(`Error: ${data.message || 'Unknown error'}`, "error");
            }
        }).catch(error => {
            showToast(`Network error updating settings: ${error.message}`, "error");
        });
    }

    function updateStats() {
        fetch("/api/stats")
        .then(response => response.text().then(text => ({ok: response.ok, status: response.status, text: text})))
        .then(result => {
            if (!result.ok) {
                return Promise.reject(`Failed to fetch stats: ${result.text}`);
            }
            const data = parseResponseText(result.text);
            const fpsElem = document.getElementById("sidebarFpsValue");
            const statusDot = document.getElementById("sidebarScanStatusDot");
            const headerFpsElem = document.getElementById("headerFpsValue");
            const headerStatusSpan = document.getElementById("headerScanStatus");
            const headerStatusDot = document.getElementById("headerScanStatusDot");
            const capTimeElem = document.getElementById("captureTimeValue");
            const procTimeElem = document.getElementById("processingTimeValue");
            
            let fpsText = (data.fps !== undefined && data.fps !== null) ? parseFloat(data.fps).toFixed(1) : "N/A";
            let statusActive = data.is_running === '1';
            
            if (fpsElem) fpsElem.innerText = fpsText;
            if (statusDot) statusDot.classList.toggle('active', statusActive);
            if (headerFpsElem) headerFpsElem.textContent = fpsText;
            if (headerStatusSpan) headerStatusSpan.textContent = statusActive ? 'Active' : 'Inactive';
            if (headerStatusDot) headerStatusDot.classList.toggle('active', statusActive);
            if (capTimeElem) capTimeElem.textContent = (data.capture_ms !== undefined && data.capture_ms !== null) ? parseFloat(data.capture_ms).toFixed(2) : 'N/A';
            if (procTimeElem) procTimeElem.textContent = (data.processing_ms !== undefined && data.processing_ms !== null) ? parseFloat(data.processing_ms).toFixed(2) : 'N/A';
            
            updateFavicon(statusActive);
            updatePerformanceIndicators(data);
            if (typeof window.updateCharts === 'function') {
                window.updateCharts({
                    fps: parseFloat(data.fps),
                    capture_ms: parseFloat(data.capture_ms),
                    processing_ms: parseFloat(data.processing_ms)
                });
            }
        }).catch(error => {
            document.querySelectorAll("#sidebarFpsValue, #headerFpsValue, #captureTimeValue, #processingTimeValue").forEach(el => el.textContent = "Err");
            document.querySelectorAll("#sidebarScanStatusDot, #headerScanStatusDot").forEach(el => el.classList.remove('active'));
            if(document.getElementById("headerScanStatus")) document.getElementById("headerScanStatus").textContent = 'Error';
            updateFavicon(false);
        });
    }
    
    function updatePerformanceIndicators(data) {
        const fpsIndicator = document.getElementById('fpsIndicator');
        const captureIndicator = document.getElementById('captureIndicator');
        const processingIndicator = document.getElementById('processingIndicator');
        
        if (fpsIndicator && data.fps !== undefined) {
            const fps = parseFloat(data.fps);
            fpsIndicator.className = 'performance-dot';
            if (fps >= 60) fpsIndicator.classList.add('good');
            else if (fps >= 30) fpsIndicator.classList.add('warning');
            else fpsIndicator.classList.add('bad');
        }
        
        if (captureIndicator && data.capture_ms !== undefined) {
            const captureMs = parseFloat(data.capture_ms);
            captureIndicator.className = 'performance-dot';
            if (captureMs <= 5) captureIndicator.classList.add('good');
            else if (captureMs <= 15) captureIndicator.classList.add('warning');
            else captureIndicator.classList.add('bad');
        }
        
        if (processingIndicator && data.processing_ms !== undefined) {
            const processingMs = parseFloat(data.processing_ms);
            processingIndicator.className = 'performance-dot';
            if (processingMs <= 10) processingIndicator.classList.add('good');
            else if (processingMs <= 25) processingIndicator.classList.add('warning');
            else processingIndicator.classList.add('bad');
        }
    }
    
    function updateFavicon(isActive) {
        const favicon = document.getElementById('favicon');
        if (favicon) {
            favicon.href = isActive ? FAVICON_GREEN : FAVICON_RED;
        }
    }

    // Current membership tier (updated by refreshMembershipStatus)
    let currentMembershipTier = 'none';
    
    // Expiry warning state (global for access from multiple functions)
    let expiryWarningShown = false;
    let shutdownCountdown = null;
    
    // Show expiry warning modal with countdown (global function)
    function showExpiryWarning() {
        if (expiryWarningShown) return; // Prevent duplicate
        expiryWarningShown = true;
        let secondsLeft = 15 * 60; // 15 minutes
        
        // Create warning modal
        let warningModal = document.createElement('div');
        warningModal.id = 'expiryWarningModal';
        warningModal.style.cssText = `
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.95); z-index: 99999;
            display: flex; align-items: center; justify-content: center;
            backdrop-filter: blur(10px);
        `;
        warningModal.innerHTML = `
            <div style="background: linear-gradient(135deg, #1a1d26 0%, #0f1015 100%); 
                        border: 3px solid #ef4444; border-radius: 24px; padding: 48px; 
                        max-width: 500px; text-align: center; box-shadow: 0 0 60px rgba(239, 68, 68, 0.4);
                        animation: pulse 2s ease-in-out infinite;">
                <div style="font-size: 4rem; margin-bottom: 24px;">⚠️</div>
                <h2 style="font-size: 1.75rem; font-weight: 700; color: #ef4444; margin-bottom: 16px;">
                    License Expired
                </h2>
                <p style="color: #f87171; font-size: 1.1rem; margin-bottom: 24px;">
                    Your membership has expired. The software will close in:
                </p>
                <div id="expiryCountdown" style="font-size: 3rem; font-weight: 700; color: #fff; 
                                                  font-family: 'JetBrains Mono', monospace; margin-bottom: 24px;">
                    15:00
                </div>
                <p style="color: rgba(255,255,255,0.6); font-size: 0.9rem; margin-bottom: 24px;">
                    Please save your work and renew your membership to continue.
                </p>
                <button onclick="window.location.href='/license'" 
                        style="padding: 16px 32px; background: linear-gradient(135deg, #fbbf24, #f59e0b); 
                               border: none; border-radius: 12px; color: #000; font-weight: 700; 
                               font-size: 1.1rem; cursor: pointer;">
                    <i class="fas fa-crown"></i> Renew Membership
                </button>
            </div>
        `;
        document.body.appendChild(warningModal);
        
        // Start countdown
        shutdownCountdown = setInterval(() => {
            secondsLeft--;
            const mins = Math.floor(secondsLeft / 60);
            const secs = secondsLeft % 60;
            const countdownEl = document.getElementById('expiryCountdown');
            if (countdownEl) {
                countdownEl.textContent = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
                
                // Flash red when under 1 minute
                if (secondsLeft < 60) {
                    countdownEl.style.color = secondsLeft % 2 === 0 ? '#ef4444' : '#fff';
                    countdownEl.style.textShadow = secondsLeft % 2 === 0 ? '0 0 20px #ef4444' : 'none';
                }
            }
            
            if (secondsLeft <= 0) {
                clearInterval(shutdownCountdown);
                window.location.href = '/license?expired=1';
            }
        }, 1000);
    }
    
    // Full Access only features - Regular users cannot access these
    const FULL_ACCESS_FEATURES = [
        'triggerbot-content',
        'crosshair-content', 
        'rcs-content',
        'antidetect-content'
    ];
    
    function showUpgradeModal(featureName) {
        // Create modal if it doesn't exist
        let modal = document.getElementById('upgradeModal');
        if (!modal) {
            modal = document.createElement('div');
            modal.id = 'upgradeModal';
            modal.style.cssText = `
                position: fixed; top: 0; left: 0; width: 100%; height: 100%; 
                background: rgba(0,0,0,0.85); display: flex; align-items: center; 
                justify-content: center; z-index: 10000; backdrop-filter: blur(10px);
            `;
            document.body.appendChild(modal);
        }
        
        modal.innerHTML = `
            <div style="background: linear-gradient(135deg, var(--bg-tertiary) 0%, var(--bg-secondary) 100%); 
                        border: 2px solid rgba(251, 191, 36, 0.4); border-radius: 24px; 
                        padding: 48px; max-width: 500px; text-align: center; animation: scaleIn 0.3s ease;">
                <div style="font-size: 4rem; margin-bottom: 24px;">🔒</div>
                <h2 style="font-size: 1.75rem; font-weight: 700; color: #fbbf24; margin-bottom: 16px;">
                    Full Access Required
                </h2>
                <p style="color: var(--text-secondary); font-size: 1.1rem; line-height: 1.6; margin-bottom: 24px;">
                    <strong style="color: var(--text-primary);">${featureName}</strong> is a premium feature 
                    available only to <span style="color: #fbbf24;">Full Access</span> members.
                </p>
                <p style="color: var(--text-tertiary); font-size: 0.9rem; margin-bottom: 32px;">
                    Upgrade now to unlock Triggerbot, Crosshair Overlay, Anti-Recoil, Anti-Detection, 
                    and all other premium features!
                </p>
                <div style="display: flex; gap: 16px; justify-content: center;">
                    <button onclick="document.getElementById('upgradeModal').style.display='none'" 
                            style="padding: 12px 28px; background: var(--bg-quaternary); border: 1px solid var(--border-primary); 
                                   color: var(--text-secondary); border-radius: 12px; cursor: pointer; font-weight: 600;">
                        Maybe Later
                    </button>
                    <button onclick="switchTab('membership-content'); document.getElementById('upgradeModal').style.display='none';" 
                            style="padding: 12px 28px; background: linear-gradient(135deg, #fbbf24, #f59e0b); 
                                   border: none; color: #000; border-radius: 12px; cursor: pointer; 
                                   font-weight: 700; box-shadow: 0 4px 20px rgba(251, 191, 36, 0.4);">
                        <i class="fas fa-crown"></i> Upgrade Now
                    </button>
                </div>
            </div>
        `;
        modal.style.display = 'flex';
    }

    function switchTab(targetId) {
        // Check if this is a Full Access only feature
        if (FULL_ACCESS_FEATURES.includes(targetId) && currentMembershipTier !== 'full_access') {
            // Get feature name for display
            const featureNames = {
                'triggerbot-content': "Rudolph's Trigger (Triggerbot)",
                'crosshair-content': 'Star Sights (Crosshair Overlay)',
                'rcs-content': 'Recoil Gifts (Anti-Recoil)',
                'antidetect-content': 'Anti-Detection Settings'
            };
            const featureName = featureNames[targetId] || 'This Feature';
            showUpgradeModal(featureName);
            return; // Don't switch to the tab
        }
        
        document.querySelectorAll('.nav-link').forEach(link => link.classList.remove('active'));
        document.querySelectorAll('.content-section').forEach(section => section.classList.remove('active'));
        
        const activeLink = document.querySelector(`.nav-link[href="#${targetId}"]`);
        const activeSection = document.getElementById(targetId);
        
        if (activeLink) activeLink.classList.add('active');
        if (activeSection) activeSection.classList.add('active');
        
        if (targetId === 'recording-content') loadRecordings();
        if (targetId === 'logs-content') loadRecentLogs();
        if (targetId === 'profiles-content') listProfiles();
        if (targetId === 'rcs-content') { loadRcsProfiles(); rcsEditor.resize(); }
        if (targetId === 'membership-content') initMembershipTab();
    }

    function sendCommand(command, payload = null) {
        let endpoint = '';
        let confirmation = null;
        let method = 'POST';
        let body = payload ? new URLSearchParams(payload).toString() : null;
        
        if (command === 'shutdown') {
            endpoint = '/api/shutdown';
            confirmation = confirm("Are you sure you want to close the application?");
        } else if (command === 'reset_settings') {
            endpoint = '/api/reset_settings';
            confirmation = confirm("Reset ALL settings to defaults?");
        } else if (command === 'save_profile') {
            endpoint = `/api/profiles/save`;
        } else if (command === 'load_profile') {
            endpoint = `/api/profiles/load`;
        } else if (command === 'delete_profile') {
            endpoint = `/api/profiles/delete`;
            confirmation = confirm(`Delete profile "${payload.profile_name}"?`);
        } else {
            showToast("Error: Unknown internal command.", "error");
            return;
        }

        if (confirmation === null || confirmation === true) {
            fetch(endpoint, {
                method: method,
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                body: body
            })
            .then(response => response.text().then(text => ({
                ok: response.ok,
                status: response.status,
                text: text
            })))
            .then(result => {
                const data = parseResponseText(result.text);
                if (result.ok && data.success === '1') {
                    showToast(data.message || `Command '${command}' successful`, "success");
                    if (command === 'reset_settings') {
                        // Force reload to refresh all UI state from defaults
                        setTimeout(() => window.location.reload(), 1000);
                    } else if (command === 'load_profile') {
                        updateFormValuesFromServerData(data);
                    } else if (command === 'shutdown') {
                        document.body.innerHTML = "<div style='display: flex; align-items: center; justify-content: center; height: 100vh; color: var(--text-primary); font-size: 1.5rem; font-weight: 600;'>Application is closing...</div>";
                        window.onbeforeunload = null;
                    } else if (command.includes('_profile')) {
                        listProfiles();
                    }
                } else {
                    showToast(`Command failed: ${data.message || `Status ${result.status}`}`, "error");
                }
            }).catch(error => {
                showToast(`Network error during command '${command}'.`, "error");
            });
        }
    }
    
    function updateFormValuesFromServerData(serverData) {
        const settings = {};
        for (const key in serverData) {
            if (key.startsWith("settings.")) {
                settings[key.substring("settings.".length)] = serverData[key];
            }
        }
        updateFormValues(settings);
        if (typeof window.redrawRecoilEditor === 'function') window.redrawRecoilEditor();
    }

    function updateFormValues(settings) {
        const form = document.getElementById('settingsForm');
        if (!form) return;
        
        for (const key in settings) {
            if (!settings.hasOwnProperty(key)) continue;
            const value = settings[key];
            const elements = form.querySelectorAll(`[name="${key}"]`);
            
            if (elements.length > 0) {
                const element = elements[0];
                try {
                    if (element.type === 'checkbox') {
                        element.checked = (value === true || value === '1' || value === 1 || value === "True");
                    } else if (element.type === 'radio') {
                        form.querySelectorAll(`input[type="radio"][name="${key}"]`).forEach(radio => {
                            radio.checked = (radio.value == value);
                        });
                    } else if (element.tagName === 'SELECT') {
                        element.value = value;
                    } else if (element.type === 'number' || element.type === 'range') {
                        let numericValue = parseFloat(value);
                        if (isNaN(numericValue)) continue;
                        
                        const sliderElement = form.querySelector(`input[type="range"][name="${key}_slider"]`) || (element.type === 'range' ? element : null);
                        const numberElement = form.querySelector(`input[type="number"][name="${key}"]`) || (element.type === 'number' ? element : null);
                        const outputSpan = document.getElementById(`${key}_output`);
                        const hiddenInput = form.querySelector(`input[type="hidden"][name="${key}"]`);
                        
                        let outputValueToSet = numericValue;
                        if (element.step && element.step.includes('.')) {
                            outputValueToSet = numericValue.toFixed(element.step.split('.')[1].length);
                        } else if (sliderElement && sliderElement.hasAttribute('data-decimals')) {
                            outputValueToSet = numericValue.toFixed(parseInt(sliderElement.getAttribute('data-decimals')));
                        }
                        
                        if (sliderElement) {
                            const scale = parseFloat(sliderElement.getAttribute('data-scale-factor') || 1);
                            sliderElement.value = Math.round(numericValue * scale);
                        }
                        if (numberElement) numberElement.value = outputValueToSet;
                        if (outputSpan) outputSpan.textContent = outputValueToSet;
                        if (hiddenInput) hiddenInput.value = outputValueToSet;
                    } else if (key.endsWith('_custom_bind_key')) {
                        const displayEl = document.getElementById(key + '_display');
                        if(displayEl) displayEl.textContent = value || 'Not Set';
                        element.value = value;
                    } else {
                        element.value = value;
                    }
                } catch (uiError) {
                    console.error(`UI update error for ${key}:`, uiError);
                }
            }
        }
        updateAllSliderOutputs();
        updateDetectionVisualizer();
    }

    function initCharts() {
        try {
            const commonOptions = (yLabel) => ({
                responsive: true,
                maintainAspectRatio: false,
                animation: false,
                scales: {
                    x: { display: false },
                    y: {
                        beginAtZero: true,
                        ticks: {
                            color: 'var(--text-secondary)',
                            font: { size: 11 }
                        },
                        grid: { color: 'rgba(255, 255, 255, 0.1)' },
                        title: {
                            display: true,
                            text: yLabel,
                            color: 'var(--text-secondary)',
                            font: {size: 11}
                        }
                    }
                },
                plugins: { legend: { display: false } },
                elements: {
                    point: { radius: 0 },
                    line: { borderWidth: 2, tension: 0.3 }
                }
            });
            
            charts.fps = new Chart(document.getElementById('fpsChart').getContext('2d'), {
                type: 'line',
                data: {
                    labels: Array(60).fill(''),
                    datasets: [{
                        data: Array(60).fill(null),
                        borderColor: '#6366F1',
                        backgroundColor: 'rgba(99, 102, 241, 0.1)',
                        fill: true
                    }]
                },
                options: commonOptions('FPS')
            });
            
            charts.timing = new Chart(document.getElementById('timingChart').getContext('2d'), {
                type: 'line',
                data: {
                    labels: Array(60).fill(''),
                    datasets: [
                        {
                            label: 'Capture',
                            data: Array(60).fill(null),
                            borderColor: '#F59E0B',
                            backgroundColor: 'rgba(245, 158, 11, 0.1)',
                            fill: true
                        },
                        {
                            label: 'Process',
                            data: Array(60).fill(null),
                            borderColor: '#8B5CF6',
                            backgroundColor: 'rgba(139, 92, 246, 0.1)',
                            fill: true
                        }
                    ]
                },
                options: {
                    ...commonOptions('Time (ms)'),
                    plugins: {
                        legend: {
                            display: true,
                            position: 'bottom',
                            labels: {color: 'var(--text-primary)', font: {size: 11}}
                        }
                    }
                }
            });
            
            let lastUpdateTime = 0;
            const updateInterval = 500;
            
            window.updateCharts = function(newData) {
                const now = Date.now();
                if (now - lastUpdateTime < updateInterval && newData.fps !== undefined) return;
                lastUpdateTime = now;
                
                const maxDataPoints = 60;
                const updateChartData = (chart, ...newValues) => {
                    chart.data.labels.push('');
                    newValues.forEach((value, index) => {
                        chart.data.datasets[index].data.push(value ?? null);
                    });
                    if (chart.data.labels.length > maxDataPoints) {
                        chart.data.labels.shift();
                        chart.data.datasets.forEach(dataset => dataset.data.shift());
                    }
                    chart.update('none');
                };
                
                if(newData.fps !== undefined) updateChartData(charts.fps, newData.fps);
                if(newData.capture_ms !== undefined || newData.processing_ms !== undefined) updateChartData(charts.timing, newData.capture_ms, newData.processing_ms);
            };
        } catch (error) {
            console.error("Error initializing charts:", error);
        }
    }

    function loadRecordings() {
        const listElement = document.getElementById('recordingsList');
        const loadingElement = document.getElementById('recordingsLoading');
        if (!listElement || !loadingElement) return;
        
        loadingElement.style.display = 'block';
        listElement.innerHTML = '';
        
        fetch('/api/list_recordings')
        .then(response => response.text().then(text => ({ok: response.ok, text: text})))
        .then(result => {
            loadingElement.style.display = 'none';
            if (result.ok) {
                const recordings = result.text.split('\n').filter(name => name.trim() !== '');
                if (recordings.length > 0) {
                    recordings.forEach(filename => {
                        const li = document.createElement('div');
                        li.className = 'list-item';
                        
                        const nameSpan = document.createElement('span');
                        nameSpan.className = 'font-mono text-sm';
                        nameSpan.textContent = filename;
                        nameSpan.title = filename;
                        li.appendChild(nameSpan);
                        
                        const actionsDiv = document.createElement('div');
                        actionsDiv.className = 'list-item-actions';
                        const viewLink = document.createElement('a');
                        viewLink.href = `/recordings/${encodeURIComponent(filename)}`;
                        viewLink.textContent = 'View/DL';
                        viewLink.target = '_blank';
                        viewLink.className = 'btn small secondary';
                        actionsDiv.appendChild(viewLink);
                        li.appendChild(actionsDiv);
                        listElement.appendChild(li);
                    });
                } else {
                    const li = document.createElement('div');
                    li.className = 'list-item';
                    li.textContent = 'No recordings found.';
                    listElement.appendChild(li);
                }
            } else {
                const errorData = parseResponseText(result.text);
                const li = document.createElement('div');
                li.className = 'list-item';
                li.style.color = 'var(--accent-danger)';
                li.textContent = `Failed: ${errorData.message || result.text}`;
                listElement.appendChild(li);
            }
        }).catch(error => {
            loadingElement.style.display = 'none';
            const li = document.createElement('div');
            li.className = 'list-item';
            li.style.color = 'var(--accent-danger)';
            li.textContent = `Error: ${error.message}.`;
            listElement.appendChild(li);
        });
    }
    
    function loadRecentLogs() {
        const logViewer = document.getElementById('logViewer');
        if(!logViewer) return;
        logViewer.textContent = 'Loading recent logs...';
        
        fetch('/api/logs/recent')
        .then(response => response.text())
        .then(data => {
            logViewer.textContent = data;
            logViewer.scrollTop = logViewer.scrollHeight;
        })
        .catch(error => {
            logViewer.textContent = `Error loading logs: ${error}`;
        });
    }

    function updateAllSliderOutputs() {
        document.querySelectorAll('#settingsForm input[type="range"]').forEach(elem => {
            const baseName = elem.name.replace('_slider', '');
            const outputSpan = document.getElementById(`${baseName}_output`);
            if (!outputSpan) return;

            const isScaled = elem.hasAttribute('data-scale-factor');
            let displayValue;
            
            if (isScaled) {
                const scale = parseFloat(elem.getAttribute('data-scale-factor'));
                const decimals = parseInt(elem.getAttribute('data-decimals'));
                displayValue = (elem.value / scale).toFixed(decimals);
            } else {
                displayValue = elem.value;
            }
            
            outputSpan.textContent = displayValue;
            const hiddenInput = document.querySelector(`input[type="hidden"][name="${baseName}"]`);
            if(hiddenInput) hiddenInput.value = displayValue;
        });
    }

    function updateDetectionVisualizer() {
        const canvas = document.getElementById('detectionVisualizer');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        const container = canvas.parentElement;
        
        canvas.width = Math.min(container.clientWidth - 80, 350);
        canvas.height = canvas.width;
        
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const scale = canvas.width / 300;
        
        // Clear and set background
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        const gradient = ctx.createRadialGradient(centerX, centerY, 0, centerX, centerY, canvas.width / 2);
        gradient.addColorStop(0, '#151621');
        gradient.addColorStop(1, '#0D0E14');
        ctx.fillStyle = gradient;
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        const aimFovSize = parseInt(document.querySelector('input[name="aimbot_pixel_size"]')?.value || 50) * scale;
        const trigFovSize = parseInt(document.querySelector('input[name="triggerbot_pixel_size"]')?.value || 4) * scale;
        
        // Draw aimbot FOV
        ctx.shadowBlur = 20;
        ctx.shadowColor = '#6366F1';
        ctx.strokeStyle = '#6366F1';
        ctx.lineWidth = 2;
        ctx.strokeRect(centerX - aimFovSize / 2, centerY - aimFovSize / 2, aimFovSize, aimFovSize);
        ctx.fillStyle = 'rgba(99, 102, 241, 0.1)';
        ctx.fillRect(centerX - aimFovSize / 2, centerY - aimFovSize / 2, aimFovSize, aimFovSize);
        
        // Draw triggerbot zone
        ctx.shadowColor = '#EF4444';
        ctx.strokeStyle = '#EF4444';
        ctx.lineWidth = 2;
        ctx.strokeRect(centerX - trigFovSize / 2, centerY - trigFovSize / 2, trigFovSize, trigFovSize);
        ctx.fillStyle = 'rgba(239, 68, 68, 0.2)';
        ctx.fillRect(centerX - trigFovSize / 2, centerY - trigFovSize / 2, trigFovSize, trigFovSize);
        
        // Draw crosshair
        ctx.shadowBlur = 10;
        ctx.shadowColor = '#ffffff';
        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(centerX - 15, centerY);
        ctx.lineTo(centerX + 15, centerY);
        ctx.moveTo(centerX, centerY - 15);
        ctx.lineTo(centerX, centerY + 15);
        ctx.stroke();
        
        ctx.shadowBlur = 0;
    }

    const rcsEditor = {
        canvas: null, ctx: null, points: [], centerX: 0, centerY: 0, scale: 2,
        init() {
            this.canvas = document.getElementById('rcsCanvas');
            if (!this.canvas) return;
            this.ctx = this.canvas.getContext('2d');
            this.centerX = this.canvas.width / 2;
            this.centerY = this.canvas.height / 5;
            this.canvas.addEventListener('click', e => this.addPoint(e));
            this.canvas.addEventListener('contextmenu', e => {
                e.preventDefault();
                this.removeLastPoint();
            });
            this.draw();
        },
        resize() {
            const wrapper = this.canvas.parentElement;
            if (wrapper.clientWidth > 0 && this.canvas.width != wrapper.clientWidth) {
                this.canvas.width = wrapper.clientWidth;
                this.centerX = this.canvas.width / 2;
                this.draw();
            }
        },
        draw() {
            const gradient = this.ctx.createLinearGradient(0, 0, 0, this.canvas.height);
            gradient.addColorStop(0, '#151621');
            gradient.addColorStop(1, '#0D0E14');
            this.ctx.fillStyle = gradient;
            this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
            this.drawGrid();
            this.drawPattern();
            this.drawCenter();
        },
        drawGrid() {
            this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
            this.ctx.lineWidth = 1;
            for (let x = this.centerX % 20; x < this.canvas.width; x += 20) {
                this.ctx.beginPath(); this.ctx.moveTo(x, 0); this.ctx.lineTo(x, this.canvas.height); this.ctx.stroke();
            }
            for (let y = this.centerY % 20; y < this.canvas.height; y += 20) {
                this.ctx.beginPath(); this.ctx.moveTo(0, y); this.ctx.lineTo(this.canvas.width, y); this.ctx.stroke();
            }
        },
        drawCenter() {
            this.ctx.shadowBlur = 15;
            this.ctx.shadowColor = '#F59E0B';
            this.ctx.strokeStyle = '#F59E0B';
            this.ctx.lineWidth = 2;
            this.ctx.beginPath();
            this.ctx.moveTo(this.centerX - 15, this.centerY); this.ctx.lineTo(this.centerX + 15, this.centerY);
            this.ctx.moveTo(this.centerX, this.centerY - 15); this.ctx.lineTo(this.centerX, this.centerY + 15);
            this.ctx.stroke();
            this.ctx.shadowBlur = 0;
        },
        drawPattern() {
            if (this.points.length === 0) return;
            
            this.ctx.shadowBlur = 20;
            this.ctx.shadowColor = '#6366F1';
            this.ctx.strokeStyle = '#6366F1';
            this.ctx.lineWidth = 3;
            this.ctx.beginPath();
            this.ctx.moveTo(this.centerX + this.points[0][0] * this.scale, this.centerY + this.points[0][1] * this.scale);
            for (let i = 1; i < this.points.length; i++) {
                this.ctx.lineTo(this.centerX + this.points[i][0] * this.scale, this.centerY + this.points[i][1] * this.scale);
            }
            this.ctx.stroke();
            
            this.points.forEach((p, i) => {
                this.ctx.shadowBlur = 15;
                this.ctx.shadowColor = i === this.points.length - 1 ? '#EF4444' : '#6366F1';
                this.ctx.fillStyle = i === this.points.length - 1 ? '#EF4444' : '#6366F1';
                this.ctx.beginPath();
                this.ctx.arc(this.centerX + p[0] * this.scale, this.centerY + p[1] * this.scale, 6, 0, 2 * Math.PI);
                this.ctx.fill();
            });
            this.ctx.shadowBlur = 0;
        },
        addPoint(event) {
            const rect = this.canvas.getBoundingClientRect();
            const x = Math.round((event.clientX - rect.left - this.centerX) / this.scale);
            const y = Math.round((event.clientY - rect.top - this.centerY) / this.scale);
            this.points.push([x, y]);
            this.draw();
        },
        removeLastPoint() {
            if (this.points.length > 0) {
                this.points.pop();
                this.draw();
            }
        },
        loadPattern(points) {
            try {
                this.points = Array.isArray(points) ? points : this.deserializePointsText(points || '');
            } catch (e) {
                console.error("Failed to parse points:", e);
                this.points = [];
            }
            this.draw();
        },
        clearPattern() {
            this.points = [];
            this.draw();
        },
        serializePointsText(points) {
            if (!Array.isArray(points)) return '';
            return points.map(p => `${p[0]};${p[1]}`).join('|');
        },
        deserializePointsText(text) {
            if (!text) return [];
            return text.split('|').map(point => {
                const [x, y] = point.split(';');
                return [parseInt(x), parseInt(y)];
            }).filter(p => !isNaN(p[0]) && !isNaN(p[1]));
        }
    };

    function loadRcsProfiles() {
        const selectEl = document.getElementById('rcs_current_profile_name_select');
        if (!selectEl) return;
        const selectedValue = selectEl.value;
        fetch('/api/rcs/profiles/list').then(res => res.text()).then(text => {
            const data = parseResponseText(text);
            selectEl.innerHTML = '';
            
            // Parse profiles from text format: profile1=points1&profile2=points2
            const profilePairs = text.split('&');
            for (const pair of profilePairs) {
                if (pair.includes('=')) {
                    const [name, _] = pair.split('=', 2);
                    const option = document.createElement('option');
                    option.value = name;
                    option.textContent = name;
                    selectEl.appendChild(option);
                }
            }
            
            if (data.current && selectEl.querySelector(`option[value="${data.current}"]`)) {
                selectEl.value = data.current;
            } else if (selectEl.options.length > 0) {
                selectEl.selectedIndex = 0;
            }
            selectEl.dispatchEvent(new Event('change'));
        });
    }
    
    function onRcsProfileSelect() {
        const selectEl = document.getElementById('rcs_current_profile_name_select');
        const delayInputEl = document.getElementById('rcs_profile_delay_ms_input');
        const profileName = selectEl.value;
        if (!profileName) {
            rcsEditor.clearPattern();
            delayInputEl.value = 100;
            return;
        }
        fetch(`/api/rcs/profiles/get?profile_name=${encodeURIComponent(profileName)}`)
        .then(res => res.text())
        .then(text => {
            const data = parseResponseText(text);
            if (data.success === '1') {
                rcsEditor.loadPattern(data.points);
                delayInputEl.value = data.delay_ms;
            } else {
                console.error("Failed to load profile", data.message);
            }
        });
    }
    
    function saveCurrentRcsProfile() {
        const selectEl = document.getElementById('rcs_current_profile_name_select');
        const delayInputEl = document.getElementById('rcs_profile_delay_ms_input');
        const profileName = selectEl.value;
        if (!profileName) {
            showToast("No profile selected to save.", "warning");
            return;
        }
        const payload = new URLSearchParams();
        payload.append('profile_name', profileName);
        payload.append('points', rcsEditor.serializePointsText(rcsEditor.points));
        payload.append('delay_ms', delayInputEl.value);

        fetch('/api/rcs/profiles/save', { method: 'POST', body: payload })
        .then(res => res.text())
        .then(text => {
            const data = parseResponseText(text);
            if(data.success === '1') showToast("RCS Profile saved successfully!", "success");
            else showToast("Error saving RCS profile: " + data.message, "error");
        });
    }

    function createNewRcsProfile() {
        const newName = prompt("Enter new recoil profile name:", "NewProfile");
        if (!newName || !newName.trim()) return;
        if (!/^[a-zA-Z0-9_-]+$/.test(newName)) { 
            showToast("Invalid name. Use letters, numbers, underscore, hyphen.", "error"); 
            return; 
        }
        
        const payload = new URLSearchParams();
        payload.append('profile_name', newName.trim());
        payload.append('points', '');
        payload.append('delay_ms', '100');

        fetch('/api/rcs/profiles/save', { method: 'POST', body: payload })
        .then(res => res.text())
        .then(text => {
            const data = parseResponseText(text);
            if (data.success === '1') {
                loadRcsProfiles();
                showToast("New RCS profile created!", "success");
            } else {
                showToast("Error creating profile: " + data.message, "error");
            }
        });
    }
    
    function deleteSelectedRcsProfile() {
        const selectEl = document.getElementById('rcs_current_profile_name_select');
        const profileName = selectEl.value;
        if (!profileName) { showToast("No profile selected.", "warning"); return; }
        if (!confirm(`Are you sure you want to delete the recoil profile '${profileName}'?`)) return;
        
        fetch('/api/rcs/profiles/delete', { method: 'POST', body: new URLSearchParams({profile_name: profileName}) })
        .then(res => res.text())
        .then(text => {
            const data = parseResponseText(text);
            if (data.success === '1') {
                loadRcsProfiles();
                showToast("RCS profile deleted!", "success");
            } else {
                showToast("Error deleting profile: " + data.message, "error");
            }
        });
    }

    function listProfiles() {
        const listEl = document.getElementById('profileListDisplay'); 
        if(!listEl) return; 
        listEl.innerHTML = '<div class="list-item loading">Loading profiles...</div>';
        
        fetch('/api/profiles/list').then(res => res.text()).then(text => {
            listEl.innerHTML = ''; 
            const profiles = text.split('\n').filter(p => p.trim());
            if (profiles.length === 0) { 
                const li = document.createElement('div');
                li.className = 'list-item';
                li.textContent = 'No profiles saved yet.';
                listEl.appendChild(li);
                return; 
            }
            profiles.forEach(name => {
                const li = document.createElement('div');
                li.className = 'list-item';
                
                const nameSpan = document.createElement('span'); 
                nameSpan.textContent = name; 
                nameSpan.className = 'font-mono';
                li.appendChild(nameSpan);
                
                const actionsDiv = document.createElement('div');
                actionsDiv.className = 'list-item-actions';
                
                const loadBtn = document.createElement('button'); 
                loadBtn.innerHTML = '<i class="fas fa-download"></i> Load'; 
                loadBtn.className = 'btn small secondary';
                loadBtn.onclick = () => sendCommand('load_profile', {profile_name: name});
                
                const deleteBtn = document.createElement('button'); 
                deleteBtn.innerHTML = '<i class="fas fa-trash"></i> Delete'; 
                deleteBtn.className = 'btn small danger';
                deleteBtn.onclick = () => sendCommand('delete_profile', {profile_name: name});
                
                actionsDiv.appendChild(loadBtn); 
                actionsDiv.appendChild(deleteBtn);
                li.appendChild(actionsDiv); 
                listEl.appendChild(li);
            });
        }).catch(e => { 
            listEl.innerHTML = '<div class="list-item">Error loading profiles.</div>'; 
            console.error(e); 
        });
    }

    function saveCurrentProfile() {
        const nameInput = document.getElementById('newProfileNameInput'); 
        if(!nameInput) return;
        const name = nameInput.value.trim();
        if (!name) { 
            showToast("Please enter a profile name.", "warning"); 
            return; 
        }
        if (!/^[a-zA-Z0-9_-]+$/.test(name)) { 
            showToast("Invalid profile name. Use letters, numbers, underscore, hyphen.", "error"); 
            return; 
        }
        sendCommand('save_profile', {profile_name: name}); 
        nameInput.value = '';
    }

    function showToast(message, type = 'info') {
        const container = document.getElementById('toastContainer') || createToastContainer();
        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        
        const icon = getToastIcon(type);
        toast.innerHTML = `<i class="fas fa-${icon}"></i> <span>${message}</span>`;
        
        container.appendChild(toast);
        
        setTimeout(() => toast.classList.add('show'), 10);
        
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => {
                if (toast.parentNode) toast.remove();
            }, 300);
        }, 4000);
        
        toast.addEventListener('click', () => {
            toast.classList.remove('show');
            setTimeout(() => {
                if (toast.parentNode) toast.remove();
            }, 300);
        });
    }

    function getToastIcon(type) {
        switch(type) {
            case 'success': return 'check-circle';
            case 'error': return 'exclamation-triangle';
            case 'warning': return 'exclamation-circle';
            case 'info': 
            default: return 'info-circle';
        }
    }

    function createToastContainer() {
        const container = document.createElement('div');
        container.id = 'toastContainer';
        container.className = 'toast-container';
        document.body.appendChild(container);
        return container;
    }

    // ============================================
    // Anti-Detection Tab Functions
    // ============================================
    
    // Regenerate behavioral fingerprint
    async function regenerateFingerprint() {
        const btn = document.getElementById('regenerateFingerprintBtn');
        const originalText = btn.innerHTML;
        btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Regenerating...';
        btn.disabled = true;
        
        try {
            const response = await fetch('/api/regenerate_fingerprint', { method: 'POST' });
            const data = await response.json();
            
            if (data.success === '1') {
                // Update fingerprint display
                if (data.fingerprint) {
                    document.getElementById('fp-speed').textContent = data.fingerprint.speed.toFixed(2) + 'x';
                    document.getElementById('fp-tremor').textContent = data.fingerprint.tremor.toFixed(2) + 'x';
                    document.getElementById('fp-overshoot').textContent = data.fingerprint.overshoot.toFixed(2) + 'x';
                    document.getElementById('fp-reaction').textContent = (data.fingerprint.reaction_offset_ms >= 0 ? '+' : '') + 
                        data.fingerprint.reaction_offset_ms.toFixed(0) + 'ms';
                }
                showToast('Behavioral fingerprint regenerated! Your movement pattern is now different.', 'success');
            } else {
                showToast('Failed to regenerate fingerprint: ' + (data.message || 'Unknown error'), 'error');
            }
        } catch (error) {
            console.error('Error regenerating fingerprint:', error);
            showToast('Error connecting to server', 'error');
        } finally {
            btn.innerHTML = originalText;
            btn.disabled = false;
        }
    }
    
    // Refresh humanizer statistics
    async function refreshHumanizerStats() {
        try {
            const response = await fetch('/api/humanizer_stats');
            const data = await response.json();
            
            if (data.success === '1') {
                // Update stats display
                if (data.stats) {
                    document.getElementById('stat-total-movements').textContent = 
                        data.stats.total_movements ? data.stats.total_movements.toLocaleString() : '0';
                    document.getElementById('stat-overshoot-rate').textContent = 
                        data.stats.overshoot_rate ? (data.stats.overshoot_rate * 100).toFixed(1) + '%' : '0%';
                    document.getElementById('stat-frame-skips').textContent = 
                        data.stats.frame_skips ? data.stats.frame_skips.toLocaleString() : '0';
                    document.getElementById('stat-avg-distance').textContent = 
                        data.stats.avg_distance ? data.stats.avg_distance.toFixed(1) + 'px' : '0px';
                }
                
                // Update fingerprint display if available
                if (data.fingerprint) {
                    document.getElementById('fp-speed').textContent = data.fingerprint.speed_tendency.toFixed(2) + 'x';
                    document.getElementById('fp-tremor').textContent = data.fingerprint.tremor_intensity.toFixed(2) + 'x';
                    document.getElementById('fp-overshoot').textContent = data.fingerprint.overshoot_tendency.toFixed(2) + 'x';
                    document.getElementById('fp-reaction').textContent = (data.fingerprint.reaction_offset_ms >= 0 ? '+' : '') + 
                        data.fingerprint.reaction_offset_ms.toFixed(0) + 'ms';
                }
                
                showToast('Statistics refreshed', 'info');
            } else {
                showToast('Failed to get stats: ' + (data.message || 'Unknown error'), 'warning');
            }
        } catch (error) {
            console.error('Error fetching humanizer stats:', error);
            showToast('Controller not initialized yet - stats will appear after first aim movement', 'info');
        }
    }
    
    // Initialize Anti-Detection slider value displays
    function initAntiDetectionSliders() {
        const sliders = [
            { id: 'humanizer_polling_jitter', suffix: '%' },
            { id: 'humanizer_bezier_deviation', suffix: '' },
            { id: 'humanizer_min_points', suffix: '' },
            { id: 'humanizer_max_points', suffix: '' },
            { id: 'humanizer_tremor_amplitude', suffix: 'px' },
            { id: 'humanizer_tremor_frequency', suffix: '' },
            { id: 'humanizer_stress_multiplier', suffix: 'x' },
            { id: 'humanizer_overshoot_chance', suffix: '%' },
            { id: 'humanizer_overshoot_amount', suffix: '%' },
            { id: 'humanizer_correction_delay', suffix: 'ms' },
            { id: 'humanizer_reaction_min', suffix: 'ms' },
            { id: 'humanizer_reaction_mean', suffix: 'ms' },
            { id: 'humanizer_miss_chance', suffix: '%' },
            { id: 'humanizer_miss_offset', suffix: 'px' },
            { id: 'humanizer_frame_skip', suffix: '%' }
        ];
        
        // Also include dropdown
        const pollingRateSelect = document.getElementById('humanizer_polling_rate');
        if (pollingRateSelect) {
            pollingRateSelect.addEventListener('change', function() {
                updateHumanizerSetting(this.name || this.id, this.value);
                saveSettingsToCookie();
            });
        }
        
        sliders.forEach(({ id, suffix }) => {
            const slider = document.getElementById(id);
            const valueDisplay = document.getElementById(id + '_value');
            
            if (slider && valueDisplay) {
                // Set initial value
                valueDisplay.textContent = slider.value + suffix;
                
                // Update display on input (realtime)
                slider.addEventListener('input', function() {
                    valueDisplay.textContent = this.value + suffix;
                });
                
                // Send to backend on change (when slider released)
                slider.addEventListener('change', function() {
                    updateHumanizerSetting(this.name || this.id, this.value);
                    saveSettingsToCookie();
                });
            }
        });
    }
    
    // Send a single humanizer setting to the backend
    async function updateHumanizerSetting(name, value) {
        try {
            const formData = new FormData();
            formData.append(name, value);
            
            const response = await fetch('/api/humanizer_settings', {
                method: 'POST',
                body: formData
            });
            
            const data = await response.json();
            if (data.success === '1') {
                console.log(`[Humanizer] Updated ${name}=${value}`);
            } else {
                console.warn(`[Humanizer] Failed to update ${name}: ${data.message}`);
            }
        } catch (error) {
            console.error('[Humanizer] Error updating setting:', error);
        }
    }
    
    // Load humanizer stats on page load
    function loadHumanizerStatsOnInit() {
        // Delay to allow controller to initialize
        setTimeout(() => {
            refreshHumanizerStats();
        }, 2000);
    }


    let keybindListeningFor = null;
    let originalKeydownHandler = null;

    function startKeybindListen(bindName) {
        const displayElement = document.getElementById(bindName + '_display');
        if (!displayElement) return;

        if (keybindListeningFor) {
            stopKeybindListen(false);
        }

        displayElement.textContent = 'Press key or mouse...';
        displayElement.classList.add('listening');
        keybindListeningFor = {
            name: bindName,
            display: displayElement,
            input: document.getElementById(bindName + '_input')
        };

        originalKeydownHandler = window.onkeydown;
        window.onkeydown = handleKeybindCapture;
        window.addEventListener('mousedown', handleMousebindCapture, true);
    }

    function stopKeybindListen(shouldUpdate = true) {
        if (keybindListeningFor) {
            keybindListeningFor.display.classList.remove('listening');
            if (!keybindListeningFor.input.value) {
                keybindListeningFor.display.textContent = 'Not Set';
            }
            if(shouldUpdate) autoUpdate();
        }
        window.onkeydown = originalKeydownHandler;
        window.removeEventListener('mousedown', handleMousebindCapture, true);
        originalKeydownHandler = null;
        keybindListeningFor = null;
    }
    
    function handleKeybindCapture(event) {
        if (!keybindListeningFor) return;
        event.preventDefault();
        event.stopPropagation();
        
        let keyString;
        if (event.key.length === 1) {
            keyString = event.key.toLowerCase();
        } else {
            keyString = event.key;
        }

        keybindListeningFor.input.value = keyString;
        keybindListeningFor.display.textContent = keyString;
        stopKeybindListen();
    }

    function handleMousebindCapture(event) {
        if (!keybindListeningFor) return;

        if(event.target.closest('.keybind-display')) {
            return;
        }

        event.preventDefault();
        event.stopPropagation();
        
        let buttonString = '';
        switch (event.button) {
            case 0: buttonString = 'left'; break;
            case 1: buttonString = 'middle'; break;
            case 2: buttonString = 'right'; break;
            case 3: buttonString = 'x1'; break;
            case 4: buttonString = 'x2'; break;
            default: return;
        }

        keybindListeningFor.input.value = buttonString;
        keybindListeningFor.display.textContent = `Mouse ${buttonString}`;
        stopKeybindListen();
    }

    function initializeTabs() {
        document.querySelectorAll('.tab-button').forEach(button => {
            button.addEventListener('click', () => {
                const targetTab = button.getAttribute('data-tab-target');
                
                document.querySelectorAll('.tab-button').forEach(btn => btn.classList.remove('active'));
                document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
                
                button.classList.add('active');
                document.getElementById(targetTab).classList.add('active');
            });
        });
        
        const firstTab = document.querySelector('.tab-button');
        if (firstTab) {
            firstTab.click();
        }
    }

    // Crosshair Functions
    let allCrosshairs = [];
    
    function loadCrosshairs() {
        const grid = document.getElementById('crosshairGrid');
        if (!grid) return;
        
        // Show loading state
        grid.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 2rem;">Loading crosshairs...</div>';
        
        fetch('/api/crosshairs')
            .then(response => response.json())
            .then(data => {
                allCrosshairs = data;
                renderCrosshairs(data);
            })
            .catch(error => {
                console.error('Error loading crosshairs:', error);
                grid.innerHTML = '<div style="grid-column: 1/-1; text-align: center; class="error-text">Failed to load crosshairs</div>';
            });
    }
    
    function renderCrosshairs(crosshairs) {
        const grid = document.getElementById('crosshairGrid');
        if (!grid) return;
        
        grid.innerHTML = '';
        
        if (crosshairs.length === 0) {
            grid.innerHTML = '<div style="grid-column: 1/-1; text-align: center; padding: 2rem; color: var(--text-tertiary);">No crosshairs found.</div>';
            return;
        }
        
        crosshairs.forEach((crosshair, index) => {
            const card = document.createElement('div');
            card.className = 'crosshair-card';
            card.onclick = () => openCrosshairModal(crosshair);
            
            // Create canvas for preview
            const canvasId = `crosshair-canvas-${index}`;
            
            card.innerHTML = `
                <div class="crosshair-preview-box">
                    <canvas id="${canvasId}" width="128" height="128"></canvas>
                </div>
                <div class="crosshair-name">${crosshair.name}</div>
                <div class="text-sm" style="color: var(--text-tertiary);">Click to copy</div>
            `;
            
            grid.appendChild(card);
            
            // Render the crosshair on the canvas
            setTimeout(() => {
                const canvas = document.getElementById(canvasId);
                if (canvas) {
                    drawCrosshairOnCanvas(canvas, crosshair.code);
                }
            }, 0);
        });
    }

    function parseCrosshairCode(code) {
        // Default values
        const params = {
            // General
            c: 0, // Color index
            u: null, // Custom color hex
            h: 0, // Outlines enabled? (This parameter is weird in valorant, usually checks 'o' for outlines)
            
            // Outlines
            o: 1, // Outline opacity usually, or thickness depending on position. Assume thickness/enable
            ot: 1, // Outline thickness
            oa: 0.5, // Outline opacity
            
            // Center Dot
            d: 0, // Center dot enabled
            do: 1, // Center dot opacity
            dt: 2, // Center dot thickness
            
            // Inner Lines (0)
            l0_enabled: 1, // We assume enabled unless we see otherwise (no direct flag usually)
            l0_o: 1, // opacity
            l0_l: 6, // length
            l0_t: 2, // thickness
            l0_off: 3, // offset
            
            // Outer Lines (1)
            l1_enabled: 0, // usually disabled by default if not present
            l1_o: 1,
            l1_l: 2,
            l1_t: 2,
            l1_off: 10
        };

        if (!code) return params;

        const parts = code.split(';');
        for (let i = 0; i < parts.length; i++) {
            const keys = parts[i];
            const nextVal = parts[i + 1]; // Value is usually next

            // General
            if (keys === 'c') params.c = parseInt(nextVal);
            if (keys === 'u') params.u = nextVal; // Custom color
            
            // Center Dot
            if (keys === 'd') params.d = parseInt(nextVal); // Dot enabled
            // In val code: d;1 = enabled.
            
            // Inner Lines (Prefix 0)
            if (keys === '0l') params.l0_l = parseFloat(nextVal);
            if (keys === '0t') params.l0_t = parseFloat(nextVal);
            if (keys === '0o') params.l0_off = parseFloat(nextVal);
            if (keys === '0a') params.l0_o = parseFloat(nextVal);
            
            // Outer Lines (Prefix 1)
            if (keys === '1l') params.l1_l = parseFloat(nextVal);
            if (keys === '1t') params.l1_t = parseFloat(nextVal);
            if (keys === '1o') params.l1_off = parseFloat(nextVal);
            if (keys === '1a') params.l1_o = parseFloat(nextVal); 
            
            // Some codes enable outer lines just by having params, others is explicit. 
            // We'll treat standard parsing.
        }
        
        return params;
    }

    function getCrosshairColor(params) {
        if (params.u) return '#' + params.u.replace('#', ''); // Custom hex
        
        // Standard Colors (approximate Valorant defaults)
        const colors = [
            '#ffffff', // 0: White
            '#00ff00', // 1: Green
            '#7fff00', // 2: Yellow Green
            '#adff2f', // 3: Green Yellow
            '#ffff00', // 4: Yellow
            '#00ffff', // 5: Cyan
            '#ff00ff', // 6: Pink
            '#ff0000', // 7: Red
            '#0000ff'  // 8: Blue
        ];
        return colors[params.c] || '#00ff00';
    }

    function drawCrosshairOnCanvas(canvas, code) {
        const ctx = canvas.getContext('2d');
        const w = canvas.width;
        const h = canvas.height;
        const cx = w / 2;
        const cy = h / 2;
        
        // Clear
        ctx.clearRect(0, 0, w, h);
        
        const p = parseCrosshairCode(code);
        const color = getCrosshairColor(p);
        
        // Convert Valorant units to pixels (rough approximation for preview)
        // 1 val unit approx 1-2 pixels depending on resolution, we'll use 2x for visibility
        const scale = 2; 

        // Helper to draw rect
        const drawRect = (x, y, w, h, fill, alpha) => {
            ctx.fillStyle = fill;
            ctx.globalAlpha = alpha;
            ctx.fillRect(x, y, w, h);
            ctx.globalAlpha = 1.0;
        };

        // --- Inner Lines ---
        // (Only if opacity > 0 and length > 0)
        if (p.l0_o > 0 && p.l0_l > 0) {
            const thick = Math.max(1, p.l0_t * scale);
            const len = p.l0_l * scale;
            const off = p.l0_off * scale;
            
            // Horizontal
            drawRect(cx - off - len, cy - thick/2, len, thick, color, p.l0_o); // Left
            drawRect(cx + off, cy - thick/2, len, thick, color, p.l0_o); // Right
            
            // Vertical
            drawRect(cx - thick/2, cy - off - len, thick, len, color, p.l0_o); // Top
            drawRect(cx - thick/2, cy + off, thick, len, color, p.l0_o); // Bottom
        }

        // --- Outer Lines ---
        if (p.l1_o > 0 && p.l1_l > 0) {
            const thick = Math.max(1, p.l1_t * scale);
            const len = p.l1_l * scale;
            const off = p.l1_off * scale;
             
            // Horizontal
            drawRect(cx - off - len, cy - thick/2, len, thick, color, p.l1_o); // Left
            drawRect(cx + off, cy - thick/2, len, thick, color, p.l1_o); // Right
            
            // Vertical
            drawRect(cx - thick/2, cy - off - len, thick, len, color, p.l1_o); // Top
            drawRect(cx - thick/2, cy + off, thick, len, color, p.l1_o); // Bottom
        }

        // --- Center Dot ---
        if (p.d === 1) {
            // Dot thickness in Val is size.
            const size = Math.max(2, p.dt * scale); 
            drawRect(cx - size/2, cy - size/2, size, size, color, p.do || 1);
        }
    }
    
    function openCrosshairModal(crosshair) {
        document.getElementById('modalTitle').textContent = crosshair.name;
        document.getElementById('crosshairCode').textContent = crosshair.code;
        
        // Draw large preview
        const modal = document.getElementById('crosshairModal');
        const largePreviewContainer = modal.querySelector('.preview-large');
        
        // Clear previous content (text overlay)
        largePreviewContainer.innerHTML = '';
        
        // Create large canvas
        const canvas = document.createElement('canvas');
        canvas.width = 500;
        canvas.height = 250;
        largePreviewContainer.appendChild(canvas);
        
        drawCrosshairOnCanvas(canvas, crosshair.code);
        
        modal.classList.add('active');
    }
    
    function closeCrosshairModal() {
        document.getElementById('crosshairModal').classList.remove('active');
    }
    
    function copyCrosshairCode() {
        const code = document.getElementById('crosshairCode').textContent;
        
        // Try modern Clipboard API first
        if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(code).then(() => {
                showToast('Crosshair code copied to clipboard!', 'success');
                closeCrosshairModal();
            }).catch(err => {
                console.error('Clipboard write failed:', err);
                fallbackCopy(code);
            });
        } else {
            // Fallback for non-secure contexts (http)
            fallbackCopy(code);
        }
    }
    
    function fallbackCopy(text) {
        const textArea = document.createElement("textarea");
        textArea.value = text;
        
        // Ensure it's not visible but part of DOM
        textArea.style.position = "fixed";
        textArea.style.left = "-9999px";
        textArea.style.top = "0";
        document.body.appendChild(textArea);
        
        textArea.focus();
        textArea.select();
        
        try {
            const successful = document.execCommand('copy');
            if (successful) {
                showToast('Crosshair code copied!', 'success');
                closeCrosshairModal();
            } else {
                showToast('Failed to copy code. Please copy manually.', 'error');
            }
        } catch (err) {
            console.error('Fallback copy failed:', err);
            showToast('Failed to copy code. Please copy manually.', 'error');
        }
        
        document.body.removeChild(textArea);
    }
    
    // Close modal when clicking outside
    window.addEventListener('click', (e) => {
        const modal = document.getElementById('crosshairModal');
        if (e.target === modal) {
            closeCrosshairModal();
        }
    });

    // ============================================
    // Membership Functions
    // ============================================
    
    async function refreshMembershipStatus() {
        try {
            // Use refresh=1 to force fresh validation from Supabase
            const response = await fetch('/api/membership/info?refresh=1');
            const data = await response.json();
            
            if (data.success && data.membership) {
                const m = data.membership;
                
                // Update global membership tier for feature locking
                currentMembershipTier = m.tier;
                
                // Update tier display
                const tierDisplay = document.getElementById('membershipTierDisplay');
                if (tierDisplay) tierDisplay.textContent = m.tier_display || m.tier;
                
                // Update days remaining
                const daysDisplay = document.getElementById('membershipDaysDisplay');
                const currentPlanDays = document.getElementById('currentPlanDays');
                if (daysDisplay) {
                    if (m.is_lifetime) {
                        daysDisplay.textContent = '∞ Lifetime';
                        if (currentPlanDays) currentPlanDays.textContent = '∞ Lifetime';
                    } else {
                        daysDisplay.textContent = m.days_remaining + ' days';
                        if (currentPlanDays) currentPlanDays.textContent = m.days_remaining + ' days';
                    }
                }
                
                // Count unlocked features
                const featuresUnlocked = Object.values(m.features).filter(v => v === true).length;
                const featuresCount = document.getElementById('membershipFeaturesCount');
                if (featuresCount) featuresCount.textContent = featuresUnlocked + '/8';
                
                // Update feature access grid
                updateFeatureAccessGrid(m.features);
                
                // Hide/show upgrade section based on tier
                const upgradeSection = document.getElementById('upgradeSection');
                const fullAccessMessage = document.getElementById('fullAccessMessage');
                
                if (m.tier === 'full_access') {
                    // User has Full Access - hide upgrade options
                    if (upgradeSection) upgradeSection.style.display = 'none';
                    if (fullAccessMessage) fullAccessMessage.style.display = 'block';
                    
                    // Hide PRO badges since user has Full Access
                    document.querySelectorAll('.nav-pro-badge').forEach(badge => {
                        badge.innerHTML = '<i class="fas fa-check" style="color: #10b981;"></i>';
                        badge.style.background = 'rgba(16, 185, 129, 0.2)';
                        badge.style.color = '#10b981';
                    });
                } else {
                    // User has Regular or no tier - show upgrade options
                    if (upgradeSection) upgradeSection.style.display = 'block';
                    if (fullAccessMessage) fullAccessMessage.style.display = 'none';
                    
                    // Show PRO badges since user doesn't have Full Access
                    document.querySelectorAll('.nav-pro-badge').forEach(badge => {
                        badge.innerHTML = 'PRO';
                        badge.style.background = 'linear-gradient(135deg, #fbbf24, #f59e0b)';
                        badge.style.color = '#000';
                    });
                }
                
                showToast('Membership status refreshed', 'success');
                
                // Also check for expiry after refresh
                if (!m.is_active || m.days_remaining <= 0) {
                    showExpiryWarning();
                }
            } else {
                document.getElementById('membershipTierDisplay').textContent = 'No License';
                document.getElementById('membershipDaysDisplay').textContent = '0 days';
                document.getElementById('membershipFeaturesCount').textContent = '0/8';
                showToast('No active membership found', 'warning');
                
                // Show expiry warning for expired/no license
                showExpiryWarning();
            }
        } catch (error) {
            console.error('Error fetching membership:', error);
            document.getElementById('membershipTierDisplay').textContent = 'Error';
            showToast('Failed to fetch membership status', 'error');
        }
    }
    
    function updateFeatureAccessGrid(features) {
        const grid = document.getElementById('featureAccessGrid');
        if (!grid) return;
        
        // Feature definitions with special states for Regular tier
        const featureNames = {
            'aimbot': { name: 'Aimbot', icon: 'fa-crosshairs', regularNote: null },
            'triggerbot': { name: 'Triggerbot', icon: 'fa-bolt', regularNote: null },
            'anti_recoil': { name: 'Anti-Recoil', icon: 'fa-arrows-down-to-line', regularNote: null },
            'crosshair_overlay': { name: 'Crosshair', icon: 'fa-plus', regularNote: null },
            'humanizer': { name: 'Humanizer', icon: 'fa-hand-paper', regularNote: 'Read-Only' },
            'fingerprint_randomization': { name: 'Fingerprint', icon: 'fa-fingerprint', regularNote: 'Static' },
            'advanced_settings': { name: 'Settings', icon: 'fa-cog', regularNote: null },
            'web_ui': { name: 'Web UI', icon: 'fa-globe', regularNote: null }
        };
        
        grid.innerHTML = '';
        
        for (const [key, info] of Object.entries(featureNames)) {
            const hasAccess = features[key] === true;
            const isRegularTier = currentMembershipTier === 'regular';
            const hasSpecialNote = isRegularTier && info.regularNote && hasAccess;
            
            // Determine status text and color
            let statusText, statusColor, bgColor, borderColor;
            
            if (hasSpecialNote) {
                // Feature is accessible but with limitations (Read-Only, Static, etc.)
                statusText = info.regularNote;
                statusColor = '#f59e0b'; // Orange/warning
                bgColor = 'rgba(245, 158, 11, 0.1)';
                borderColor = 'rgba(245, 158, 11, 0.3)';
            } else if (hasAccess) {
                // Full access to feature
                statusText = '✓ Unlocked';
                statusColor = 'var(--accent-secondary)';
                bgColor = 'rgba(16, 185, 129, 0.1)';
                borderColor = 'rgba(16, 185, 129, 0.3)';
            } else {
                // No access
                statusText = '🔒 Locked';
                statusColor = 'var(--accent-danger)';
                bgColor = 'rgba(239, 68, 68, 0.1)';
                borderColor = 'rgba(239, 68, 68, 0.3)';
            }
            
            const card = document.createElement('div');
            card.style.cssText = `
                text-align: center; 
                padding: var(--space-4); 
                background: ${bgColor}; 
                border: 1px solid ${borderColor}; 
                border-radius: var(--radius-lg);
            `;
            card.innerHTML = `
                <i class="fas ${info.icon}" style="font-size: 1.5rem; color: ${statusColor}; margin-bottom: var(--space-2);"></i>
                <div style="font-weight: 600; color: var(--text-primary); font-size: 0.875rem;">${info.name}</div>
                <div style="font-size: 0.75rem; color: ${statusColor}; margin-top: var(--space-1);">
                    ${statusText}
                </div>
            `;
            grid.appendChild(card);
        }
    }
    
    async function selectPlan(tier) {
        const selectId = tier === 'regular' ? 'regularDurationSelect' : 'fullAccessDurationSelect';
        const select = document.getElementById(selectId);
        const duration = select.value;
        const price = select.options[select.selectedIndex].getAttribute('data-price');
        
        // Show confirmation
        const tierName = tier === 'regular' ? 'Regular' : 'Full Access';
        const durationText = duration.replace('_', ' ');
        
        if (confirm(`Upgrade to ${tierName} for ${durationText} ($${price})?\n\nYou will be redirected to Stripe to complete your payment securely.`)) {
            // Show loading state
            showToast('Creating checkout session...', 'info');
            
            try {
                const response = await fetch('/api/membership/create_checkout', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ tier: tier, duration: duration })
                });
                
                const data = await response.json();
                
                if (data.success && data.checkout_url) {
                    showToast('Redirecting to Stripe...', 'success');
                    // Redirect to Stripe Checkout
                    window.location.href = data.checkout_url;
                } else {
                    showToast('Failed to create checkout: ' + (data.message || 'Unknown error'), 'error');
                }
            } catch (error) {
                console.error('Checkout error:', error);
                showToast('Error creating checkout session. Please try again.', 'error');
            }
        }
    }
    
    async function performUpgrade(tier, duration) {
        try {
            const response = await fetch('/api/membership/upgrade', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ tier: tier, duration: duration })
            });
            
            const data = await response.json();
            
            if (data.success) {
                showToast(data.message, 'success');
                refreshMembershipStatus();
            } else {
                showToast('Upgrade failed: ' + (data.message || 'Unknown error'), 'error');
            }
        } catch (error) {
            console.error('Upgrade error:', error);
            showToast('Failed to process upgrade', 'error');
        }
    }
    
    // Load membership status when switching to the membership tab
    function initMembershipTab() {
        // Auto-refresh when tab is opened
        setTimeout(() => {
            refreshMembershipStatus();
        }, 500);
    }
    
    // License Transfer Functions
    async function generateTransferCode() {
        if (!confirm('⚠️ WARNING: This will deactivate your license on THIS PC.\n\nYou will need to enter the transfer code on your NEW PC to reactivate.\n\nContinue?')) {
            return;
        }
        
        try {
            const response = await fetch('/api/membership/transfer/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' }
            });
            
            const data = await response.json();
            
            if (data.success && data.transfer_code) {
                // Display the transfer code
                document.getElementById('transferCodeDisplay').style.display = 'block';
                document.getElementById('generatedTransferCode').textContent = data.transfer_code;
                showToast('Transfer code generated! Write it down.', 'success');
            } else {
                showToast(data.message || 'Failed to generate transfer code', 'error');
            }
        } catch (error) {
            console.error('Transfer error:', error);
            showToast('Error generating transfer code', 'error');
        }
    }
    
    async function redeemTransferCode() {
        const code = document.getElementById('transferCodeInput').value.trim().toUpperCase();
        
        if (!code || code.length !== 6) {
            showToast('Please enter a valid 6-character transfer code', 'warning');
            return;
        }
        
        try {
            const response = await fetch('/api/membership/transfer/redeem', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ transfer_code: code })
            });
            
            const data = await response.json();
            
            if (data.success) {
                showToast(data.message || 'License transferred successfully!', 'success');
                // Clear input and refresh
                document.getElementById('transferCodeInput').value = '';
                setTimeout(() => {
                    refreshMembershipStatus();
                }, 1000);
            } else {
                showToast(data.message || 'Failed to redeem transfer code', 'error');
            }
        } catch (error) {
            console.error('Redeem error:', error);
            showToast('Error redeeming transfer code', 'error');
        }
    }

    // ============================================
    // SPOTIFY PLAYER FUNCTIONS
    // ============================================
    let spotifyQueue = [];
    let spotifyCurrentIndex = -1;
    let spotifyAudio = null;
    let spotifyAudioPreload = null;  // Second audio element for preloading
    let spotifyIsPlaying = false;
    let preloadedNextTrack = false;  // Flag to track if next song is preloaded
    let nextTrackUrl = null;         // Store preloaded URL
    
    function initSpotifyPlayer() {
        spotifyAudio = document.getElementById('spotifyAudio');
        
        // Create preload audio element
        spotifyAudioPreload = document.createElement('audio');
        spotifyAudioPreload.preload = 'auto';
        spotifyAudioPreload.style.display = 'none';
        document.body.appendChild(spotifyAudioPreload);
        
        if (spotifyAudio) {
            spotifyAudio.volume = 0.8;
            
            spotifyAudio.addEventListener('timeupdate', updateSpotifyProgress);
            spotifyAudio.addEventListener('ended', onTrackEnded);
            spotifyAudio.addEventListener('loadedmetadata', () => {
                document.getElementById('spotifyDuration').textContent = formatTime(spotifyAudio.duration);
            });
        }
    }
    
    function formatTime(seconds) {
        if (isNaN(seconds)) return '0:00';
        const mins = Math.floor(seconds / 60);
        const secs = Math.floor(seconds % 60);
        return `${mins}:${secs.toString().padStart(2, '0')}`;
    }
    
    function updateSpotifyProgress() {
        if (!spotifyAudio) return;
        const progress = (spotifyAudio.currentTime / spotifyAudio.duration) * 100;
        document.getElementById('spotifyProgressBar').style.width = `${progress}%`;
        document.getElementById('spotifyCurrentTime').textContent = formatTime(spotifyAudio.currentTime);
        
        // Preload next track 30 seconds before current ends
        const timeRemaining = spotifyAudio.duration - spotifyAudio.currentTime;
        if (timeRemaining <= 30 && timeRemaining > 0 && !preloadedNextTrack) {
            preloadNextTrack();
        }
    }
    
    // Preload the next track in the queue
    async function preloadNextTrack() {
        const nextIndex = spotifyCurrentIndex + 1;
        if (nextIndex >= spotifyQueue.length) {
            preloadedNextTrack = false;
            nextTrackUrl = null;
            return;
        }
        
        preloadedNextTrack = true;  // Mark as started to prevent duplicate calls
        const nextTrack = spotifyQueue[nextIndex];
        
        console.log('[Spotify] Preloading next track:', nextTrack.title);
        
        try {
            const response = await fetch('/api/spotify/stream', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ query: `${nextTrack.artist} ${nextTrack.title}` })
            });
            
            const data = await response.json();
            
            if (data.success && data.stream_url) {
                nextTrackUrl = data.stream_url;
                spotifyAudioPreload.src = data.stream_url;
                spotifyAudioPreload.load();  // Start buffering
                console.log('[Spotify] Next track preloaded and buffering');
            }
        } catch (error) {
            console.error('[Spotify] Failed to preload next track:', error);
            preloadedNextTrack = false;
        }
    }
    
    // Called when current track ends - use preloaded audio if available
    function onTrackEnded() {
        if (spotifyCurrentIndex < spotifyQueue.length - 1) {
            // Move to next track
            spotifyCurrentIndex++;
            const track = spotifyQueue[spotifyCurrentIndex];
            
            // Update Now Playing UI
            document.getElementById('spotifyNowPlayingTitle').textContent = track.title;
            document.getElementById('spotifyNowPlayingArtist').textContent = track.artist;
            if (track.thumbnail) {
                document.getElementById('spotifyNowPlayingArt').innerHTML = `<img src="${track.thumbnail}" style="width: 100%; height: 100%; object-fit: cover; border-radius: var(--radius-lg);">`;
            }
            updateQueueUI();
            
            // Use preloaded audio if available
            if (nextTrackUrl && spotifyAudioPreload.src) {
                console.log('[Spotify] Using preloaded track - gapless playback!');
                spotifyAudio.src = nextTrackUrl;
                spotifyAudio.play();
                
                // Reset preload state for next track
                preloadedNextTrack = false;
                nextTrackUrl = null;
            } else {
                // Fallback: fetch and play normally
                playSpotifyTrack(spotifyCurrentIndex);
            }
        } else {
            // End of queue
            spotifyIsPlaying = false;
            document.querySelector('#spotifyPlayBtn i').className = 'fas fa-play';
            document.querySelector('#spotifyPlayBtn i').style.marginLeft = '4px';
            preloadedNextTrack = false;
            nextTrackUrl = null;
        }
    }
    
    function seekSpotify(event) {
        if (!spotifyAudio || !spotifyAudio.duration) return;
        const bar = event.currentTarget;
        const rect = bar.getBoundingClientRect();
        const percent = (event.clientX - rect.left) / rect.width;
        spotifyAudio.currentTime = percent * spotifyAudio.duration;
    }
    
    function setSpotifyVolume(value) {
        if (spotifyAudio) {
            spotifyAudio.volume = value / 100;
        }
    }
    
    function toggleSpotifyPlay() {
        if (!spotifyAudio) return;
        
        if (spotifyIsPlaying) {
            spotifyAudio.pause();
            spotifyIsPlaying = false;
            document.querySelector('#spotifyPlayBtn i').className = 'fas fa-play';
        } else {
            if (spotifyAudio.src) {
                spotifyAudio.play();
                spotifyIsPlaying = true;
                document.querySelector('#spotifyPlayBtn i').className = 'fas fa-pause';
            } else if (spotifyQueue.length > 0) {
                playSpotifyTrack(0);
            }
        }
    }
    
    function spotifyPrev() {
        if (spotifyCurrentIndex > 0) {
            playSpotifyTrack(spotifyCurrentIndex - 1);
        }
    }
    
    function spotifyNext() {
        if (spotifyCurrentIndex < spotifyQueue.length - 1) {
            playSpotifyTrack(spotifyCurrentIndex + 1);
        } else {
            // End of queue
            spotifyIsPlaying = false;
            document.querySelector('#spotifyPlayBtn i').className = 'fas fa-play';
        }
    }
    
    async function playSpotifyTrack(index) {
        if (index < 0 || index >= spotifyQueue.length) return;
        
        spotifyCurrentIndex = index;
        const track = spotifyQueue[index];
        
        // Update UI
        document.getElementById('spotifyNowPlayingTitle').textContent = track.title;
        document.getElementById('spotifyNowPlayingArtist').textContent = track.artist;
        
        if (track.thumbnail) {
            document.getElementById('spotifyNowPlayingArt').innerHTML = `<img src="${track.thumbnail}" style="width: 100%; height: 100%; object-fit: cover;">`;
        }
        
        // Show loading
        showToast(`Loading: ${track.title}...`, 'info');
        
        try {
            // Request stream URL from backend
            const response = await fetch('/api/spotify/stream', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ query: `${track.artist} ${track.title}` })
            });
            
            const data = await response.json();
            
            if (data.success && data.stream_url) {
                spotifyAudio.src = data.stream_url;
                spotifyAudio.play();
                spotifyIsPlaying = true;
                document.querySelector('#spotifyPlayBtn i').className = 'fas fa-pause';
                updateQueueUI();
            } else {
                showToast(data.message || 'Failed to load track', 'error');
            }
        } catch (error) {
            console.error('Spotify play error:', error);
            showToast('Error loading track', 'error');
        }
    }
    
    function addToSpotifyQueue(track) {
        spotifyQueue.push(track);
        updateQueueUI();
        showToast(`Added: ${track.title}`, 'success');
        
        // Auto-play if first track
        if (spotifyQueue.length === 1) {
            playSpotifyTrack(0);
        }
    }
    
    function clearSpotifyQueue() {
        spotifyQueue = [];
        spotifyCurrentIndex = -1;
        if (spotifyAudio) {
            spotifyAudio.pause();
            spotifyAudio.src = '';
        }
        spotifyIsPlaying = false;
        document.querySelector('#spotifyPlayBtn i').className = 'fas fa-play';
        document.getElementById('spotifyNowPlayingTitle').textContent = 'No song playing';
        document.getElementById('spotifyNowPlayingArtist').textContent = 'Select a song to start';
        document.getElementById('spotifyNowPlayingArt').innerHTML = '<i class="fas fa-music" style="font-size: 3rem; color: var(--text-tertiary);"></i>';
        document.getElementById('spotifyProgressBar').style.width = '0%';
        updateQueueUI();
    }
    
    function updateQueueUI() {
        const queueDiv = document.getElementById('spotifyQueue');
        
        if (spotifyQueue.length === 0) {
            queueDiv.innerHTML = `
                <div style="text-align: center; padding: var(--space-6); color: var(--text-tertiary);">
                    <i class="fas fa-music" style="font-size: 2rem; margin-bottom: var(--space-2); opacity: 0.5;"></i>
                    <p style="font-size: 0.85rem;">Queue is empty</p>
                    <p style="font-size: 0.75rem; opacity: 0.7;">Add songs to play them</p>
                </div>
            `;
            return;
        }
        
        queueDiv.innerHTML = spotifyQueue.map((track, i) => `
            <div style="display: flex; align-items: center; gap: var(--space-3); padding: var(--space-2); background: ${i === spotifyCurrentIndex ? 'rgba(30, 215, 96, 0.2)' : 'var(--bg-quaternary)'}; border-radius: var(--radius-md); cursor: pointer;" onclick="playSpotifyTrack(${i})">
                <div style="width: 40px; height: 40px; background: var(--bg-tertiary); border-radius: var(--radius-sm); overflow: hidden; display: flex; align-items: center; justify-content: center;">
                    ${track.thumbnail ? `<img src="${track.thumbnail}" style="width: 100%; height: 100%; object-fit: cover;">` : '<i class="fas fa-music" style="color: var(--text-tertiary);"></i>'}
                </div>
                <div style="flex: 1; overflow: hidden;">
                    <div style="font-size: 0.85rem; font-weight: 600; color: ${i === spotifyCurrentIndex ? '#1DB954' : 'var(--text-primary)'}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${track.title}</div>
                    <div style="font-size: 0.75rem; color: var(--text-tertiary); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${track.artist}</div>
                </div>
                ${i === spotifyCurrentIndex ? '<i class="fas fa-volume-up" style="color: #1DB954;"></i>' : ''}
            </div>
        `).join('');
    }
    
    async function searchSpotify() {
        const query = document.getElementById('spotifySearchInput').value.trim();
        if (!query) return;
        
        const resultsDiv = document.getElementById('spotifyResults');
        resultsDiv.innerHTML = '<div style="text-align: center; padding: var(--space-8);"><i class="fas fa-spinner fa-spin" style="font-size: 2rem; color: #1DB954;"></i><p style="margin-top: var(--space-4); color: var(--text-secondary);">Searching...</p></div>';
        
        document.getElementById('spotifyResultsTitle').textContent = `Results for "${query}"`;
        
        try {
            const response = await fetch('/api/spotify/search', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ query })
            });
            
            const data = await response.json();
            
            if (data.success && data.tracks && data.tracks.length > 0) {
                displaySpotifyResults(data.tracks);
            } else {
                resultsDiv.innerHTML = '<div style="text-align: center; padding: var(--space-8); color: var(--text-tertiary);"><i class="fas fa-search" style="font-size: 3rem; margin-bottom: var(--space-4); opacity: 0.5;"></i><p>No results found</p></div>';
            }
        } catch (error) {
            console.error('Search error:', error);
            resultsDiv.innerHTML = '<div style="text-align: center; padding: var(--space-8); color: var(--accent-danger);"><i class="fas fa-exclamation-circle" style="font-size: 2rem; margin-bottom: var(--space-2);"></i><p>Error searching. Try again.</p></div>';
        }
    }
    
    function displaySpotifyResults(tracks) {
        const resultsDiv = document.getElementById('spotifyResults');
        
        resultsDiv.innerHTML = tracks.map(track => `
            <div style="display: flex; align-items: center; gap: var(--space-4); padding: var(--space-3); background: var(--bg-tertiary); border-radius: var(--radius-lg); transition: all 0.2s;" onmouseover="this.style.background='rgba(30, 215, 96, 0.1)'" onmouseout="this.style.background='var(--bg-tertiary)'">
                <div style="width: 56px; height: 56px; background: var(--bg-quaternary); border-radius: var(--radius-md); overflow: hidden; flex-shrink: 0;">
                    ${track.thumbnail ? `<img src="${track.thumbnail}" style="width: 100%; height: 100%; object-fit: cover;">` : '<div style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center;"><i class="fas fa-music" style="color: var(--text-tertiary);"></i></div>'}
                </div>
                <div style="flex: 1; overflow: hidden;">
                    <div style="font-weight: 600; color: var(--text-primary); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${track.title}</div>
                    <div style="font-size: 0.85rem; color: var(--text-secondary);">${track.artist}</div>
                    ${track.duration ? `<div style="font-size: 0.75rem; color: var(--text-tertiary);">${track.duration}</div>` : ''}
                </div>
                <button class="btn" style="background: #1DB954; color: #000; padding: var(--space-2) var(--space-4);" onclick='addToSpotifyQueue(${JSON.stringify(track).replace(/'/g, "\\'")})'>
                    <i class="fas fa-plus"></i> Add
                </button>
            </div>
        `).join('');
    }
    
    async function loadPopularTracks() {
        document.getElementById('spotifyResultsTitle').textContent = 'Popular Tracks';
        document.getElementById('spotifyResults').innerHTML = '<div style="text-align: center; padding: var(--space-8);"><i class="fas fa-spinner fa-spin" style="font-size: 2rem; color: #1DB954;"></i><p style="margin-top: var(--space-4); color: var(--text-secondary);">Loading popular tracks...</p></div>';
        
        try {
            const response = await fetch('/api/spotify/popular');
            const data = await response.json();
            
            if (data.success && data.tracks) {
                displaySpotifyResults(data.tracks);
            }
        } catch (error) {
            console.error('Load popular error:', error);
        }
    }
    
    async function loadPlaylist(type) {
        showToast(`Loading ${type} playlist...`, 'info');
        
        try {
            const response = await fetch(`/api/spotify/playlist/${type}`);
            const data = await response.json();
            
            if (data.success && data.tracks) {
                spotifyQueue = data.tracks;
                updateQueueUI();
                if (spotifyQueue.length > 0) {
                    playSpotifyTrack(0);
                }
                showToast(`Loaded ${spotifyQueue.length} tracks`, 'success');
            }
        } catch (error) {
            console.error('Load playlist error:', error);
            showToast('Error loading playlist', 'error');
        }
    }
    
    // ============================================
    // CUSTOM PLAYLISTS (localStorage)
    // ============================================
    let spotifyPlaylists = [];
    let pendingAddTrack = null;
    
    function loadSpotifyPlaylists() {
        try {
            const saved = localStorage.getItem('spotify_playlists');
            if (saved) {
                spotifyPlaylists = JSON.parse(saved);
            }
        } catch (e) {
            spotifyPlaylists = [];
        }
        renderMyPlaylists();
        updatePlaylistCount();
    }
    
    function saveSpotifyPlaylists() {
        try {
            localStorage.setItem('spotify_playlists', JSON.stringify(spotifyPlaylists));
            updatePlaylistCount();
        } catch (e) {
            console.error('Failed to save playlists:', e);
        }
    }
    
    function updatePlaylistCount() {
        const countEl = document.getElementById('spotifyPlaylistCount');
        if (countEl) {
            countEl.textContent = spotifyPlaylists.length;
        }
    }
    
    function createNewPlaylist() {
        // Open custom styled modal instead of ugly browser prompt
        const modal = document.getElementById('createPlaylistModal');
        const input = document.getElementById('createPlaylistInput');
        modal.style.display = 'flex';
        input.value = '';
        setTimeout(() => input.focus(), 100);
    }
    
    function closeCreatePlaylistModal() {
        document.getElementById('createPlaylistModal').style.display = 'none';
    }
    
    function confirmCreatePlaylist() {
        const input = document.getElementById('createPlaylistInput');
        const name = input.value.trim();
        
        if (!name) {
            showToast('Please enter a playlist name', 'warning');
            return;
        }
        
        const playlist = {
            id: Date.now(),
            name: name,
            tracks: [],
            created: new Date().toISOString()
        };
        
        spotifyPlaylists.push(playlist);
        saveSpotifyPlaylists();
        renderMyPlaylists();
        closeCreatePlaylistModal();
        showToast(`Playlist "${name}" created!`, 'success');
    }
    
    function renderMyPlaylists() {
        const container = document.getElementById('spotifyMyPlaylists');
        if (!container) return;
        
        if (spotifyPlaylists.length === 0) {
            container.innerHTML = `
                <div style="text-align: center; padding: var(--space-6); color: rgba(255,255,255,0.3);">
                    <i class="fas fa-folder-open" style="font-size: 1.5rem; margin-bottom: var(--space-2);"></i>
                    <p style="font-size: 0.85rem;">No playlists yet</p>
                    <p style="font-size: 0.75rem; opacity: 0.7;">Click "New" to create one</p>
                </div>
            `;
            return;
        }
        
        container.innerHTML = spotifyPlaylists.map(pl => `
            <div style="display: flex; align-items: center; gap: var(--space-3); padding: var(--space-2); background: rgba(255,255,255,0.05); border-radius: var(--radius-md); margin-bottom: var(--space-2); cursor: pointer;" onmouseover="this.style.background='rgba(233, 30, 99, 0.15)'" onmouseout="this.style.background='rgba(255,255,255,0.05)'">
                <div style="width: 36px; height: 36px; background: linear-gradient(135deg, #e91e63, #c2185b); border-radius: var(--radius-sm); display: flex; align-items: center; justify-content: center; flex-shrink: 0;" onclick="loadMyPlaylist(${pl.id})">
                    <i class="fas fa-music" style="color: #fff; font-size: 0.8rem;"></i>
                </div>
                <div style="flex: 1; overflow: hidden;" onclick="loadMyPlaylist(${pl.id})">
                    <div style="font-size: 0.85rem; font-weight: 600; color: #fff; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${pl.name}</div>
                    <div style="font-size: 0.7rem; color: rgba(255,255,255,0.4);">${pl.tracks.length} tracks</div>
                </div>
                <button style="background: transparent; border: none; color: rgba(255,255,255,0.4); cursor: pointer; padding: 4px;" onclick="event.stopPropagation(); openEditPlaylistModal(${pl.id})" title="Edit">
                    <i class="fas fa-pen" style="font-size: 0.7rem;"></i>
                </button>
                <button style="background: transparent; border: none; color: rgba(255,255,255,0.3); cursor: pointer; padding: 4px;" onclick="event.stopPropagation(); deletePlaylist(${pl.id})" title="Delete">
                    <i class="fas fa-trash" style="font-size: 0.7rem;"></i>
                </button>
            </div>
        `).join('');
    }
    
    function loadMyPlaylist(playlistId) {
        const playlist = spotifyPlaylists.find(p => p.id === playlistId);
        if (!playlist) return;
        
        if (playlist.tracks.length === 0) {
            showToast(`"${playlist.name}" is empty`, 'warning');
            return;
        }
        
        spotifyQueue = [...playlist.tracks];
        updateQueueUI();
        playSpotifyTrack(0);
        showToast(`Playing "${playlist.name}"`, 'success');
    }
    
    function deletePlaylist(playlistId) {
        const playlist = spotifyPlaylists.find(p => p.id === playlistId);
        if (!playlist) return;
        
        if (!confirm(`Delete playlist "${playlist.name}"?`)) return;
        
        spotifyPlaylists = spotifyPlaylists.filter(p => p.id !== playlistId);
        saveSpotifyPlaylists();
        renderMyPlaylists();
        showToast(`Playlist deleted`, 'info');
    }
    
    // Edit Playlist Modal
    let editingPlaylistId = null;
    
    function openEditPlaylistModal(playlistId) {
        const playlist = spotifyPlaylists.find(p => p.id === playlistId);
        if (!playlist) return;
        
        editingPlaylistId = playlistId;
        const modal = document.getElementById('editPlaylistModal');
        const content = document.getElementById('editPlaylistContent');
        const title = document.getElementById('editPlaylistTitle');
        
        title.textContent = playlist.name;
        
        if (playlist.tracks.length === 0) {
            content.innerHTML = `
                <div style="text-align: center; padding: 40px; color: rgba(255,255,255,0.4);">
                    <i class="fas fa-music" style="font-size: 3rem; margin-bottom: 16px; opacity: 0.3;"></i>
                    <p>This playlist is empty</p>
                    <p style="font-size: 0.85rem; opacity: 0.7;">Search for songs and click "Save" to add them</p>
                </div>
            `;
        } else {
            content.innerHTML = playlist.tracks.map((track, index) => `
                <div style="display: flex; align-items: center; gap: 12px; padding: 12px; background: rgba(255,255,255,0.05); border-radius: 12px; margin-bottom: 8px;">
                    <div style="width: 48px; height: 48px; background: #282828; border-radius: 8px; overflow: hidden; flex-shrink: 0;">
                        ${track.thumbnail ? `<img src="${track.thumbnail}" style="width: 100%; height: 100%; object-fit: cover;">` : '<div style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center;"><i class="fas fa-music" style="color: #404040;"></i></div>'}
                    </div>
                    <div style="flex: 1; overflow: hidden;">
                        <div style="font-weight: 600; color: #fff; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${track.title}</div>
                        <div style="font-size: 0.85rem; color: rgba(255,255,255,0.5);">${track.artist}</div>
                    </div>
                    <button style="background: rgba(239, 68, 68, 0.2); border: 1px solid rgba(239, 68, 68, 0.4); color: #ef4444; padding: 8px 14px; border-radius: 20px; cursor: pointer; font-size: 0.85rem; font-weight: 600; transition: all 0.2s;" onclick="removeTrackFromPlaylist(${playlistId}, ${index})" onmouseover="this.style.background='rgba(239, 68, 68, 0.3)'" onmouseout="this.style.background='rgba(239, 68, 68, 0.2)'">
                        <i class="fas fa-trash"></i> Remove
                    </button>
                </div>
            `).join('');
        }
        
        modal.style.display = 'flex';
    }
    
    function closeEditPlaylistModal() {
        document.getElementById('editPlaylistModal').style.display = 'none';
        editingPlaylistId = null;
    }
    
    function removeTrackFromPlaylist(playlistId, trackIndex) {
        const playlist = spotifyPlaylists.find(p => p.id === playlistId);
        if (!playlist) return;
        
        const trackName = playlist.tracks[trackIndex]?.title || 'Track';
        playlist.tracks.splice(trackIndex, 1);
        saveSpotifyPlaylists();
        renderMyPlaylists();
        
        // Refresh the modal content
        openEditPlaylistModal(playlistId);
        showToast(`Removed "${trackName}"`, 'info');
    }
    
    function openAddToPlaylistModal(track) {
        pendingAddTrack = track;
        const modal = document.getElementById('addToPlaylistModal');
        const content = document.getElementById('playlistModalContent');
        
        if (spotifyPlaylists.length === 0) {
            content.innerHTML = `
                <div style="text-align: center; padding: var(--space-6); color: rgba(255,255,255,0.5);">
                    <p>No playlists yet</p>
                    <button style="margin-top: var(--space-4); background: #1DB954; border: none; color: #000; padding: 10px 20px; border-radius: 20px; cursor: pointer; font-weight: 600;" onclick="closePlaylistModal(); createNewPlaylist();">
                        Create Playlist
                    </button>
                </div>
            `;
        } else {
            content.innerHTML = spotifyPlaylists.map(pl => `
                <div style="display: flex; align-items: center; gap: var(--space-3); padding: var(--space-3); background: rgba(255,255,255,0.05); border-radius: var(--radius-md); margin-bottom: var(--space-2); cursor: pointer;" onclick="addTrackToPlaylist(${pl.id})" onmouseover="this.style.background='rgba(29, 185, 84, 0.2)'" onmouseout="this.style.background='rgba(255,255,255,0.05)'">
                    <div style="width: 40px; height: 40px; background: linear-gradient(135deg, #e91e63, #c2185b); border-radius: var(--radius-sm); display: flex; align-items: center; justify-content: center;">
                        <i class="fas fa-music" style="color: #fff;"></i>
                    </div>
                    <div>
                        <div style="font-weight: 600; color: #fff;">${pl.name}</div>
                        <div style="font-size: 0.8rem; color: rgba(255,255,255,0.5);">${pl.tracks.length} tracks</div>
                    </div>
                </div>
            `).join('');
        }
        
        modal.style.display = 'flex';
    }
    
    function closePlaylistModal() {
        document.getElementById('addToPlaylistModal').style.display = 'none';
        pendingAddTrack = null;
    }
    
    function addTrackToPlaylist(playlistId) {
        if (!pendingAddTrack) return;
        
        const playlist = spotifyPlaylists.find(p => p.id === playlistId);
        if (!playlist) return;
        
        // Check if already in playlist
        const exists = playlist.tracks.some(t => t.title === pendingAddTrack.title && t.artist === pendingAddTrack.artist);
        if (exists) {
            showToast('Track already in playlist', 'warning');
            closePlaylistModal();
            return;
        }
        
        playlist.tracks.push(pendingAddTrack);
        saveSpotifyPlaylists();
        renderMyPlaylists();
        showToast(`Added to "${playlist.name}"`, 'success');
        closePlaylistModal();
    }
    
    function shuffleSpotifyQueue() {
        if (spotifyQueue.length <= 1) return;
        
        // Fisher-Yates shuffle
        for (let i = spotifyQueue.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [spotifyQueue[i], spotifyQueue[j]] = [spotifyQueue[j], spotifyQueue[i]];
        }
        
        spotifyCurrentIndex = 0;
        updateQueueUI();
        showToast('Queue shuffled', 'info');
    }
    
    function toggleRepeat() {
        // Simple implementation - replay current track when it ends
        showToast('Repeat mode toggled', 'info');
    }
    
    // Update queue count in header
    function updateQueueUI() {
        const queueDiv = document.getElementById('spotifyQueue');
        const countEl = document.getElementById('spotifyQueueCount');
        
        if (countEl) {
            countEl.textContent = spotifyQueue.length;
        }
        
        if (spotifyQueue.length === 0) {
            queueDiv.innerHTML = `
                <div style="text-align: center; padding: var(--space-6); color: rgba(255,255,255,0.3);">
                    <i class="fas fa-music" style="font-size: 1.5rem; margin-bottom: var(--space-2);"></i>
                    <p style="font-size: 0.85rem;">Queue is empty</p>
                </div>
            `;
            return;
        }
        
        queueDiv.innerHTML = spotifyQueue.map((track, i) => `
            <div style="display: flex; align-items: center; gap: var(--space-3); padding: var(--space-2); background: ${i === spotifyCurrentIndex ? 'rgba(30, 215, 96, 0.2)' : 'rgba(255,255,255,0.05)'}; border-radius: var(--radius-md); cursor: pointer; margin-bottom: var(--space-1);" onclick="playSpotifyTrack(${i})">
                <div style="width: 36px; height: 36px; background: var(--bg-tertiary); border-radius: var(--radius-sm); overflow: hidden; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                    ${track.thumbnail ? `<img src="${track.thumbnail}" style="width: 100%; height: 100%; object-fit: cover;">` : '<i class="fas fa-music" style="color: rgba(255,255,255,0.3);"></i>'}
                </div>
                <div style="flex: 1; overflow: hidden;">
                    <div style="font-size: 0.8rem; font-weight: 600; color: ${i === spotifyCurrentIndex ? '#1DB954' : '#fff'}; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${track.title}</div>
                    <div style="font-size: 0.7rem; color: rgba(255,255,255,0.4); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${track.artist}</div>
                </div>
                ${i === spotifyCurrentIndex ? '<i class="fas fa-volume-up" style="color: #1DB954; font-size: 0.8rem;"></i>' : ''}
            </div>
        `).join('');
    }
    
    // Update displaySpotifyResults with Play and Add to Playlist buttons
    // Also filter out songs shorter than 1 minute
    function displaySpotifyResults(tracks) {
        const resultsDiv = document.getElementById('spotifyResults');
        
        // Filter out songs shorter than 1 minute (60 seconds)
        const filteredTracks = tracks.filter(track => {
            if (!track.duration) return true; // Keep if no duration info
            const parts = track.duration.split(':');
            if (parts.length === 2) {
                const mins = parseInt(parts[0]) || 0;
                const secs = parseInt(parts[1]) || 0;
                return (mins * 60 + secs) >= 60;
            }
            return true;
        });
        
        if (filteredTracks.length === 0) {
            resultsDiv.innerHTML = `
                <div style="text-align: center; padding: var(--space-12); color: rgba(255,255,255,0.4);">
                    <i class="fas fa-search" style="font-size: 3rem; margin-bottom: var(--space-4); opacity: 0.3;"></i>
                    <p style="font-size: 1.1rem;">No results found (songs under 1 min filtered)</p>
                </div>
            `;
            return;
        }
        
        resultsDiv.innerHTML = filteredTracks.map(track => `
            <div style="display: flex; align-items: center; gap: var(--space-4); padding: var(--space-3); background: rgba(255,255,255,0.03); border-radius: var(--radius-lg); transition: all 0.2s; margin-bottom: var(--space-2);" onmouseover="this.style.background='rgba(30, 215, 96, 0.1)'" onmouseout="this.style.background='rgba(255,255,255,0.03)'">
                <div style="width: 56px; height: 56px; background: #282828; border-radius: var(--radius-md); overflow: hidden; flex-shrink: 0;">
                    ${track.thumbnail ? `<img src="${track.thumbnail}" style="width: 100%; height: 100%; object-fit: cover;">` : '<div style="width: 100%; height: 100%; display: flex; align-items: center; justify-content: center;"><i class="fas fa-music" style="color: #404040;"></i></div>'}
                </div>
                <div style="flex: 1; overflow: hidden;">
                    <div style="font-weight: 600; color: #fff; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">${track.title}</div>
                    <div style="font-size: 0.85rem; color: rgba(255,255,255,0.5);">${track.artist}</div>
                    ${track.duration ? `<div style="font-size: 0.75rem; color: rgba(255,255,255,0.3);">${track.duration}</div>` : ''}
                </div>
                <button style="background: transparent; border: 1px solid rgba(233, 30, 99, 0.4); color: #e91e63; padding: 10px 16px; border-radius: 20px; cursor: pointer; font-size: 0.85rem; font-weight: 600; transition: all 0.2s;" onclick='openAddToPlaylistModal(${JSON.stringify(track).replace(/'/g, "\\'")})' onmouseover="this.style.background='rgba(233, 30, 99, 0.15)'; this.style.borderColor='#e91e63'" onmouseout="this.style.background='transparent'; this.style.borderColor='rgba(233, 30, 99, 0.4)'" title="Add to Playlist">
                    <i class="fas fa-heart"></i> Save
                </button>
                <button style="background: #1DB954; border: none; color: #000; padding: 10px 20px; border-radius: 20px; cursor: pointer; font-weight: 700; font-size: 0.9rem; transition: all 0.2s; display: flex; align-items: center; gap: 6px;" onclick='playSingleTrack(${JSON.stringify(track).replace(/'/g, "\\'")})' onmouseover="this.style.transform='scale(1.05)'; this.style.boxShadow='0 4px 16px rgba(29, 185, 84, 0.4)'" onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='none'">
                    <i class="fas fa-play"></i> Play
                </button>
            </div>
        `).join('');
    }
    
    // Play a single track immediately (clears queue, plays just this song)
    async function playSingleTrack(track) {
        spotifyQueue = [track];
        spotifyCurrentIndex = 0;
        updateQueueUI();
        
        // Update Now Playing UI
        document.getElementById('spotifyNowPlayingTitle').textContent = track.title;
        document.getElementById('spotifyNowPlayingArtist').textContent = track.artist;
        
        if (track.thumbnail) {
            document.getElementById('spotifyNowPlayingArt').innerHTML = `<img src="${track.thumbnail}" style="width: 100%; height: 100%; object-fit: cover; border-radius: var(--radius-lg);">`;
        }
        
        showToast(`Playing: ${track.title}`, 'info');
        
        try {
            const response = await fetch('/api/spotify/stream', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ query: `${track.artist} ${track.title}` })
            });
            
            const data = await response.json();
            
            if (data.success && data.stream_url) {
                spotifyAudio.src = data.stream_url;
                spotifyAudio.play();
                spotifyIsPlaying = true;
                document.querySelector('#spotifyPlayBtn i').className = 'fas fa-pause';
                document.querySelector('#spotifyPlayBtn i').style.marginLeft = '0';
            } else {
                showToast(data.message || 'Failed to play track', 'error');
            }
        } catch (error) {
            console.error('Play error:', error);
            showToast('Error playing track', 'error');
        }
    }


    document.addEventListener('DOMContentLoaded', function() {
        // Load saved settings from cookie first
        const loaded = loadSettingsFromCookie();
        if (loaded) {
            // Apply loaded settings to the server
            setTimeout(() => {
                autoUpdate();
                showToast('Settings restored from previous session', 'info');
            }, 500);
        }
        
        updateStats();
        setInterval(updateStats, 1500);
        initCharts();
        initializeTabs();
        loadCrosshairs();
        
        // Initialize Spotify Player
        initSpotifyPlayer();
        loadSpotifyPlaylists();
        
        // Auto-load membership status on page load
        refreshMembershipStatus();
        
        // ================================================
        // License Expiry Check - Every 2 Hours
        // ================================================
        async function checkLicenseExpiry() {
            try {
                // Force fresh check from Supabase
                const response = await fetch('/api/membership/info?refresh=1');
                const data = await response.json();
                
                if (data.success && data.membership) {
                    const m = data.membership;
                    
                    // Check if expired
                    if (!m.is_active || m.days_remaining <= 0) {
                        if (!expiryWarningShown) {
                            showExpiryWarning();
                        }
                    }
                }
            } catch (error) {
                console.log('License check failed - will retry');
            }
        }
        
        // Check license every 2 hours (7200000 ms)
        setInterval(checkLicenseExpiry, 2 * 60 * 60 * 1000);
        // Also check 5 seconds after load (for testing/quick catch)
        setTimeout(checkLicenseExpiry, 5000);
        
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                switchTab(link.getAttribute('href').substring(1));
            });
        });
        
        document.querySelectorAll('#settingsForm input, #settingsForm select').forEach(elem => {
            if (elem.type === 'range') {
                const updateAndSend = () => {
                    updateAllSliderOutputs();
                    autoUpdate(elem);
                }
                elem.addEventListener('input', updateAllSliderOutputs);
                elem.addEventListener('change', updateAndSend);
            } else {
                elem.addEventListener('change', () => autoUpdate(elem));
            }
        });

        const rcsProfileSelect = document.getElementById('rcs_current_profile_name_select');
        if (rcsProfileSelect) {
            rcsProfileSelect.addEventListener('change', () => {
                onRcsProfileSelect();
                autoUpdate(); 
            });
        }
        
        document.querySelectorAll('input[name="aimbot_pixel_size"], input[name="triggerbot_pixel_size"]').forEach(slider => {
            slider.addEventListener('input', updateDetectionVisualizer);
            slider.addEventListener('change', updateDetectionVisualizer);
        });
        
        updateDetectionVisualizer();
        switchTab('system-content');
        
        document.getElementById('resetSettingsButton')?.addEventListener('click', () => sendCommand('reset_settings'));
        document.getElementById('closeAppButton')?.addEventListener('click', () => sendCommand('shutdown'));
        document.getElementById('refreshRecordingsBtn')?.addEventListener('click', loadRecordings);
        document.getElementById('refreshLogsBtn')?.addEventListener('click', loadRecentLogs);
        document.getElementById('saveProfileBtn')?.addEventListener('click', saveCurrentProfile);
        
        
        listProfiles();
        
        // Initialize Anti-Detection tab sliders
        initAntiDetectionSliders();
        
        // Load humanizer stats after delay (allows controller to init)
        loadHumanizerStatsOnInit();
        
        
        // Christmas Snow Effect (Enhanced)
        function createSnowflakes() {
            const container = document.createElement('div');
            container.className = 'snow-container';
            document.body.prepend(container);
    
            const snowflakeCount = 150; // Increased count
            for (let i = 0; i < snowflakeCount; i++) {
                const snowflake = document.createElement('div');
                snowflake.className = 'snowflake';
                snowflake.innerHTML = Math.random() > 0.5 ? '❄' : '❅'; // Varied shapes
                snowflake.style.left = Math.random() * 100 + 'vw';
                snowflake.style.top = Math.random() * -100 + 'vh'; // Random start height
                snowflake.style.animationDuration = Math.random() * 3 + 4 + 's';
                snowflake.style.opacity = Math.random() * 0.6 + 0.2;
                snowflake.style.fontSize = Math.random() * 20 + 10 + 'px'; // Varied sizes
                snowflake.style.animationDelay = Math.random() * 5 + 's';
                
                // Rotation
                const rotation = Math.random() * 360;
                snowflake.style.transform = `rotate(${rotation}deg)`;
                
                container.appendChild(snowflake);
            }
        }
        createSnowflakes();
    });
</script>

</head>

<body>
    <!-- Hanging Lights Decoration -->
    <ul class="light-rope">
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
        <li class="light-bulb"></li>
    </ul>

    <!-- Winter Footer Decoration -->
    <div class="winter-footer"></div>

    <div class="app-container">
        <!-- Sidebar -->
        <aside class="sidebar">
            <div class="sidebar-header">
                <div class="logo">
                    <div class="logo-icon" style="position: relative;">
                        <i class="fas fa-snowflake" style="color: var(--accent-secondary);"></i>
                        <!-- Santa Hat Overlay -->
                        <div style="position: absolute; top: -12px; left: -8px; font-size: 1.2rem; transform: rotate(-10deg);">🎅</div>
                    </div>
                    <div class="logo-text">
                        <div class="logo-title">{{ APP_NAME }}</div>
                        <div class="logo-version" style="color: var(--accent-primary);">Holiday Edition 🎄</div>
                    </div>
                </div>
            </div>

            <nav class="nav">
                <ul class="nav-list">
                    <li class="nav-item">
                        <a href="#system-content" class="nav-link">
                            <div class="nav-icon"><i class="fas fa-igloo"></i></div>
                            <span class="nav-text">North Pole System</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="#aimbot-content" class="nav-link">
                            <div class="nav-icon"><i class="fas fa-crosshairs"></i></div>
                            <span class="nav-text">Elf Aim Assist</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="#triggerbot-content" class="nav-link" data-requires="full_access">
                            <div class="nav-icon"><i class="fas fa-bolt" style="color: var(--accent-warning);"></i></div>
                            <span class="nav-text">Rudolph's Trigger</span>
                            <span class="nav-pro-badge" style="margin-left: auto; font-size: 0.65rem; background: linear-gradient(135deg, #fbbf24, #f59e0b); padding: 2px 6px; border-radius: 4px; color: #000; font-weight: 700;">PRO</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="#crosshair-content" class="nav-link" data-requires="full_access">
                            <div class="nav-icon"><i class="fas fa-star"></i></div>
                            <span class="nav-text">Star Sights</span>
                            <span class="nav-pro-badge" style="margin-left: auto; font-size: 0.65rem; background: linear-gradient(135deg, #fbbf24, #f59e0b); padding: 2px 6px; border-radius: 4px; color: #000; font-weight: 700;">PRO</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="#rcs-content" class="nav-link" data-requires="full_access">
                            <div class="nav-icon"><i class="fas fa-gift"></i></div>
                            <span class="nav-text">Recoil Gifts</span>
                            <span class="nav-pro-badge" style="margin-left: auto; font-size: 0.65rem; background: linear-gradient(135deg, #fbbf24, #f59e0b); padding: 2px 6px; border-radius: 4px; color: #000; font-weight: 700;">PRO</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="#sensitivity-content" class="nav-link">
                            <div class="nav-icon"><i class="fas fa-sliders"></i></div>
                            <span class="nav-text">Sensitivity</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="#keybinds-content" class="nav-link">
                            <div class="nav-icon"><i class="fas fa-keyboard"></i></div>
                            <span class="nav-text">Keybinds</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="#membership-content" class="nav-link" style="background: linear-gradient(135deg, rgba(251, 191, 36, 0.1) 0%, rgba(245, 158, 11, 0.1) 100%); border: 1px solid rgba(251, 191, 36, 0.3);">
                            <div class="nav-icon"><i class="fas fa-crown" style="color: #fbbf24;"></i></div>
                            <span class="nav-text" style="color: #fbbf24;">Membership</span>
                            <span style="margin-left: auto; font-size: 0.7rem; background: linear-gradient(135deg, #fbbf24, #f59e0b); padding: 2px 6px; border-radius: 4px; color: #000; font-weight: 700;">PRO</span>
                        </a>
                    </li>
                    <li class="nav-item">
                        <a href="#spotify-content" class="nav-link" style="background: linear-gradient(135deg, rgba(30, 215, 96, 0.1) 0%, rgba(25, 185, 84, 0.1) 100%); border: 1px solid rgba(30, 215, 96, 0.3);" data-requires="full_access">
                            <div class="nav-icon"><i class="fab fa-spotify" style="color: #1DB954;"></i></div>
                            <span class="nav-text" style="color: #1DB954;">Spotify</span>
                            <span class="nav-pro-badge" style="margin-left: auto; font-size: 0.65rem; background: linear-gradient(135deg, #1DB954, #1aa34a); padding: 2px 6px; border-radius: 4px; color: #000; font-weight: 700;">PRO</span>
                        </a>
                    </li>
                    <li class="nav-item nav-item-danger">
                        <a href="#antidetect-content" class="nav-link nav-link-danger" data-requires="full_access">
                            <div class="nav-icon"><i class="fas fa-shield-virus"></i></div>
                            <span class="nav-text">Anti-Detection</span>
                            <span class="nav-pro-badge" style="margin-left: auto; font-size: 0.65rem; background: linear-gradient(135deg, #fbbf24, #f59e0b); padding: 2px 6px; border-radius: 4px; color: #000; font-weight: 700;">PRO</span>
                        </a>
                    </li>
                </ul>
            </nav>

            <div class="sidebar-footer">
                <div class="status-card">
                    <div class="status-info">
                        <span>FPS: <span id="sidebarFpsValue">N/A</span> ❄️</span>
                    </div>
                    <div class="status-dot {% if aimbot_thread_running %}active{% endif %}" id="sidebarScanStatusDot"></div>
                </div>
            </div>
        </aside>

        <!-- Main Content -->
        <div class="main-content">
            <!-- Header -->
            <header class="header">
                <div class="stats-grid">
                    <div class="stat-item">
                        <div class="stat-icon"><i class="fas fa-tachometer-alt"></i></div>
                        <div class="stat-content">
                            <div class="stat-label">FPS</div>
                            <div class="stat-value">
                                <span id="headerFpsValue">N/A</span>
                                <div class="performance-indicator">
                                    <div class="performance-dot" id="fpsIndicator"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-icon"><i class="fas fa-camera"></i></div>
                        <div class="stat-content">
                            <div class="stat-label">Capture</div>
                            <div class="stat-value">
                                <span id="captureTimeValue">N/A</span>ms
                                <div class="performance-indicator">
                                    <div class="performance-dot" id="captureIndicator"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-icon"><i class="fas fa-cog"></i></div>
                        <div class="stat-content">
                            <div class="stat-label">Process</div>
                            <div class="stat-value">
                                <span id="processingTimeValue">N/A</span>ms
                                <div class="performance-indicator">
                                    <div class="performance-dot" id="processingIndicator"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-icon"><i class="fas fa-power-off"></i></div>
                        <div class="stat-content">
                            <div class="stat-label">Status</div>
                            <div class="stat-value">
                                <span id="headerScanStatus">{% if aimbot_thread_running %}Running 🎅{% else %}Sleeping 💤{% endif %}</span>
                                <div class="performance-indicator">
                                    <div class="status-dot {% if aimbot_thread_running %}active{% endif %}" id="headerScanStatusDot"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </header>

            <!-- Content Area -->
            <div class="content-area">
                <form id="settingsForm" onsubmit="return false;">
                    
                    <!-- System Content -->
                    <section id="system-content" class="content-section">
                        <div class="card">
                            <div class="card-header">
                                <div class="card-icon"><i class="fas fa-monitor-waveform"></i></div>
                                <h2 class="card-title">System Monitoring</h2>
                            </div>
                            <div class="card-content">
                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-desktop"></i>
                                        Screen Capture Monitor
                                    </div>
                                    <div class="form-controls">
                                        <div class="select">
                                            <select name="selected_monitor">
                                                {% if not monitors %}
                                                <option>No monitors found</option>
                                                {% else %}
                                                {% for monitor in monitors %}
                                                <option value="{{ loop.index0 }}" {% if selected_monitor == loop.index0 %}selected{% endif %}>
                                                    Monitor {{ loop.index0 }}: {{ monitor.width }}x{{ monitor.height }} @ ({{ monitor.left }}, {{ monitor.top }})
                                                </option>
                                                {% endfor %}
                                                {% endif %}
                                            </select>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="card">
                            <div class="card-header">
                                <div class="card-icon"><i class="fas fa-chart-line"></i></div>
                                <h2 class="card-title">Real-Time Performance Analytics</h2>
                            </div>
                            <div class="card-content">
                                <div class="chart-container">
                                    <canvas id="fpsChart"></canvas>
                                </div>
                                <div class="chart-container">
                                    <canvas id="timingChart"></canvas>
                                </div>
                            </div>
                        </div>
                        
                        <div class="card">
                            <div class="card-header">
                                <div class="card-icon"><i class="fas fa-power-off"></i></div>
                                <h2 class="card-title">Application Control</h2>
                            </div>
                            <div class="card-content">
                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-undo"></i>
                                        Reset all settings to their default values
                                    </div>
                                    <div class="form-controls">
                                        <button type="button" id="resetSettingsButton" class="btn warning">
                                            <i class="fas fa-undo"></i> Reset to Nice List 📜
                                        </button>
                                    </div>
                                </div>
                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-times-circle"></i>
                                        Stop processes and close the application
                                    </div>
                                    <div class="form-controls">
                                        <button type="button" id="closeAppButton" class="btn danger">
                                            <i class="fas fa-times-circle"></i> Hibernate to North Pole ❄️
                                        </button>
                                    </div>
                                </div>
                                <div class="info-box info">
                                    <i class="fas fa-info-circle"></i>
                                    <strong>Quick Exit:</strong> Press <kbd style="background: var(--bg-quaternary); padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.2); font-family: var(--font-mono);">F10</kbd> to force-close the application at any time.
                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- Continue with rest of HTML content... -->
                    
                    <!-- Aimbot Content -->
                    <section id="aimbot-content" class="content-section">
                        <div class="card">
                            <div class="card-header">
                                <div class="card-icon"><i class="fas fa-crosshairs"></i></div>
                                <h2 class="card-title">Professional Aimbot Configuration</h2>
                            </div>
                            <div class="card-content">
                                <div class="tabs">
                                    <button type="button" class="tab-button active" data-tab-target="aimbot-basic-tab">
                                        <i class="fas fa-sliders"></i> Basic Settings
                                    </button>
                                    <button type="button" class="tab-button" data-tab-target="aimbot-movement-tab">
                                        <i class="fas fa-arrows-alt"></i> Movement
                                    </button>
                                    <button type="button" class="tab-button" data-tab-target="aimbot-visualizer-tab">
                                        <i class="fas fa-eye"></i> Visualizer
                                    </button>
                                </div>
                                
                                <div id="aimbot-basic-tab" class="tab-content active">
                                    <div class="form-row">
                                        <div class="form-label premium">
                                            <i class="fas fa-toggle-on"></i>
                                            Enable Professional Aimbot
                                        </div>
                                        <div class="form-controls">
                                            <label class="toggle">
                                                <input type="checkbox" name="aimbot_enabled" value="1" {% if aimbot_enabled %}checked{% endif %}>
                                                <span class="toggle-slider"></span>
                                            </label>
                                        </div>
                                    </div>
                                    
                                    <div class="form-row">
                                        <div class="form-label tooltip">
                                            <i class="fas fa-expand"></i>
                                            Detection Field of View
                                            <i class="fas fa-circle-info"></i>
                                            <span class="tooltip-content">Size of the square detection area (pixels) around the crosshair for enemy detection. Larger values detect enemies from further away.</span>
                                        </div>
                                        <div class="form-controls">
                                            <div class="range-control">
                                                <input type="range" name="aimbot_pixel_size" min="10" max="400" step="5" value="{{ aimbot_pixel_size }}" class="range-input">
                                                <span class="range-output" id="aimbot_pixel_size_output">{{ aimbot_pixel_size }}</span>
                                            </div>
                                        </div>
                                    </div>
                                    
                                    <div class="form-row">
                                        <div class="form-label tooltip">
                                            <i class="fas fa-arrows-left-right"></i>
                                            Horizontal Aim Offset
                                            <i class="fas fa-circle-info"></i>
                                            <span class="tooltip-content">Fine-tune horizontal aiming. Positive values aim right, negative values aim left. Adjust based on your weapon and playstyle.</span>
                                        </div>
                                        <div class="form-controls">
                                            <div class="range-control">
                                                <input type="range" name="aim_offset_x" min="-100" max="100" step="1" value="{{ aim_offset_x }}" class="range-input">
                                                <span class="range-output" id="aim_offset_x_output">{{ aim_offset_x }}</span>
                                            </div>
                                        </div>
                                    </div>
                                    
                                    <div class="form-row">
                                        <div class="form-label tooltip">
                                            <i class="fas fa-arrows-up-down"></i>
                                            Vertical Aim Offset
                                            <i class="fas fa-circle-info"></i>
                                            <span class="tooltip-content">Fine-tune vertical aiming. Positive values aim down, negative values aim up. Perfect for headshot adjustments.</span>
                                        </div>
                                        <div class="form-controls">
                                            <div class="range-control">
                                                <input type="range" name="aim_offset_y" min="-100" max="100" step="1" value="{{ aim_offset_y }}" class="range-input">
                                                <span class="range-output" id="aim_offset_y_output">{{ aim_offset_y }}</span>
                                            </div>
                                        </div>
                                    </div>
                                    
                                    <div class="form-row">
                                        <div class="form-label">
                                            <i class="fas fa-palette"></i>
                                            Enemy Outline Color Detection
                                        </div>
                                        <div class="form-controls">
                                            <div class="select">
                                                <select name="enemy_color">
                                                    {% for color, data in enemy_hsv_thresholds.items() %}
                                                    <option value="{{ color }}" {% if enemy_color == color %}selected{% endif %}>
                                                        {{ color|capitalize }}
                                                    </option>
                                                    {% endfor %}
                                                </select>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                
                                <div id="aimbot-movement-tab" class="tab-content">
                                    <div class="form-row premium-feature">
                                        <div class="form-label tooltip">
                                            <i class="fas fa-bolt"></i>
                                            Enable Flick Shot Technology
                                            <i class="fas fa-circle-info"></i>
                                            <span class="tooltip-content">Advanced flick shooting mechanism for quick target acquisition. Performs initial overshoot followed by precise correction.</span>
                                        </div>
                                        <div class="form-controls">
                                            <label class="toggle">
                                                <input type="checkbox" name="flick_shot_enabled" value="1" {% if flick_shot_enabled %}checked{% endif %}>
                                                <span class="toggle-slider"></span>
                                            </label>
                                        </div>
                                    </div>
                                    
                                    <div class="form-row">
                                        <div class="form-label tooltip">
                                            <i class="fas fa-chart-line"></i>
                                            Flick Overshoot Intensity
                                            <i class="fas fa-circle-info"></i>
                                            <span class="tooltip-content">Controls how much the initial flick overshoots the target. Higher values = more aggressive flicks. Recommended: 0.2-0.4</span>
                                        </div>
                                        <div class="form-controls">
                                            <div class="range-control">
                                                <input type="range" name="flick_overshoot_factor_slider" min="0" max="200" step="5" value="{{ (flick_overshoot_factor * 100)|int }}" data-scale-factor="100" data-decimals="2" class="range-input">
                                                <span class="range-output" id="flick_overshoot_factor_output">{{ "%.2f"|format(flick_overshoot_factor) }}</span>
                                                <input type="hidden" name="flick_overshoot_factor" value="{{ flick_overshoot_factor }}">
                                            </div>
                                        </div>
                                    </div>
                                    
                                    <div class="form-row premium-feature">
                                        <div class="form-label tooltip">
                                            <i class="fas fa-water"></i>
                                            Enable Movement Smoothing
                                            <i class="fas fa-circle-info"></i>
                                            <span class="tooltip-content">Smooths out mouse movements to appear more natural and reduce detection by anti-cheat systems.</span>
                                        </div>
                                        <div class="form-controls">
                                            <label class="toggle">
                                                <input type="checkbox" name="smoothing_enabled" value="1" {% if smoothing_enabled %}checked{% endif %}>
                                                <span class="toggle-slider"></span>
                                            </label>
                                        </div>
                                    </div>
                                    
                                    <div class="form-row">
                                        <div class="form-label tooltip">
                                            <i class="fas fa-wave-square"></i>
                                            Smoothing Intensity
                                            <i class="fas fa-circle-info"></i>
                                            <span class="tooltip-content">Higher values = smoother movement but slower response. Lower values = faster but more robotic. Recommended: 0.3-0.7</span>
                                        </div>
                                        <div class="form-controls">
                                            <div class="range-control">
                                                <input type="range" name="smoothing_factor_slider" min="1" max="99" step="1" value="{{ (smoothing_factor * 100)|int }}" data-scale-factor="100" data-decimals="2" class="range-input">
                                                <span class="range-output" id="smoothing_factor_output">{{ "%.2f"|format(smoothing_factor) }}</span>
                                                <input type="hidden" name="smoothing_factor" value="{{ smoothing_factor }}">
                                            </div>
                                        </div>
                                    </div>
                                    
                                    <div class="info-box premium">
                                        <i class="fas fa-crown"></i>
                                        <strong>Pro Tip:</strong> Combine flick shots with smoothing for the most natural-looking aim assistance. Start with conservative settings and adjust based on your gameplay style.
                                    </div>
                                </div>
                                
                                <div id="aimbot-visualizer-tab" class="tab-content">
                                    <p class="text-center text-secondary mb-6">
                                        <i class="fas fa-eye"></i>
                                        Live preview of detection zones: <span style="color: var(--accent-primary);">■ Aimbot FOV</span> and <span style="color: var(--accent-danger);">■ Trigger Zone</span>
                                    </p>
                                    <div class="visualizer-container">
                                        <canvas id="detectionVisualizer"></canvas>
                                    </div>
                                    <div class="info-box info">
                                        <i class="fas fa-lightbulb"></i>
                                        The blue area shows where enemies will be automatically targeted, while the red area shows where the triggerbot will fire. Adjust the sizes based on your preferred engagement range.
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- Triggerbot Content -->
                    <section id="triggerbot-content" class="content-section">
                        <div class="card">
                            <div class="card-header">
                                <div class="card-icon"><i class="fas fa-bolt"></i></div>
                                <h2 class="card-title">Professional Triggerbot Configuration</h2>
                            </div>
                            <div class="card-content">
                                <div class="form-row">
                                    <div class="form-label premium">
                                        <i class="fas fa-toggle-on"></i>
                                        Enable Professional Triggerbot
                                    </div>
                                    <div class="form-controls">
                                        <label class="toggle">
                                            <input type="checkbox" name="triggerbot_enabled" value="1" {% if triggerbot_enabled %}checked{% endif %}>
                                            <span class="toggle-slider"></span>
                                        </label>
                                    </div>
                                </div>
                                
                                <div class="form-row">
                                    <div class="form-label tooltip">
                                        <i class="fas fa-crosshairs"></i>
                                        Trigger Zone Size
                                        <i class="fas fa-circle-info"></i>
                                        <span class="tooltip-content">Size of the trigger zone at screen center. Smaller = more precise but requires better aim, Larger = more forgiving but may trigger on unintended targets.</span>
                                    </div>
                                    <div class="form-controls">
                                        <div class="range-control">
                                            <input type="range" name="triggerbot_pixel_size" min="1" max="50" step="1" value="{{ triggerbot_pixel_size }}" class="range-input">
                                            <span class="range-output" id="triggerbot_pixel_size_output">{{ triggerbot_pixel_size }}</span>
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="form-row">
                                    <div class="form-label tooltip">
                                        <i class="fas fa-running"></i>
                                        Shoot While Moving
                                        <i class="fas fa-circle-info"></i>
                                        <span class="tooltip-content">Allow triggerbot to fire even when movement keys are pressed. Disable for more tactical gameplay.</span>
                                    </div>
                                    <div class="form-controls">
                                        <label class="toggle">
                                            <input type="checkbox" name="shoot_while_moving" value="1" {% if shoot_while_moving %}checked{% endif %}>
                                            <span class="toggle-slider"></span>
                                        </label>
                                    </div>
                                </div>
                                
                                <div class="form-row">
                                    <div class="form-label tooltip">
                                        <i class="fas fa-triangle-exclamation" style="color: var(--accent-warning);"></i>
                                        Blatant Mode
                                        <i class="fas fa-circle-info"></i>
                                        <span class="tooltip-content">WARNING: Hold fire button continuously when target is in zone. More detectable but faster response.</span>
                                    </div>
                                    <div class="form-controls">
                                        <label class="toggle">
                                            <input type="checkbox" name="blatent_wyen" value="1" {% if blatent_wyen %}checked{% endif %}>
                                            <span class="toggle-slider"></span>
                                        </label>
                                    </div>
                                </div>
                                
                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-list"></i>
                                        Selected Weapon Profile
                                    </div>
                                    <div class="form-controls">
                                        <div class="select">
                                            <select name="selected_valorant_gun">
                                                {% for gun_name, profile in valorant_gun_profiles_dict.items() %}
                                                <option value="{{ gun_name }}" {% if selected_valorant_gun == gun_name %}selected{% endif %}>
                                                    {{ gun_name }}
                                                </option>
                                                {% endfor %}
                                            </select>
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="form-row">
                                    <div class="form-label tooltip">
                                        <i class="fas fa-cog"></i>
                                        Use Profile Fire Rate
                                        <i class="fas fa-circle-info"></i>
                                        <span class="tooltip-content">Use the selected weapon's authentic fire rate. Disable to use custom cooldown below.</span>
                                    </div>
                                    <div class="form-controls">
                                        <label class="toggle">
                                            <input type="checkbox" name="triggerbot_use_profile_cooldown" value="1" {% if triggerbot_use_profile_cooldown %}checked{% endif %}>
                                            <span class="toggle-slider"></span>
                                        </label>
                                    </div>
                                </div>
                                
                                <div class="form-row">
                                    <div class="form-label tooltip">
                                        <i class="fas fa-clock"></i>
                                        Custom Fire Rate Cooldown
                                        <i class="fas fa-circle-info"></i>
                                        <span class="tooltip-content">Manual fire rate override when "Use Profile Fire Rate" is disabled. Lower = faster firing.</span>
                                    </div>
                                    <div class="form-controls">
                                        <input type="number" name="triggerbot_custom_cooldown" min="0.01" max="5" step="0.01" value="{{ triggerbot_custom_cooldown }}" class="input"> s
                                    </div>
                                </div>
                                
                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-palette"></i>
                                        Enemy Outline Color Detection
                                    </div>
                                    <div class="form-controls">
                                        <div class="select">
                                            <select name="enemy_color">
                                                {% for color, data in enemy_hsv_thresholds.items() %}
                                                <option value="{{ color }}" {% if enemy_color == color %}selected{% endif %}>
                                                    {{ color|capitalize }}
                                                </option>
                                                {% endfor %}
                                            </select>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- Crosshair Content -->
                    <section id="crosshair-content" class="content-section">
                        <div class="card">
                            <div class="card-header">
                                <div class="card-icon"><i class="fas fa-crosshairs"></i></div>
                                <h2 class="card-title">Crosshair Database</h2>
                            </div>
                            <div class="card-content">
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
                                    <p style="color: var(--text-secondary);">Browse top 50 professional crosshairs. Click to copy code.</p>
                                    <button class="btn primary" onclick="loadCrosshairs()">
                                        <i class="fas fa-sync"></i> Refresh
                                    </button>
                                </div>
                                <div id="crosshairGrid" class="crosshair-grid">
                                    <div style="grid-column: 1/-1; text-align: center; padding: 2rem;">
                                        Loading crosshairs...
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Crosshair Modal -->
                        <div id="crosshairModal" class="modal-overlay">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h3 class="modal-title" id="modalTitle">Crosshair Preview</h3>
                                    <button class="modal-close" onclick="closeCrosshairModal()">
                                        <i class="fas fa-times"></i>
                                    </button>
                                </div>
                                <div class="preview-large">
                                    <div style="position: absolute; color: white; display: flex; flex-direction: column; align-items: center; justify-content: center; width: 100%; height: 100%; text-shadow: 0 2px 4px rgba(0,0,0,0.8);">
                                        <i class="fas fa-crosshairs" style="font-size: 3rem; margin-bottom: 1rem;"></i>
                                        <span style="font-size: 0.9rem; opacity: 0.8;">Preview not available<br>(requires in-game rendering)</span>
                                    </div>
                                </div>
                                <div class="code-box">
                                    <span id="crosshairCode" style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;"></span>
                                    <button class="btn secondary small" onclick="copyCrosshairCode()">
                                        <i class="fas fa-copy"></i>
                                    </button>
                                </div>
                                <div class="form-row">
                                    <button class="btn primary full-width" onclick="copyCrosshairCode()">
                                        <i class="fas fa-copy"></i> Copy Code to Clipboard
                                    </button>
                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- RCS Content - Coming Soon -->
                    <section id="rcs-content" class="content-section">
                        <div class="card">
                            <div class="card-header">
                                <div class="card-icon"><i class="fas fa-arrows-down-to-line"></i></div>
                                <h2 class="card-title">Recoil Control System (RCS)</h2>
                            </div>
                            <div class="card-content" style="text-align: center; padding: 80px 40px;">
                                <div style="font-size: 4rem; margin-bottom: 24px; opacity: 0.3;">
                                    <i class="fas fa-clock"></i>
                                </div>
                                <h3 style="font-size: 2rem; font-weight: 700; background: var(--gradient-primary); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 16px;">
                                    Coming Soon
                                </h3>
                                <p style="color: var(--text-secondary); max-width: 400px; margin: 0 auto; line-height: 1.6;">
                                    Advanced Recoil Control System with weapon-specific patterns and real-time compensation is currently in development. Stay tuned for updates!
                                </p>
                            </div>
                        </div>
                    </section>

                    <!-- Sensitivity Content -->
                    <section id="sensitivity-content" class="content-section">
                        <div class="card">
                            <div class="card-header">
                                <div class="card-icon"><i class="fas fa-sliders"></i></div>
                                <h2 class="card-title">Advanced Sensitivity Configuration</h2>
                            </div>
                            <div class="card-content">
                                <div class="form-row">
                                    <div class="form-label tooltip">
                                        <i class="fas fa-hand-point-up"></i>
                                        Hipfire Sensitivity
                                        <i class="fas fa-circle-info"></i>
                                        <span class="tooltip-content">Aimbot strength when NOT aiming down sights. Lower = more precise, Higher = more responsive.</span>
                                    </div>
                                    <div class="form-controls">
                                        <div class="range-control">
                                            <input type="range" name="left_sensitivity_slider" min="1" max="100" step="1" value="{{ (left_sensitivity * 100)|int }}" data-scale-factor="100" data-decimals="2" class="range-input">
                                            <span class="range-output" id="left_sensitivity_output">{{ "%.2f"|format(left_sensitivity) }}</span>
                                            <input type="hidden" name="left_sensitivity" value="{{ left_sensitivity }}">
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="form-row">
                                    <div class="form-label tooltip">
                                        <i class="fas fa-crosshairs"></i>
                                        ADS Sensitivity
                                        <i class="fas fa-circle-info"></i>
                                        <span class="tooltip-content">Aimbot strength when aiming down sights. Usually lower than hipfire for precision.</span>
                                    </div>
                                    <div class="form-controls">
                                        <div class="range-control">
                                            <input type="range" name="right_sensitivity_slider" min="1" max="100" step="1" value="{{ (right_sensitivity * 100)|int }}" data-scale-factor="100" data-decimals="2" class="range-input">
                                            <span class="range-output" id="right_sensitivity_output">{{ "%.2f"|format(right_sensitivity) }}</span>
                                            <input type="hidden" name="right_sensitivity" value="{{ right_sensitivity }}">
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="form-row">
                                    <div class="form-label tooltip">
                                        <i class="fas fa-gauge-high"></i>
                                        Sensitivity Multiplier
                                        <i class="fas fa-circle-info"></i>
                                        <span class="tooltip-content">Global sensitivity multiplier. Affects overall aimbot strength. Recommended: 2.0-6.0</span>
                                    </div>
                                    <div class="form-controls">
                                        <div class="range-control">
                                            <input type="range" name="sensitivity_multiplier_slider" min="10" max="2000" step="10" value="{{ (sensitivity_multiplier * 100)|int }}" data-scale-factor="100" data-decimals="2" class="range-input">
                                            <span class="range-output" id="sensitivity_multiplier_output">{{ "%.2f"|format(sensitivity_multiplier) }}</span>
                                            <input type="hidden" name="sensitivity_multiplier" value="{{ sensitivity_multiplier }}">
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="form-row">
                                    <div class="form-label tooltip">
                                        <i class="fas fa-chart-line"></i>
                                        Movement Scale
                                        <i class="fas fa-circle-info"></i>
                                        <span class="tooltip-content">Fine-tune movement responsiveness. Lower = smoother but slower, Higher = faster but more aggressive.</span>
                                    </div>
                                    <div class="form-controls">
                                        <div class="range-control">
                                            <input type="range" name="move_scale_slider" min="10" max="200" step="2" value="{{ (move_scale * 100)|int }}" data-scale-factor="100" data-decimals="2" class="range-input">
                                            <span class="range-output" id="move_scale_output">{{ "%.2f"|format(move_scale) }}</span>
                                            <input type="hidden" name="move_scale" value="{{ move_scale }}">
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- Keybinds Content -->
                    <section id="keybinds-content" class="content-section">
                        <div class="card">
                            <div class="card-header">
                                <div class="card-icon"><i class="fas fa-keyboard"></i></div>
                                <h2 class="card-title">Enhanced Custom Keybinds</h2>
                            </div>
                            <div class="card-content">
                                <h3 style="margin-bottom: var(--space-6); color: var(--text-secondary); font-weight: 600; font-size: 1.125rem; display: flex; align-items: center; gap: var(--space-3);">
                                    <i class="fas fa-crosshairs" style="color: var(--accent-primary);"></i>
                                    Aimbot Activation Settings
                                </h3>
                                
                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-cog"></i>
                                        Activation Mode
                                    </div>
                                    <div class="form-controls">
                                        <div class="select">
                                            <select name="aimbot_activation_mode">
                                                <option value="always_on" {% if aimbot_activation_mode == "always_on" %}selected{% endif %}>Always Active</option>
                                                <option value="mouse_hold" {% if aimbot_activation_mode == "mouse_hold" %}selected{% endif %}>Mouse Buttons</option>
                                                <option value="custom_bind" {% if aimbot_activation_mode == "custom_bind" %}selected{% endif %}>Custom Keybind</option>
                                            </select>
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-keyboard"></i> Custom Aimbot Keybind
                                    </div>
                                    <div class="form-controls">
                                        <span id="aimbot_custom_bind_key_display" class="keybind-display" onclick="startKeybindListen('aimbot_custom_bind_key')">{{ aimbot_custom_bind_key if aimbot_custom_bind_key else 'Not Set' }}</span>
                                        <button type="button" class="btn secondary small" onclick="startKeybindListen('aimbot_custom_bind_key')">
                                            <i class="fas fa-edit"></i> Set Key
                                        </button>
                                        <input type="hidden" name="aimbot_custom_bind_key" id="aimbot_custom_bind_key_input" value="{{ aimbot_custom_bind_key }}">
                                    </div>
                                </div>
                                
                                <h3 style="margin: var(--space-12) 0 var(--space-6) 0; color: var(--text-secondary); font-weight: 600; font-size: 1.125rem; display: flex; align-items: center; gap: var(--space-3);">
                                    <i class="fas fa-bolt" style="color: var(--accent-warning);"></i>
                                    Triggerbot Activation Settings
                                </h3>
                                
                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-cog"></i>
                                        Activation Mode
                                    </div>
                                    <div class="form-controls">
                                        <div class="select">
                                            <select name="triggerbot_activation_mode">
                                                <option value="always_on" {% if triggerbot_activation_mode == "always_on" %}selected{% endif %}>Always Active</option>
                                                <option value="custom_bind" {% if triggerbot_activation_mode == "custom_bind" %}selected{% endif %}>Hold to Activate</option>
                                            </select>
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-keyboard"></i> Custom Triggerbot Keybind
                                    </div>
                                    <div class="form-controls">
                                        <span id="triggerbot_custom_bind_key_display" class="keybind-display" onclick="startKeybindListen('triggerbot_custom_bind_key')">{{ triggerbot_custom_bind_key if triggerbot_custom_bind_key else 'Not Set' }}</span>
                                        <button type="button" class="btn secondary small" onclick="startKeybindListen('triggerbot_custom_bind_key')">
                                            <i class="fas fa-edit"></i> Set Key
                                        </button>
                                        <input type="hidden" name="triggerbot_custom_bind_key" id="triggerbot_custom_bind_key_input" value="{{ triggerbot_custom_bind_key }}">
                                    </div>
                                </div>
                                
                                <div class="info-box info">
                                    <i class="fas fa-rocket"></i>
                                    <strong>Enhanced Keybind System:</strong> This improved system supports all keyboard keys and mouse buttons with better detection and responsiveness. Click "Set Key" and press any key or mouse button to assign it.
                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- Anti-Detection Content -->
                    <section id="antidetect-content" class="content-section">
                        <!-- Warning Banner -->
                        <div class="antidetect-warning">
                            <div class="antidetect-warning-icon">
                                <i class="fas fa-exclamation-triangle"></i>
                            </div>
                            <div class="antidetect-warning-content">
                                <h3><i class="fas fa-shield-virus"></i> Anti-Detection Settings</h3>
                                <p>
                                    <strong>⚠️ ADVANCED USERS ONLY</strong><br>
                                    These settings control how your mouse movements are humanized to avoid detection by behavioral analysis anti-cheat systems. 
                                    Incorrect settings may either reduce effectiveness or make your inputs look suspicious.
                                    <br><br>
                                    <strong>How it works:</strong> Modern anti-cheat records your mouse inputs and analyzes patterns like polling rate consistency, 
                                    path linearity, velocity curves, and reaction times. Our system makes your inputs statistically indistinguishable from natural human movement.
                                </p>
                            </div>
                        </div>

                        <!-- Session Fingerprint Card -->
                        <div class="card antidetect-card">
                            <div class="card-header">
                                <div class="card-icon"><i class="fas fa-fingerprint"></i></div>
                                <h2 class="card-title">Session Behavioral Fingerprint</h2>
                            </div>
                            <div class="card-content">
                                <div class="info-box warning">
                                    <i class="fas fa-sync-alt"></i>
                                    <strong>Regenerate Between Matches:</strong> Click the button below after each match to change your behavioral fingerprint, preventing the anti-cheat from building a profile on you.
                                </div>
                                
                                <div class="fingerprint-display" id="fingerprintDisplay">
                                    <div class="fingerprint-stat">
                                        <div class="fingerprint-stat-value" id="fp-speed">--</div>
                                        <div class="fingerprint-stat-label">Speed Tendency</div>
                                    </div>
                                    <div class="fingerprint-stat">
                                        <div class="fingerprint-stat-value" id="fp-tremor">--</div>
                                        <div class="fingerprint-stat-label">Tremor Intensity</div>
                                    </div>
                                    <div class="fingerprint-stat">
                                        <div class="fingerprint-stat-value" id="fp-overshoot">--</div>
                                        <div class="fingerprint-stat-label">Overshoot Tendency</div>
                                    </div>
                                    <div class="fingerprint-stat">
                                        <div class="fingerprint-stat-value" id="fp-reaction">--</div>
                                        <div class="fingerprint-stat-label">Reaction Offset (ms)</div>
                                    </div>
                                </div>

                                <div class="form-row" style="margin-top: var(--space-6);">
                                    <div class="form-label">
                                        <i class="fas fa-dice"></i>
                                        Generate New Fingerprint
                                        <span class="help-tooltip">
                                            <i class="fas fa-question"></i>
                                            <span class="tooltip-content">
                                                Creates a new random behavioral profile. Your mouse movements will have slightly different characteristics (speed, tremor, etc.) making it harder to track you across multiple matches.
                                            </span>
                                        </span>
                                    </div>
                                    <div class="form-controls">
                                        <button type="button" id="regenerateFingerprintBtn" class="btn btn-regenerate" onclick="regenerateFingerprint()">
                                            <i class="fas fa-sync-alt"></i> Regenerate Fingerprint
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Polling Rate Settings -->
                        <div class="card antidetect-card">
                            <div class="card-header">
                                <div class="card-icon"><i class="fas fa-clock"></i></div>
                                <h2 class="card-title">Polling Rate Emulation</h2>
                            </div>
                            <div class="card-content">
                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-tachometer-alt"></i>
                                        Base Polling Rate (Hz)
                                        <span class="help-tooltip">
                                            <i class="fas fa-question"></i>
                                            <span class="tooltip-content">
                                                Your mouse's polling rate. Most gaming mice are 1000Hz. We add natural jitter to this to simulate real USB timing variance. Set this to match your actual mouse.
                                            </span>
                                        </span>
                                    </div>
                                    <div class="form-controls">
                                        <div class="select">
                                            <select name="humanizer_polling_rate" id="humanizer_polling_rate">
                                                <option value="500">500 Hz</option>
                                                <option value="1000" selected>1000 Hz</option>
                                                <option value="2000">2000 Hz</option>
                                                <option value="4000">4000 Hz</option>
                                                <option value="8000">8000 Hz</option>
                                            </select>
                                        </div>
                                    </div>
                                </div>

                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-random"></i>
                                        Polling Jitter (%)
                                        <span class="help-tooltip">
                                            <i class="fas fa-question"></i>
                                            <span class="tooltip-content">
                                                How much the polling interval varies. Real USB has natural timing variance. 12% is realistic for most setups. Too low = robotic, too high = may cause stuttering.
                                            </span>
                                        </span>
                                    </div>
                                    <div class="form-controls">
                                        <input type="range" name="humanizer_polling_jitter" id="humanizer_polling_jitter" min="5" max="25" value="12" step="1">
                                        <span class="slider-value" id="humanizer_polling_jitter_value">12%</span>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Path Generation Settings -->
                        <div class="card antidetect-card">
                            <div class="card-header">
                                <div class="card-icon"><i class="fas fa-route"></i></div>
                                <h2 class="card-title">Path Generation (Bézier Curves)</h2>
                            </div>
                            <div class="card-content">
                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-bezier-curve"></i>
                                        Path Curvature
                                        <span class="help-tooltip">
                                            <i class="fas fa-question"></i>
                                            <span class="tooltip-content">
                                                How curved your mouse paths are. Higher = more curved (natural but slower), Lower = straighter (faster but more detectable). 0.35 is a good balance.
                                            </span>
                                        </span>
                                    </div>
                                    <div class="form-controls">
                                        <input type="range" name="humanizer_bezier_deviation" id="humanizer_bezier_deviation" min="0.1" max="0.6" value="0.35" step="0.05">
                                        <span class="slider-value" id="humanizer_bezier_deviation_value">0.35</span>
                                    </div>
                                </div>

                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-ellipsis-h"></i>
                                        Min Path Points
                                        <span class="help-tooltip">
                                            <i class="fas fa-question"></i>
                                            <span class="tooltip-content">
                                                Minimum number of points in a curved path. More points = smoother curve but slightly slower. 4 is good for short movements.
                                            </span>
                                        </span>
                                    </div>
                                    <div class="form-controls">
                                        <input type="range" name="humanizer_min_points" id="humanizer_min_points" min="2" max="8" value="4" step="1">
                                        <span class="slider-value" id="humanizer_min_points_value">4</span>
                                    </div>
                                </div>

                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-ellipsis-h"></i>
                                        Max Path Points
                                        <span class="help-tooltip">
                                            <i class="fas fa-question"></i>
                                            <span class="tooltip-content">
                                                Maximum number of points for long movements. Higher = smoother long-range flicks but takes more time. 25 is a good balance.
                                            </span>
                                        </span>
                                    </div>
                                    <div class="form-controls">
                                        <input type="range" name="humanizer_max_points" id="humanizer_max_points" min="10" max="40" value="25" step="1">
                                        <span class="slider-value" id="humanizer_max_points_value">25</span>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Tremor Settings -->
                        <div class="card antidetect-card">
                            <div class="card-header">
                                <div class="card-icon"><i class="fas fa-hand-paper"></i></div>
                                <h2 class="card-title">Hand Tremor Simulation</h2>
                            </div>
                            <div class="card-content">
                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-wave-square"></i>
                                        Tremor Amplitude (pixels)
                                        <span class="help-tooltip">
                                            <i class="fas fa-question"></i>
                                            <span class="tooltip-content">
                                                How much your aim naturally "shakes" like a real hand. Uses Perlin noise for smooth, natural tremor. 1.5px is realistic. Lower for steadier aim, higher for more human-like shake.
                                            </span>
                                        </span>
                                    </div>
                                    <div class="form-controls">
                                        <input type="range" name="humanizer_tremor_amplitude" id="humanizer_tremor_amplitude" min="0.5" max="4" value="1.5" step="0.25">
                                        <span class="slider-value" id="humanizer_tremor_amplitude_value">1.5px</span>
                                    </div>
                                </div>

                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-heartbeat"></i>
                                        Tremor Frequency
                                        <span class="help-tooltip">
                                            <i class="fas fa-question"></i>
                                            <span class="tooltip-content">
                                                How fast the tremor oscillates. Higher = faster shake. 8.0 simulates natural hand tremor frequency. Affects how "shaky" you appear.
                                            </span>
                                        </span>
                                    </div>
                                    <div class="form-controls">
                                        <input type="range" name="humanizer_tremor_frequency" id="humanizer_tremor_frequency" min="4" max="15" value="8" step="0.5">
                                        <span class="slider-value" id="humanizer_tremor_frequency_value">8.0</span>
                                    </div>
                                </div>

                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-fire-alt"></i>
                                        Stress Multiplier
                                        <span class="help-tooltip">
                                            <i class="fas fa-question"></i>
                                            <span class="tooltip-content">
                                                In close combat, tremor increases (like real humans get nervous). This multiplies tremor when targets are very close. 1.8x means 80% more tremor during "stressful" moments.
                                            </span>
                                        </span>
                                    </div>
                                    <div class="form-controls">
                                        <input type="range" name="humanizer_stress_multiplier" id="humanizer_stress_multiplier" min="1.0" max="3.0" value="1.8" step="0.1">
                                        <span class="slider-value" id="humanizer_stress_multiplier_value">1.8x</span>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Overshoot Settings -->
                        <div class="card antidetect-card">
                            <div class="card-header">
                                <div class="card-icon"><i class="fas fa-bullseye"></i></div>
                                <h2 class="card-title">Overshoot & Correction</h2>
                            </div>
                            <div class="card-content">
                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-percentage"></i>
                                        Overshoot Chance (%)
                                        <span class="help-tooltip">
                                            <i class="fas fa-question"></i>
                                            <span class="tooltip-content">
                                                How often you "overshoot" the target and correct back. Real humans don't stop perfectly on target. 35% is realistic for skilled players. Higher = more human, lower = more precise.
                                            </span>
                                        </span>
                                    </div>
                                    <div class="form-controls">
                                        <input type="range" name="humanizer_overshoot_chance" id="humanizer_overshoot_chance" min="10" max="60" value="35" step="5">
                                        <span class="slider-value" id="humanizer_overshoot_chance_value">35%</span>
                                    </div>
                                </div>

                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-arrows-alt-h"></i>
                                        Overshoot Amount (%)
                                        <span class="help-tooltip">
                                            <i class="fas fa-question"></i>
                                            <span class="tooltip-content">
                                                When overshooting, how far past the target you go as a percentage of the movement. 8% means you go 8% past then correct. Too high = looks like aim shake.
                                            </span>
                                        </span>
                                    </div>
                                    <div class="form-controls">
                                        <input type="range" name="humanizer_overshoot_amount" id="humanizer_overshoot_amount" min="3" max="15" value="8" step="1">
                                        <span class="slider-value" id="humanizer_overshoot_amount_value">8%</span>
                                    </div>
                                </div>

                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-hourglass-half"></i>
                                        Correction Delay (ms)
                                        <span class="help-tooltip">
                                            <i class="fas fa-question"></i>
                                            <span class="tooltip-content">
                                                Time between overshoot and correction movement. Simulates the tiny human reaction to realize you overshot. 25ms is natural. Lower = faster, higher = more deliberate.
                                            </span>
                                        </span>
                                    </div>
                                    <div class="form-controls">
                                        <input type="range" name="humanizer_correction_delay" id="humanizer_correction_delay" min="10" max="50" value="25" step="5">
                                        <span class="slider-value" id="humanizer_correction_delay_value">25ms</span>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Reaction Time & Miss Settings -->
                        <div class="card antidetect-card">
                            <div class="card-header">
                                <div class="card-icon"><i class="fas fa-stopwatch"></i></div>
                                <h2 class="card-title">Reaction Time & Accuracy</h2>
                            </div>
                            <div class="card-content">
                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-bolt"></i>
                                        Min Reaction Time (ms)
                                        <span class="help-tooltip">
                                            <i class="fas fa-question"></i>
                                            <span class="tooltip-content">
                                                Fastest possible reaction. Pro players react in ~140ms. If your reactions are consistently faster than human limits, you'll get flagged. This adds minimum delay before aiming.
                                            </span>
                                        </span>
                                    </div>
                                    <div class="form-controls">
                                        <input type="range" name="humanizer_reaction_min" id="humanizer_reaction_min" min="100" max="200" value="140" step="10">
                                        <span class="slider-value" id="humanizer_reaction_min_value">140ms</span>
                                    </div>
                                </div>

                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-hourglass-start"></i>
                                        Average Reaction Time (ms)
                                        <span class="help-tooltip">
                                            <i class="fas fa-question"></i>
                                            <span class="tooltip-content">
                                                Your average reaction time. Human average is ~215ms. This is the center of the reaction time distribution. Set based on your skill level persona.
                                            </span>
                                        </span>
                                    </div>
                                    <div class="form-controls">
                                        <input type="range" name="humanizer_reaction_mean" id="humanizer_reaction_mean" min="150" max="300" value="215" step="5">
                                        <span class="slider-value" id="humanizer_reaction_mean_value">215ms</span>
                                    </div>
                                </div>

                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-crosshairs"></i>
                                        Miss Chance (%)
                                        <span class="help-tooltip">
                                            <i class="fas fa-question"></i>
                                            <span class="tooltip-content">
                                                Chance to intentionally miss slightly. Even pros don't hit 100% of shots. 2.5% adds occasional misses to look more human. Set to 0 to disable.
                                            </span>
                                        </span>
                                    </div>
                                    <div class="form-controls">
                                        <input type="range" name="humanizer_miss_chance" id="humanizer_miss_chance" min="0" max="10" value="2.5" step="0.5">
                                        <span class="slider-value" id="humanizer_miss_chance_value">2.5%</span>
                                    </div>
                                </div>

                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-expand-arrows-alt"></i>
                                        Miss Offset (pixels)
                                        <span class="help-tooltip">
                                            <i class="fas fa-question"></i>
                                            <span class="tooltip-content">
                                                Maximum distance when you "miss". When a miss occurs, aim lands within this many pixels of the target instead of on it. 6px is subtle enough to not be obvious.
                                            </span>
                                        </span>
                                    </div>
                                    <div class="form-controls">
                                        <input type="range" name="humanizer_miss_offset" id="humanizer_miss_offset" min="2" max="15" value="6" step="1">
                                        <span class="slider-value" id="humanizer_miss_offset_value">6px</span>
                                    </div>
                                </div>

                                <div class="form-row">
                                    <div class="form-label">
                                        <i class="fas fa-forward"></i>
                                        Frame Skip Chance (%)
                                        <span class="help-tooltip">
                                            <i class="fas fa-question"></i>
                                            <span class="tooltip-content">
                                                Chance to skip processing a frame entirely. Simulates momentary attention lapses. 1.8% is subtle. Prevents unnaturally perfect frame-by-frame tracking.
                                            </span>
                                        </span>
                                    </div>
                                    <div class="form-controls">
                                        <input type="range" name="humanizer_frame_skip" id="humanizer_frame_skip" min="0" max="5" value="1.8" step="0.2">
                                        <span class="slider-value" id="humanizer_frame_skip_value">1.8%</span>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Statistics Card -->
                        <div class="card antidetect-card">
                            <div class="card-header">
                                <div class="card-icon"><i class="fas fa-chart-bar"></i></div>
                                <h2 class="card-title">Humanizer Statistics</h2>
                            </div>
                            <div class="card-content">
                                <div class="fingerprint-display" id="humanizerStatsDisplay">
                                    <div class="fingerprint-stat">
                                        <div class="fingerprint-stat-value" id="stat-total-movements">0</div>
                                        <div class="fingerprint-stat-label">Total Movements</div>
                                    </div>
                                    <div class="fingerprint-stat">
                                        <div class="fingerprint-stat-value" id="stat-overshoot-rate">0%</div>
                                        <div class="fingerprint-stat-label">Overshoot Rate</div>
                                    </div>
                                    <div class="fingerprint-stat">
                                        <div class="fingerprint-stat-value" id="stat-frame-skips">0</div>
                                        <div class="fingerprint-stat-label">Frame Skips</div>
                                    </div>
                                    <div class="fingerprint-stat">
                                        <div class="fingerprint-stat-value" id="stat-avg-distance">0px</div>
                                        <div class="fingerprint-stat-label">Avg Movement</div>
                                    </div>
                                </div>

                                <div class="form-row" style="margin-top: var(--space-4);">
                                    <div class="form-controls" style="width: 100%; display: flex; gap: var(--space-3);">
                                        <button type="button" class="btn secondary" onclick="refreshHumanizerStats()">
                                            <i class="fas fa-sync"></i> Refresh Stats
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </section>

                    <!-- Membership Content -->
                    <section id="membership-content" class="content-section">
                        <!-- Current Membership Status -->
                        <div class="card" style="border: 2px solid rgba(251, 191, 36, 0.3); background: linear-gradient(135deg, rgba(251, 191, 36, 0.05) 0%, rgba(245, 158, 11, 0.05) 100%);">
                            <div class="card-header">
                                <div class="card-icon" style="background: linear-gradient(135deg, #fbbf24, #f59e0b);"><i class="fas fa-crown"></i></div>
                                <h2 class="card-title" style="background: linear-gradient(135deg, #fbbf24, #f59e0b); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Membership Status</h2>
                            </div>
                            <div class="card-content">
                                <div id="membershipStatusDisplay" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: var(--space-6);">
                                    <div style="text-align: center; padding: var(--space-6); background: rgba(0,0,0,0.2); border-radius: var(--radius-xl);">
                                        <div style="font-size: 3rem; margin-bottom: var(--space-2);">👑</div>
                                        <div style="font-size: 1.5rem; font-weight: 700; color: #fbbf24;" id="membershipTierDisplay">Loading...</div>
                                        <div style="font-size: 0.875rem; color: var(--text-secondary);">Current Tier</div>
                                    </div>
                                    <div style="text-align: center; padding: var(--space-6); background: rgba(0,0,0,0.2); border-radius: var(--radius-xl);">
                                        <div style="font-size: 3rem; margin-bottom: var(--space-2);">⏰</div>
                                        <div style="font-size: 1.5rem; font-weight: 700; color: var(--text-primary);" id="membershipDaysDisplay">--</div>
                                        <div style="font-size: 0.875rem; color: var(--text-secondary);">Days Remaining</div>
                                    </div>
                                    <div style="text-align: center; padding: var(--space-6); background: rgba(0,0,0,0.2); border-radius: var(--radius-xl);">
                                        <div style="font-size: 3rem; margin-bottom: var(--space-2);">🔓</div>
                                        <div style="font-size: 1.5rem; font-weight: 700; color: var(--accent-secondary);" id="membershipFeaturesCount">--</div>
                                        <div style="font-size: 0.875rem; color: var(--text-secondary);">Features Unlocked</div>
                                    </div>
                                </div>
                                
                                <div class="form-row" style="margin-top: var(--space-6);">
                                    <div class="form-controls" style="width: 100%; display: flex; justify-content: center;">
                                        <button type="button" class="btn secondary" onclick="refreshMembershipStatus()">
                                            <i class="fas fa-sync"></i> Refresh Status
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Full Access Congratulations - hidden by default, shown when user has Full Access -->
                        <div id="fullAccessMessage" class="card" style="display: none; border: 2px solid rgba(16, 185, 129, 0.4); background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(16, 185, 129, 0.05) 100%);">
                            <div class="card-content" style="text-align: center; padding: var(--space-10);">
                                <div style="font-size: 4rem; margin-bottom: var(--space-4);">🎉</div>
                                <h2 style="font-size: 2rem; font-weight: 700; background: linear-gradient(135deg, #10b981, #059669); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: var(--space-4);">You Have Full Access!</h2>
                                <p style="color: var(--text-secondary); font-size: 1.1rem; max-width: 500px; margin: 0 auto;">Congratulations! You have unlocked all features and have the best membership tier available. Enjoy your premium experience!</p>
                            </div>
                        </div>

                        <!-- Pricing Plans - hidden when user has Full Access -->
                        <div id="upgradeSection" class="card">
                            <div class="card-header">
                                <div class="card-icon"><i class="fas fa-arrow-up"></i></div>
                                <h2 class="card-title">Your Plan & Upgrade Options</h2>
                            </div>
                            <div class="card-content">
                                <div id="pricingPlansContainer" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: var(--space-8);">
                                    
                                    <!-- YOUR CURRENT PLAN (Left Side) -->
                                    <div class="pricing-card" style="background: rgba(99, 102, 241, 0.1); border: 2px solid rgba(99, 102, 241, 0.5); border-radius: var(--radius-2xl); padding: var(--space-8); position: relative; overflow: hidden;">
                                        <div style="position: absolute; top: 0; right: 0; background: linear-gradient(135deg, #10b981, #059669); padding: var(--space-2) var(--space-4); border-bottom-left-radius: var(--radius-lg); font-weight: 700; color: #fff; font-size: 0.75rem;">✓ YOUR CURRENT PLAN</div>
                                        
                                        <div style="text-align: center; margin-bottom: var(--space-6);">
                                            <div style="font-size: 2.5rem; margin-bottom: var(--space-2);">🎮</div>
                                            <h3 style="font-size: 1.75rem; font-weight: 700; color: #6366f1; margin-bottom: var(--space-2);">Regular</h3>
                                            <p style="color: var(--text-secondary); font-size: 0.9rem;">Your active membership</p>
                                        </div>
                                        
                                        <div style="text-align: center; padding: var(--space-4); background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: var(--radius-lg); margin-bottom: var(--space-6);">
                                            <div style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 4px;">Time Remaining:</div>
                                            <div style="font-size: 1.5rem; font-weight: 700; color: #10b981;" id="currentPlanDays">-- days</div>
                                        </div>
                                        
                                        <div style="font-weight: 600; color: var(--text-primary); margin-bottom: var(--space-3);">What you have:</div>
                                        <ul style="list-style: none; margin-bottom: var(--space-6);">
                                            <li style="display: flex; align-items: center; gap: var(--space-3); padding: var(--space-2) 0; color: var(--text-primary);">
                                                <i class="fas fa-check" style="color: #10b981;"></i> Aimbot
                                            </li>
                                            <li style="display: flex; align-items: center; gap: var(--space-3); padding: var(--space-2) 0; color: var(--text-primary);">
                                                <i class="fas fa-check" style="color: #10b981;"></i> Humanizer Engine <span style="font-size: 0.75rem; color: var(--accent-warning); margin-left: 4px;">(Read-Only)</span>
                                            </li>
                                            <li style="display: flex; align-items: center; gap: var(--space-3); padding: var(--space-2) 0; color: var(--text-primary);">
                                                <i class="fas fa-check" style="color: #10b981;"></i> Fingerprint <span style="font-size: 0.75rem; color: var(--accent-warning); margin-left: 4px;">(Static)</span>
                                            </li>
                                            <li style="display: flex; align-items: center; gap: var(--space-3); padding: var(--space-2) 0; color: var(--text-primary);">
                                                <i class="fas fa-check" style="color: #10b981;"></i> Web UI
                                            </li>
                                        </ul>
                                        
                                        <div style="padding: var(--space-4); background: rgba(0,0,0,0.3); border-radius: var(--radius-lg); text-align: center;">
                                            <div style="color: var(--text-tertiary); font-size: 0.9rem;">Want to extend your Regular plan?</div>
                                            <select id="regularExtendSelect" style="width: 100%; padding: var(--space-3); background: var(--bg-quaternary); border: 1px solid rgba(255,255,255,0.2); border-radius: var(--radius-lg); color: var(--text-primary); margin: var(--space-3) 0;">
                                                <option value="1_week" data-price="0.50">1 Week - $0.50</option>
                                                <option value="1_month" data-price="24.99" selected>1 Month - $24.99</option>
                                                <option value="1_year" data-price="149.99">1 Year - $149.99</option>
                                            </select>
                                            <button type="button" class="btn" style="width: 100%; background: linear-gradient(135deg, #6366f1, #4f46e5);" onclick="selectPlan('regular')">
                                                <i class="fas fa-plus"></i> Extend Regular
                                            </button>
                                        </div>
                                    </div>
                                    
                                    <!-- UPGRADE TO FULL ACCESS (Right Side) -->
                                    <div class="pricing-card" style="background: linear-gradient(135deg, rgba(251, 191, 36, 0.15) 0%, rgba(245, 158, 11, 0.15) 100%); border: 2px solid rgba(251, 191, 36, 0.5); border-radius: var(--radius-2xl); padding: var(--space-8); position: relative; overflow: hidden; box-shadow: 0 0 40px rgba(251, 191, 36, 0.2);">
                                        <div style="position: absolute; top: 0; right: 0; background: linear-gradient(135deg, #fbbf24, #f59e0b); padding: var(--space-2) var(--space-4); border-bottom-left-radius: var(--radius-lg); font-weight: 700; color: #000; font-size: 0.75rem;">⬆️ UPGRADE AVAILABLE</div>
                                        
                                        <div style="text-align: center; margin-bottom: var(--space-6);">
                                            <div style="font-size: 2.5rem; margin-bottom: var(--space-2);">👑</div>
                                            <h3 style="font-size: 1.75rem; font-weight: 700; background: linear-gradient(135deg, #fbbf24, #f59e0b); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: var(--space-2);">Full Access</h3>
                                            <p style="color: var(--text-secondary); font-size: 0.9rem;">Unlock ALL features</p>
                                        </div>
                                        
                                        <div style="font-weight: 600; color: #fbbf24; margin-bottom: var(--space-3);">🔓 You'll unlock:</div>
                                        <ul style="list-style: none; margin-bottom: var(--space-6);">
                                            <li style="display: flex; align-items: center; gap: var(--space-3); padding: var(--space-2) 0; color: var(--text-primary); font-weight: 600;">
                                                <i class="fas fa-plus-circle" style="color: #fbbf24;"></i> Triggerbot
                                            </li>
                                            <li style="display: flex; align-items: center; gap: var(--space-3); padding: var(--space-2) 0; color: var(--text-primary); font-weight: 600;">
                                                <i class="fas fa-plus-circle" style="color: #fbbf24;"></i> Crosshair Overlay
                                            </li>
                                            <li style="display: flex; align-items: center; gap: var(--space-3); padding: var(--space-2) 0; color: var(--text-primary); font-weight: 600;">
                                                <i class="fas fa-plus-circle" style="color: #fbbf24;"></i> Anti-Recoil System
                                            </li>
                                            <li style="display: flex; align-items: center; gap: var(--space-3); padding: var(--space-2) 0; color: var(--text-primary); font-weight: 600;">
                                                <i class="fas fa-plus-circle" style="color: #fbbf24;"></i> Anti-Detection Settings
                                            </li>
                                            <li style="display: flex; align-items: center; gap: var(--space-3); padding: var(--space-2) 0; color: var(--text-primary); font-weight: 600;">
                                                <i class="fas fa-plus-circle" style="color: #fbbf24;"></i> Modify Humanizer Settings
                                            </li>
                                            <li style="display: flex; align-items: center; gap: var(--space-3); padding: var(--space-2) 0; color: var(--text-primary); font-weight: 600;">
                                                <i class="fas fa-plus-circle" style="color: #fbbf24;"></i> Regenerate Fingerprint
                                            </li>
                                            <li style="display: flex; align-items: center; gap: var(--space-3); padding: var(--space-2) 0; color: #fbbf24; font-weight: 600;">
                                                <i class="fas fa-star" style="color: #fbbf24;"></i> Priority Support
                                            </li>
                                        </ul>
                                        
                                        <div style="margin-top: var(--space-4);">
                                            <label style="display: block; margin-bottom: var(--space-2); color: var(--text-secondary); font-size: 0.875rem;">Select Duration:</label>
                                            <select id="fullAccessDurationSelect" style="width: 100%; padding: var(--space-3); background: var(--bg-quaternary); border: 1px solid rgba(251, 191, 36, 0.3); border-radius: var(--radius-lg); color: var(--text-primary); margin-bottom: var(--space-4);">
                                                <option value="1_week" data-price="0.50">1 Week - $0.50</option>
                                                <option value="1_month" data-price="49.99" selected>1 Month - $49.99</option>
                                                <option value="3_months" data-price="119.99">3 Months - $119.99</option>
                                                <option value="1_year" data-price="299.99">1 Year - $299.99</option>
                                                <option value="lifetime" data-price="499.99">Lifetime - $499.99 🔥</option>
                                            </select>
                                            <button type="button" class="btn" style="width: 100%; background: linear-gradient(135deg, #fbbf24, #f59e0b); color: #000; font-weight: 700; font-size: 1.1rem; padding: var(--space-4);" onclick="selectPlan('full_access')">
                                                <i class="fas fa-crown"></i> Upgrade to Full Access
                                            </button>
                                        </div>
                                    </div>
                                </div>
                                
                                <div style="margin-top: var(--space-6); padding: var(--space-4); background: rgba(251, 191, 36, 0.1); border: 1px solid rgba(251, 191, 36, 0.3); border-radius: var(--radius-lg); display: flex; align-items: center; gap: var(--space-3);">
                                    <i class="fas fa-info-circle" style="color: #fbbf24;"></i>
                                    <span style="color: var(--text-secondary); font-size: 0.9rem;">
                                        <strong style="color: #fbbf24;">Secure Payment:</strong> All payments are processed securely. Your license key is tied to your hardware ID for security. After purchase, your membership will be automatically upgraded.
                                    </span>
                                </div>
                            </div>
                        </div>

                        <!-- Feature Comparison -->
                        <div class="card">
                            <div class="card-header">
                                <div class="card-icon"><i class="fas fa-list-check"></i></div>
                                <h2 class="card-title">Feature Access by Tier</h2>
                            </div>
                            <div class="card-content">
                                <div id="featureAccessGrid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: var(--space-4);">
                                    <!-- Features will be populated by JS -->
                                </div>
                            </div>
                        </div>
                        
                        <!-- License Transfer Section -->
                        <div class="card">
                            <div class="card-header">
                                <div class="card-icon"><i class="fas fa-exchange-alt"></i></div>
                                <h2 class="card-title">License Transfer</h2>
                            </div>
                            <div class="card-content">
                                <!-- Generate Transfer Code (Old PC) -->
                                <div style="padding: var(--space-6); background: rgba(99, 102, 241, 0.1); border: 1px solid rgba(99, 102, 241, 0.3); border-radius: var(--radius-xl); max-width: 500px;">
                                    <div style="text-align: center; margin-bottom: var(--space-4);">
                                        <i class="fas fa-upload" style="font-size: 2rem; color: #6366f1; margin-bottom: var(--space-2);"></i>
                                        <h4 style="color: var(--text-primary); font-weight: 600;">Transfer to a New PC</h4>
                                        <p style="color: var(--text-secondary); font-size: 0.85rem; margin-top: var(--space-2);">Moving to a new PC? Generate a transfer code here, then enter it on your new PC to claim your license.</p>
                                    </div>
                                    <button type="button" class="btn" style="width: 100%; background: linear-gradient(135deg, #6366f1, #4f46e5);" onclick="generateTransferCode()">
                                        <i class="fas fa-key"></i> Generate Transfer Code
                                    </button>
                                    <div id="transferCodeDisplay" style="display: none; margin-top: var(--space-4); padding: var(--space-4); background: rgba(0,0,0,0.3); border-radius: var(--radius-lg); text-align: center;">
                                        <div style="font-size: 0.85rem; color: var(--text-secondary); margin-bottom: var(--space-2);">Your Transfer Code:</div>
                                        <div id="generatedTransferCode" style="font-size: 2rem; font-weight: 700; letter-spacing: 4px; color: #10b981; font-family: var(--font-mono);"></div>
                                        <div style="font-size: 0.75rem; color: var(--accent-warning); margin-top: var(--space-2);">⚠️ Write this down! It won't be shown again.</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>

                    <!-- ============================================ -->
                    <!-- SPOTIFY SECTION - Full Access Only -->
                    <!-- ============================================ -->
                    <section id="spotify-content" class="content-section" data-requires="full_access">
                        <!-- Spotify Header with Gradient -->
                        <div style="background: linear-gradient(135deg, #1DB954 0%, #191414 60%); border-radius: var(--radius-2xl); padding: var(--space-8); margin-bottom: var(--space-6); position: relative; overflow: hidden;">
                            <div style="position: absolute; top: 0; right: 0; width: 300px; height: 300px; background: radial-gradient(circle, rgba(29, 185, 84, 0.3) 0%, transparent 70%); pointer-events: none;"></div>
                            <div style="display: flex; align-items: center; gap: var(--space-6); position: relative; z-index: 1;">
                                <div style="width: 80px; height: 80px; background: #1DB954; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 8px 32px rgba(29, 185, 84, 0.4);">
                                    <i class="fab fa-spotify" style="font-size: 3rem; color: #000;"></i>
                                </div>
                                <div>
                                    <h1 style="font-size: 2.5rem; font-weight: 800; color: #fff; margin: 0; text-shadow: 0 2px 20px rgba(0,0,0,0.3);">Spotify Premium</h1>
                                    <p style="color: rgba(255,255,255,0.8); margin: 0; font-size: 1.1rem;">Ad-Free Music • Full Access Exclusive Perk</p>
                                </div>
                                <div style="margin-left: auto; display: flex; gap: var(--space-3);">
                                    <div style="background: rgba(0,0,0,0.4); backdrop-filter: blur(10px); padding: var(--space-4) var(--space-6); border-radius: var(--radius-xl); text-align: center;">
                                        <div style="font-size: 1.5rem; font-weight: 700; color: #1DB954;" id="spotifyQueueCount">0</div>
                                        <div style="font-size: 0.75rem; color: rgba(255,255,255,0.6);">In Queue</div>
                                    </div>
                                    <div style="background: rgba(0,0,0,0.4); backdrop-filter: blur(10px); padding: var(--space-4) var(--space-6); border-radius: var(--radius-xl); text-align: center;">
                                        <div style="font-size: 1.5rem; font-weight: 700; color: #fff;" id="spotifyPlaylistCount">0</div>
                                        <div style="font-size: 0.75rem; color: rgba(255,255,255,0.6);">Playlists</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Search Bar - Premium Design -->
                        <div style="background: linear-gradient(135deg, rgba(30, 215, 96, 0.1) 0%, rgba(18, 18, 18, 0.95) 100%); border: 1px solid rgba(30, 215, 96, 0.2); border-radius: var(--radius-2xl); padding: var(--space-6); margin-bottom: var(--space-6); backdrop-filter: blur(20px);">
                            <div style="display: flex; gap: var(--space-4); align-items: center;">
                                <div style="flex: 1; position: relative;">
                                    <i class="fas fa-search" style="position: absolute; left: 20px; top: 50%; transform: translateY(-50%); color: #1DB954; font-size: 1.2rem;"></i>
                                    <input type="text" id="spotifySearchInput" placeholder="What do you want to listen to?" 
                                           style="width: 100%; padding: 18px 20px 18px 56px; background: rgba(0,0,0,0.4); border: 2px solid transparent; border-radius: 50px; color: #fff; font-size: 1.1rem; transition: all 0.3s; outline: none;"
                                           onfocus="this.style.borderColor='#1DB954'; this.style.background='rgba(0,0,0,0.6)'"
                                           onblur="this.style.borderColor='transparent'; this.style.background='rgba(0,0,0,0.4)'"
                                           onkeypress="if(event.key==='Enter') searchSpotify()">
                                </div>
                                <button style="padding: 18px 40px; background: #1DB954; border: none; border-radius: 50px; color: #000; font-weight: 700; font-size: 1rem; cursor: pointer; transition: all 0.3s; display: flex; align-items: center; gap: 10px;" onclick="searchSpotify()" onmouseover="this.style.transform='scale(1.05)'; this.style.boxShadow='0 8px 32px rgba(29, 185, 84, 0.4)'" onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='none'">
                                    <i class="fas fa-search"></i> Search
                                </button>
                            </div>
                        </div>
                        
                        <div style="display: grid; grid-template-columns: 1fr 400px; gap: var(--space-6);">
                            <!-- Main Content Area -->
                            <div>
                                <!-- Now Playing - Premium Card -->
                                <div style="background: linear-gradient(135deg, rgba(29, 185, 84, 0.2) 0%, rgba(18, 18, 18, 0.98) 40%); border: 1px solid rgba(29, 185, 84, 0.3); border-radius: var(--radius-2xl); padding: var(--space-8); margin-bottom: var(--space-6); position: relative; overflow: hidden;">
                                    <!-- Animated Background Glow -->
                                    <div id="spotifyBgGlow" style="position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: radial-gradient(circle at center, rgba(29, 185, 84, 0.15) 0%, transparent 50%); opacity: 0.5; animation: pulse 4s ease-in-out infinite; pointer-events: none;"></div>
                                    
                                    <div style="display: flex; gap: var(--space-8); align-items: center; position: relative; z-index: 1;">
                                        <!-- Album Art with Reflection -->
                                        <div style="position: relative;">
                                            <div id="spotifyNowPlayingArt" style="width: 180px; height: 180px; background: linear-gradient(135deg, #282828 0%, #121212 100%); border-radius: var(--radius-xl); display: flex; align-items: center; justify-content: center; overflow: hidden; box-shadow: 0 20px 60px rgba(0,0,0,0.5);">
                                                <i class="fas fa-music" style="font-size: 4rem; color: #404040;"></i>
                                            </div>
                                            <div style="position: absolute; bottom: -30px; left: 0; right: 0; height: 30px; background: linear-gradient(to bottom, rgba(29, 185, 84, 0.1), transparent); filter: blur(10px);"></div>
                                        </div>
                                        
                                        <div style="flex: 1;">
                                            <div style="font-size: 0.75rem; color: #1DB954; font-weight: 700; letter-spacing: 2px; margin-bottom: var(--space-2);">♪ NOW PLAYING</div>
                                            <div id="spotifyNowPlayingTitle" style="font-size: 2rem; font-weight: 800; color: #fff; margin-bottom: var(--space-1); line-height: 1.2;">No song playing</div>
                                            <div id="spotifyNowPlayingArtist" style="font-size: 1.1rem; color: rgba(255,255,255,0.6);">Select a song to start</div>
                                            
                                            <!-- Waveform Visualizer (CSS Animation) -->
                                            <div id="spotifyVisualizer" style="display: none; height: 40px; margin: var(--space-4) 0; display: flex; align-items: flex-end; gap: 3px;">
                                                <div style="width: 4px; background: #1DB954; border-radius: 2px; animation: wave 0.5s ease-in-out infinite;"></div>
                                                <div style="width: 4px; background: #1DB954; border-radius: 2px; animation: wave 0.5s ease-in-out infinite 0.1s;"></div>
                                                <div style="width: 4px; background: #1DB954; border-radius: 2px; animation: wave 0.5s ease-in-out infinite 0.2s;"></div>
                                                <div style="width: 4px; background: #1DB954; border-radius: 2px; animation: wave 0.5s ease-in-out infinite 0.3s;"></div>
                                                <div style="width: 4px; background: #1DB954; border-radius: 2px; animation: wave 0.5s ease-in-out infinite 0.4s;"></div>
                                                <div style="width: 4px; background: #1DB954; border-radius: 2px; animation: wave 0.5s ease-in-out infinite 0.15s;"></div>
                                                <div style="width: 4px; background: #1DB954; border-radius: 2px; animation: wave 0.5s ease-in-out infinite 0.25s;"></div>
                                                <div style="width: 4px; background: #1DB954; border-radius: 2px; animation: wave 0.5s ease-in-out infinite 0.35s;"></div>
                                            </div>
                                            
                                            <!-- Progress Bar -->
                                            <div style="margin-top: var(--space-6);">
                                                <div style="height: 6px; background: rgba(255,255,255,0.1); border-radius: 3px; overflow: hidden; cursor: pointer; position: relative;" onclick="seekSpotify(event)">
                                                    <div id="spotifyProgressBar" style="height: 100%; width: 0%; background: linear-gradient(90deg, #1DB954 0%, #1ed760 100%); transition: width 0.1s; border-radius: 3px;"></div>
                                                    <div id="spotifyProgressDot" style="position: absolute; top: 50%; transform: translate(-50%, -50%); width: 14px; height: 14px; background: #fff; border-radius: 50%; box-shadow: 0 2px 8px rgba(0,0,0,0.3); left: 0%; opacity: 0; transition: opacity 0.2s;"></div>
                                                </div>
                                                <div style="display: flex; justify-content: space-between; font-size: 0.8rem; color: rgba(255,255,255,0.5); margin-top: var(--space-2);">
                                                    <span id="spotifyCurrentTime">0:00</span>
                                                    <span id="spotifyDuration">0:00</span>
                                                </div>
                                            </div>
                                            
                                            <!-- Controls -->
                                            <div style="display: flex; align-items: center; gap: var(--space-4); margin-top: var(--space-4);">
                                                <button style="background: transparent; border: none; color: rgba(255,255,255,0.6); font-size: 1.2rem; cursor: pointer; transition: all 0.2s; padding: 10px;" onclick="shuffleSpotifyQueue()" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='rgba(255,255,255,0.6)'">
                                                    <i class="fas fa-random"></i>
                                                </button>
                                                <button style="background: transparent; border: none; color: #fff; font-size: 1.5rem; cursor: pointer; transition: all 0.2s; padding: 10px;" onclick="spotifyPrev()" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
                                                    <i class="fas fa-step-backward"></i>
                                                </button>
                                                <button id="spotifyPlayBtn" style="width: 64px; height: 64px; border-radius: 50%; background: #fff; border: none; color: #000; font-size: 1.8rem; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; justify-content: center; box-shadow: 0 8px 24px rgba(0,0,0,0.3);" onclick="toggleSpotifyPlay()" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
                                                    <i class="fas fa-play" style="margin-left: 4px;"></i>
                                                </button>
                                                <button style="background: transparent; border: none; color: #fff; font-size: 1.5rem; cursor: pointer; transition: all 0.2s; padding: 10px;" onclick="spotifyNext()" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'">
                                                    <i class="fas fa-step-forward"></i>
                                                </button>
                                                <button style="background: transparent; border: none; color: rgba(255,255,255,0.6); font-size: 1.2rem; cursor: pointer; transition: all 0.2s; padding: 10px;" onclick="toggleRepeat()" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='rgba(255,255,255,0.6)'">
                                                    <i class="fas fa-redo"></i>
                                                </button>
                                                <div style="margin-left: auto; display: flex; align-items: center; gap: var(--space-3);">
                                                    <i class="fas fa-volume-up" style="color: rgba(255,255,255,0.6);"></i>
                                                    <input type="range" id="spotifyVolume" min="0" max="100" value="80" style="width: 120px; accent-color: #1DB954;" onchange="setSpotifyVolume(this.value)">
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- Search Results -->
                                <div style="background: rgba(18, 18, 18, 0.95); border: 1px solid rgba(255,255,255,0.1); border-radius: var(--radius-2xl); overflow: hidden;">
                                    <div style="padding: var(--space-6); border-bottom: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: space-between;">
                                        <div style="display: flex; align-items: center; gap: var(--space-3);">
                                            <i class="fas fa-compact-disc" style="font-size: 1.5rem; color: #1DB954;"></i>
                                            <h2 id="spotifyResultsTitle" style="font-size: 1.5rem; font-weight: 700; color: #fff; margin: 0;">Discover Music</h2>
                                        </div>
                                        <button style="background: rgba(29, 185, 84, 0.2); border: none; color: #1DB954; padding: 10px 20px; border-radius: 20px; cursor: pointer; font-weight: 600;" onclick="loadPopularTracks()">
                                            <i class="fas fa-fire"></i> Load Popular
                                        </button>
                                    </div>
                                    <div id="spotifyResults" style="padding: var(--space-4); max-height: 400px; overflow-y: auto;">
                                        <div style="text-align: center; padding: var(--space-12); color: rgba(255,255,255,0.4);">
                                            <i class="fas fa-headphones" style="font-size: 4rem; margin-bottom: var(--space-4); opacity: 0.3;"></i>
                                            <p style="font-size: 1.1rem;">Search for songs or load popular tracks</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Right Sidebar -->
                            <div style="display: flex; flex-direction: column; gap: var(--space-4);">
                                <!-- Queue -->
                                <div style="background: rgba(18, 18, 18, 0.95); border: 1px solid rgba(255,255,255,0.1); border-radius: var(--radius-2xl); overflow: hidden;">
                                    <div style="padding: var(--space-4) var(--space-5); border-bottom: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: space-between;">
                                        <div style="display: flex; align-items: center; gap: var(--space-2);">
                                            <i class="fas fa-list" style="color: #1DB954;"></i>
                                            <span style="font-weight: 700; color: #fff;">Queue</span>
                                        </div>
                                        <button style="background: transparent; border: none; color: rgba(255,255,255,0.4); cursor: pointer; font-size: 0.85rem;" onclick="clearSpotifyQueue()">
                                            <i class="fas fa-trash"></i> Clear
                                        </button>
                                    </div>
                                    <div id="spotifyQueue" style="padding: var(--space-3); max-height: 250px; overflow-y: auto;">
                                        <div style="text-align: center; padding: var(--space-6); color: rgba(255,255,255,0.3);">
                                            <i class="fas fa-music" style="font-size: 1.5rem; margin-bottom: var(--space-2);"></i>
                                            <p style="font-size: 0.85rem;">Queue is empty</p>
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- My Playlists -->
                                <div style="background: rgba(18, 18, 18, 0.95); border: 1px solid rgba(255,255,255,0.1); border-radius: var(--radius-2xl); overflow: hidden;">
                                    <div style="padding: var(--space-4) var(--space-5); border-bottom: 1px solid rgba(255,255,255,0.1); display: flex; align-items: center; justify-content: space-between;">
                                        <div style="display: flex; align-items: center; gap: var(--space-2);">
                                            <i class="fas fa-heart" style="color: #e91e63;"></i>
                                            <span style="font-weight: 700; color: #fff;">My Playlists</span>
                                        </div>
                                        <button style="background: #1DB954; border: none; color: #000; padding: 6px 12px; border-radius: 20px; cursor: pointer; font-size: 0.8rem; font-weight: 600;" onclick="createNewPlaylist()">
                                            <i class="fas fa-plus"></i> New
                                        </button>
                                    </div>
                                    <div id="spotifyMyPlaylists" style="padding: var(--space-3); max-height: 200px; overflow-y: auto;">
                                        <!-- Playlists loaded from localStorage -->
                                    </div>
                                </div>
                                
                                <!-- Quick Play -->
                                <div style="background: rgba(18, 18, 18, 0.95); border: 1px solid rgba(255,255,255,0.1); border-radius: var(--radius-2xl); overflow: hidden;">
                                    <div style="padding: var(--space-4) var(--space-5); border-bottom: 1px solid rgba(255,255,255,0.1);">
                                        <div style="display: flex; align-items: center; gap: var(--space-2);">
                                            <i class="fas fa-bolt" style="color: #fbbf24;"></i>
                                            <span style="font-weight: 700; color: #fff;">Quick Play</span>
                                        </div>
                                    </div>
                                    <div style="padding: var(--space-3); display: flex; flex-direction: column; gap: var(--space-2);">
                                        <button style="display: flex; align-items: center; gap: var(--space-3); padding: var(--space-3); background: rgba(255,255,255,0.05); border: none; border-radius: var(--radius-lg); color: #fff; cursor: pointer; transition: all 0.2s; width: 100%;" onclick="loadPlaylist('top50')" onmouseover="this.style.background='rgba(29, 185, 84, 0.2)'" onmouseout="this.style.background='rgba(255,255,255,0.05)'">
                                            <div style="width: 40px; height: 40px; background: linear-gradient(135deg, #ff6b6b, #ee5a24); border-radius: var(--radius-md); display: flex; align-items: center; justify-content: center;">
                                                <i class="fas fa-fire" style="color: #fff;"></i>
                                            </div>
                                            <span>Top 50 Global</span>
                                        </button>
                                        <button style="display: flex; align-items: center; gap: var(--space-3); padding: var(--space-3); background: rgba(255,255,255,0.05); border: none; border-radius: var(--radius-lg); color: #fff; cursor: pointer; transition: all 0.2s; width: 100%;" onclick="loadPlaylist('gaming')" onmouseover="this.style.background='rgba(29, 185, 84, 0.2)'" onmouseout="this.style.background='rgba(255,255,255,0.05)'">
                                            <div style="width: 40px; height: 40px; background: linear-gradient(135deg, #a855f7, #7c3aed); border-radius: var(--radius-md); display: flex; align-items: center; justify-content: center;">
                                                <i class="fas fa-gamepad" style="color: #fff;"></i>
                                            </div>
                                            <span>Gaming Mix</span>
                                        </button>
                                        <button style="display: flex; align-items: center; gap: var(--space-3); padding: var(--space-3); background: rgba(255,255,255,0.05); border: none; border-radius: var(--radius-lg); color: #fff; cursor: pointer; transition: all 0.2s; width: 100%;" onclick="loadPlaylist('chill')" onmouseover="this.style.background='rgba(29, 185, 84, 0.2)'" onmouseout="this.style.background='rgba(255,255,255,0.05)'">
                                            <div style="width: 40px; height: 40px; background: linear-gradient(135deg, #38bdf8, #0ea5e9); border-radius: var(--radius-md); display: flex; align-items: center; justify-content: center;">
                                                <i class="fas fa-cloud" style="color: #fff;"></i>
                                            </div>
                                            <span>Chill Vibes</span>
                                        </button>
                                        <button style="display: flex; align-items: center; gap: var(--space-3); padding: var(--space-3); background: rgba(255,255,255,0.05); border: none; border-radius: var(--radius-lg); color: #fff; cursor: pointer; transition: all 0.2s; width: 100%;" onclick="loadPlaylist('hiphop')" onmouseover="this.style.background='rgba(29, 185, 84, 0.2)'" onmouseout="this.style.background='rgba(255,255,255,0.05)'">
                                            <div style="width: 40px; height: 40px; background: linear-gradient(135deg, #f97316, #ea580c); border-radius: var(--radius-md); display: flex; align-items: center; justify-content: center;">
                                                <i class="fas fa-microphone" style="color: #fff;"></i>
                                            </div>
                                            <span>Hip Hop Hits</span>
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Add to Playlist Modal -->
                        <div id="addToPlaylistModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); z-index: 99999; align-items: center; justify-content: center; backdrop-filter: blur(8px);">
                            <div style="background: linear-gradient(135deg, #282828 0%, #1a1a1a 100%); border-radius: 24px; padding: 32px; max-width: 420px; width: 90%; box-shadow: 0 25px 80px rgba(0,0,0,0.6); border: 1px solid rgba(255,255,255,0.1);">
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px;">
                                    <div style="display: flex; align-items: center; gap: 12px;">
                                        <div style="width: 48px; height: 48px; background: linear-gradient(135deg, #1DB954, #1aa34a); border-radius: 12px; display: flex; align-items: center; justify-content: center;">
                                            <i class="fas fa-heart" style="color: #fff; font-size: 1.2rem;"></i>
                                        </div>
                                        <h3 style="color: #fff; font-size: 1.4rem; margin: 0; font-weight: 700;">Add to Playlist</h3>
                                    </div>
                                    <button style="background: rgba(255,255,255,0.1); border: none; color: #fff; width: 36px; height: 36px; border-radius: 50%; cursor: pointer; font-size: 1.2rem; transition: all 0.2s;" onclick="closePlaylistModal()" onmouseover="this.style.background='rgba(255,255,255,0.2)'" onmouseout="this.style.background='rgba(255,255,255,0.1)'">×</button>
                                </div>
                                <div id="playlistModalContent" style="max-height: 320px; overflow-y: auto;">
                                    <!-- Playlists will be listed here -->
                                </div>
                            </div>
                        </div>
                        
                        <!-- Create Playlist Modal -->
                        <div id="createPlaylistModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); z-index: 99999; align-items: center; justify-content: center; backdrop-filter: blur(8px);">
                            <div style="background: linear-gradient(135deg, #282828 0%, #1a1a1a 100%); border-radius: 24px; padding: 40px; max-width: 450px; width: 90%; box-shadow: 0 25px 80px rgba(0,0,0,0.6); border: 1px solid rgba(255,255,255,0.1);">
                                <div style="text-align: center; margin-bottom: 32px;">
                                    <div style="width: 80px; height: 80px; background: linear-gradient(135deg, #e91e63, #c2185b); border-radius: 20px; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; box-shadow: 0 12px 40px rgba(233, 30, 99, 0.3);">
                                        <i class="fas fa-plus" style="color: #fff; font-size: 2rem;"></i>
                                    </div>
                                    <h2 style="color: #fff; font-size: 1.75rem; margin: 0 0 8px; font-weight: 800;">Create Playlist</h2>
                                    <p style="color: rgba(255,255,255,0.5); margin: 0; font-size: 0.95rem;">Give your playlist a name</p>
                                </div>
                                <div style="margin-bottom: 28px;">
                                    <input type="text" id="createPlaylistInput" placeholder="My Awesome Playlist" 
                                           style="width: 100%; padding: 18px 24px; background: rgba(0,0,0,0.4); border: 2px solid rgba(255,255,255,0.1); border-radius: 16px; color: #fff; font-size: 1.1rem; outline: none; transition: all 0.3s; box-sizing: border-box;"
                                           onfocus="this.style.borderColor='#1DB954'; this.style.background='rgba(0,0,0,0.6)'"
                                           onblur="this.style.borderColor='rgba(255,255,255,0.1)'; this.style.background='rgba(0,0,0,0.4)'"
                                           onkeypress="if(event.key==='Enter') confirmCreatePlaylist()">
                                </div>
                                <div style="display: flex; gap: 12px;">
                                    <button style="flex: 1; padding: 16px; background: rgba(255,255,255,0.1); border: none; border-radius: 50px; color: #fff; font-size: 1rem; font-weight: 600; cursor: pointer; transition: all 0.2s;" onclick="closeCreatePlaylistModal()" onmouseover="this.style.background='rgba(255,255,255,0.15)'" onmouseout="this.style.background='rgba(255,255,255,0.1)'">
                                        Cancel
                                    </button>
                                    <button style="flex: 1; padding: 16px; background: linear-gradient(135deg, #1DB954, #1aa34a); border: none; border-radius: 50px; color: #000; font-size: 1rem; font-weight: 700; cursor: pointer; transition: all 0.2s;" onclick="confirmCreatePlaylist()" onmouseover="this.style.transform='scale(1.02)'; this.style.boxShadow='0 8px 24px rgba(29, 185, 84, 0.4)'" onmouseout="this.style.transform='scale(1)'; this.style.boxShadow='none'">
                                        <i class="fas fa-check"></i> Create
                                    </button>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Edit Playlist Modal -->
                        <div id="editPlaylistModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); z-index: 99999; align-items: center; justify-content: center; backdrop-filter: blur(8px);">
                            <div style="background: linear-gradient(135deg, #282828 0%, #1a1a1a 100%); border-radius: 24px; padding: 32px; max-width: 550px; width: 95%; box-shadow: 0 25px 80px rgba(0,0,0,0.6); border: 1px solid rgba(255,255,255,0.1);">
                                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px;">
                                    <div style="display: flex; align-items: center; gap: 12px;">
                                        <div style="width: 48px; height: 48px; background: linear-gradient(135deg, #e91e63, #c2185b); border-radius: 12px; display: flex; align-items: center; justify-content: center;">
                                            <i class="fas fa-pen" style="color: #fff; font-size: 1.2rem;"></i>
                                        </div>
                                        <div>
                                            <h3 id="editPlaylistTitle" style="color: #fff; font-size: 1.4rem; margin: 0; font-weight: 700;">Edit Playlist</h3>
                                            <p style="color: rgba(255,255,255,0.5); margin: 0; font-size: 0.85rem;">Remove songs you don't want</p>
                                        </div>
                                    </div>
                                    <button style="background: rgba(255,255,255,0.1); border: none; color: #fff; width: 40px; height: 40px; border-radius: 50%; cursor: pointer; font-size: 1.4rem; transition: all 0.2s;" onclick="closeEditPlaylistModal()" onmouseover="this.style.background='rgba(255,255,255,0.2)'" onmouseout="this.style.background='rgba(255,255,255,0.1)'">×</button>
                                </div>
                                <div id="editPlaylistContent" style="max-height: 400px; overflow-y: auto;">
                                    <!-- Songs will be listed here with delete buttons -->
                                </div>
                                <div style="margin-top: 20px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.1);">
                                    <button style="width: 100%; padding: 14px; background: linear-gradient(135deg, #1DB954, #1aa34a); border: none; border-radius: 50px; color: #000; font-size: 1rem; font-weight: 700; cursor: pointer; transition: all 0.2s;" onclick="closeEditPlaylistModal()" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
                                        <i class="fas fa-check"></i> Done
                                    </button>
                                </div>
                            </div>
                        </div>
                        
                        <!-- CSS for Waveform Animation -->
                        <style>
                            @keyframes wave {
                                0%, 100% { height: 8px; }
                                50% { height: 30px; }
                            }
                            #createPlaylistInput::placeholder {
                                color: rgba(255,255,255,0.3);
                            }
                        </style>
                        
                        <!-- Hidden Audio Element -->
                        <audio id="spotifyAudio" style="display: none;"></audio>
                    </section>


                </form>
            </div>
        </div>
    </div>

    <!-- Toast Container -->
    <div id="toastContainer" class="toast-container"></div>

</body>
</html>
"""