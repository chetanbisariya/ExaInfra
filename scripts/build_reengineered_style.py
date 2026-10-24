css_content = """/* ==========================================================================
   ExaInfra.in - National Real Estate, Commercial Yield & Asset Terminal
   Aesthetic: Sovereign-grade Indian Institutional Fintech / Legaltech
   Inspired by India Stack, RERA, MCA21 & Institutional Asset Terminals
   ========================================================================== */

:root {
  /* Sovereign & Institutional Palette */
  --navy-deep: #071326;
  --navy-dark: #0D1F38;
  --navy-surface: #132A4A;
  --navy-card: #183359;
  --navy-border: #234675;

  --saffron-500: #F59E0B;
  --saffron-600: #D97706;
  --saffron-glow: rgba(245, 158, 11, 0.25);

  --emerald-500: #10B981;
  --emerald-600: #059669;
  --emerald-glow: rgba(16, 185, 129, 0.2);

  --crimson-500: #EF4444;
  --crimson-600: #DC2626;

  --blue-sky: #38BDF8;
  --blue-accent: #0284C7;

  /* Neutrals */
  --bg-dark: #071326;
  --bg-card-light: #FFFFFF;
  --bg-surface-light: #F8FAFC;
  --bg-elevated: #F1F5F9;

  --text-dark: #0F172A;
  --text-sub: #475569;
  --text-light: #94A3B8;
  --text-white: #FFFFFF;

  --border-light: #E2E8F0;
  --border-card: #CBD5E1;

  --font-main: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --radius-full: 9999px;

  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.08);
  --shadow-md: 0 4px 16px rgba(7, 19, 38, 0.12);
  --shadow-lg: 0 12px 32px rgba(7, 19, 38, 0.2);
  --shadow-glow: 0 0 25px rgba(245, 158, 11, 0.2);
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: var(--font-main);
  background: var(--navy-deep);
  color: var(--text-white);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}

/* Container */
.container {
  width: 100%;
  max-width: 1240px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

/* ==========================================================================
   Top National Statutory Ticker Bar
   ========================================================================== */
.national-ticker-bar {
  background: #040B17;
  border-bottom: 1px solid #1A2E4C;
  color: #94A3B8;
  font-size: 0.76rem;
  padding: 0.45rem 0;
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
   Main Navigation Header
   ========================================================================== */
.navbar-terminal {
  background: rgba(13, 31, 56, 0.95);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--navy-border);
  position: sticky;
  top: 0;
  z-index: 1000;
  padding: 0.75rem 0;
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
  background: linear-gradient(135deg, var(--navy-card), #0A1B33);
  border: 1px solid var(--saffron-500);
  border-radius: var(--radius-md);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--saffron-500);
  box-shadow: 0 0 15px var(--saffron-glow);
}

.brand-text-col {
  display: flex;
  flex-direction: column;
}

.brand-title {
  font-size: 1.25rem;
  font-weight: 800;
  color: #FFFFFF;
  letter-spacing: -0.02em;
}

.brand-title span {
  color: var(--saffron-500);
}

.brand-sub {
  font-size: 0.68rem;
  font-family: var(--font-mono);
  color: #94A3B8;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.nav-menu {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.nav-link {
  color: #CBD5E1;
  text-decoration: none;
  font-size: 0.88rem;
  font-weight: 600;
  transition: color 0.15s ease;
  position: relative;
}

.nav-link:hover, .nav-link.active {
  color: var(--saffron-500);
}

.nav-actions {
  display: flex;
  align-items: center;
  gap: 0.75rem;
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
}

.btn-primary {
  background: linear-gradient(135deg, var(--saffron-500), var(--saffron-600));
  color: #071326;
  box-shadow: 0 2px 10px rgba(245, 158, 11, 0.3);
}

.btn-primary:hover {
  background: linear-gradient(135deg, #FBBF24, var(--saffron-500));
  transform: translateY(-1px);
  box-shadow: 0 4px 14px rgba(245, 158, 11, 0.4);
}

.btn-secondary {
  background: var(--navy-card);
  border-color: var(--navy-border);
  color: #FFFFFF;
}

.btn-secondary:hover {
  background: var(--navy-surface);
  border-color: #38BDF8;
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
}

.btn-lg {
  padding: 0.85rem 1.6rem;
  font-size: 1rem;
}

.btn-full {
  width: 100%;
}

/* ==========================================================================
   Hero Section: Institutional Asset Terminal
   ========================================================================== */
.hero-terminal {
  padding: 4.5rem 0 3.5rem 0;
  background: radial-gradient(circle at 50% 20%, #11284A 0%, var(--navy-deep) 70%);
  border-bottom: 1px solid var(--navy-border);
  text-align: center;
}

.hero-seal-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  background: rgba(245, 158, 11, 0.12);
  border: 1px solid rgba(245, 158, 11, 0.35);
  padding: 0.35rem 1rem;
  border-radius: var(--radius-full);
  margin-bottom: 1.5rem;
  font-size: 0.78rem;
  font-weight: 800;
  color: var(--saffron-500);
  font-family: var(--font-mono);
  letter-spacing: 0.05em;
}

.hero-headline {
  font-size: 3.2rem;
  line-height: 1.15;
  font-weight: 800;
  letter-spacing: -0.03em;
  max-width: 980px;
  margin: 0 auto 1.25rem auto;
}

.highlight-saffron {
  background: linear-gradient(135deg, #FCD34D 0%, #F59E0B 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-description {
  font-size: 1.1rem;
  color: #94A3B8;
  max-width: 820px;
  margin: 0 auto 2.25rem auto;
  line-height: 1.6;
}

/* 4 Pillars Interactive Tab Switcher in Hero */
.hero-pillars-nav {
  display: inline-flex;
  background: rgba(13, 31, 56, 0.8);
  border: 1px solid var(--navy-border);
  padding: 0.35rem;
  border-radius: var(--radius-full);
  margin-bottom: 2.5rem;
  gap: 0.25rem;
  flex-wrap: wrap;
  justify-content: center;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
}

.pillar-tab-btn {
  background: transparent;
  border: none;
  color: #CBD5E1;
  padding: 0.6rem 1.25rem;
  font-size: 0.85rem;
  font-weight: 700;
  border-radius: var(--radius-full);
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-main);
}

.pillar-tab-btn:hover {
  color: #FFFFFF;
  background: rgba(255, 255, 255, 0.06);
}

.pillar-tab-btn.active {
  background: var(--saffron-500);
  color: #071326;
  box-shadow: 0 2px 8px rgba(245, 158, 11, 0.3);
}

/* Hero Live Metric Bar */
.hero-metric-bar {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.25rem;
  background: rgba(19, 42, 74, 0.6);
  border: 1px solid var(--navy-border);
  border-radius: var(--radius-lg);
  padding: 1.5rem;
  backdrop-filter: blur(8px);
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
  background: rgba(255, 255, 255, 0.1);
}

.metric-val {
  font-size: 1.8rem;
  font-weight: 800;
  font-family: var(--font-mono);
  color: #FFFFFF;
}

.metric-lbl {
  font-size: 0.8rem;
  color: #94A3B8;
  font-weight: 600;
  margin-top: 0.25rem;
}

/* ==========================================================================
   Section Headers (Authoritative Institutional)
   ========================================================================== */
.section-header-block {
  text-align: center;
  max-width: 780px;
  margin: 0 auto 3rem auto;
}

.section-tag {
  display: inline-block;
  padding: 0.3rem 0.85rem;
  background: rgba(56, 189, 248, 0.12);
  border: 1px solid rgba(56, 189, 248, 0.3);
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
  font-size: 2.25rem;
  font-weight: 800;
  color: #FFFFFF;
  letter-spacing: -0.02em;
  margin-bottom: 0.65rem;
}

.section-desc {
  font-size: 1rem;
  color: #94A3B8;
  line-height: 1.6;
}

/* ==========================================================================
   Pillar 1: Property Due Diligence & Scam Risk Radar
   ========================================================================== */
.radar-section {
  padding: 5rem 0;
  background: #09182E;
  border-bottom: 1px solid var(--navy-border);
}

.radar-terminal-card {
  background: var(--navy-dark);
  border: 1px solid var(--navy-border);
  border-radius: var(--radius-lg);
  padding: 2rem;
  box-shadow: var(--shadow-lg);
}

.radar-search-box {
  display: grid;
  grid-template-columns: 1fr 1fr 1.5fr auto;
  gap: 1rem;
  background: #081528;
  border: 1px solid var(--navy-surface);
  padding: 1.25rem;
  border-radius: var(--radius-md);
  margin-bottom: 1.5rem;
  align-items: flex-end;
}

.form-field-radar label {
  display: block;
  font-size: 0.78rem;
  font-weight: 700;
  color: #94A3B8;
  margin-bottom: 0.4rem;
  font-family: var(--font-mono);
}

.form-control-terminal {
  width: 100%;
  background: #0D1F38;
  border: 1px solid var(--navy-border);
  color: #FFFFFF;
  padding: 0.65rem 0.85rem;
  border-radius: var(--radius-sm);
  font-size: 0.9rem;
  font-family: var(--font-main);
  outline: none;
}

.form-control-terminal:focus {
  border-color: var(--saffron-500);
}

.sample-queries-row {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

.sample-query-chip {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--navy-border);
  color: #CBD5E1;
  padding: 0.35rem 0.75rem;
  border-radius: var(--radius-full);
  font-size: 0.78rem;
  cursor: pointer;
  transition: all 0.15s ease;
}

.sample-query-chip:hover {
  background: var(--navy-card);
  color: var(--saffron-500);
  border-color: var(--saffron-500);
}

/* Radar Audit Results Display */
.radar-results-grid {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 1.5rem;
}

.gauge-card {
  background: #081528;
  border: 1px solid var(--navy-border);
  border-radius: var(--radius-md);
  padding: 1.75rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.risk-dial {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  border: 10px solid #1E3E62;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-bottom: 1rem;
  position: relative;
}

.risk-dial.safe {
  border-color: var(--emerald-500);
  box-shadow: 0 0 20px var(--emerald-glow);
}

.risk-dial.danger {
  border-color: var(--crimson-500);
  box-shadow: 0 0 20px rgba(239, 68, 68, 0.3);
}

.dial-score {
  font-size: 2.8rem;
  font-weight: 800;
  font-family: var(--font-mono);
  line-height: 1;
}

.dial-lbl {
  font-size: 0.7rem;
  text-transform: uppercase;
  color: #94A3B8;
  font-family: var(--font-mono);
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
  background: #081528;
  border: 1px solid var(--navy-border);
  border-radius: var(--radius-md);
  padding: 1rem 1.25rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.matrix-info h4 {
  font-size: 0.95rem;
  font-weight: 700;
  color: #FFFFFF;
  margin-bottom: 0.2rem;
}

.matrix-info p {
  font-size: 0.8rem;
  color: #94A3B8;
}

.status-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.3rem 0.75rem;
  border-radius: var(--radius-full);
  font-size: 0.75rem;
  font-weight: 800;
  font-family: var(--font-mono);
  white-space: nowrap;
}

.status-badge.pass {
  background: rgba(16, 185, 129, 0.15);
  color: #34D399;
  border: 1px solid rgba(16, 185, 129, 0.3);
}

.status-badge.fail {
  background: rgba(239, 68, 68, 0.15);
  color: #F87171;
  border: 1px solid rgba(239, 68, 68, 0.3);
}

.status-badge.warn {
  background: rgba(245, 158, 11, 0.15);
  color: #FBBF24;
  border: 1px solid rgba(245, 158, 11, 0.3);
}

/* ==========================================================================
   Pillar 2: Commercial Real Estate (CRE) & Pre-Leased Yield Terminal
   ========================================================================== */
.cre-section {
  padding: 5rem 0;
  background: #071326;
  border-bottom: 1px solid var(--navy-border);
}

.cre-assets-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  margin-bottom: 3rem;
}

.cre-card {
  background: var(--navy-dark);
  border: 1px solid var(--navy-border);
  border-radius: var(--radius-lg);
  overflow: hidden;
  transition: all 0.2s ease;
  display: flex;
  flex-direction: column;
}

.cre-card:hover {
  transform: translateY(-4px);
  border-color: var(--saffron-500);
  box-shadow: var(--shadow-lg);
}

.cre-card-header {
  padding: 1.25rem;
  border-bottom: 1px solid var(--navy-border);
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.cre-tenant-pill {
  background: rgba(245, 158, 11, 0.15);
  border: 1px solid rgba(245, 158, 11, 0.3);
  color: var(--saffron-500);
  font-size: 0.72rem;
  font-weight: 800;
  padding: 0.25rem 0.6rem;
  border-radius: var(--radius-full);
  font-family: var(--font-mono);
}

.cre-asset-title {
  font-size: 1.15rem;
  font-weight: 800;
  color: #FFFFFF;
  margin-top: 0.5rem;
}

.cre-location {
  font-size: 0.8rem;
  color: #94A3B8;
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
  background: #081528;
  padding: 1rem;
  border-radius: var(--radius-md);
  margin-bottom: 1rem;
}

.cre-spec-item span {
  font-size: 0.72rem;
  color: #94A3B8;
  display: block;
}

.cre-spec-item strong {
  font-size: 1.1rem;
  color: #FFFFFF;
  font-family: var(--font-mono);
}

.cre-covenant-tag {
  font-size: 0.75rem;
  color: var(--emerald-500);
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  margin-bottom: 1rem;
}

/* CRE Interactive Simulator */
.cre-simulator-card {
  background: var(--navy-dark);
  border: 1px solid var(--navy-border);
  border-radius: var(--radius-lg);
  padding: 2rem;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2.5rem;
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
  color: #CBD5E1;
}

.sim-slider-hdr strong {
  font-family: var(--font-mono);
  color: var(--saffron-500);
  font-size: 1.1rem;
}

.custom-range {
  width: 100%;
  height: 6px;
  background: #1E3E62;
  border-radius: var(--radius-full);
  outline: none;
  -webkit-appearance: none;
}

.custom-range::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: var(--saffron-500);
  cursor: pointer;
  box-shadow: 0 0 8px var(--saffron-500);
}

.sim-outputs-panel {
  background: #081528;
  border: 1px solid var(--navy-border);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.sim-result-hero {
  border-bottom: 1px solid var(--navy-border);
  padding-bottom: 1.25rem;
  margin-bottom: 1.25rem;
}

.sim-result-hero span {
  font-size: 0.8rem;
  color: #94A3B8;
  display: block;
}

.sim-result-hero strong {
  font-size: 2.2rem;
  font-weight: 800;
  color: var(--emerald-500);
  font-family: var(--font-mono);
}

.sim-grid-stats {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.sim-stat-box span {
  font-size: 0.75rem;
  color: #94A3B8;
  display: block;
}

.sim-stat-box strong {
  font-size: 1.1rem;
  color: #FFFFFF;
  font-family: var(--font-mono);
}

/* ==========================================================================
   Pillar 3: Construction BoQ Cost Engine & Contractor Escrow
   ========================================================================== */
.boq-section {
  padding: 5rem 0;
  background: #09182E;
  border-bottom: 1px solid var(--navy-border);
}

.boq-workbench {
  background: var(--navy-dark);
  border: 1px solid var(--navy-border);
  border-radius: var(--radius-lg);
  padding: 2rem;
}

.boq-inputs-row {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr 1fr;
  gap: 1.25rem;
  margin-bottom: 2rem;
  background: #081528;
  padding: 1.25rem;
  border-radius: var(--radius-md);
  border: 1px solid var(--navy-border);
}

.boq-table-wrap {
  overflow-x: auto;
  margin-bottom: 2rem;
}

.boq-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
  font-size: 0.88rem;
}

.boq-table th {
  background: #0B1B33;
  padding: 0.85rem 1rem;
  color: #94A3B8;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  border-bottom: 1px solid var(--navy-border);
}

.boq-table td {
  padding: 0.85rem 1rem;
  border-bottom: 1px solid rgba(35, 70, 117, 0.4);
  color: #CBD5E1;
}

.boq-table tr:hover td {
  background: rgba(255, 255, 255, 0.02);
}

.boq-total-card {
  background: linear-gradient(135deg, #102A4C, #091930);
  border: 1px solid var(--saffron-500);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
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
  background: #081528;
  border: 1px solid var(--navy-border);
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
  background: var(--navy-dark);
  border: 1px solid var(--navy-border);
  padding: 1rem;
  border-radius: var(--radius-sm);
  text-align: center;
}

.step-pct {
  font-size: 1.25rem;
  font-weight: 800;
  color: var(--saffron-500);
  font-family: var(--font-mono);
}

.step-phase {
  font-size: 0.8rem;
  font-weight: 700;
  color: #FFFFFF;
  margin: 0.25rem 0;
}

.step-trigger {
  font-size: 0.72rem;
  color: #94A3B8;
  line-height: 1.4;
}

/* ==========================================================================
   Pillar 4: VAHAN & Fleet Asset Compliance Terminal
   ========================================================================== */
.vahan-section {
  padding: 5rem 0;
  background: #071326;
  border-bottom: 1px solid var(--navy-border);
}

.vahan-terminal-card {
  background: var(--navy-dark);
  border: 1px solid var(--navy-border);
  border-radius: var(--radius-lg);
  padding: 2rem;
}

.vahan-lookup-bar {
  display: flex;
  gap: 0.75rem;
  max-width: 640px;
  margin: 0 auto 1.5rem auto;
}

.plate-input-wrap {
  flex: 1;
  display: flex;
  align-items: center;
  background: #081528;
  border: 2px solid var(--navy-border);
  border-radius: var(--radius-md);
  padding: 0 0.75rem;
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
  color: #FFFFFF;
  font-size: 1.25rem;
  font-weight: 800;
  font-family: var(--font-mono);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  outline: none;
  padding: 0.75rem 0;
}

.vahan-results-box {
  background: #081528;
  border: 1px solid var(--navy-border);
  border-radius: var(--radius-md);
  padding: 1.75rem;
  margin-top: 1.5rem;
}

.vahan-vehicle-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid var(--navy-border);
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

.vahan-cell span {
  font-size: 0.72rem;
  color: #94A3B8;
  display: block;
  font-family: var(--font-mono);
}

.vahan-cell strong {
  font-size: 0.95rem;
  color: #FFFFFF;
}

/* Challan Table */
.challan-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.85rem;
  margin-top: 1rem;
}

.challan-table th {
  background: #0D1F38;
  padding: 0.65rem 0.85rem;
  color: #94A3B8;
  text-align: left;
}

.challan-table td {
  padding: 0.65rem 0.85rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

/* ==========================================================================
   Statutory Pricing & Plans
   ========================================================================== */
.pricing-terminal-section {
  padding: 5rem 0;
  background: #09182E;
  border-bottom: 1px solid var(--navy-border);
}

.pricing-cards-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1.25rem;
}

.pricing-card-terminal {
  background: var(--navy-dark);
  border: 1px solid var(--navy-border);
  border-radius: var(--radius-lg);
  padding: 1.75rem;
  display: flex;
  flex-direction: column;
  position: relative;
  transition: all 0.2s ease;
}

.pricing-card-terminal:hover {
  transform: translateY(-4px);
  border-color: var(--saffron-500);
}

.pricing-card-terminal.featured {
  border-color: var(--saffron-500);
  background: linear-gradient(180deg, #122B4C 0%, var(--navy-dark) 100%);
  box-shadow: 0 0 25px rgba(245, 158, 11, 0.15);
}

.featured-pill {
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  background: var(--saffron-500);
  color: #071326;
  font-size: 0.7rem;
  font-weight: 800;
  padding: 0.2rem 0.75rem;
  border-radius: var(--radius-full);
  font-family: var(--font-mono);
}

.p-tier-name {
  font-size: 1.25rem;
  font-weight: 800;
  color: #FFFFFF;
  margin-bottom: 0.35rem;
}

.p-tier-desc {
  font-size: 0.8rem;
  color: #94A3B8;
  margin-bottom: 1.25rem;
  min-height: 40px;
}

.p-price-block {
  margin-bottom: 1.25rem;
  border-bottom: 1px solid var(--navy-border);
  padding-bottom: 1rem;
}

.p-price-block .amt {
  font-size: 2rem;
  font-weight: 800;
  color: #FFFFFF;
  font-family: var(--font-mono);
}

.p-price-block .dur {
  font-size: 0.8rem;
  color: #94A3B8;
}

.p-features-list {
  list-style: none;
  margin-bottom: 1.75rem;
  flex: 1;
}

.p-features-list li {
  font-size: 0.82rem;
  color: #CBD5E1;
  margin-bottom: 0.65rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.p-features-list svg {
  color: var(--emerald-500);
  flex-shrink: 0;
}

/* ==========================================================================
   Regulatory Framework Section (RERA, IT Act, VAHAN, NBC)
   ========================================================================== */
.compliance-section {
  padding: 5rem 0;
  background: #071326;
  border-bottom: 1px solid var(--navy-border);
}

.compliance-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
}

.comp-card {
  background: var(--navy-dark);
  border: 1px solid var(--navy-border);
  border-radius: var(--radius-md);
  padding: 1.5rem;
}

.comp-act-badge {
  font-size: 0.72rem;
  font-family: var(--font-mono);
  color: var(--saffron-500);
  font-weight: 800;
  display: block;
  margin-bottom: 0.4rem;
}

.comp-title {
  font-size: 1.05rem;
  font-weight: 800;
  color: #FFFFFF;
  margin-bottom: 0.4rem;
}

.comp-desc {
  font-size: 0.85rem;
  color: #94A3B8;
  line-height: 1.5;
}

/* ==========================================================================
   Footer
   ========================================================================== */
.footer-terminal {
  background: #040B17;
  padding: 4rem 0 2rem 0;
  border-top: 1px solid var(--navy-border);
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
  background: rgba(4, 11, 23, 0.85);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2000;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s ease;
  padding: 1.5rem;
}

.modal-backdrop.active {
  opacity: 1;
  pointer-events: auto;
}

.modal-box {
  background: var(--navy-dark);
  border: 1px solid var(--navy-border);
  border-radius: var(--radius-lg);
  width: 100%;
  max-width: 680px;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
  padding: 2rem;
  color: #FFFFFF;
}

.modal-box.modal-lg {
  max-width: 860px;
}

.modal-close-btn {
  position: absolute;
  top: 1.25rem;
  right: 1.25rem;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid var(--navy-border);
  color: #94A3B8;
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
  color: #FFFFFF;
  background: rgba(255, 255, 255, 0.15);
}

/* Official Document Style (Section 65B Certificate) */
.cert-paper {
  background: #FFFFFF;
  color: #0F172A;
  border-radius: 8px;
  padding: 2rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  position: relative;
}

.cert-header {
  border-bottom: 2px solid #0F172A;
  padding-bottom: 1rem;
  margin-bottom: 1.25rem;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.cert-emblem-text {
  font-size: 0.75rem;
  font-weight: 800;
  color: #1E3E62;
  text-transform: uppercase;
}

.cert-title {
  font-size: 1.4rem;
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
}

/* ==========================================================================
   Toast Notification System
   ========================================================================== */
.toast-container {
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  z-index: 3000;
  pointer-events: none;
}

.toast-item {
  background: var(--navy-card);
  border: 1px solid var(--navy-border);
  color: #FFFFFF;
  padding: 0.85rem 1.25rem;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-lg);
  font-size: 0.88rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  pointer-events: auto;
  animation: slideInToast 0.25s ease forwards;
  min-width: 300px;
}

.toast-emerald {
  border-left: 4px solid var(--emerald-500);
}

.toast-saffron {
  border-left: 4px solid var(--saffron-500);
}

.toast-crimson {
  border-left: 4px solid var(--crimson-500);
}

.toast-close {
  background: none;
  border: none;
  color: #94A3B8;
  cursor: pointer;
  margin-left: auto;
  font-size: 1.2rem;
}

@keyframes slideInToast {
  from { transform: translateX(100%); opacity: 0; }
  to { transform: translateX(0); opacity: 1; }
}

/* Responsive adjustments */
@media (max-width: 1024px) {
  .hero-headline { font-size: 2.5rem; }
  .cre-assets-grid { grid-template-columns: repeat(2, 1fr); }
  .pricing-cards-grid { grid-template-columns: repeat(2, 1fr); }
  .compliance-grid { grid-template-columns: repeat(2, 1fr); }
  .radar-results-grid { grid-template-columns: 1fr; }
  .cre-simulator-card { grid-template-columns: 1fr; }
  .hero-metric-bar { grid-template-columns: repeat(2, 1fr); }
  .footer-top { grid-template-columns: 1fr 1fr; }
}

@media (max-width: 768px) {
  .hero-headline { font-size: 2rem; }
  .radar-search-box { grid-template-columns: 1fr; }
  .boq-inputs-row { grid-template-columns: 1fr; }
  .escrow-steps-grid { grid-template-columns: 1fr; }
  .cre-assets-grid { grid-template-columns: 1fr; }
  .pricing-cards-grid { grid-template-columns: 1fr; }
  .compliance-grid { grid-template-columns: 1fr; }
  .nav-menu { display: none; }
  .vahan-grid-details { grid-template-columns: 1fr 1fr; }
}
"""

with open('/Users/chetanbisariya/.gemini/antigravity-ide/scratch/exainfra-in/style.css', 'w') as f:
    f.write(css_content)

print(f"Generated clean sovereign style.css ({len(css_content)} bytes) successfully.")
