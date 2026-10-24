# Script to generate clean white theme style.css with full mobile responsiveness

css_content = """/* ==========================================================================
   ExaInfra.in - National Real Estate, Commercial Yield & Asset Terminal
   Aesthetic: Sovereign-grade Indian Institutional White / Light Theme
   Clean, Authoritative, High-Contrast & 100% Mobile Compatible
   ========================================================================== */

:root {
  /* Crisp Light Theme Tokens */
  --bg-body: #F8FAFC;
  --bg-card: #FFFFFF;
  --bg-subtle: #F1F5F9;
  --bg-elevated: #FFFFFF;

  /* Sovereign National Accents */
  --navy-authority: #0A192F;
  --navy-dark: #0F2544;
  --navy-surface: #1E3E62;
  --navy-border: #E2E8F0;

  --saffron-500: #F59E0B;
  --saffron-600: #D97706;
  --saffron-700: #B45309;
  --saffron-light: rgba(245, 158, 11, 0.1);

  --emerald-500: #10B981;
  --emerald-600: #059669;
  --emerald-light: rgba(16, 185, 129, 0.1);

  --crimson-500: #EF4444;
  --crimson-600: #DC2626;
  --crimson-light: rgba(239, 68, 68, 0.1);

  --blue-sky: #0284C7;
  --blue-light: rgba(2, 132, 199, 0.08);

  /* Text Colors */
  --text-main: #0F172A;
  --text-secondary: #334155;
  --text-muted: #64748B;
  --text-light: #94A3B8;

  /* Borders & Shadows */
  --border-card: #E2E8F0;
  --border-input: #CBD5E1;
  --border-hover: #D97706;

  --shadow-sm: 0 1px 3px rgba(15, 23, 42, 0.06);
  --shadow-card: 0 4px 16px rgba(15, 23, 42, 0.06);
  --shadow-hover: 0 10px 25px rgba(15, 23, 42, 0.1);
  --shadow-modal: 0 25px 50px -12px rgba(15, 23, 42, 0.25);

  --font-main: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 14px;
  --radius-full: 9999px;
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
  -webkit-text-size-adjust: 100%;
}

body {
  font-family: var(--font-main);
  background: var(--bg-body);
  color: var(--text-main);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
  width: 100%;
}

/* Container */
.container {
  width: 100%;
  max-width: 1240px;
  margin: 0 auto;
  padding: 0 1.25rem;
}

/* ==========================================================================
   Top National Statutory Ticker Bar (Official Sovereign Ribbon)
   ========================================================================== */
.national-ticker-bar {
  background: var(--navy-authority);
  border-bottom: 1px solid #1E293B;
  color: #CBD5E1;
  font-size: 0.78rem;
  padding: 0.5rem 0;
  font-family: var(--font-mono);
}

.ticker-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}

.compliance-status-pill {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  white-space: nowrap;
}

.live-pulse-dot {
  width: 8px;
  height: 8px;
  background: var(--emerald-500);
  border-radius: 50%;
  box-shadow: 0 0 8px var(--emerald-500);
  animation: pulseGreen 1.8s infinite;
}

@keyframes pulseGreen {
  0% { transform: scale(0.9); opacity: 0.8; }
  50% { transform: scale(1.3); opacity: 1; }
  100% { transform: scale(0.9); opacity: 0.8; }
}

.ticker-text {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.ticker-node {
  color: var(--saffron-500);
  font-weight: 700;
  white-space: nowrap;
}

/* ==========================================================================
   Main Navigation Header (Crisp Light Institutional Theme)
   ========================================================================== */
.navbar-terminal {
  background: rgba(255, 255, 255, 0.97);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border-card);
  position: sticky;
  top: 0;
  z-index: 1000;
  padding: 0.75rem 0;
  box-shadow: var(--shadow-sm);
}

.nav-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.brand-wrap {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  text-decoration: none;
}

.brand-emblem {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, var(--navy-authority), #1E3E62);
  border: 1px solid var(--saffron-600);
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--saffron-500);
  box-shadow: 0 2px 8px rgba(217, 119, 6, 0.2);
}

.brand-text-col {
  display: flex;
  flex-direction: column;
}

.brand-title {
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--navy-authority);
  letter-spacing: -0.02em;
}

.brand-title span {
  color: var(--saffron-600);
}

.brand-sub {
  font-size: 0.65rem;
  font-family: var(--font-mono);
  color: var(--text-muted);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  font-weight: 700;
}

.nav-menu {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.nav-link {
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 0.88rem;
  font-weight: 600;
  transition: all 0.15s ease;
  position: relative;
}

.nav-link:hover, .nav-link.active {
  color: var(--saffron-600);
}

.nav-actions {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

/* Mobile Hamburger Toggle Button */
.mobile-toggle-btn {
  display: none;
  background: none;
  border: 1px solid var(--border-card);
  padding: 0.5rem;
  border-radius: var(--radius-sm);
  cursor: pointer;
  flex-direction: column;
  gap: 4px;
}

.mobile-toggle-btn span {
  display: block;
  width: 22px;
  height: 2px;
  background: var(--navy-authority);
  border-radius: 2px;
}

/* Mobile Navigation Drawer */
.mobile-nav-drawer {
  position: fixed;
  inset: 0;
  background: #FFFFFF;
  z-index: 2500;
  display: flex;
  flex-direction: column;
  transform: translateX(-100%);
  transition: transform 0.25s ease-in-out;
  padding: 1.5rem;
  overflow-y: auto;
}

.mobile-nav-drawer.active {
  transform: translateX(0);
}

.mobile-nav-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid var(--border-card);
  padding-bottom: 1rem;
  margin-bottom: 1.5rem;
}

.mobile-close-btn {
  background: none;
  border: none;
  font-size: 1.75rem;
  color: var(--text-main);
  cursor: pointer;
  line-height: 1;
}

.mobile-nav-links {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.mobile-link {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--navy-authority);
  text-decoration: none;
  padding: 0.75rem;
  border-radius: var(--radius-md);
  background: var(--bg-subtle);
}

.mobile-link:hover {
  background: var(--saffron-light);
  color: var(--saffron-700);
}

/* ==========================================================================
   Buttons & Interactive Elements
   ========================================================================== */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.65rem 1.25rem;
  font-size: 0.88rem;
  font-weight: 700;
  border-radius: var(--radius-md);
  cursor: pointer;
  border: 1px solid transparent;
  transition: all 0.2s ease;
  text-decoration: none;
  font-family: var(--font-main);
  min-height: 40px;
}

.btn-primary {
  background: linear-gradient(135deg, var(--saffron-500), var(--saffron-600));
  color: #FFFFFF;
  box-shadow: 0 2px 8px rgba(217, 119, 6, 0.25);
}

.btn-primary:hover {
  background: linear-gradient(135deg, #F59E0B, var(--saffron-700));
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(217, 119, 6, 0.35);
}

.btn-secondary {
  background: #FFFFFF;
  border: 1px solid var(--border-input);
  color: var(--navy-authority);
  box-shadow: var(--shadow-sm);
}

.btn-secondary:hover {
  background: var(--bg-subtle);
  border-color: var(--saffron-600);
  color: var(--saffron-700);
}

.btn-emerald {
  background: var(--emerald-600);
  color: #FFFFFF;
}

.btn-emerald:hover {
  background: #047857;
}

.btn-sm {
  padding: 0.45rem 0.85rem;
  font-size: 0.8rem;
  min-height: 36px;
}

.btn-lg {
  padding: 0.85rem 1.6rem;
  font-size: 1rem;
  min-height: 48px;
}

.btn-full {
  width: 100%;
}

/* ==========================================================================
   Hero Section (White / Light Institutional Theme)
   ========================================================================== */
.hero-terminal {
  padding: 4.5rem 0 3.5rem 0;
  background: linear-gradient(180deg, #FFFFFF 0%, #F1F5F9 100%);
  border-bottom: 1px solid var(--border-card);
  text-align: center;
}

.hero-seal-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  background: var(--saffron-light);
  border: 1px solid rgba(217, 119, 6, 0.3);
  padding: 0.4rem 1.1rem;
  border-radius: var(--radius-full);
  margin-bottom: 1.5rem;
  font-size: 0.78rem;
  font-weight: 800;
  color: var(--saffron-700);
  font-family: var(--font-mono);
  letter-spacing: 0.05em;
}

.hero-headline {
  font-size: clamp(1.9rem, 4.5vw, 3.2rem);
  line-height: 1.18;
  font-weight: 800;
  letter-spacing: -0.03em;
  color: var(--navy-authority);
  max-width: 980px;
  margin: 0 auto 1.25rem auto;
}

.highlight-saffron {
  background: linear-gradient(135deg, var(--saffron-600) 0%, #B45309 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-description {
  font-size: clamp(0.95rem, 1.8vw, 1.12rem);
  color: var(--text-secondary);
  max-width: 820px;
  margin: 0 auto 2.25rem auto;
  line-height: 1.65;
}

/* 4 Pillars Interactive Tab Switcher in Hero */
.hero-pillars-nav {
  display: inline-flex;
  background: #FFFFFF;
  border: 1px solid var(--border-card);
  padding: 0.35rem;
  border-radius: var(--radius-full);
  margin-bottom: 2.5rem;
  gap: 0.35rem;
  flex-wrap: wrap;
  justify-content: center;
  box-shadow: var(--shadow-card);
}

.pillar-tab-btn {
  background: transparent;
  border: none;
  color: var(--text-secondary);
  padding: 0.65rem 1.25rem;
  font-size: 0.88rem;
  font-weight: 700;
  border-radius: var(--radius-full);
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-main);
  min-height: 40px;
}

.pillar-tab-btn:hover {
  color: var(--navy-authority);
  background: var(--bg-subtle);
}

.pillar-tab-btn.active {
  background: var(--navy-authority);
  color: #FFFFFF;
  box-shadow: 0 2px 8px rgba(10, 25, 47, 0.2);
}

/* Hero Live Metric Bar */
.hero-metric-bar {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.25rem;
  background: #FFFFFF;
  border: 1px solid var(--border-card);
  border-radius: var(--radius-lg);
  padding: 1.5rem;
  box-shadow: var(--shadow-card);
  max-width: 1040px;
  margin: 0 auto;
}

.metric-cell {
  text-align: center;
  position: relative;
}

.metric-cell:not(:last-child)::after {
  content: "";
  position: absolute;
  right: -0.6rem;
  top: 15%;
  height: 70%;
  width: 1px;
  background: var(--border-card);
}

.metric-val {
  font-size: 1.8rem;
  font-weight: 800;
  font-family: var(--font-mono);
  color: var(--navy-authority);
}

.metric-lbl {
  font-size: 0.8rem;
  color: var(--text-muted);
  font-weight: 600;
  margin-top: 0.25rem;
}

/* ==========================================================================
   Section Headers (Authoritative Institutional Light)
   ========================================================================== */
.section-header-block {
  text-align: center;
  max-width: 780px;
  margin: 0 auto 3rem auto;
}

.section-tag {
  display: inline-block;
  padding: 0.35rem 0.95rem;
  background: var(--blue-light);
  border: 1px solid rgba(2, 132, 199, 0.25);
  color: var(--blue-sky);
  font-size: 0.74rem;
  font-weight: 800;
  border-radius: var(--radius-full);
  font-family: var(--font-mono);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 0.75rem;
}

.section-title {
  font-size: clamp(1.6rem, 3.5vw, 2.3rem);
  font-weight: 800;
  color: var(--navy-authority);
  letter-spacing: -0.02em;
  margin-bottom: 0.65rem;
}

.section-desc {
  font-size: 1rem;
  color: var(--text-secondary);
  line-height: 1.6;
}

/* ==========================================================================
   Pillar 1: Property Due Diligence & Scam Risk Radar
   ========================================================================== */
.radar-section {
  padding: 5rem 0;
  background: #FFFFFF;
  border-bottom: 1px solid var(--border-card);
}

.radar-terminal-card {
  background: #FFFFFF;
  border: 1px solid var(--border-card);
  border-radius: var(--radius-lg);
  padding: 2rem;
  box-shadow: var(--shadow-card);
}

.radar-search-box {
  display: grid;
  grid-template-columns: 1fr 1fr 1.5fr auto;
  gap: 1rem;
  background: var(--bg-subtle);
  border: 1px solid var(--border-card);
  padding: 1.25rem;
  border-radius: var(--radius-md);
  margin-bottom: 1.5rem;
  align-items: flex-end;
}

.form-field-radar label {
  display: block;
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--text-secondary);
  margin-bottom: 0.4rem;
  font-family: var(--font-mono);
}

.form-control-terminal {
  width: 100%;
  background: #FFFFFF;
  border: 1px solid var(--border-input);
  color: var(--navy-authority);
  padding: 0.65rem 0.85rem;
  border-radius: var(--radius-sm);
  font-size: 0.9rem;
  font-family: var(--font-main);
  outline: none;
  min-height: 42px;
}

.form-control-terminal:focus {
  border-color: var(--saffron-600);
  box-shadow: 0 0 0 3px rgba(217, 119, 6, 0.15);
}

.sample-queries-row {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

.sample-query-chip {
  background: #FFFFFF;
  border: 1px solid var(--border-input);
  color: var(--text-secondary);
  padding: 0.45rem 0.85rem;
  border-radius: var(--radius-full);
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s ease;
  min-height: 34px;
}

.sample-query-chip:hover {
  background: var(--bg-subtle);
  color: var(--saffron-700);
  border-color: var(--saffron-600);
}

/* Radar Audit Results Display */
.radar-results-grid {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 1.5rem;
}

.gauge-card {
  background: var(--bg-subtle);
  border: 1px solid var(--border-card);
  border-radius: var(--radius-md);
  padding: 1.75rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.risk-dial {
  width: 140px;
  height: 140px;
  border-radius: 50%;
  border: 10px solid #E2E8F0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-bottom: 1rem;
  background: #FFFFFF;
  box-shadow: var(--shadow-sm);
}

.risk-dial.safe {
  border-color: var(--emerald-500);
  box-shadow: 0 0 20px var(--emerald-light);
}

.risk-dial.danger {
  border-color: var(--crimson-500);
  box-shadow: 0 0 20px var(--crimson-light);
}

.dial-score {
  font-size: 2.6rem;
  font-weight: 800;
  font-family: var(--font-mono);
  line-height: 1;
  color: var(--navy-authority);
}

.dial-lbl {
  font-size: 0.7rem;
  text-transform: uppercase;
  color: var(--text-muted);
  font-family: var(--font-mono);
  font-weight: 700;
}

.risk-verdict-title {
  font-size: 1.15rem;
  font-weight: 800;
  margin-bottom: 0.35rem;
}

/* Checklist 5-Point Matrix */
.matrix-container {
  display: grid;
  grid-template-columns: 1fr;
  gap: 0.75rem;
}

.matrix-row {
  background: #FFFFFF;
  border: 1px solid var(--border-card);
  border-radius: var(--radius-md);
  padding: 1rem 1.25rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
}

.matrix-info h4 {
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--navy-authority);
  margin-bottom: 0.2rem;
}

.matrix-info p {
  font-size: 0.8rem;
  color: var(--text-muted);
}

.status-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.35rem 0.85rem;
  border-radius: var(--radius-full);
  font-size: 0.78rem;
  font-weight: 800;
  font-family: var(--font-mono);
  white-space: nowrap;
}

.status-badge.pass {
  background: #ECFDF5;
  color: #059669;
  border: 1px solid #A7F3D0;
}

.status-badge.fail {
  background: #FEF2F2;
  color: #DC2626;
  border: 1px solid #FECACA;
}

.status-badge.warn {
  background: #FFFBEB;
  color: #D97706;
  border: 1px solid #FDE68A;
}

/* ==========================================================================
   Pillar 2: Commercial Real Estate (CRE) & Pre-Leased Yield Terminal
   ========================================================================== */
.cre-section {
  padding: 5rem 0;
  background: var(--bg-body);
  border-bottom: 1px solid var(--border-card);
}

.cre-assets-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  margin-bottom: 3rem;
}

.cre-card {
  background: #FFFFFF;
  border: 1px solid var(--border-card);
  border-radius: var(--radius-lg);
  overflow: hidden;
  transition: all 0.2s ease;
  display: flex;
  flex-direction: column;
  box-shadow: var(--shadow-card);
}

.cre-card:hover {
  transform: translateY(-4px);
  border-color: var(--saffron-600);
  box-shadow: var(--shadow-hover);
}

.cre-card-header {
  padding: 1.25rem;
  border-bottom: 1px solid var(--border-card);
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  background: #FAFAFA;
}

.cre-tenant-pill {
  background: var(--saffron-light);
  border: 1px solid rgba(217, 119, 6, 0.3);
  color: var(--saffron-700);
  font-size: 0.72rem;
  font-weight: 800;
  padding: 0.25rem 0.65rem;
  border-radius: var(--radius-full);
  font-family: var(--font-mono);
}

.cre-asset-title {
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--navy-authority);
  margin-top: 0.5rem;
}

.cre-location {
  font-size: 0.8rem;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  gap: 0.35rem;
  margin-top: 0.2rem;
}

.cre-card-body {
  padding: 1.25rem;
  flex: 1;
}

.cre-metrics-strip {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.75rem;
  background: var(--bg-subtle);
  padding: 1rem;
  border-radius: var(--radius-md);
  margin-bottom: 1rem;
  border: 1px solid var(--border-card);
}

.cre-spec-item span {
  font-size: 0.72rem;
  color: var(--text-muted);
  display: block;
  font-weight: 600;
}

.cre-spec-item strong {
  font-size: 1.1rem;
  color: var(--navy-authority);
  font-family: var(--font-mono);
}

.cre-covenant-tag {
  font-size: 0.78rem;
  color: var(--emerald-600);
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  margin-bottom: 1.25rem;
}

/* CRE Interactive Simulator (Clean Light) */
.cre-simulator-card {
  background: #FFFFFF;
  border: 1px solid var(--border-card);
  border-radius: var(--radius-lg);
  padding: 2rem;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2.5rem;
  box-shadow: var(--shadow-card);
}

.sim-slider-box {
  margin-bottom: 1.5rem;
}

.sim-slider-hdr {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.sim-slider-hdr span {
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--text-secondary);
}

.sim-slider-hdr strong {
  font-family: var(--font-mono);
  color: var(--saffron-600);
  font-size: 1.15rem;
}

.custom-range {
  width: 100%;
  height: 6px;
  background: #CBD5E1;
  border-radius: var(--radius-full);
  outline: none;
  -webkit-appearance: none;
}

.custom-range::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--saffron-600);
  cursor: pointer;
  box-shadow: 0 0 8px rgba(217, 119, 6, 0.4);
}

.sim-outputs-panel {
  background: var(--bg-subtle);
  border: 1px solid var(--border-card);
  border-radius: var(--radius-md);
  padding: 1.75rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.sim-result-hero {
  border-bottom: 1px solid var(--border-card);
  padding-bottom: 1.25rem;
  margin-bottom: 1.25rem;
}

.sim-result-hero span {
  font-size: 0.8rem;
  color: var(--text-muted);
  display: block;
  font-weight: 700;
}

.sim-result-hero strong {
  font-size: 2.2rem;
  font-weight: 800;
  color: var(--emerald-600);
  font-family: var(--font-mono);
}

.sim-grid-stats {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.sim-stat-box span {
  font-size: 0.75rem;
  color: var(--text-muted);
  display: block;
  font-weight: 600;
}

.sim-stat-box strong {
  font-size: 1.1rem;
  color: var(--navy-authority);
  font-family: var(--font-mono);
}

/* ==========================================================================
   Pillar 3: Construction BoQ Cost Engine & Contractor Escrow
   ========================================================================== */
.boq-section {
  padding: 5rem 0;
  background: #FFFFFF;
  border-bottom: 1px solid var(--border-card);
}

.boq-workbench {
  background: #FFFFFF;
  border: 1px solid var(--border-card);
  border-radius: var(--radius-lg);
  padding: 2rem;
  box-shadow: var(--shadow-card);
}

.boq-inputs-row {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr 1fr;
  gap: 1.25rem;
  margin-bottom: 2rem;
  background: var(--bg-subtle);
  padding: 1.25rem;
  border-radius: var(--radius-md);
  border: 1px solid var(--border-card);
}

.boq-table-wrap {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  margin-bottom: 2rem;
  border: 1px solid var(--border-card);
  border-radius: var(--radius-md);
}

.boq-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
  font-size: 0.88rem;
  min-width: 650px;
}

.boq-table th {
  background: #F1F5F9;
  padding: 0.85rem 1rem;
  color: var(--navy-authority);
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 800;
  border-bottom: 1px solid var(--border-card);
}

.boq-table td {
  padding: 0.85rem 1rem;
  border-bottom: 1px solid var(--border-card);
  color: var(--text-secondary);
}

.boq-table tr:hover td {
  background: #F8FAFC;
}

.boq-total-card {
  background: linear-gradient(135deg, var(--navy-authority) 0%, #1E3E62 100%);
  color: #FFFFFF;
  border-radius: var(--radius-md);
  padding: 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
  box-shadow: var(--shadow-card);
}

.boq-total-col span {
  font-size: 0.8rem;
  color: #CBD5E1;
  display: block;
}

.boq-total-col strong {
  font-size: 2rem;
  color: var(--saffron-500);
  font-family: var(--font-mono);
}

/* Milestone Escrow Steps */
.escrow-flow-card {
  background: var(--bg-subtle);
  border: 1px solid var(--border-card);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  margin-top: 2rem;
}

.escrow-steps-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 1rem;
  margin-top: 1.25rem;
}

.escrow-step-item {
  background: #FFFFFF;
  border: 1px solid var(--border-card);
  padding: 1rem;
  border-radius: var(--radius-sm);
  text-align: center;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
}

.step-pct {
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--saffron-600);
  font-family: var(--font-mono);
}

.step-phase {
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--navy-authority);
  margin: 0.25rem 0;
}

.step-trigger {
  font-size: 0.72rem;
  color: var(--text-muted);
  line-height: 1.4;
}

/* ==========================================================================
   Pillar 4: VAHAN & Fleet Asset Compliance Terminal
   ========================================================================== */
.vahan-section {
  padding: 5rem 0;
  background: var(--bg-body);
  border-bottom: 1px solid var(--border-card);
}

.vahan-terminal-card {
  background: #FFFFFF;
  border: 1px solid var(--border-card);
  border-radius: var(--radius-lg);
  padding: 2rem;
  box-shadow: var(--shadow-card);
}

.vahan-lookup-bar {
  display: flex;
  gap: 0.75rem;
  max-width: 640px;
  margin: 0 auto 1.5rem auto;
  flex-wrap: wrap;
}

.plate-input-wrap {
  flex: 1;
  min-width: 240px;
  display: flex;
  align-items: center;
  background: #FFFFFF;
  border: 2px solid var(--border-input);
  border-radius: var(--radius-md);
  padding: 0 0.75rem;
}

.plate-input-wrap:focus-within {
  border-color: var(--navy-authority);
}

.ind-badge {
  background: #003366;
  color: #FFFFFF;
  font-size: 0.7rem;
  font-weight: 800;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  margin-right: 0.75rem;
  font-family: var(--font-mono);
}

.plate-input {
  flex: 1;
  background: transparent;
  border: none;
  color: var(--navy-authority);
  font-size: 1.2rem;
  font-weight: 800;
  font-family: var(--font-mono);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  outline: none;
  padding: 0.75rem 0;
  width: 100%;
}

.vahan-results-box {
  background: var(--bg-subtle);
  border: 1px solid var(--border-card);
  border-radius: var(--radius-md);
  padding: 1.75rem;
  margin-top: 1.5rem;
}

.vahan-vehicle-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid var(--border-card);
  padding-bottom: 1rem;
  margin-bottom: 1.25rem;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.vahan-grid-details {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.vahan-cell {
  background: #FFFFFF;
  padding: 0.85rem;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-card);
}

.vahan-cell span {
  font-size: 0.72rem;
  color: var(--text-muted);
  display: block;
  font-family: var(--font-mono);
  font-weight: 700;
}

.vahan-cell strong {
  font-size: 0.95rem;
  color: var(--navy-authority);
}

/* Challan Table */
.challan-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.85rem;
  margin-top: 1rem;
  background: #FFFFFF;
}

.challan-table th {
  background: #F1F5F9;
  padding: 0.65rem 0.85rem;
  color: var(--text-secondary);
  text-align: left;
  border-bottom: 1px solid var(--border-card);
}

.challan-table td {
  padding: 0.65rem 0.85rem;
  border-bottom: 1px solid var(--border-card);
  color: var(--text-secondary);
}

/* ==========================================================================
   Statutory Pricing & Plans (Light Theme)
   ========================================================================== */
.pricing-terminal-section {
  padding: 5rem 0;
  background: #FFFFFF;
  border-bottom: 1px solid var(--border-card);
}

.pricing-cards-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.25rem;
}

.pricing-card-terminal {
  background: #FFFFFF;
  border: 1px solid var(--border-card);
  border-radius: var(--radius-lg);
  padding: 1.75rem;
  display: flex;
  flex-direction: column;
  position: relative;
  transition: all 0.2s ease;
  box-shadow: var(--shadow-sm);
}

.pricing-card-terminal:hover {
  transform: translateY(-4px);
  border-color: var(--saffron-600);
  box-shadow: var(--shadow-hover);
}

.pricing-card-terminal.featured {
  border: 2px solid var(--saffron-600);
  background: #FFFFFF;
  box-shadow: 0 8px 30px rgba(217, 119, 6, 0.12);
}

.featured-pill {
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  background: var(--saffron-600);
  color: #FFFFFF;
  font-size: 0.7rem;
  font-weight: 800;
  padding: 0.2rem 0.75rem;
  border-radius: var(--radius-full);
  font-family: var(--font-mono);
}

.p-tier-name {
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--navy-authority);
  margin-bottom: 0.35rem;
}

.p-tier-desc {
  font-size: 0.8rem;
  color: var(--text-muted);
  margin-bottom: 1.25rem;
  min-height: 40px;
}

.p-price-block {
  margin-bottom: 1.25rem;
  border-bottom: 1px solid var(--border-card);
  padding-bottom: 1rem;
}

.p-price-block .amt {
  font-size: 2rem;
  font-weight: 800;
  color: var(--navy-authority);
  font-family: var(--font-mono);
}

.p-price-block .dur {
  font-size: 0.8rem;
  color: var(--text-muted);
}

.p-features-list {
  list-style: none;
  margin-bottom: 1.75rem;
  flex: 1;
}

.p-features-list li {
  font-size: 0.82rem;
  color: var(--text-secondary);
  margin-bottom: 0.65rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.p-features-list svg {
  color: var(--emerald-600);
  flex-shrink: 0;
}

/* ==========================================================================
   Regulatory Framework Section (Light Theme)
   ========================================================================== */
.compliance-section {
  padding: 5rem 0;
  background: var(--bg-body);
  border-bottom: 1px solid var(--border-card);
}

.compliance-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.comp-card {
  background: #FFFFFF;
  border: 1px solid var(--border-card);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  box-shadow: var(--shadow-sm);
}

.comp-act-badge {
  font-size: 0.72rem;
  font-family: var(--font-mono);
  color: var(--saffron-700);
  font-weight: 800;
  display: block;
  margin-bottom: 0.4rem;
}

.comp-title {
  font-size: 1.05rem;
  font-weight: 800;
  color: var(--navy-authority);
  margin-bottom: 0.4rem;
}

.comp-desc {
  font-size: 0.85rem;
  color: var(--text-secondary);
  line-height: 1.5;
}

/* ==========================================================================
   Footer (Authoritative Deep Navy Grounding)
   ========================================================================== */
.footer-terminal {
  background: var(--navy-authority);
  padding: 4rem 0 2rem 0;
  border-top: 1px solid #1E293B;
  color: #94A3B8;
}

.footer-top {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1.5fr;
  gap: 2.5rem;
  margin-bottom: 3rem;
}

.footer-col h4 {
  font-size: 0.95rem;
  font-weight: 800;
  color: #FFFFFF;
  margin-bottom: 1rem;
}

.footer-col ul {
  list-style: none;
}

.footer-col li {
  margin-bottom: 0.5rem;
}

.footer-col a {
  color: #94A3B8;
  text-decoration: none;
  font-size: 0.85rem;
  transition: color 0.15s ease;
}

.footer-col a:hover {
  color: var(--saffron-500);
}

.footer-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  padding-top: 1.5rem;
  font-size: 0.8rem;
  flex-wrap: wrap;
  gap: 1rem;
}

/* ==========================================================================
   Modals (Official Certificates & Dossiers)
   ========================================================================== */
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(15, 23, 42, 0.65);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2000;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s ease;
  padding: 1rem;
}

.modal-backdrop.active {
  opacity: 1;
  pointer-events: auto;
}

.modal-box {
  background: #FFFFFF;
  border: 1px solid var(--border-card);
  border-radius: var(--radius-lg);
  width: 100%;
  max-width: 680px;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
  box-shadow: var(--shadow-modal);
  padding: 2rem;
  color: var(--text-main);
}

.modal-box.modal-lg {
  max-width: 860px;
}

.modal-close-btn {
  position: absolute;
  top: 1.25rem;
  right: 1.25rem;
  background: var(--bg-subtle);
  border: 1px solid var(--border-card);
  color: var(--text-muted);
  width: 32px;
  height: 32px;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  line-height: 1;
}

.modal-close-btn:hover {
  color: var(--text-main);
  background: #E2E8F0;
}

/* Official Document Style (Section 65B Certificate) */
.cert-paper {
  background: #FFFFFF;
  color: #0F172A;
  border-radius: 8px;
  padding: 1.75rem;
  border: 1px solid var(--border-card);
}

.cert-header {
  border-bottom: 2px solid #0F172A;
  padding-bottom: 1rem;
  margin-bottom: 1.25rem;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.cert-emblem-text {
  font-size: 0.75rem;
  font-weight: 800;
  color: #1E3E62;
  text-transform: uppercase;
}

.cert-title {
  font-size: 1.35rem;
  font-weight: 800;
  color: #0F172A;
}

.cert-meta-row {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  color: #475569;
}

.cert-body-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-bottom: 1.5rem;
  background: #F8FAFC;
  padding: 1rem;
  border-radius: 6px;
  border: 1px solid #E2E8F0;
}

.cert-field span {
  font-size: 0.72rem;
  color: #64748B;
  display: block;
}

.cert-field strong {
  font-size: 0.95rem;
  color: #0F172A;
}

.cert-verdict-box {
  padding: 1rem;
  border-radius: 6px;
  margin-bottom: 1.5rem;
  font-size: 0.88rem;
  line-height: 1.5;
}

.cert-verdict-box.safe {
  background: #ECFDF5;
  border: 1px solid #A7F3D0;
  color: #065F46;
}

.cert-verdict-box.risk {
  background: #FEF2F2;
  border: 1px solid #FECACA;
  color: #991B1B;
}

.cert-sign-strip {
  border-top: 1px dashed #CBD5E1;
  padding-top: 1.25rem;
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  font-size: 0.78rem;
  color: #64748B;
  flex-wrap: wrap;
  gap: 1rem;
}

/* ==========================================================================
   Toast Notification System
   ========================================================================== */
.toast-container {
  position: fixed;
  bottom: 1.5rem;
  right: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  z-index: 3000;
  pointer-events: none;
  max-width: calc(100vw - 3rem);
}

.toast-item {
  background: #FFFFFF;
  border: 1px solid var(--border-card);
  color: var(--navy-authority);
  padding: 0.85rem 1.25rem;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-modal);
  font-size: 0.88rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  pointer-events: auto;
  animation: slideInToast 0.25s ease forwards;
  min-width: 280px;
}

.toast-emerald {
  border-left: 4px solid var(--emerald-600);
}

.toast-saffron {
  border-left: 4px solid var(--saffron-600);
}

.toast-crimson {
  border-left: 4px solid var(--crimson-600);
}

.toast-close {
  background: none;
  border: none;
  color: var(--text-muted);
  cursor: pointer;
  margin-left: auto;
  font-size: 1.2rem;
}

@keyframes slideInToast {
  from { transform: translateX(100%); opacity: 0; }
  to { transform: translateX(0); opacity: 1; }
}

/* ==========================================================================
   MOBILE & RESPONSIVE COMPATIBILITY (Up to 1024px & 768px & 480px)
   ========================================================================== */
@media (max-width: 1024px) {
  .cre-assets-grid { grid-template-columns: repeat(2, 1fr); }
  .pricing-cards-grid { grid-template-columns: repeat(2, 1fr); }
  .compliance-grid { grid-template-columns: repeat(2, 1fr); }
  .radar-results-grid { grid-template-columns: 1fr; }
  .cre-simulator-card { grid-template-columns: 1fr; }
  .hero-metric-bar { grid-template-columns: repeat(2, 1fr); }
  .footer-top { grid-template-columns: 1fr 1fr; }
}

@media (max-width: 768px) {
  .national-ticker-bar { display: none; }
  .nav-menu { display: none; }
  .mobile-toggle-btn { display: flex; }
  
  .hero-terminal { padding: 3rem 0 2.5rem 0; }
  .hero-seal-badge { font-size: 0.72rem; padding: 0.35rem 0.75rem; }
  .hero-description { font-size: 0.95rem; }

  .hero-pillars-nav {
    border-radius: var(--radius-lg);
    width: 100%;
    padding: 0.5rem;
  }
  .pillar-tab-btn {
    width: 100%;
    justify-content: center;
    border-radius: var(--radius-md);
  }

  .hero-metric-bar {
    grid-template-columns: 1fr 1fr;
    gap: 0.75rem;
    padding: 1rem;
  }
  .metric-cell:not(:last-child)::after { display: none; }
  .metric-val { font-size: 1.4rem; }

  /* Pillar 1 */
  .radar-search-box { grid-template-columns: 1fr; }
  .radar-terminal-card { padding: 1.25rem; }
  .matrix-row { flex-direction: column; align-items: flex-start; gap: 0.5rem; }
  .cert-body-grid { grid-template-columns: 1fr; }

  /* Pillar 2 */
  .cre-assets-grid { grid-template-columns: 1fr; }
  .cre-simulator-card { padding: 1.25rem; }

  /* Pillar 3 */
  .boq-workbench { padding: 1.25rem; }
  .boq-inputs-row { grid-template-columns: 1fr; }
  .escrow-steps-grid { grid-template-columns: 1fr; }
  .boq-total-card { flex-direction: column; align-items: flex-start; }

  /* Pillar 4 */
  .vahan-terminal-card { padding: 1.25rem; }
  .vahan-lookup-bar { flex-direction: column; }
  .vahan-lookup-bar .btn { width: 100%; }
  .vahan-grid-details { grid-template-columns: 1fr 1fr; }
  .vahan-results-box { padding: 1.25rem; }

  /* Pricing & Compliance */
  .pricing-cards-grid { grid-template-columns: 1fr; }
  .compliance-grid { grid-template-columns: 1fr; }
  .footer-top { grid-template-columns: 1fr; gap: 1.5rem; }
  .footer-bottom { flex-direction: column; text-align: center; }

  .modal-box { padding: 1.25rem; max-width: 95vw; }
}

@media (max-width: 480px) {
  .vahan-grid-details { grid-template-columns: 1fr; }
  .hero-metric-bar { grid-template-columns: 1fr; }
  .sim-grid-stats { grid-template-columns: 1fr; }
}
"""

with open('/Users/chetanbisariya/.gemini/antigravity-ide/scratch/exainfra-in/style.css', 'w') as f:
    f.write(css_content)

print(f"Generated clean white & mobile style.css ({len(css_content)} bytes) successfully.")
