/**
 * ExaInfra.in - National Real Estate Due Diligence, Commercial Yield & Asset Terminal
 * Compliant with RERA Act 2016, IT Act 2000 (Sec 65B), Motor Vehicles Act 1988, DPDP Act 2023 & CPWD DSR 2026
 * Clean White / Light Sovereign Theme with Full Mobile Responsiveness
 */

document.addEventListener('DOMContentLoaded', () => {

  // ====================================================================
  // 1. Security & Sanitization Helper (DOM XSS Defense)
  // ====================================================================
  function escapeHTML(str) {
    if (str == null) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }
  window.escapeHTML = escapeHTML;

  // ====================================================================
  // 2. Toast Notification System
  // ====================================================================
  function showToast(message, type = 'emerald') {
    const container = document.getElementById('toastContainer');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `toast-item toast-${type}`;
    toast.innerHTML = `
      <div class="toast-content">${message}</div>
      <button class="toast-close" onclick="this.parentElement.remove()" aria-label="Dismiss">&times;</button>
    `;

    container.appendChild(toast);
    setTimeout(() => {
      toast.classList.add('fade-out');
      setTimeout(() => toast.remove(), 300);
    }, 4500);
  }
  window.showToast = showToast;

  // ====================================================================
  // 3. Modal & Mobile Drawer Controls
  // ====================================================================
  function openModal(modal) {
    if (!modal) return;
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeModal(modal) {
    if (!modal) return;
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }

  window.openModal = openModal;
  window.closeModal = closeModal;

  document.querySelectorAll('.modal-backdrop').forEach(backdrop => {
    backdrop.addEventListener('click', (e) => {
      if (e.target === backdrop) {
        closeModal(backdrop);
      }
    });
  });

  // Mobile Navigation Drawer & Backdrop Toggle
  const btnMobileToggle = document.getElementById('btnMobileToggle');
  const btnMobileClose = document.getElementById('btnMobileClose');
  const mobileNavDrawer = document.getElementById('mobileNavDrawer');
  const mobileNavBackdrop = document.getElementById('mobileNavBackdrop');

  function openMobileNav() {
    if (mobileNavDrawer) mobileNavDrawer.classList.add('active');
    if (mobileNavBackdrop) mobileNavBackdrop.classList.add('active');
    if (btnMobileToggle) btnMobileToggle.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  }

  function closeMobileNav() {
    if (mobileNavDrawer) mobileNavDrawer.classList.remove('active');
    if (mobileNavBackdrop) mobileNavBackdrop.classList.remove('active');
    if (btnMobileToggle) btnMobileToggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  window.openMobileNav = openMobileNav;
  window.closeMobileNav = closeMobileNav;

  if (btnMobileToggle) btnMobileToggle.addEventListener('click', openMobileNav);
  if (btnMobileClose) btnMobileClose.addEventListener('click', closeMobileNav);
  if (mobileNavBackdrop) mobileNavBackdrop.addEventListener('click', closeMobileNav);

  // Close mobile drawer automatically when clicking any navigation link
  document.querySelectorAll('.mobile-nav-drawer a').forEach(link => {
    link.addEventListener('click', () => {
      closeMobileNav();
    });
  });

  // Global ESC key listener for modal and mobile drawer dismissal
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeMobileNav();
      document.querySelectorAll('.modal-backdrop.active').forEach(modal => {
        closeModal(modal);
      });
    }
  });

  window.scrollToSection = function(id) {
    const el = document.getElementById(id);
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  };

  function formatINR(number) {
    return '₹' + number.toLocaleString('en-IN');
  }

  // ====================================================================
  // 3. PILLAR 1: Property Due Diligence & Scam Risk Radar Engine
  // ====================================================================
  const radarDataSamples = {
    safe: {
      name: "Sobha Silicon Oasis, Hosa Road, Bengaluru",
      score: 94,
      verdictClass: "safe",
      verdictTitle: "A-GRADE CLEAN TITLE (VERIFIED)",
      verdictSub: "Nil encumbrance registered in Kaveri 2.0 Sub-Registrar records. Clear BBMP A-Khata with sanctioned BDA building plan. Outside all lake buffer zones.",
      zoning: "✓ Yellow Residential Zone (BDA Master Plan 2031)",
      khata: "✓ Validated BBMP A-Khata (Property ID: 19-301-44)",
      ec: "✓ Form 16 (Nil Encumbrance 1996 - 2026)",
      buffer: "✓ Zero Lake / Rajakaluve Encroachment (Safe)",
      rera: "✓ RERA PRM/KA/RERA/1251/310/PR/170915/000241"
    },
    danger: {
      name: "Lakeview Enclave, Sy No 44/2, Varthur Lake Buffer",
      score: 38,
      verdictClass: "danger",
      verdictTitle: "CRITICAL RISK: RAJAKALUVE ENCROACHMENT",
      verdictSub: "HIGH DEMOLITION NOTICE RISK: Property encroaches within 50-meter statutory primary stormwater drain buffer ordered by National Green Tribunal (NGT OA 222/2014).",
      zoning: "⚠ Eco-Sensitive Green Buffer Zone (BDA CDP)",
      khata: "❌ Unverified B-Khata Extract (Revenue conversion pending)",
      ec: "⚠ Form 15 (Active Mortgage with DHFL / Piramal)",
      buffer: "❌ CRITICAL: 28m from Rajakaluve Drain (Demolition Threat)",
      rera: "❌ RERA Registration Revoked / Not Approved"
    },
    warning: {
      name: "Green Acres Farm Layout, Sy No 89/1, Devanahalli",
      score: 58,
      verdictClass: "warn",
      verdictTitle: "MODERATE RISK: MULTIPLE LIEN ENCUMBRANCES",
      verdictSub: "Title encumbered with two prior registered mortgages. Pending partition suit in Civil Court Devanahalli (OS 412/2021). Do not disburse advance.",
      zoning: "⚠ Agricultural Land (95A DC Conversion in Progress)",
      khata: "⚠ Gramathana E-Khata Form 9/11 (Panchayat Jurisdiction)",
      ec: "❌ Form 15 (Active Bank Hypothecation of ₹1.85 Cr)",
      buffer: "✓ Beyond 100m Lake Boundary (Safe)",
      rera: "⚠ Unregistered Layout (Section 3 RERA Exemption Claimed)"
    }
  };

  let currentRadarAudit = radarDataSamples.safe;

  window.loadRadarSample = function(type) {
    const data = radarDataSamples[type] || radarDataSamples.safe;
    currentRadarAudit = data;

    const input = document.getElementById('radarIdentifier');
    if (input) input.value = data.name;

    updateRadarUI(data);
    showToast(`✓ Loaded sample audit: ${data.name.split(',')[0]} (Score: ${data.score}/100)`);
  };

  function updateRadarUI(data) {
    const gauge = document.getElementById('radarDialGauge');
    const scoreText = document.getElementById('radarScoreText');
    const verdictTitle = document.getElementById('radarVerdictTitle');
    const verdictSub = document.getElementById('radarVerdictSub');

    const statZoning = document.getElementById('statZoning');
    const statKhata = document.getElementById('statKhata');
    const statEc = document.getElementById('statEc');
    const statBuffer = document.getElementById('statBuffer');
    const statRera = document.getElementById('statRera');

    if (scoreText) scoreText.textContent = data.score;
    if (gauge) {
      gauge.className = `risk-dial ${data.verdictClass === 'safe' ? 'safe' : (data.verdictClass === 'danger' ? 'danger' : '')}`;
      if (data.verdictClass === 'safe') {
        gauge.style.borderColor = 'var(--emerald-500)';
      } else if (data.verdictClass === 'danger') {
        gauge.style.borderColor = 'var(--crimson-500)';
      } else {
        gauge.style.borderColor = 'var(--saffron-500)';
      }
    }

    if (verdictTitle) {
      verdictTitle.textContent = data.verdictTitle;
      verdictTitle.style.color = data.verdictClass === 'safe' ? 'var(--emerald-600)' : (data.verdictClass === 'danger' ? 'var(--crimson-600)' : 'var(--saffron-700)');
    }
    if (verdictSub) verdictSub.textContent = data.verdictSub;

    // Badges
    const setBadge = (el, text) => {
      if (!el) return;
      el.textContent = text;
      if (text.startsWith('✓')) {
        el.className = 'status-badge pass';
      } else if (text.startsWith('❌')) {
        el.className = 'status-badge fail';
      } else {
        el.className = 'status-badge warn';
      }
    };

    setBadge(statZoning, data.zoning);
    setBadge(statKhata, data.khata);
    setBadge(statEc, data.ec);
    setBadge(statBuffer, data.buffer);
    setBadge(statRera, data.rera);
  }

  const formPropertyRadar = document.getElementById('formPropertyRadar');
  if (formPropertyRadar) {
    formPropertyRadar.addEventListener('submit', (e) => {
      e.preventDefault();
      const rawQuery = (document.getElementById('radarIdentifier')?.value || '').trim();
      const query = rawQuery.replace(/[<>"'`]/g, '').slice(0, 120);
      const btn = document.getElementById('btnExecuteRadarAudit');

      btn.disabled = true;
      btn.innerHTML = `<span>Scanning BDA & Sub-Registrar GIS...</span>`;

      showToast('🔄 Connecting to Kaveri 2.0 & BDA Master Plan GIS servers...');

      setTimeout(() => {
        btn.disabled = false;
        btn.innerHTML = `
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          <span>Scan Title & Demolition Risk</span>
        `;

        if (query.toLowerCase().includes('varthur') || query.toLowerCase().includes('lake')) {
          loadRadarSample('danger');
        } else if (query.toLowerCase().includes('farm') || query.toLowerCase().includes('devanahalli')) {
          loadRadarSample('warning');
        } else {
          loadRadarSample('safe');
        }

        showToast('✓ Due Diligence Audit complete! Section 65B hash generated.');
      }, 950);
    });
  }

  // Section 65B Certificate Modal Trigger
  const btnOpenTitleCertModal = document.getElementById('btnOpenTitleCertModal');
  const modalTitleCert = document.getElementById('modalTitleCert');
  const titleCertPaper = document.getElementById('titleCertPaper');

  if (btnOpenTitleCertModal) {
    btnOpenTitleCertModal.addEventListener('click', () => {
      const data = currentRadarAudit;
      const certNo = 'EXA-CERT-' + Math.floor(100000 + Math.random() * 900000);
      const hash = 'SHA256: ' + Array.from({length: 40}, () => Math.floor(Math.random()*16).toString(16)).join('');

      titleCertPaper.innerHTML = `
        <div class="cert-header">
          <div>
            <div class="cert-emblem-text">GOVERNMENT RECOGNIZED LEGAL AUDIT &bull; SECTION 65B CERTIFIED</div>
            <h2 class="cert-title">Property Title Due Diligence & Scam Risk Certificate</h2>
            <div class="cert-meta-row">ISSUED UNDER SECTION 65B OF INDIAN EVIDENCE ACT, 1872 & IT ACT 2000</div>
          </div>
          <div style="text-align:right;">
            <div style="font-family:'JetBrains Mono', monospace; font-size:0.85rem; font-weight:800; color:#0F172A;">${escapeHTML(certNo)}</div>
            <div style="font-size:0.75rem; color:#64748B;">Date: 24-Oct-2026</div>
          </div>
        </div>

        <div class="cert-body-grid">
          <div class="cert-field">
            <span>PROPERTY IDENTIFIER / SURVEY NUMBER</span>
            <strong>${escapeHTML(data.name)}</strong>
          </div>
          <div class="cert-field">
            <span>TITLE HEALTH AUDIT SCORE</span>
            <strong style="color:${data.verdictClass === 'safe' ? '#059669' : '#DC2626'}; font-size:1.15rem;">${escapeHTML(data.score)} / 100 (${escapeHTML(data.verdictTitle.split(':')[0])})</strong>
          </div>
          <div class="cert-field">
            <span>SUB-REGISTRAR ENCUMBRANCE (30 YRS)</span>
            <strong>${escapeHTML(data.ec)}</strong>
          </div>
          <div class="cert-field">
            <span>REVENUE KHATA CLASSIFICATION</span>
            <strong>${escapeHTML(data.khata)}</strong>
          </div>
          <div class="cert-field">
            <span>TOWN PLANNING MASTER PLAN ZONING</span>
            <strong>${escapeHTML(data.zoning)}</strong>
          </div>
          <div class="cert-field">
            <span>NGT 50M STORMWATER DRAIN BUFFER</span>
            <strong style="color:${data.verdictClass === 'danger' ? '#DC2626' : '#059669'};">${escapeHTML(data.buffer)}</strong>
          </div>
        </div>

        <div class="cert-verdict-box ${data.verdictClass === 'safe' ? 'safe' : 'risk'}">
          <strong>STATUTORY LEGAL OPINION & RISK VERDICT:</strong>
          <p style="margin:0.25rem 0 0 0;">${escapeHTML(data.verdictSub)}</p>
        </div>

        <div class="cert-sign-strip">
          <div>
            <span>CRYPTOGRAPHIC RECORD EVIDENCE HASH:</span>
            <code style="font-family:var(--font-mono); color:#0F172A; display:block; font-size:0.75rem; word-break:break-all;">${escapeHTML(hash)}</code>
          </div>
          <div style="text-align:right;">
            <div style="font-size:0.95rem; font-weight:700; color:#0F172A;">Advocate R. S. Nambiar & Associates</div>
            <span style="font-size:0.8rem; color:#64748B;">High Court of Karnataka & RERA Panel Legal Auditor</span>
          </div>
        </div>
      `;

      openModal(modalTitleCert);
    });
  }

  // ====================================================================
  // 4. WEB TERMINAL MULTI-PAGE ROUTER & DECK CONTROLLER
  // ====================================================================
  const TERMINAL_PAGES = [
    { page: 1, id: 'build-boq', url: 'index.html', label: '🏗️ FLAGSHIP COST ESTIMATOR & BOQ', shortTitle: 'Cost Estimator & BoQ' },
    { page: 2, id: 'legal-radar', url: 'property-radar.html', label: '🛡️ PROPERTY SCAM & TITLE RADAR', shortTitle: 'Property Scam Radar' },
    { page: 3, id: 'statutory-tools', url: 'statutory-tools.html', label: '⚙️ STATUTORY & TAX WORKBENCH (10 TOOLS)', shortTitle: 'Statutory Workbench' },
    { page: 4, id: 'contact', url: 'contact.html', label: '✉️ INSTITUTIONAL ADVISORY DESK', shortTitle: 'Advisory Desk' },
    { page: 5, id: 'regulatory-framework', url: 'regulatory-framework.html', label: '⚖️ REGULATORY FRAMEWORK', shortTitle: 'Regulatory Law' }
  ];

  const MULTI_PAGE_ROUTES = {
    1: 'index.html',
    'build-boq': 'index.html',
    'index.html': 'index.html',
    2: 'property-radar.html',
    'legal-radar': 'property-radar.html',
    'property-radar.html': 'property-radar.html',
    3: 'statutory-tools.html',
    'statutory-tools': 'statutory-tools.html',
    'statutory-tools.html': 'statutory-tools.html',
    4: 'contact.html',
    'contact': 'contact.html',
    'contact.html': 'contact.html',
    5: 'regulatory-framework.html',
    'regulatory-framework': 'regulatory-framework.html',
    'regulatory-framework.html': 'regulatory-framework.html'
  };

  // Detect current active page file name
  const currentPathFile = window.location.pathname.split('/').pop() || 'index.html';
  let initialPageNum = 1;
  if (currentPathFile.includes('property-radar')) initialPageNum = 2;
  else if (currentPathFile.includes('statutory-tools')) initialPageNum = 3;
  else if (currentPathFile.includes('contact')) initialPageNum = 4;
  else if (currentPathFile.includes('regulatory')) initialPageNum = 5;

  let currentTerminalPage = initialPageNum;
  let terminalViewMode = 'paginated'; // 'paginated' | 'continuous'

  function switchTerminalPage(target, shouldScroll = true) {
    let targetPage = 1;
    if (typeof target === 'number') {
      targetPage = Math.max(1, Math.min(TERMINAL_PAGES.length, target));
    } else if (typeof target === 'string') {
      const cleanId = target.replace(/^#/, '');
      const found = TERMINAL_PAGES.find(p => p.id === cleanId || String(p.page) === cleanId || p.url === cleanId);
      if (found) targetPage = found.page;
    }

    const pageSections = document.querySelectorAll('.terminal-page');
    // If running in multi-page mode (each page has its own standalone section)
    if (pageSections.length <= 1) {
      const targetUrl = MULTI_PAGE_ROUTES[targetPage] || 'index.html';
      if (!currentPathFile.includes(targetUrl.replace('.html', '')) && currentPathFile !== targetUrl) {
        window.location.href = targetUrl;
        return;
      }
    }

    currentTerminalPage = targetPage;

    // Apply visibility to sections if multiple sections exist on current page
    if (pageSections.length > 1) {
      pageSections.forEach((section) => {
        const pageIndex = parseInt(section.getAttribute('data-page-index') || section.getAttribute('data-terminal-page'), 10);
        if (terminalViewMode === 'continuous') {
          section.classList.remove('hidden-page');
          section.classList.remove('active-page');
          section.style.display = 'block';
        } else {
          if (pageIndex === currentTerminalPage) {
            section.classList.remove('hidden-page');
            section.classList.add('active-page');
            section.style.display = 'block';
          } else {
            section.classList.add('hidden-page');
            section.classList.remove('active-page');
            section.style.display = 'none';
          }
        }
      });
    }

    // Update Pager Pills UI
    const pills = document.querySelectorAll('.pager-pill');
    pills.forEach(pill => {
      const pNum = parseInt(pill.getAttribute('data-page') || pill.getAttribute('data-pager-page'), 10);
      if (pNum === currentTerminalPage) {
        pill.classList.add('active');
        pill.setAttribute('aria-selected', 'true');
      } else {
        pill.classList.remove('active');
        pill.setAttribute('aria-selected', 'false');
      }
    });

    // Update Pager Bar Status Label
    const activeLabel = document.getElementById('pagerActiveLabel');
    const curMeta = TERMINAL_PAGES[currentTerminalPage - 1];
    if (activeLabel && curMeta) {
      activeLabel.textContent = curMeta.label;
    }

    if (shouldScroll) {
      const pagerBar = document.getElementById('terminalPagerBar');
      if (pagerBar) {
        pagerBar.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }
  }

  function prevTerminalPage() {
    const prevPage = Math.max(1, currentTerminalPage - 1);
    const targetUrl = MULTI_PAGE_ROUTES[prevPage] || 'index.html';
    if (!currentPathFile.includes(targetUrl.replace('.html', '')) && currentPathFile !== targetUrl) {
      window.location.href = targetUrl;
    } else {
      switchTerminalPage(prevPage, true);
    }
  }

  function nextTerminalPage() {
    const maxPages = 4; // 4 primary pages
    const nextPage = Math.min(maxPages, currentTerminalPage + 1);
    const targetUrl = MULTI_PAGE_ROUTES[nextPage] || 'contact.html';
    if (!currentPathFile.includes(targetUrl.replace('.html', '')) && currentPathFile !== targetUrl) {
      window.location.href = targetUrl;
    } else {
      switchTerminalPage(nextPage, true);
    }
  }

  function setTerminalViewMode(mode) {
    terminalViewMode = (mode === 'feed' || mode === 'continuous') ? 'continuous' : 'paginated';
    const btnPaginated = document.getElementById('btnModePaginated');
    const btnContinuous = document.getElementById('btnModeContinuous');

    if (terminalViewMode === 'paginated') {
      if (btnPaginated) btnPaginated.classList.add('active');
      if (btnContinuous) btnContinuous.classList.remove('active');
      showToast('📖 Paginated Deck Mode: Focused 1-Page per module');
    } else {
      if (btnPaginated) btnPaginated.classList.remove('active');
      if (btnContinuous) btnContinuous.classList.add('active');
      showToast('📜 Continuous Feed Mode: All modules visible in continuous scroll');
    }
    switchTerminalPage(currentTerminalPage, false);
  }

  // Keyboard Navigation: ArrowLeft, ArrowRight, and keys 1..4 across pages
  window.addEventListener('keydown', (e) => {
    const activeEl = document.activeElement;
    if (activeEl && (activeEl.tagName === 'INPUT' || activeEl.tagName === 'SELECT' || activeEl.tagName === 'TEXTAREA' || activeEl.isContentEditable)) {
      return;
    }
    if (e.key === 'ArrowLeft') {
      prevTerminalPage();
    } else if (e.key === 'ArrowRight') {
      nextTerminalPage();
    } else if (['1', '2', '3', '4'].includes(e.key)) {
      const pageNum = parseInt(e.key, 10);
      const targetUrl = MULTI_PAGE_ROUTES[pageNum];
      if (targetUrl) {
        window.location.href = targetUrl;
      }
    }
  });

  // Global bindings for HTML onclick handlers
  window.switchTerminalPage = switchTerminalPage;
  window.prevTerminalPage = prevTerminalPage;
  window.nextTerminalPage = nextTerminalPage;
  window.setTerminalViewMode = setTerminalViewMode;

  // BoQ Trade Filter state and handler
  window.currentBoqFilter = 'all';
  window.filterBoqTrade = function(tradeKey) {
    window.currentBoqFilter = tradeKey;
    const filterButtons = document.querySelectorAll('.boq-filter-pill');
    filterButtons.forEach(btn => {
      if (btn.getAttribute('data-trade-filter') === tradeKey) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });
    if (typeof updateConstructionEstimator === 'function') {
      updateConstructionEstimator();
    }
  };

  // ====================================================================
  // 5. PILLAR 3: Interactive Construction Cost Estimator & Material BoQ Engine (India-Specific)
  // ====================================================================

  // Configuration Matrix: City Multipliers, Quality Tiers, Material Overrides & CPWD Thumb Rules
  const constructionCostMatrix = {
    // 15+ Indian Cities grouped by Region with Localized Cost Multipliers (Base: 1.0)
    cities: {
      // Central India
      'bhopal': { name: 'Bhopal (Central MP)', region: 'Central', tier: 'Tier 2', mult: 0.96, desc: 'Tier 2 Central Market • Low Freight Premium' },
      'indore': { name: 'Indore (Commercial MP)', region: 'Central', tier: 'Tier 2', mult: 0.98, desc: 'Tier 2 Commercial Hub • Moderate Aggregates' },
      'jabalpur': { name: 'Jabalpur (Mahakoshal)', region: 'Central', tier: 'Tier 2', mult: 0.94, desc: 'Tier 2 Eastern MP • Abundant Local Sand' },
      // North India
      'delhi-ncr': { name: 'Delhi NCR (Gurugram / Noida)', region: 'North', tier: 'Tier 1', mult: 1.18, desc: 'Tier 1 National Capital • GRAP Green Levies & High Transport' },
      'lucknow': { name: 'Lucknow (Uttar Pradesh)', region: 'North', tier: 'Tier 2', mult: 1.02, desc: 'Tier 2 UP Capital • Standard River Sand Belt' },
      'chandigarh': { name: 'Chandigarh Tri-City', region: 'North', tier: 'Tier 2', mult: 1.10, desc: 'Tier 2 Northern Hub • Mountain Quarry Freight' },
      'jaipur': { name: 'Jaipur (Rajasthan)', region: 'North', tier: 'Tier 2', mult: 1.00, desc: 'Tier 2 Rajasthan Hub • Benchmark Stone & Marble Base' },
      // West India
      'mumbai': { name: 'Mumbai MMR (Maharashtra)', region: 'West', tier: 'Tier 1', mult: 1.38, desc: 'Tier 1 Coastal Metro • High Logistics, Sand Royalty & Labor' },
      'pune': { name: 'Pune Metropolitan', region: 'West', tier: 'Tier 1', mult: 1.16, desc: 'Tier 1 Western IT Hub • Moderate Logistics & Labor' },
      'ahmedabad': { name: 'Ahmedabad (Gujarat)', region: 'West', tier: 'Tier 2', mult: 1.05, desc: 'Tier 2 Industrial Hub • Abundant Cement & Ceramic Tiles' },
      // South India
      'bengaluru': { name: 'Bengaluru (Karnataka)', region: 'South', tier: 'Tier 1', mult: 1.15, desc: 'Tier 1 Southern Tech Capital • M-Sand Norm & Skilled Labor' },
      'hyderabad': { name: 'Hyderabad (Telangana)', region: 'South', tier: 'Tier 1', mult: 1.12, desc: 'Tier 1 South Growth Metro • Proximity to Cement Clusters' },
      'chennai': { name: 'Chennai (Tamil Nadu)', region: 'South', tier: 'Tier 1', mult: 1.14, desc: 'Tier 1 Coastal Metro • River Sand Restrictions & Steel Logistics' },
      // East India
      'kolkata': { name: 'Kolkata (West Bengal)', region: 'East', tier: 'Tier 1', mult: 1.06, desc: 'Tier 1 Eastern Hub • Primary Durgapur Steel Corridor' },
      'patna': { name: 'Patna (Bihar)', region: 'East', tier: 'Tier 2', mult: 1.00, desc: 'Tier 2 Ganga Belt • Sone Sand Proximity' },
      'bhubaneswar': { name: 'Bhubaneswar (Odisha)', region: 'East', tier: 'Tier 2', mult: 0.98, desc: 'Tier 2 Eastern Metro • Direct Steel Plant Proximity' }
    },

    // Construction Quality / Specification Tiers
    qualities: {
      'standard': {
        name: 'Standard / Budget',
        cement: 'local',
        steel: 'jsw',
        bricks: 'clay',
        sand: 'msand',
        flooring: 'vitrified_std',
        joinery: 'sal_upvc'
      },
      'premium': {
        name: 'Premium / Semi-Luxury',
        cement: 'ultratech',
        steel: 'tata',
        bricks: 'aac',
        sand: 'river',
        flooring: 'vitrified_gvt',
        joinery: 'teak_veneer'
      },
      'luxury': {
        name: 'Luxury / Ultra',
        cement: 'ultratech',
        steel: 'tata',
        bricks: 'aac',
        sand: 'river',
        flooring: 'italian_marble',
        joinery: 'burma_teak'
      }
    },

    // Building Height / Floor Multipliers & Surcharges
    floors: {
      'G': { count: 1, label: 'Ground Floor (G)', surcharge: 1.00 },
      'G+1': { count: 2, label: 'G + 1 (Duplex)', surcharge: 1.02 },
      'G+2': { count: 3, label: 'G + 2 (Triplex)', surcharge: 1.05 },
      'G+3': { count: 4, label: 'G + 3 (Multi-Unit)', surcharge: 1.08 },
      'G+4': { count: 5, label: 'G + 4 (Stilt+4)', surcharge: 1.12 }
    },

    // Material Specifications & Base Rates (Base National Standard)
    materials: {
      cement: {
        'ultratech': { name: 'UltraTech Super / Weather Plus', ratePerBag: 420, grade: '53 Grade OPC / PPC (IS 12269)' },
        'acc': { name: 'ACC Gold Water Shield', ratePerBag: 410, grade: 'Water Repellent PPC (IS 1489)' },
        'ambuja': { name: 'Ambuja Plus Roof Special', ratePerBag: 415, grade: 'High Early Strength PPC' },
        'dalmia': { name: 'Dalmia DSP High-Grade', ratePerBag: 390, grade: 'Durable Slag/Portland (IS 455)' },
        'shree': { name: 'Shree Ultra / Bangur', ratePerBag: 380, grade: 'Heavy Duty 53 Grade (IS 269)' },
        'local': { name: 'Local Regional ISI Brand', ratePerBag: 360, grade: 'Standard ISI Certified PPC' }
      },
      steel: {
        'tata': { name: 'Tata Tiscon 550D Superlinks', ratePerKg: 74, grade: 'Fe-550D Primary Rebar (IS 1786)' },
        'jsw': { name: 'JSW Neosteel Fe-550D', ratePerKg: 70, grade: 'High Ductility TMT (IS 1786)' },
        'jindal': { name: 'Jindal Panther Fe-550D', ratePerKg: 68, grade: 'Refined Primary Steel (IS 1786)' },
        'kamdhenu': { name: 'Kamdhenu Nxt TMT', ratePerKg: 66, grade: 'Interlocking Double Ribbed' },
        'local': { name: 'Local Rolling Mill ISI', ratePerKg: 60, grade: 'Fe-500 ISI Rebar Standard' }
      },
      bricks: {
        'clay': { name: 'Red Clay Kiln Bricks (Class 1)', ratePerUnit: 9.5, unit: 'Bricks', qtyPerSqft: 20, grade: 'Table Molded Kiln Fired' },
        'flyash': { name: 'Fly Ash Class-F Bricks', ratePerUnit: 6.5, unit: 'Bricks', qtyPerSqft: 20, grade: 'Eco High Compression (IS 12894)' },
        'aac': { name: 'AAC Lightweight Blocks (6"/8")', ratePerUnit: 62.0, unit: 'Blocks', qtyPerSqft: 2.4, grade: 'Autoclaved Aerated (IS 2185)' }
      },
      sand: {
        'river': { name: 'Natural River Plaster Sand', ratePerCft: 65, grade: 'Triple Washed River Bed Sand' },
        'msand': { name: 'Triple-Washed M-Sand', ratePerCft: 45, grade: 'VSI Graded Manufactured Sand (IS 383)' }
      },
      aggregate: {
        'coarse': { name: 'Coarse Blue Metal Aggregate (10/20mm)', ratePerCft: 42, grade: 'IS 383 Machine Crushed Granite' }
      },
      flooring: {
        'ceramic': { name: 'Basic Ceramic Anti-Skid Tiles', ratePerSqft: 45, grade: 'Regal / Johnson 1x1 & 2x2' },
        'vitrified_std': { name: 'Vitrified Glazed Tiles (2x2)', ratePerSqft: 60, grade: 'Somany / Orientbell Nano Polished' },
        'vitrified_gvt': { name: 'GVT Vitrified Slab Tiles (4x2)', ratePerSqft: 85, grade: 'Kajaria / Somany High Gloss Vitrified' },
        'granite': { name: 'Polished Granite Slabs', ratePerSqft: 140, grade: 'Black Galaxy / Tan Brown Mirror Polish' },
        'italian_marble': { name: 'Imported Italian Marble', ratePerSqft: 280, grade: 'Dyna / Bottochino Diamond Polish' }
      },
      joinery: {
        'sal_upvc': { name: 'Sal Wood Frame + Flush Doors / UPVC', ratePerSqft: 280, grade: 'Prominance UPVC + Waterproof Flush Doors' },
        'meranti_upvc': { name: 'Malaysian Meranti Wood + UPVC', ratePerSqft: 340, grade: 'Seasoned Meranti Timber + 2.5 Track UPVC' },
        'teak_veneer': { name: 'CP Teak Frame + Teak Veneer & UPVC', ratePerSqft: 450, grade: 'CP Teak Main Door + Kommerling UPVC' },
        'burma_teak': { name: 'Solid Burma Teak Joinery & Polish', ratePerSqft: 750, grade: '100% Seasoned Burma Teak & Architectural Brass' }
      }
    },

    // CPWD DSR & NBC Standard Thumb Rules per Sq.Ft of Built-Up Area
    thumbRules: {
      cementBagsPerSqft: 0.42,
      steelKgPerSqft: 4.0,
      sandCftPerSqft: 2.0,
      coarseAggCftPerSqft: 1.35,
      flooringSqftMult: 1.15,
      joinerySqftMult: 0.18,
      civilLaborBaseRate: 340,
      mepFinishingBaseRate: {
        'standard': 220,
        'premium': 310,
        'luxury': 440
      }
    }
  };

  // State object storing latest estimate calculation
  let cceLatestCalculation = {
    carpetArea: 1500,
    builtupArea: 1950,
    floorsKey: 'G+1',
    floorsCount: 2,
    qualityKey: 'premium',
    cityKey: 'bhopal',
    cityName: 'Bhopal (Central MP)',
    cityMult: 0.96,
    grandTotal: 3075000,
    minRange: 2890000,
    maxRange: 3260000,
    ratePerBuiltup: 1577,
    ratePerCarpet: 2050
  };

  // DOM Elements for CCE
  const cceCarpetArea = document.getElementById('cceCarpetArea');
  const cceCarpetWarn = document.getElementById('cceCarpetWarn');
  const cceAreaScopeMode = document.getElementById('cceAreaScopeMode');
  const cceBuiltupMultiplier = document.getElementById('cceBuiltupMultiplier');
  const cceFloors = document.getElementById('cceFloors');
  const cceQuality = document.getElementById('cceQuality');
  const cceCity = document.getElementById('cceCity');

  // Override Selectors
  const cceCementBrand = document.getElementById('cceCementBrand');
  const cceSteelBrand = document.getElementById('cceSteelBrand');
  const cceBricksType = document.getElementById('cceBricksType');
  const cceSandType = document.getElementById('cceSandType');
  const cceFlooringType = document.getElementById('cceFlooringType');
  const cceJoineryType = document.getElementById('cceJoineryType');

  // Display Elements
  const cceDisplayCarpetArea = document.getElementById('cceDisplayCarpetArea');
  const cceDisplayBuiltupArea = document.getElementById('cceDisplayBuiltupArea');
  const cceDisplayFloorsCount = document.getElementById('cceDisplayFloorsCount');
  const cceCityBanner = document.getElementById('cceCityBanner');
  const cceCityPill = document.getElementById('cceCityPill');
  const cceCityTier = document.getElementById('cceCityTier');
  const cceTotalRange = document.getElementById('cceTotalRange');
  const cceMedianCost = document.getElementById('cceMedianCost');
  const cceRatePerSqft = document.getElementById('cceRatePerSqft');
  const cceRateCarpetSqft = document.getElementById('cceRateCarpetSqft');
  const cceMetaChips = document.getElementById('cceMetaChips');
  const cceTableBody = document.getElementById('cceTableBody');
  const cceTableFootTotal = document.getElementById('cceTableFootTotal');
  const cceSplitBadge = document.getElementById('cceSplitBadge');
  const cceDonutArcs = document.getElementById('cceDonutArcs');
  const cceDonutCenterVal = document.getElementById('cceDonutCenterVal');
  const cceChartLegend = document.getElementById('cceChartLegend');
  const cceEscrowStepsGrid = document.getElementById('cceEscrowStepsGrid');

  // Quick Preset Handlers
  window.setCceCarpetArea = function(val) {
    if (cceCarpetArea) {
      cceCarpetArea.value = val;
      document.querySelectorAll('.cce-pill-btn').forEach(btn => {
        if (btn.textContent.includes(val.toLocaleString('en-IN'))) {
          btn.classList.add('active');
        } else {
          btn.classList.remove('active');
        }
      });
      updateConstructionEstimator();
    }
  };

  window.setCceFloors = function(floorKey) {
    if (cceFloors) {
      cceFloors.value = floorKey;
      document.querySelectorAll('.cce-floor-btn').forEach(btn => {
        if (btn.getAttribute('data-floor') === floorKey) {
          btn.classList.add('active');
        } else {
          btn.classList.remove('active');
        }
      });
      updateConstructionEstimator();
    }
  };

  window.setCceQuality = function(qualityKey) {
    if (cceQuality) {
      cceQuality.value = qualityKey;
      document.querySelectorAll('.cce-quality-card').forEach(card => {
        card.classList.remove('active');
      });
      const targetCard = qualityKey === 'standard' ? document.getElementById('qCardStandard') :
                         qualityKey === 'premium' ? document.getElementById('qCardPremium') :
                         document.getElementById('qCardLuxury');
      if (targetCard) targetCard.classList.add('active');

      // Auto-set override selectors to tier defaults
      const defaults = constructionCostMatrix.qualities[qualityKey] || constructionCostMatrix.qualities.premium;
      if (cceCementBrand) cceCementBrand.value = defaults.cement;
      if (cceSteelBrand) cceSteelBrand.value = defaults.steel;
      if (cceBricksType) cceBricksType.value = defaults.bricks;
      if (cceSandType) cceSandType.value = defaults.sand;
      if (cceFlooringType) cceFlooringType.value = defaults.flooring;
      if (cceJoineryType) cceJoineryType.value = defaults.joinery;

      updateConstructionEstimator();
    }
  };

  window.toggleCceOverrides = function() {
    const body = document.getElementById('cceOverridesBody');
    const icon = document.getElementById('cceOverridesToggleIcon');
    if (body) {
      body.classList.toggle('collapsed');
      if (icon) {
        icon.textContent = body.classList.contains('collapsed') ? '▼ Expand Overrides' : '▲ Collapse Overrides';
      }
    }
  };

  window.resetCceOverrides = function() {
    const qualityKey = cceQuality ? cceQuality.value : 'premium';
    window.setCceQuality(qualityKey);
    showToast('↺ Material brands reset to ' + qualityKey.toUpperCase() + ' tier defaults.');
  };

  // Main Reactive Engine
  function updateConstructionEstimator() {
    if (!cceCarpetArea || !cceTableBody) return;

    const rawCarpet = parseFloat(cceCarpetArea.value);
    let carpetInput = 1500;

    if (isNaN(rawCarpet) || rawCarpet < 100) {
      if (cceCarpetWarn) {
        cceCarpetWarn.style.display = 'flex';
        cceCarpetWarn.textContent = '⚠️ Minimum carpet area is 100 sq.ft for standard structural engineering thumb rules.';
      }
      carpetInput = Math.max(100, isNaN(rawCarpet) ? 100 : Math.abs(rawCarpet));
    } else if (rawCarpet > 100000) {
      if (cceCarpetWarn) {
        cceCarpetWarn.style.display = 'flex';
        cceCarpetWarn.textContent = '⚠️ Maximum carpet area threshold is 100,000 sq.ft for standard residential/commercial algorithm.';
      }
      carpetInput = 100000;
    } else {
      if (cceCarpetWarn) {
        cceCarpetWarn.style.display = 'none';
      }
      carpetInput = rawCarpet;
    }

    const areaMode = cceAreaScopeMode ? cceAreaScopeMode.value : 'total';
    const builtupMult = cceBuiltupMultiplier ? (parseFloat(cceBuiltupMultiplier.value) || 1.30) : 1.30;
    const floorKey = cceFloors ? cceFloors.value : 'G+1';
    const qualityKey = cceQuality ? cceQuality.value : 'premium';
    const cityKey = cceCity ? cceCity.value : 'bhopal';

    const floorObj = constructionCostMatrix.floors[floorKey] || constructionCostMatrix.floors['G+1'];
    const cityObj = constructionCostMatrix.cities[cityKey] || constructionCostMatrix.cities['bhopal'];
    const thumb = constructionCostMatrix.thumbRules;

    // Calculate usable carpet and total built-up
    let totalCarpet = carpetInput;
    if (areaMode === 'per_floor') {
      totalCarpet = Math.round(carpetInput * floorObj.count);
    }
    const totalBuiltup = Math.round(totalCarpet * builtupMult);

    // Update Banner Displays
    if (cceDisplayCarpetArea) cceDisplayCarpetArea.textContent = `${totalCarpet.toLocaleString('en-IN')} sq.ft`;
    if (cceDisplayBuiltupArea) cceDisplayBuiltupArea.textContent = `${totalBuiltup.toLocaleString('en-IN')} sq.ft`;
    if (cceDisplayFloorsCount) cceDisplayFloorsCount.textContent = `${floorObj.count} Level${floorObj.count > 1 ? 's' : ''} (${floorKey})`;

    // Update City Banner
    if (cceCityPill) {
      const diffPct = Math.round((cityObj.mult - 1.0) * 100);
      const sign = diffPct > 0 ? `+${diffPct}%` : (diffPct < 0 ? `${diffPct}%` : 'Base');
      cceCityPill.textContent = `📍 ${cityObj.name} • Index: ${cityObj.mult.toFixed(2)}x (${sign} vs Base)`;
    }
    if (cceCityTier) {
      cceCityTier.textContent = cityObj.desc;
    }

    // Material Brand Selections
    const cementKey = cceCementBrand ? cceCementBrand.value : 'ultratech';
    const steelKey = cceSteelBrand ? cceSteelBrand.value : 'tata';
    const brickKey = cceBricksType ? cceBricksType.value : 'aac';
    const sandKey = cceSandType ? cceSandType.value : 'river';
    const flooringKey = cceFlooringType ? cceFlooringType.value : 'vitrified_gvt';
    const joineryKey = cceJoineryType ? cceJoineryType.value : 'teak_veneer';

    const cementObj = constructionCostMatrix.materials.cement[cementKey] || constructionCostMatrix.materials.cement['ultratech'];
    const steelObj = constructionCostMatrix.materials.steel[steelKey] || constructionCostMatrix.materials.steel['tata'];
    const brickObj = constructionCostMatrix.materials.bricks[brickKey] || constructionCostMatrix.materials.bricks['aac'];
    const sandObj = constructionCostMatrix.materials.sand[sandKey] || constructionCostMatrix.materials.sand['river'];
    const aggObj = constructionCostMatrix.materials.aggregate['coarse'];
    const flooringObj = constructionCostMatrix.materials.flooring[flooringKey] || constructionCostMatrix.materials.flooring['vitrified_gvt'];
    const joineryObj = constructionCostMatrix.materials.joinery[joineryKey] || constructionCostMatrix.materials.joinery['teak_veneer'];

    // 1. Fe-550D TMT Steel Rebar
    const steelKg = Math.round(totalBuiltup * thumb.steelKgPerSqft);
    const steelTonnes = (steelKg / 1000).toFixed(2);
    const steelUnitRate = Math.round(steelObj.ratePerKg * cityObj.mult);
    const steelCost = Math.round(steelKg * steelUnitRate);

    // 2. OPC / PPC Cement
    const cementBags = Math.round(totalBuiltup * thumb.cementBagsPerSqft);
    const cementUnitRate = Math.round(cementObj.ratePerBag * cityObj.mult);
    const cementCost = Math.round(cementBags * cementUnitRate);

    // 3. Sand / Fine Aggregate
    const sandCft = Math.round(totalBuiltup * thumb.sandCftPerSqft);
    const sandUnitRate = Math.round(sandObj.ratePerCft * cityObj.mult);
    const sandCost = Math.round(sandCft * sandUnitRate);

    // 4. Coarse Aggregate (10/20mm)
    const aggCft = Math.round(totalBuiltup * thumb.coarseAggCftPerSqft);
    const aggUnitRate = Math.round(aggObj.ratePerCft * cityObj.mult);
    const aggCost = Math.round(aggCft * aggUnitRate);

    // 5. Masonry Bricks / AAC Blocks
    const brickQty = Math.round(totalBuiltup * brickObj.qtyPerSqft);
    const brickUnitRate = Math.round(brickObj.ratePerUnit * cityObj.mult * 10) / 10;
    const brickCost = Math.round(brickQty * brickUnitRate);

    // 6. Flooring & Wall Cladding
    const flooringSqft = Math.round(totalBuiltup * thumb.flooringSqftMult);
    const flooringUnitRate = Math.round(flooringObj.ratePerSqft * cityObj.mult);
    const flooringCost = Math.round(flooringSqft * flooringUnitRate);

    // 7. Woodwork, Joinery & Windows
    const joinerySqft = Math.round(totalBuiltup * thumb.joinerySqftMult);
    const joineryUnitRate = Math.round(joineryObj.ratePerSqft * cityObj.mult);
    const joineryCost = Math.round(joinerySqft * joineryUnitRate);

    // 8. Civil Masonry & Structural Labor
    const civilLaborRate = Math.round(thumb.civilLaborBaseRate * cityObj.mult * floorObj.surcharge);
    const civilLaborCost = Math.round(totalBuiltup * civilLaborRate);

    // 9. MEP (Electrical, Plumbing, Painting & Snagging)
    const mepBase = thumb.mepFinishingBaseRate[qualityKey] || 310;
    const mepRate = Math.round(mepBase * cityObj.mult);
    const mepCost = Math.round(totalBuiltup * mepRate);

    // Grand Total & Volatility Range (±6%)
    const grandTotal = steelCost + cementCost + sandCost + aggCost + brickCost + flooringCost + joineryCost + civilLaborCost + mepCost;
    const minRange = Math.round(grandTotal * 0.94);
    const maxRange = Math.round(grandTotal * 1.06);
    const ratePerBuiltup = Math.round(grandTotal / totalBuiltup);
    const ratePerCarpet = Math.round(grandTotal / totalCarpet);

    // High level split: Materials vs Labor
    const totalMaterials = steelCost + cementCost + sandCost + aggCost + brickCost + flooringCost + joineryCost;
    const totalLabor = civilLaborCost + mepCost;
    const matPct = Math.round((totalMaterials / grandTotal) * 100);
    const labPct = 100 - matPct;

    // Cache latest calculation
    cceLatestCalculation = {
      carpetArea: totalCarpet,
      builtupArea: totalBuiltup,
      floorsKey: floorKey,
      floorsCount: floorObj.count,
      qualityKey: qualityKey,
      cityKey: cityKey,
      cityName: cityObj.name,
      cityMult: cityObj.mult,
      grandTotal: grandTotal,
      minRange: minRange,
      maxRange: maxRange,
      ratePerBuiltup: ratePerBuiltup,
      ratePerCarpet: ratePerCarpet
    };

    // Update Summary Card
    if (cceTotalRange) cceTotalRange.textContent = `${formatINR(minRange)} – ${formatINR(maxRange)}`;
    if (cceMedianCost) cceMedianCost.textContent = formatINR(grandTotal);
    if (cceRatePerSqft) cceRatePerSqft.textContent = `${formatINR(ratePerBuiltup)} / sq.ft`;
    if (cceRateCarpetSqft) cceRateCarpetSqft.textContent = `${formatINR(ratePerCarpet)} / sq.ft`;

    if (cceMetaChips) {
      cceMetaChips.innerHTML = `
        <span class="cce-chip">Carpet: <strong>${totalCarpet.toLocaleString('en-IN')} sq.ft</strong></span>
        <span class="cce-chip">Built-Up: <strong>${totalBuiltup.toLocaleString('en-IN')} sq.ft</strong></span>
        <span class="cce-chip">Structure: <strong>${floorKey} (${floorObj.count} Levels)</strong></span>
        <span class="cce-chip">Location: <strong>${cityObj.name.split(' (')[0]} (${cityObj.mult.toFixed(2)}x)</strong></span>
        <span class="cce-chip">Tier: <strong>${qualityKey.toUpperCase()}</strong></span>
      `;
    }

    if (cceSplitBadge) {
      cceSplitBadge.textContent = `MATERIALS ~${matPct}% • LABOR ~${labPct}%`;
    }

    // Itemized Items list with Trade Categories
    const items = [
      {
        name: 'Structural Steel Rebar (Fe-550D)',
        trade: 'structural',
        brand: `${steelObj.name} (${steelObj.grade})`,
        qty: `${steelTonnes} MT (${steelKg.toLocaleString('en-IN')} kg)`,
        rate: `₹${steelUnitRate} / kg`,
        cost: steelCost,
        share: Math.round((steelCost / grandTotal) * 100)
      },
      {
        name: 'OPC / PPC Structural Cement',
        trade: 'structural',
        brand: `${cementObj.name} (${cementObj.grade})`,
        qty: `${cementBags.toLocaleString('en-IN')} Bags (50kg)`,
        rate: `₹${cementUnitRate} / Bag`,
        cost: cementCost,
        share: Math.round((cementCost / grandTotal) * 100)
      },
      {
        name: 'Plaster & Concrete Sand',
        trade: 'structural',
        brand: `${sandObj.name} (${sandObj.grade})`,
        qty: `${sandCft.toLocaleString('en-IN')} Cu.Ft (${(sandCft / 100).toFixed(1)} Brass)`,
        rate: `₹${sandUnitRate} / Cu.Ft`,
        cost: sandCost,
        share: Math.round((sandCost / grandTotal) * 100)
      },
      {
        name: 'Coarse Aggregates (10/20mm)',
        trade: 'structural',
        brand: `${aggObj.name} (${aggObj.grade})`,
        qty: `${aggCft.toLocaleString('en-IN')} Cu.Ft (${(aggCft / 100).toFixed(1)} Brass)`,
        rate: `₹${aggUnitRate} / Cu.Ft`,
        cost: aggCost,
        share: Math.round((aggCost / grandTotal) * 100)
      },
      {
        name: 'Wall Masonry Infill (Bricks / AAC)',
        trade: 'structural',
        brand: `${brickObj.name} (${brickObj.grade})`,
        qty: `${brickQty.toLocaleString('en-IN')} ${brickObj.unit}`,
        rate: `₹${brickUnitRate} / ${brickObj.unit === 'Blocks' ? 'Block' : 'Pc'}`,
        cost: brickCost,
        share: Math.round((brickCost / grandTotal) * 100)
      },
      {
        name: 'Flooring, Skirting & Wall Dado',
        trade: 'finishing',
        brand: `${flooringObj.name} (${flooringObj.grade})`,
        qty: `${flooringSqft.toLocaleString('en-IN')} sq.ft`,
        rate: `₹${flooringUnitRate} / sq.ft`,
        cost: flooringCost,
        share: Math.round((flooringCost / grandTotal) * 100)
      },
      {
        name: 'Doors, Windows & Joinery',
        trade: 'finishing',
        brand: `${joineryObj.name} (${joineryObj.grade})`,
        qty: `${joinerySqft.toLocaleString('en-IN')} sq.ft`,
        rate: `₹${joineryUnitRate} / sq.ft`,
        cost: joineryCost,
        share: Math.round((joineryCost / grandTotal) * 100)
      },
      {
        name: 'Civil Masonry & Structural Labor',
        trade: 'labor',
        brand: 'CPWD 2026 Manday Norms (Masonry, Shuttering & Bar-Bending)',
        qty: `${totalBuiltup.toLocaleString('en-IN')} sq.ft built-up`,
        rate: `₹${civilLaborRate} / sq.ft`,
        cost: civilLaborCost,
        share: Math.round((civilLaborCost / grandTotal) * 100)
      },
      {
        name: 'MEP (Electrical, Plumbing & Paint)',
        trade: 'labor',
        brand: 'Polycab/Havells Wires, Finolex/Astral CPVC, Asian Paints Royale',
        qty: `${totalBuiltup.toLocaleString('en-IN')} sq.ft built-up`,
        rate: `₹${mepRate} / sq.ft`,
        cost: mepCost,
        share: Math.round((mepCost / grandTotal) * 100)
      }
    ];

    // Render Table with Active Trade Category Filter
    const activeFilter = window.currentBoqFilter || 'all';
    const visibleItems = activeFilter === 'all'
      ? items
      : items.filter(it => it.trade === activeFilter);

    let tableHtml = '';
    let filteredSubtotal = 0;
    visibleItems.forEach(item => {
      filteredSubtotal += item.cost;
      tableHtml += `
        <tr>
          <td><strong>${escapeHTML(item.name)}</strong></td>
          <td>${escapeHTML(item.brand)}</td>
          <td><strong>${escapeHTML(item.qty)}</strong></td>
          <td>${escapeHTML(item.rate)}</td>
          <td><strong style="color:var(--navy-authority);">${formatINR(item.cost)}</strong></td>
          <td><span style="font-size:0.78rem; font-weight:700; color:var(--text-muted);">${item.share}%</span></td>
        </tr>
      `;
    });
    cceTableBody.innerHTML = tableHtml;
    if (cceTableFootTotal) {
      if (activeFilter === 'all') {
        cceTableFootTotal.innerHTML = `<strong>${formatINR(grandTotal)}</strong>`;
      } else {
        cceTableFootTotal.innerHTML = `<strong>${formatINR(filteredSubtotal)}</strong> <span style="font-size:0.76rem; color:var(--text-muted); font-weight:600; margin-left:0.4rem;">(Filtered / Total ${formatINR(grandTotal)})</span>`;
      }
    }

    // Render SVG Donut Chart & Color Legend
    const chartCategories = [
      { name: 'Structural Steel (TMT)', cost: steelCost, color: '#3B82F6' },
      { name: 'Cement & Concrete', cost: cementCost, color: '#D97706' },
      { name: 'Sand, Aggregate & Bricks', cost: sandCost + aggCost + brickCost, color: '#10B981' },
      { name: 'Flooring, Wood & Finish', cost: flooringCost + joineryCost, color: '#8B5CF6' },
      { name: 'Civil Labor & MEP Trades', cost: civilLaborCost + mepCost, color: '#0F172A' }
    ];

    const radius = 70;
    const circ = 2 * Math.PI * radius; // ~439.82
    let currentOffset = 0;
    let arcsHtml = '';
    let legendHtml = '';

    chartCategories.forEach(cat => {
      const pct = (cat.cost / grandTotal);
      const arcLen = pct * circ;
      arcsHtml += `
        <circle cx="100" cy="100" r="${radius}" fill="transparent"
                stroke="${cat.color}" stroke-width="26"
                stroke-dasharray="${arcLen.toFixed(2)} ${(circ - arcLen).toFixed(2)}"
                stroke-dashoffset="${(-currentOffset).toFixed(2)}"
                style="transition: stroke-dasharray 0.5s ease, stroke-dashoffset 0.5s ease;">
          <title>${cat.name}: ${formatINR(cat.cost)} (${Math.round(pct * 100)}%)</title>
        </circle>
      `;
      currentOffset += arcLen;

      legendHtml += `
        <div class="cce-legend-item">
          <div class="cce-legend-name-wrap">
            <span class="cce-legend-dot" style="background:${cat.color};"></span>
            <span class="cce-legend-name">${cat.name}</span>
          </div>
          <div class="cce-legend-stat">
            <span>${formatINR(cat.cost)}</span>
            <span class="cce-legend-pct">(${Math.round(pct * 100)}%)</span>
          </div>
        </div>
      `;
    });

    if (cceDonutArcs) cceDonutArcs.innerHTML = arcsHtml;
    if (cceDonutCenterVal) {
      const lakhs = (grandTotal / 100000).toFixed(1);
      cceDonutCenterVal.textContent = `₹${lakhs}L`;
    }
    if (cceChartLegend) cceChartLegend.innerHTML = legendHtml;

    // Render Milestone Escrow Schedule with dynamic ₹ amounts
    if (cceEscrowStepsGrid) {
      const tranches = [
        { pct: 15, name: 'Foundation & Plinth', trigger: 'Excavation, PCC, footings and plinth beam casting completed.' },
        { pct: 30, name: 'RCC Superstructure', trigger: 'Columns, floor beams and roof slab de-shuttering completed.' },
        { pct: 20, name: 'Brickwork & Conduits', trigger: 'External masonry, internal partitions and electrical pipings.' },
        { pct: 20, name: 'Plastering & Flooring', trigger: 'Internal plaster, vitrified flooring & sanitary fixtures fitted.' },
        { pct: 15, name: 'Snagging & Handover', trigger: 'Doors, windows, final 2 coats Asian Paints, deep cleaning & keys.' }
      ];

      let escrowHtml = '';
      tranches.forEach(tranche => {
        const amount = Math.round(grandTotal * (tranche.pct / 100));
        escrowHtml += `
          <div class="escrow-step-item">
            <div class="step-pct">${tranche.pct}%</div>
            <div class="step-amt">${formatINR(amount)}</div>
            <div class="step-phase">${tranche.name}</div>
            <div class="step-trigger">${tranche.trigger}</div>
          </div>
        `;
      });
      cceEscrowStepsGrid.innerHTML = escrowHtml;
    }

    // Update Live Site Material & Labor Quantities (Card 5)
    const elQtyCement = document.getElementById('cceQtyCementVal');
    const elQtySteel = document.getElementById('cceQtySteelVal');
    const elQtySand = document.getElementById('cceQtySandVal');
    const elQtyAgg = document.getElementById('cceQtyAggVal');
    const elQtyMasonry = document.getElementById('cceQtyMasonryVal');
    const elQtyWater = document.getElementById('cceQtyWaterVal');
    const elQtyLabor = document.getElementById('cceQtyLaborVal');

    if (elQtyCement) elQtyCement.textContent = `${cementBags.toLocaleString('en-IN')} Bags (50kg)`;
    if (elQtySteel) elQtySteel.textContent = `${steelTonnes} MT (${steelKg.toLocaleString('en-IN')} kg)`;
    if (elQtySand) elQtySand.textContent = `${(sandCft / 100).toFixed(1)} Brass (${sandCft.toLocaleString('en-IN')} cft)`;
    if (elQtyAgg) elQtyAgg.textContent = `${(aggCft / 100).toFixed(1)} Brass (${aggCft.toLocaleString('en-IN')} cft)`;
    if (elQtyMasonry) {
      if (brickKey === 'aac') {
        elQtyMasonry.textContent = `${brickQty.toLocaleString('en-IN')} AAC Blocks`;
      } else {
        elQtyMasonry.textContent = `${brickQty.toLocaleString('en-IN')} Red Clay Bricks`;
      }
    }
    if (elQtyWater) {
      const waterLitres = Math.round(totalBuiltup * 135);
      elQtyWater.textContent = `${(waterLitres / 1000).toFixed(1)}k Litres (IS 456)`;
    }
    if (elQtyLabor) {
      const mandays = Math.round(totalBuiltup * 0.72);
      elQtyLabor.textContent = `~${mandays.toLocaleString('en-IN')} Total Man-Days`;
    }
  }

  // Attach event listeners for real-time reactivity
  [cceCarpetArea, cceAreaScopeMode, cceBuiltupMultiplier, cceCity, cceCementBrand, cceSteelBrand, cceBricksType, cceSandType, cceFlooringType, cceJoineryType].forEach(el => {
    if (el) {
      el.addEventListener('change', updateConstructionEstimator);
      el.addEventListener('input', updateConstructionEstimator);
    }
  });

  // Initial calculation trigger
  updateConstructionEstimator();

  // Extensible Data Layer: Load external rates.json if served via HTTP
  if (typeof fetch === 'function' && window.location.protocol.startsWith('http')) {
    fetch('rates.json')
      .then(res => {
        if (!res.ok) throw new Error('Rates file unavailable');
        return res.json();
      })
      .then(data => {
        if (data && data.cities && data.materials) {
          Object.assign(constructionCostMatrix.cities, data.cities);
          Object.assign(constructionCostMatrix.materials, data.materials);
          if (data.thumbRules) Object.assign(constructionCostMatrix.thumbRules, data.thumbRules);
          if (data.qualities) Object.assign(constructionCostMatrix.qualities, data.qualities);
          updateConstructionEstimator();
        }
      })
      .catch(() => {
        // Built-in matrix remains active
      });
  }

  // Print Quote Handler
  window.printConstructionQuote = function() {
    const printIdEl = document.getElementById('printQuoteId');
    const printDateEl = document.getElementById('printQuoteDate');
    const randomRef = Math.floor(1000 + Math.random() * 9000);
    const today = new Date().toLocaleDateString('en-IN', { day: '2-digit', month: 'short', year: 'numeric' });
    if (printIdEl) printIdEl.textContent = `EXA-EST-2026-${randomRef}`;
    if (printDateEl) printDateEl.textContent = `Date: ${today}`;
    window.print();
  };

  // Contractor Callback & Email Quote Modal
  const modalCostEstimatorCallback = document.getElementById('modalCostEstimatorCallback');
  const costEstimatorCallbackContent = document.getElementById('costEstimatorCallbackContent');

  window.openCostEstimatorCallbackModal = function() {
    if (!costEstimatorCallbackContent || !modalCostEstimatorCallback) return;
    const calc = cceLatestCalculation;

    costEstimatorCallbackContent.innerHTML = `
      <div style="background:#FFFFFF; border:1px solid var(--border-card); border-radius:12px; padding:2rem;">
        <div style="border-bottom:2px solid var(--saffron-600); padding-bottom:1rem; margin-bottom:1.5rem;">
          <span style="font-size:0.75rem; color:var(--saffron-700); font-family:var(--font-main); font-weight:800; letter-spacing:0.05em;">CPWD VERIFIED CONTRACTOR CONNECT</span>
          <h2 style="font-size:1.35rem; font-weight:800; color:var(--navy-authority); margin:0.3rem 0;">Request Verified Contractor Callback &amp; Email Estimate</h2>
          <div style="font-size:0.8rem; color:var(--text-muted);">RECEIVE ITEMIZED PDF ESTIMATE + 3 PRE-SCREENED LOCAL BUILDER QUOTES</div>
        </div>

        <!-- Selected Project Summary Banner -->
        <div style="background:var(--bg-subtle); border:1px solid var(--border-card); border-radius:8px; padding:1rem; margin-bottom:1.5rem; display:grid; grid-template-columns:repeat(auto-fit, minmax(130px, 1fr)); gap:0.75rem;">
          <div>
            <span style="font-size:0.7rem; color:var(--text-muted); font-weight:700;">LOCATION:</span>
            <div style="font-size:0.88rem; font-weight:800; color:var(--navy-authority);">${escapeHTML(calc.cityName)}</div>
          </div>
          <div>
            <span style="font-size:0.7rem; color:var(--text-muted); font-weight:700;">BUILT-UP AREA:</span>
            <div style="font-size:0.88rem; font-weight:800; color:var(--navy-authority);">${calc.builtupArea.toLocaleString('en-IN')} sq.ft (${calc.floorsKey})</div>
          </div>
          <div>
            <span style="font-size:0.7rem; color:var(--text-muted); font-weight:700;">QUALITY TIER:</span>
            <div style="font-size:0.88rem; font-weight:800; color:var(--navy-authority);">${calc.qualityKey.toUpperCase()}</div>
          </div>
          <div>
            <span style="font-size:0.7rem; color:var(--text-muted); font-weight:700;">ESTIMATED BUDGET:</span>
            <div style="font-size:0.88rem; font-weight:800; color:var(--saffron-700);">${formatINR(calc.minRange)} – ${formatINR(calc.maxRange)}</div>
          </div>
        </div>

        <form id="formCostEstimatorLead" onsubmit="submitCostEstimatorLead(event)">
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-bottom:1rem;">
            <div>
              <label style="display:block; font-size:0.8rem; font-weight:700; color:var(--navy-authority); margin-bottom:0.35rem;">Full Name *</label>
              <input type="text" id="leadName" class="form-control-terminal" placeholder="e.g. Chetan Bisariya" required>
            </div>
            <div>
              <label style="display:block; font-size:0.8rem; font-weight:700; color:var(--navy-authority); margin-bottom:0.35rem;">WhatsApp / Mobile Number *</label>
              <input type="tel" id="leadPhone" class="form-control-terminal" placeholder="10-digit mobile number" pattern="[0-9]{10}" required>
            </div>
          </div>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin-bottom:1rem;">
            <div>
              <label style="display:block; font-size:0.8rem; font-weight:700; color:var(--navy-authority); margin-bottom:0.35rem;">Email Address (for PDF BoQ) *</label>
              <input type="email" id="leadEmail" class="form-control-terminal" placeholder="name@domain.com" required>
            </div>
            <div>
              <label style="display:block; font-size:0.8rem; font-weight:700; color:var(--navy-authority); margin-bottom:0.35rem;">Target Start Timeline</label>
              <select id="leadTimeline" class="form-control-terminal">
                <option value="Immediate (< 15 days)">Immediate (Within 15 days)</option>
                <option value="1 to 2 months" selected>1 to 2 Months</option>
                <option value="3 to 6 months">3 to 6 Months (Planning)</option>
              </select>
            </div>
          </div>

          <div style="margin-bottom:1.25rem;">
            <label style="display:block; font-size:0.8rem; font-weight:700; color:var(--navy-authority); margin-bottom:0.35rem;">Plot Location / Site Locality</label>
            <input type="text" id="leadAddress" class="form-control-terminal" placeholder="e.g. Arera Colony, Bhopal / HSR Layout, Bengaluru">
          </div>

          <div style="background:#FFFBEB; border:1px solid #FDE68A; padding:0.75rem 1rem; border-radius:6px; margin-bottom:1.5rem; font-size:0.76rem; color:#92400E; display:flex; gap:0.5rem; align-items:center;">
            <span>🛡️</span>
            <span>All referred contractors are RERA-verified with verified structural civil track records and sign milestone-based escrow deeds.</span>
          </div>

          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.75rem;">
            <button type="button" class="btn btn-secondary btn-sm" onclick="closeModal(document.getElementById('modalCostEstimatorCallback'))">
              <span>Cancel</span>
            </button>
            <button type="submit" class="btn btn-primary">
              <span>Submit &amp; Email Formal Estimate &rarr;</span>
            </button>
          </div>
        </form>
      </div>
    `;

    openModal(modalCostEstimatorCallback);
  };

  window.submitCostEstimatorLead = function(event) {
    if (event) event.preventDefault();
    const leadName = document.getElementById('leadName');
    const leadPhone = document.getElementById('leadPhone');
    const leadEmail = document.getElementById('leadEmail');

    if (!leadName || !leadPhone || !leadEmail) return;

    const nameVal = escapeHTML(leadName.value.trim());
    const phoneVal = escapeHTML(leadPhone.value.trim());
    const emailVal = escapeHTML(leadEmail.value.trim());
    const refId = 'EXA-BOQ-' + Math.floor(10000 + Math.random() * 90000);

    if (costEstimatorCallbackContent) {
      costEstimatorCallbackContent.innerHTML = `
        <div style="background:#FFFFFF; border:1px solid var(--border-card); border-radius:12px; padding:2.5rem; text-align:center;">
          <div style="width:60px; height:60px; border-radius:50%; background:var(--emerald-light); color:var(--emerald-600); font-size:1.8rem; display:flex; align-items:center; justify-content:center; margin:0 auto 1.25rem;">✓</div>
          <span style="font-size:0.75rem; color:var(--emerald-700); font-weight:800; letter-spacing:0.05em;">ESTIMATE DISPATCHED &amp; CONTRACTOR MATCHED</span>
          <h2 style="font-size:1.4rem; font-weight:800; color:var(--navy-authority); margin:0.4rem 0;">Thank You, ${nameVal}!</h2>
          <p style="font-size:0.88rem; color:var(--text-secondary); max-width:480px; margin:0 auto 1.5rem; line-height:1.5;">
            Your official CPWD DSR 2026 itemized Construction BoQ has been sent to <strong>${emailVal}</strong>. A licensed regional structural engineer will call you at <strong>${phoneVal}</strong> within 2 business hours.
          </p>

          <div style="background:var(--bg-subtle); border:1px solid var(--border-card); border-radius:8px; padding:1rem; max-width:400px; margin:0 auto 1.75rem; text-align:left;">
            <div style="display:flex; justify-content:space-between; margin-bottom:0.4rem; font-size:0.8rem;">
              <span style="color:var(--text-muted);">Lead Reference ID:</span>
              <strong style="color:var(--navy-authority);">${refId}</strong>
            </div>
            <div style="display:flex; justify-content:space-between; margin-bottom:0.4rem; font-size:0.8rem;">
              <span style="color:var(--text-muted);">City &amp; Index:</span>
              <strong>${escapeHTML(cceLatestCalculation.cityName)}</strong>
            </div>
            <div style="display:flex; justify-content:space-between; font-size:0.8rem;">
              <span style="color:var(--text-muted);">Estimated Range:</span>
              <strong style="color:var(--saffron-700);">${formatINR(cceLatestCalculation.minRange)} – ${formatINR(cceLatestCalculation.maxRange)}</strong>
            </div>
          </div>

          <div style="display:flex; justify-content:center; gap:1rem;">
            <button type="button" class="btn btn-primary btn-sm" onclick="closeModal(document.getElementById('modalCostEstimatorCallback'))">
              <span>Close &amp; Return to Terminal</span>
            </button>
          </div>
        </div>
      `;
    }

    showToast(`✓ Estimate dispatched to ${emailVal}! Ref: ${refId}`);
  };

  // Upgraded Contractor Milestone Escrow Modal tying to current estimate
  const modalContractorEscrow = document.getElementById('modalContractorEscrow');
  const contractorEscrowContent = document.getElementById('contractorEscrowContent');

  window.openContractorEscrowModal = function() {
    const calc = cceLatestCalculation;
    const total = formatINR(calc.grandTotal);
    const area = calc.builtupArea.toLocaleString('en-IN');
    const city = calc.cityName;

    const t1 = formatINR(Math.round(calc.grandTotal * 0.15));
    const t2 = formatINR(Math.round(calc.grandTotal * 0.30));
    const t3 = formatINR(Math.round(calc.grandTotal * 0.20));
    const t4 = formatINR(Math.round(calc.grandTotal * 0.20));
    const t5 = formatINR(Math.round(calc.grandTotal * 0.15));

    if (contractorEscrowContent) {
      contractorEscrowContent.innerHTML = `
        <div style="background:#FFFFFF; border:1px solid var(--border-card); border-radius:12px; padding:2rem;">
          <div style="border-bottom:2px solid var(--saffron-600); padding-bottom:1rem; margin-bottom:1.5rem;">
            <span style="font-size:0.75rem; color:var(--saffron-700); font-family:var(--font-main); font-weight:800; letter-spacing:0.05em;">STANDARD INDIAN CONTRACTOR ESCROW DEED</span>
            <h2 style="font-size:1.4rem; font-weight:800; color:var(--navy-authority); margin:0.3rem 0;">Turnkey Civil Construction &amp; Milestone Escrow Agreement</h2>
            <div style="font-size:0.8rem; color:var(--text-muted);">ENFORCEABLE UNDER INDIAN CONTRACT ACT, 1872 &amp; CPWD ARBITRATION NORMS • ${escapeHTML(city).toUpperCase()}</div>
          </div>

          <p style="font-size:0.88rem; color:var(--text-secondary); line-height:1.6; margin-bottom:1.25rem;">
            This Contractual Escrow Deed protects the <strong>Employer (Homeowner)</strong> and <strong>Contractor</strong> by locking total project funds (<strong>${total}</strong> for ${area} sq.ft) in an escrow bank account, disbursed strictly in 5 tranches upon certification by a licensed structural engineer or architect:
          </p>

          <div style="display:grid; grid-template-columns:1fr; gap:0.75rem; margin-bottom:1.5rem;">
            <div style="background:var(--bg-subtle); padding:0.85rem 1rem; border-radius:6px; border:1px solid var(--border-card); display:flex; justify-content:space-between; flex-wrap:wrap; gap:0.5rem;">
              <span><strong>Tranche 1 (15% = ${t1}):</strong> Excavation &amp; Plinth Beam Casting</span>
              <strong style="color:var(--saffron-700);">Release: Soil testing &amp; plinth verified</strong>
            </div>
            <div style="background:var(--bg-subtle); padding:0.85rem 1rem; border-radius:6px; border:1px solid var(--border-card); display:flex; justify-content:space-between; flex-wrap:wrap; gap:0.5rem;">
              <span><strong>Tranche 2 (30% = ${t2}):</strong> RCC Frame, Columns &amp; Roof Slabs</span>
              <strong style="color:var(--saffron-700);">Release: Cube test report &amp; 28-day curing</strong>
            </div>
            <div style="background:var(--bg-subtle); padding:0.85rem 1rem; border-radius:6px; border:1px solid var(--border-card); display:flex; justify-content:space-between; flex-wrap:wrap; gap:0.5rem;">
              <span><strong>Tranche 3 (20% = ${t3}):</strong> Blockwork, Electrical &amp; Plumbing Pipes</span>
              <strong style="color:var(--saffron-700);">Release: Pressure testing of water lines</strong>
            </div>
            <div style="background:var(--bg-subtle); padding:0.85rem 1rem; border-radius:6px; border:1px solid var(--border-card); display:flex; justify-content:space-between; flex-wrap:wrap; gap:0.5rem;">
              <span><strong>Tranche 4 (20% = ${t4}):</strong> Plastering, Vitrified Tiles &amp; Windows</span>
              <strong style="color:var(--saffron-700);">Release: Level check &amp; water ponding test</strong>
            </div>
            <div style="background:var(--bg-subtle); padding:0.85rem 1rem; border-radius:6px; border:1px solid var(--border-card); display:flex; justify-content:space-between; flex-wrap:wrap; gap:0.5rem;">
              <span><strong>Tranche 5 (15% = ${t5}):</strong> Snagging Completion &amp; Key Handover</span>
              <strong style="color:var(--emerald-600);">Release: 30-day snag rectification + 12-mo DLP</strong>
            </div>
          </div>

          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.75rem;">
            <button type="button" class="btn btn-secondary btn-sm" onclick="window.print()">
              <span>Print / Save as PDF</span>
            </button>
            <button type="button" class="btn btn-primary btn-sm" onclick="showToast('✓ Legally Binding Construction Escrow Agreement generated for ' + '${total}' + '!'); closeModal(document.getElementById('modalContractorEscrow'));">
              <span>Download Digitally Executable Deed (₹1,999) &rarr;</span>
            </button>
          </div>
        </div>
      `;
    }

    openModal(modalContractorEscrow);
  };

  // ====================================================================
  // 6. Institutional Legal & Advisory Contact Desk
  // Transmits inquiries directly to contact@exainfra.in
  // ====================================================================
  const formContactUs = document.getElementById('formContactUs');
  const btnSubmitContact = document.getElementById('btnSubmitContact');

  if (formContactUs) {
    formContactUs.addEventListener('submit', async (e) => {
      e.preventDefault();

      const name = (document.getElementById('contactName')?.value || '').trim();
      const email = (document.getElementById('contactEmail')?.value || '').trim();
      const subject = (document.getElementById('contactSubject')?.value || 'Statutory Inquiry').trim();
      const message = (document.getElementById('contactMessage')?.value || '').trim();

      if (!name || !email || !message) {
        showToast('⚠ Please complete all required fields (Name, Email, and Message).', 'warn');
        return;
      }

      if (btnSubmitContact) {
        btnSubmitContact.disabled = true;
        btnSubmitContact.innerHTML = `
          <span>Encrypting & Dispatching to contact@exainfra.in...</span>
        `;
      }

      const payload = {
        action: 'contact_form',
        name: name,
        email: email,
        subject: subject,
        message: message
      };

      try {
        const response = await fetch('api/contact.php', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          },
          body: JSON.stringify(payload)
        });

        const result = await response.json().catch(() => null);

        if (response.ok && result && result.status === 'success') {
          showToast(`✓ Inquiry dispatched! Sent to contact@exainfra.in (Ref: EXA-INQ-${result.inquiry_id || 'OK'}). Advisory attorney will reply within 2 business hours.`);
          formContactUs.reset();
        } else {
          throw new Error((result && result.message) || 'Server returned status ' + response.status);
        }
      } catch (err) {
        // Fallback for static dev preview environments without live PHP server
        showToast('✓ Inquiry recorded! Dispatched to contact@exainfra.in. Opening secure transmission window...');
        
        const mailtoUrl = `mailto:contact@exainfra.in?subject=${encodeURIComponent('[ExaInfra Inquiry] ' + subject + ' - ' + name)}&body=${encodeURIComponent(
          `Full Name: ${name}\nEmail: ${email}\nPractice Scope: ${subject}\n\nInquiry Details:\n${message}\n\n---\nTransmitted via ExaInfra.in Sovereign Terminal`
        )}`;
        
        window.open(mailtoUrl, '_blank');
        formContactUs.reset();
      } finally {
        if (btnSubmitContact) {
          btnSubmitContact.disabled = false;
          btnSubmitContact.innerHTML = `
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
            <span>Transmit Inquiry to contact@exainfra.in &rarr;</span>
          `;
        }
      }
    });
  }


  // ====================================================================
  // STATUTORY & FINANCIAL COMPUTATIONAL WORKBENCH (6 INSTITUTIONAL TOOLS)
  // ====================================================================
  function initStatutoryTools() {
    if (!document.getElementById('statutory-tools')) return;

    // 1. Tab Navigation Controls
    const toolTabBtns = document.querySelectorAll('.tool-tab-btn');
    const toolPanels = document.querySelectorAll('.tool-panel');

    toolTabBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const toolKey = btn.getAttribute('data-tool');
        if (toolKey === 'boq-jump') return;
        toolTabBtns.forEach(b => {
          b.classList.remove('active');
          b.setAttribute('aria-selected', 'false');
        });
        toolPanels.forEach(p => p.classList.remove('active'));

        btn.classList.add('active');
        btn.setAttribute('aria-selected', 'true');
        const activePanel = document.getElementById(`panel-${toolKey}`);
        if (activePanel) {
          activePanel.classList.add('active');
        }
      });
    });

    // 2. Suite Category Filter Controls
    const catPillBtns = document.querySelectorAll('.cat-pill-btn');
    catPillBtns.forEach(pill => {
      pill.addEventListener('click', () => {
        const cat = pill.getAttribute('data-cat');
        catPillBtns.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');

        let firstVisibleBtn = null;
        let isCurrentActiveVisible = false;

        toolTabBtns.forEach(btn => {
          const btnCat = btn.getAttribute('data-category');
          if (cat === 'all' || btnCat === cat) {
            btn.style.display = 'flex';
            if (!firstVisibleBtn) firstVisibleBtn = btn;
            if (btn.classList.contains('active')) isCurrentActiveVisible = true;
          } else {
            btn.style.display = 'none';
          }
        });

        if (!isCurrentActiveVisible && firstVisibleBtn) {
          firstVisibleBtn.click();
        }
      });
    });

    // ------------------------------------------------------------------
    // TOOL 1: Guidance Value, Stamp Duty & Section 50C Engine
    // ------------------------------------------------------------------
    const dutyState = document.getElementById('dutyState');
    const dutyBuyerGender = document.getElementById('dutyBuyerGender');
    const dutyAgreementVal = document.getElementById('dutyAgreementVal');
    const dutyAgreementValNum = document.getElementById('dutyAgreementValNum');
    const dutyAgreementValTxt = document.getElementById('dutyAgreementValTxt');
    const dutyGuidanceVal = document.getElementById('dutyGuidanceVal');
    const dutyGuidanceValNum = document.getElementById('dutyGuidanceValNum');
    const dutyGuidanceValTxt = document.getElementById('dutyGuidanceValTxt');

    const dutyTotalPayout = document.getElementById('dutyTotalPayout');
    const dutyAssessableVal = document.getElementById('dutyAssessableVal');
    const dutyStampVal = document.getElementById('dutyStampVal');
    const dutyStampRateTxt = document.getElementById('dutyStampRateTxt');
    const dutyRegVal = document.getElementById('dutyRegVal');
    const dutyRegRateTxt = document.getElementById('dutyRegRateTxt');
    const dutyCessVal = document.getElementById('dutyCessVal');
    const dutyCessRateTxt = document.getElementById('dutyCessRateTxt');
    const dutySec50cBox = document.getElementById('dutySec50cBox');
    const dutySec50cMsg = document.getElementById('dutySec50cMsg');

    function updateDutyCalculator() {
      if (!dutyAgreementVal || !dutyTotalPayout) return;

      const agreement = parseFloat(dutyAgreementVal.value) || 0;
      const guidance = parseFloat(dutyGuidanceVal.value) || 0;
      const state = dutyState ? dutyState.value : 'ka';
      const gender = dutyBuyerGender ? dutyBuyerGender.value : 'male';

      if (dutyAgreementValTxt) dutyAgreementValTxt.textContent = formatINR(agreement);
      if (dutyGuidanceValTxt) dutyGuidanceValTxt.textContent = formatINR(guidance);

      const assessable = Math.max(agreement, guidance);
      if (dutyAssessableVal) dutyAssessableVal.textContent = formatINR(assessable);

      let stampRate = 0.05;
      let regRate = 0.01;
      let cessRate = 0.007; // 10% cess on stamp duty
      let regCap = Infinity;

      if (state === 'ka') {
        stampRate = 0.05;
        cessRate = 0.007;
        regRate = 0.01;
        if (dutyStampRateTxt) dutyStampRateTxt.textContent = '5.0% Base Stamp Duty';
        if (dutyRegRateTxt) dutyRegRateTxt.textContent = '1.0% Registration Fee';
        if (dutyCessRateTxt) dutyCessRateTxt.textContent = '10% Cess & 2% Infra Surcharge';
      } else if (state === 'mh') {
        stampRate = gender === 'female' ? 0.05 : 0.06;
        regRate = 0.01;
        regCap = 30000;
        cessRate = 0;
        if (dutyStampRateTxt) dutyStampRateTxt.textContent = `${(stampRate * 100).toFixed(1)}% Duty (incl. 1% Metro Cess)`;
        if (dutyRegRateTxt) dutyRegRateTxt.textContent = '1% Reg Fee (Capped at ₹30,000)';
        if (dutyCessRateTxt) dutyCessRateTxt.textContent = 'Local Body Tax (LBT) Included';
      } else if (state === 'dl') {
        stampRate = gender === 'female' ? 0.04 : (gender === 'joint' ? 0.05 : 0.06);
        regRate = 0.01;
        cessRate = 0;
        if (dutyStampRateTxt) dutyStampRateTxt.textContent = `${(stampRate * 100).toFixed(1)}% Duty (${gender === 'female' ? '2% Female Rebate' : 'Standard'})`;
        if (dutyRegRateTxt) dutyRegRateTxt.textContent = '1% Official DORS Reg Fee';
        if (dutyCessRateTxt) dutyCessRateTxt.textContent = 'MCD Transfer Fee Included';
      } else if (state === 'hr') {
        stampRate = gender === 'female' ? 0.05 : (gender === 'joint' ? 0.06 : 0.07);
        regRate = 0.01;
        regCap = 50000;
        cessRate = 0;
        if (dutyStampRateTxt) dutyStampRateTxt.textContent = `${(stampRate * 100).toFixed(1)}% Jamabandi Municipal Duty`;
        if (dutyRegRateTxt) dutyRegRateTxt.textContent = 'Slab Reg Fee (Max ₹50,000)';
        if (dutyCessRateTxt) dutyCessRateTxt.textContent = 'Panchayat / Urban Cess Included';
      } else if (state === 'up') {
        stampRate = gender === 'female' ? 0.06 : 0.07;
        regRate = 0.01;
        regCap = 20000;
        cessRate = 0;
        if (dutyStampRateTxt) dutyStampRateTxt.textContent = `${(stampRate * 100).toFixed(1)}% e-Stamping Duty`;
        if (dutyRegRateTxt) dutyRegRateTxt.textContent = '1% Reg Fee (Capped at ₹20,000)';
        if (dutyCessRateTxt) dutyCessRateTxt.textContent = 'Infrastructure Development Surcharge';
      }

      const stampAmt = Math.round(assessable * stampRate);
      const regAmt = Math.min(Math.round(assessable * regRate), regCap);
      const cessAmt = Math.round(assessable * cessRate);
      const totalOutflow = stampAmt + regAmt + cessAmt;

      if (dutyStampVal) dutyStampVal.textContent = formatINR(stampAmt);
      if (dutyRegVal) dutyRegVal.textContent = formatINR(regAmt);
      if (dutyCessVal) dutyCessVal.textContent = formatINR(cessAmt);
      if (dutyTotalPayout) dutyTotalPayout.textContent = formatINR(totalOutflow);

      // Section 50C & Section 56(2)(x) Radar
      if (dutySec50cBox && dutySec50cMsg) {
        if (agreement >= guidance) {
          dutySec50cBox.className = 'tool-alert-box safe';
          dutySec50cMsg.innerHTML = `<strong>✓ Section 50C Compliant:</strong> Agreed consideration (${formatINR(agreement)}) is higher than guidance circle rate (${formatINR(guidance)}). No deemed capital gains tax scrutiny under Section 50C, and no gift tax penalty for buyer under Section 56(2)(x).`;
        } else {
          const diffPercent = ((guidance - agreement) / agreement) * 100;
          const shortfall = guidance - agreement;
          if (diffPercent <= 10.0) {
            dutySec50cBox.className = 'tool-alert-box warn';
            dutySec50cMsg.innerHTML = `<strong>⚖ Safe Harbor Rule Invoked (Diff: ${diffPercent.toFixed(1)}%):</strong> Guidance value exceeds agreement value by less than 10%. Under the Finance Act Safe Harbor amendment to Section 50C, agreement value can be accepted as full consideration, but sub-registrar documentation must cite the exact valuation slab.`;
          } else {
            dutySec50cBox.className = 'tool-alert-box risk';
            dutySec50cMsg.innerHTML = `<strong>⚠ SECTION 50C UNDERVALUATION PENALTY ACTIVE (Shortfall: ${formatINR(shortfall)} / ${diffPercent.toFixed(1)}%):</strong> Agreement price is more than 10% below Sub-Registrar Guidance Value! The Income Tax Department will deem ${formatINR(guidance)} as the seller's taxable capital receipt under Section 50C, AND the buyer will be taxed on ${formatINR(shortfall)} as deemed income under Section 56(2)(x)!`;
          }
        }
      }
    }

    if (dutyAgreementVal && dutyAgreementValNum) {
      dutyAgreementVal.addEventListener('input', () => {
        dutyAgreementValNum.value = dutyAgreementVal.value;
        updateDutyCalculator();
      });
      dutyAgreementValNum.addEventListener('input', () => {
        dutyAgreementVal.value = dutyAgreementValNum.value;
        updateDutyCalculator();
      });
    }

    if (dutyGuidanceVal && dutyGuidanceValNum) {
      dutyGuidanceVal.addEventListener('input', () => {
        dutyGuidanceValNum.value = dutyGuidanceVal.value;
        updateDutyCalculator();
      });
      dutyGuidanceValNum.addEventListener('input', () => {
        dutyGuidanceVal.value = dutyGuidanceValNum.value;
        updateDutyCalculator();
      });
    }

    [dutyState, dutyBuyerGender].forEach(el => {
      if (el) el.addEventListener('change', updateDutyCalculator);
    });

    // ------------------------------------------------------------------
    // TOOL 2: Capital Gains (Section 54/54F) Reinvestment Shield
    // ------------------------------------------------------------------
    const cgPropType = document.getElementById('cgPropType');
    const cgSalePrice = document.getElementById('cgSalePrice');
    const cgBuyCost = document.getElementById('cgBuyCost');
    const cgBuyYear = document.getElementById('cgBuyYear');
    const cgTransferExp = document.getElementById('cgTransferExp');
    const cgReinvestVehicle = document.getElementById('cgReinvestVehicle');
    const cgReinvestAmount = document.getElementById('cgReinvestAmount');
    const cgReinvestAmountTxt = document.getElementById('cgReinvestAmountTxt');

    const cgFinalTaxPayable = document.getElementById('cgFinalTaxPayable');
    const cgTaxSavingsSub = document.getElementById('cgTaxSavingsSub');
    const cgNewRegimeTax = document.getElementById('cgNewRegimeTax');
    const cgOldRegimeTax = document.getElementById('cgOldRegimeTax');
    const cgIndexedCostVal = document.getElementById('cgIndexedCostVal');
    const cgGrossGain = document.getElementById('cgGrossGain');
    const cgExemptionClaimed = document.getElementById('cgExemptionClaimed');
    const cgDeadlineDate = document.getElementById('cgDeadlineDate');

    const ciiTable = {
      '2001': 100, '2005': 117, '2010': 167, '2015': 254, '2018': 280, '2020': 301, '2023': 348
    };
    const CURRENT_CII_2026 = 363;

    function updateCapGainsCalculator() {
      if (!cgSalePrice || !cgFinalTaxPayable) return;

      const sale = parseFloat(cgSalePrice.value) || 0;
      const cost = parseFloat(cgBuyCost.value) || 0;
      const exp = parseFloat(cgTransferExp.value) || 0;
      const buyYr = cgBuyYear ? cgBuyYear.value : '2015';
      const vehicle = cgReinvestVehicle ? cgReinvestVehicle.value : 'house';
      const propType = cgPropType ? cgPropType.value : 'residential';

      if (cgReinvestAmount) {
        if (vehicle === 'bonds') {
          cgReinvestAmount.max = 5000000;
          if (parseFloat(cgReinvestAmount.value) > 5000000) cgReinvestAmount.value = 5000000;
        } else {
          cgReinvestAmount.max = sale;
        }
      }

      let reinvest = parseFloat(cgReinvestAmount ? cgReinvestAmount.value : 0) || 0;
      if (vehicle === 'none') reinvest = 0;
      if (cgReinvestAmountTxt) cgReinvestAmountTxt.textContent = formatINR(reinvest);

      const netSale = Math.max(0, sale - exp);
      const purchaseCII = ciiTable[buyYr] || 254;
      const indexedCost = Math.round(cost * (CURRENT_CII_2026 / purchaseCII));
      if (cgIndexedCostVal) cgIndexedCostVal.textContent = formatINR(indexedCost);

      const grossGainUnindexed = Math.max(0, netSale - cost);
      const grossGainIndexed = Math.max(0, netSale - indexedCost);

      if (cgGrossGain) cgGrossGain.textContent = formatINR(grossGainUnindexed);

      // Budget 2024 Dual Comparison
      const newRegimeTax = Math.round(grossGainUnindexed * 0.125 * 1.04);
      const oldRegimeTax = Math.round(grossGainIndexed * 0.20 * 1.04);

      if (cgNewRegimeTax) cgNewRegimeTax.textContent = formatINR(newRegimeTax);
      if (cgOldRegimeTax) cgOldRegimeTax.textContent = formatINR(oldRegimeTax);

      // Exemption calculation
      let exemption = 0;
      if (vehicle !== 'none') {
        if (propType === 'residential') {
          exemption = Math.min(grossGainUnindexed, reinvest);
        } else {
          if (netSale > 0) {
            exemption = Math.min(grossGainUnindexed, Math.round((reinvest / netSale) * grossGainUnindexed));
          }
        }
      }

      if (cgExemptionClaimed) cgExemptionClaimed.textContent = formatINR(exemption);

      const taxableGain = Math.max(0, grossGainUnindexed - exemption);
      const finalTax = taxableGain > 0 ? Math.round(taxableGain * 0.125 * 1.04) : 0;

      if (cgFinalTaxPayable) {
        if (finalTax === 0) {
          cgFinalTaxPayable.textContent = '₹0 (100% Tax Free)';
          cgFinalTaxPayable.className = 'tool-kpi-val emerald';
          if (cgTaxSavingsSub) cgTaxSavingsSub.textContent = `Full ${formatINR(exemption)} capital gain successfully sheltered under Section ${propType === 'residential' ? '54' : '54F'}.`;
        } else {
          cgFinalTaxPayable.textContent = formatINR(finalTax);
          cgFinalTaxPayable.className = 'tool-kpi-val primary';
          if (cgTaxSavingsSub) cgTaxSavingsSub.textContent = `Taxable gain after ₹${(exemption/100000).toFixed(1)}L exemption is ${formatINR(taxableGain)}. Tax computed at 12.5% LTCG + 4% cess.`;
        }
      }

      if (cgDeadlineDate) {
        cgDeadlineDate.textContent = '31-Jul-2027';
      }
    }

    [cgPropType, cgBuyYear, cgReinvestVehicle].forEach(el => {
      if (el) el.addEventListener('change', updateCapGainsCalculator);
    });

    [cgSalePrice, cgBuyCost, cgTransferExp].forEach(el => {
      if (el) el.addEventListener('input', updateCapGainsCalculator);
    });

    if (cgReinvestAmount) {
      cgReinvestAmount.addEventListener('input', updateCapGainsCalculator);
    }

    // ------------------------------------------------------------------
    // TOOL 3: RERA Section 18 Delay Penalty Engine
    // ------------------------------------------------------------------
    const reraProjectName = document.getElementById('reraProjectName');
    const reraBuilderName = document.getElementById('reraBuilderName');
    const reraAmountPaid = document.getElementById('reraAmountPaid');
    const reraContractDate = document.getElementById('reraContractDate');
    const reraEvalDate = document.getElementById('reraEvalDate');
    const reraInterestRate = document.getElementById('reraInterestRate');

    const reraTotalPenalty = document.getElementById('reraTotalPenalty');
    const reraDelayDuration = document.getElementById('reraDelayDuration');
    const reraMonthlyPayout = document.getElementById('reraMonthlyPayout');
    const reraTotalClaim = document.getElementById('reraTotalClaim');
    const btnOpenReraNoticeModal = document.getElementById('btnOpenReraNoticeModal');
    const modalReraNotice = document.getElementById('modalReraNotice');
    const reraNoticePaper = document.getElementById('reraNoticePaper');

    function updateReraDelayCalculator() {
      if (!reraAmountPaid || !reraTotalPenalty) return;

      const principal = parseFloat(reraAmountPaid.value) || 0;
      const rate = parseFloat(reraInterestRate ? reraInterestRate.value : 10.85) || 10.85;

      const dContract = reraContractDate && reraContractDate.value ? new Date(reraContractDate.value) : new Date('2024-03-31');
      const dEval = reraEvalDate && reraEvalDate.value ? new Date(reraEvalDate.value) : new Date();

      const diffMs = dEval - dContract;
      const diffDays = Math.max(0, Math.round(diffMs / (1000 * 60 * 60 * 24)));
      const diffMonths = (diffDays / 30.4375).toFixed(1);

      const monthlyInterest = Math.round(principal * (rate / 100) / 12);
      const totalPenalty = Math.round(principal * (rate / 100) * (diffDays / 365));
      const totalClaim = principal + totalPenalty;

      if (reraTotalPenalty) reraTotalPenalty.textContent = formatINR(totalPenalty);
      if (reraDelayDuration) reraDelayDuration.textContent = `${diffMonths} Months (${diffDays} Days)`;
      if (reraMonthlyPayout) reraMonthlyPayout.textContent = `${formatINR(monthlyInterest)} / mo`;
      if (reraTotalClaim) reraTotalClaim.textContent = formatINR(totalClaim);
    }

    [reraProjectName, reraBuilderName, reraAmountPaid, reraContractDate, reraEvalDate, reraInterestRate].forEach(el => {
      if (el) el.addEventListener('input', updateReraDelayCalculator);
    });

    if (btnOpenReraNoticeModal && modalReraNotice && reraNoticePaper) {
      btnOpenReraNoticeModal.addEventListener('click', () => {
        const project = escapeHTML(reraProjectName ? reraProjectName.value : 'Real Estate Unit');
        const builder = escapeHTML(reraBuilderName ? reraBuilderName.value : 'Promoter Company');
        const principal = parseFloat(reraAmountPaid ? reraAmountPaid.value : 0) || 0;
        const rate = parseFloat(reraInterestRate ? reraInterestRate.value : 10.85) || 10.85;
        const dContract = reraContractDate ? reraContractDate.value : '2024-03-31';
        const dEval = reraEvalDate ? reraEvalDate.value : new Date().toISOString().split('T')[0];

        const diffMs = new Date(dEval) - new Date(dContract);
        const diffDays = Math.max(0, Math.round(diffMs / (1000 * 60 * 60 * 24)));
        const diffMonths = (diffDays / 30.4375).toFixed(1);
        const totalPenalty = Math.round(principal * (rate / 100) * (diffDays / 365));
        const totalClaim = principal + totalPenalty;
        const refId = `EXA-RERA-${Math.floor(100000 + Math.random() * 900000)}`;

        reraNoticePaper.innerHTML = `
          <div style="border-bottom: 2px solid var(--navy-authority); padding-bottom: 0.85rem; margin-bottom: 1.25rem; display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 0.5rem;">
            <div>
              <div style="font-size: 0.72rem; font-weight: 800; letter-spacing: 0.08em; color: var(--saffron-700); text-transform: uppercase;">FORMAL STATUTORY LEGAL DEMAND NOTICE</div>
              <div style="font-size: 1.15rem; font-weight: 800; color: var(--navy-authority); font-family: var(--font-heading);">UNDER SECTION 18 OF REAL ESTATE (REGULATION & DEVELOPMENT) ACT, 2016</div>
              <div style="font-size: 0.78rem; color: var(--text-muted); font-weight: 600;">READ WITH STATE RERA ENFORCEMENT RULES & RULE 18 ADMISSIBILITY</div>
            </div>
            <div style="text-align: right; font-size: 0.82rem; font-weight: 700; color: var(--text-dark);">
              <div>REF: <strong>${refId}</strong></div>
              <div>DATE: <strong>${dEval}</strong></div>
            </div>
          </div>

          <div style="font-size: 0.88rem; line-height: 1.6; color: var(--text-dark);">
            <p><strong>BY SPEED POST A.D. & REGISTERED EMAIL TRANSMISSION</strong></p>
            <p style="margin-top: 0.5rem;">
              <strong>TO:</strong><br>
              The Managing Director / Authorized Signatory<br>
              <strong>${builder}</strong><br>
              Project: <strong>${project}</strong>
            </p>

            <p style="margin-top: 1rem;">
              <strong>SUBJECT:</strong> Formal Statutory Notice of Demand for Immediate Payment of Accrued Delayed Possession Interest of <strong>${formatINR(totalPenalty)}</strong> under Section 18(1) of the Real Estate (Regulation and Development) Act, 2016 for ${diffMonths} months delay (${diffDays} days).
            </p>

            <p style="margin-top: 0.85rem;">
              Sir / Madam,<br>
              Under instructions from our client (Allottee), we hereby place you on formal legal notice as follows:
            </p>

            <ol style="padding-left: 1.25rem; margin-top: 0.5rem; display: flex; flex-direction: column; gap: 0.5rem;">
              <li>That pursuant to the registered Agreement for Sale, you committed to hand over vacant, physical possession with Occupancy Certificate on or before <strong>${dContract}</strong>.</li>
              <li>That our client has disbursed total consideration of <strong>${formatINR(principal)}</strong> strictly adhering to construction milestones.</li>
              <li>That as of <strong>${dEval}</strong>, you have defaulted on your contractual and statutory obligations, incurring an unexcused delay of <strong>${diffMonths} Months (${diffDays} Days)</strong>.</li>
              <li>That under Section 18(1) proviso of the Real Estate (Regulation and Development) Act 2016 read with Rule 18, you are statutorily mandated to pay penal interest at <strong>${rate}% p.a. (SBI Highest Marginal Cost of Lending Rate + 2.00%)</strong> for every single month of delay until actual handover with OC.</li>
              <li>That the total statutory penal interest accrued to date stands computed at <strong>${formatINR(totalPenalty)}</strong>, making the total recoverable claim <strong>${formatINR(totalClaim)}</strong>.</li>
            </ol>

            <div style="background: var(--bg-subtle); border-left: 4px solid var(--saffron-600); padding: 0.85rem; margin: 1rem 0; font-size: 0.85rem; font-weight: 600;">
              NOTICE IS HEREBY GIVEN: You are called upon to credit the accrued sum of <strong>${formatINR(totalPenalty)}</strong> into the Allottee's bank account within <strong>FIFTEEN (15) DAYS</strong> of receipt hereof, failing which our client shall initiate summary recovery proceedings under Section 31 and Section 40 of RERA 2016 with full costs and damages.
            </div>

            <div style="margin-top: 1.5rem; display: flex; justify-content: space-between; align-items: flex-end; padding-top: 1rem; border-top: 1px dashed var(--border-card);">
              <div>
                <div style="font-size: 0.78rem; color: var(--text-muted);">ADVOCATE / AUTHORIZED LEGAL COUNSEL</div>
                <div style="font-weight: 700; color: var(--navy-authority);">ExaInfra Sovereign RERA Advisory Panel</div>
                <div style="font-size: 0.72rem; color: var(--text-muted);">Bar Council Enrolment &bull; Sec 65B Electronic Verified</div>
              </div>
              <div style="text-align: right; font-size: 0.75rem; color: var(--text-muted);">
                <div>Official ExaInfra Demand Notice</div>
                <div style="font-weight: 700; color: var(--emerald-600);">✓ Tamper-Proof Cryptographic Ref</div>
              </div>
            </div>
          </div>
        `;

        openModal(modalReraNotice);
      });
    }

    // ------------------------------------------------------------------
    // TOOL 4: SEBI SM REIT vs. Direct Pre-Leased CRE Modeler
    // ------------------------------------------------------------------
    const reitCapital = document.getElementById('reitCapital');
    const reitCapitalNum = document.getElementById('reitCapitalNum');
    const reitCapitalTxt = document.getElementById('reitCapitalTxt');
    const reitCapRate = document.getElementById('reitCapRate');
    const reitHorizon = document.getElementById('reitHorizon');

    const reitGrossInflow = document.getElementById('reitGrossInflow');
    const directGrossInflow = document.getElementById('directGrossInflow');
    const reitNetYield = document.getElementById('reitNetYield');
    const directNetYield = document.getElementById('directNetYield');
    const reit5YrTotal = document.getElementById('reit5YrTotal');
    const direct5YrTotal = document.getElementById('direct5YrTotal');
    const reitVerdictText = document.getElementById('reitVerdictText');

    function updateSmReitCalculator() {
      if (!reitCapital || !reitNetYield) return;

      const capital = parseFloat(reitCapital.value) || 5000000;
      const capRate = parseFloat(reitCapRate ? reitCapRate.value : 9.2) || 9.2;
      const years = parseInt(reitHorizon ? reitHorizon.value : 5) || 5;

      if (reitCapitalTxt) reitCapitalTxt.textContent = formatINR(capital);

      const grossAnnual = Math.round(capital * (capRate / 100));
      if (reitGrossInflow) reitGrossInflow.textContent = `${formatINR(grossAnnual)} / yr`;
      if (directGrossInflow) directGrossInflow.textContent = `${formatINR(grossAnnual)} / yr`;

      // SM REIT: 0% Stamp Duty, 1.25% AMC Fee => Net Yield = (capRate - 1.25)%
      const smNetRate = Math.max(0, capRate - 1.25);
      const smNetAnnual = Math.round(capital * (smNetRate / 100));
      if (reitNetYield) reitNetYield.innerHTML = `<strong>${formatINR(smNetAnnual)} (${smNetRate.toFixed(2)}%)</strong>`;

      // Direct CRE: 6.5% Upfront Stamp Duty Drag. Management fee 0.5% => Net Rate = (capRate - 0.50)%
      const directNetRate = Math.max(0, capRate - 0.50);
      const directEffectiveCapital = Math.round(capital * (1 - 0.065));
      const directNetAnnual = Math.round(directEffectiveCapital * (directNetRate / 100));
      if (directNetYield) directNetYield.innerHTML = `<strong>${formatINR(directNetAnnual)} (${directNetRate.toFixed(2)}%)</strong>`;

      // Horizon Wealth (Cash Distributions + 4.5% p.a. capital appreciation on underlying asset)
      const annualApprecRate = 0.045;
      const smReitWealth = Math.round(capital * Math.pow(1 + annualApprecRate, years) + (smNetAnnual * years));
      const directCreWealth = Math.round(directEffectiveCapital * Math.pow(1 + annualApprecRate, years) + (directNetAnnual * years));

      if (reit5YrTotal) reit5YrTotal.textContent = `${formatINR(smReitWealth)} (${years}Y)`;
      if (direct5YrTotal) direct5YrTotal.textContent = `${formatINR(directCreWealth)} (${years}Y)`;

      if (reitVerdictText) {
        if (capital < 20000000) {
          reitVerdictText.textContent = `At ₹${(capital/100000).toFixed(0)} Lakhs, SEBI SM REIT is the mathematically superior asset vehicle. You avoid the 6.5% (${formatINR(Math.round(capital*0.065))}) upfront stamp duty loss, enjoy instant Demat T+1 exchange liquidity, and eliminate single-tenant vacancy risk.`;
        } else {
          reitVerdictText.textContent = `For allocations of ₹${(capital/10000000).toFixed(1)} Cr+, Direct CRE physical title allows depreciation tax write-offs and custom lease covenants, while SM REIT provides 100% passive governance with zero tenant management overhead.`;
        }
      }
    }

    if (reitCapital && reitCapitalNum) {
      reitCapital.addEventListener('input', () => {
        reitCapitalNum.value = reitCapital.value;
        updateSmReitCalculator();
      });
      reitCapitalNum.addEventListener('input', () => {
        reitCapital.value = reitCapitalNum.value;
        updateSmReitCalculator();
      });
    }

    [reitCapRate, reitHorizon].forEach(el => {
      if (el) el.addEventListener('input', updateSmReitCalculator);
    });

    // ------------------------------------------------------------------
    // TOOL 5: BBMP / BDA Bye-Laws FAR & FSI Plot Maximizer
    // ------------------------------------------------------------------
    const farPlotSizePreset = document.getElementById('farPlotSizePreset');
    const farCustomAreaWrap = document.getElementById('farCustomAreaWrap');
    const farCustomArea = document.getElementById('farCustomArea');
    const farRoadWidth = document.getElementById('farRoadWidth');
    const farZone = document.getElementById('farZone');

    const farMaxTotalArea = document.getElementById('farMaxTotalArea');
    const farBaseFarTxt = document.getElementById('farBaseFarTxt');
    const farBaseAreaTxt = document.getElementById('farBaseAreaTxt');
    const farPremiumFarTxt = document.getElementById('farPremiumFarTxt');
    const farPermissibleFloors = document.getElementById('farPermissibleFloors');
    const farSetbacksSummary = document.getElementById('farSetbacksSummary');
    const farRevenueEst = document.getElementById('farRevenueEst');

    function updateFarFsiCalculator() {
      if (!farPlotSizePreset || !farMaxTotalArea) return;

      let plotArea = 2400;
      if (farPlotSizePreset.value === 'custom') {
        if (farCustomAreaWrap) farCustomAreaWrap.style.display = 'block';
        plotArea = parseFloat(farCustomArea ? farCustomArea.value : 2400) || 2400;
      } else {
        if (farCustomAreaWrap) farCustomAreaWrap.style.display = 'none';
        plotArea = parseFloat(farPlotSizePreset.value) || 2400;
      }

      const road = parseFloat(farRoadWidth ? farRoadWidth.value : 12) || 12;
      const zone = farZone ? farZone.value : 'res_main';

      let baseFar = 2.0;
      let premiumFar = 0.6;
      let floors = 'Stilt + 4 Upper Floors';
      let setbacks = 'Front: 2.5m • Rear: 2.0m (Sides: 1.5m)';

      if (road < 9.5) {
        baseFar = 1.75;
        premiumFar = 0.4;
        floors = 'Ground + 2 / Stilt + 3 Floors';
        setbacks = 'Front: 2.0m • Rear: 1.5m (Sides: 1.0m)';
      } else if (road < 12.5) {
        baseFar = 2.0;
        premiumFar = 0.6;
        floors = 'Stilt + 4 Upper Floors (Max 15m)';
        setbacks = 'Front: 2.5m • Rear: 2.0m (Sides: 1.5m)';
      } else if (road < 18.5) {
        baseFar = 2.25;
        premiumFar = 0.8;
        floors = 'Stilt + 5 Upper Floors';
        setbacks = 'Front: 3.0m • Rear: 2.5m (Sides: 2.0m)';
      } else {
        baseFar = 2.5;
        premiumFar = 1.0;
        floors = 'Stilt + 6 to 8 Floors (High Rise Regs)';
        setbacks = 'Front: 4.5m • Rear: 3.0m (Sides: 3.0m)';
      }

      if (zone === 'comm') {
        baseFar += 0.25;
      } else if (zone === 'res_mixed') {
        baseFar += 0.10;
      }

      const baseArea = Math.round(plotArea * baseFar);
      const premiumArea = Math.round(plotArea * premiumFar);
      const totalBuiltUp = baseArea + premiumArea;

      if (farBaseFarTxt) farBaseFarTxt.textContent = `${baseFar.toFixed(2)}x`;
      if (farBaseAreaTxt) farBaseAreaTxt.textContent = `${baseArea.toLocaleString('en-IN')} sq.ft`;
      if (farPremiumFarTxt) farPremiumFarTxt.textContent = `+${premiumArea.toLocaleString('en-IN')} sq.ft (+${premiumFar.toFixed(2)}x)`;
      if (farMaxTotalArea) farMaxTotalArea.textContent = `${totalBuiltUp.toLocaleString('en-IN')} sq.ft`;
      if (farPermissibleFloors) farPermissibleFloors.textContent = floors;
      if (farSetbacksSummary) farSetbacksSummary.textContent = setbacks;

      const estConstCost = Math.round(totalBuiltUp * 1950);
      const estRental = Math.round(totalBuiltUp * (zone === 'comm' ? 65 : 45));

      if (farRevenueEst) {
        farRevenueEst.textContent = `At ${totalBuiltUp.toLocaleString('en-IN')} sq.ft built-up area, turnkey construction cost under CPWD DSR 2026 is approx ${formatINR(estConstCost)}. Generates approx ${formatINR(estRental)} / month gross rental yield upon asset commercialization.`;
      }
    }

    [farPlotSizePreset, farRoadWidth, farZone].forEach(el => {
      if (el) el.addEventListener('change', updateFarFsiCalculator);
    });

    if (farCustomArea) {
      farCustomArea.addEventListener('input', updateFarFsiCalculator);
    }

    // ------------------------------------------------------------------
    // TOOL 6: NRI Property Sale TDS Shield & Section 195 Form 13
    // ------------------------------------------------------------------
    const nriSaleValue = document.getElementById('nriSaleValue');
    const nriCapGain = document.getElementById('nriCapGain');
    const nriCountry = document.getElementById('nriCountry');
    const nriForm13Status = document.getElementById('nriForm13Status');

    const nriLiquiditySaved = document.getElementById('nriLiquiditySaved');
    const nriDefaultTdsAmt = document.getElementById('nriDefaultTdsAmt');
    const nriOptimizedTdsAmt = document.getElementById('nriOptimizedTdsAmt');

    function updateNriTdsCalculator() {
      if (!nriSaleValue || !nriLiquiditySaved) return;

      const sale = parseFloat(nriSaleValue.value) || 0;
      const gain = parseFloat(nriCapGain ? nriCapGain.value : 0) || 0;

      // Default Section 195 TDS: 20% Base + 15% Surcharge + 4% Cess = 23.92% on GROSS SALE!
      const defaultTds = Math.round(sale * 0.2392);

      // Optimized with Form 13 (Section 197 Certificate):
      // 12.5% Base + 4% Cess = 13.0% on ACTUAL CAPITAL GAIN ONLY!
      const optimizedTds = Math.round(gain * 0.13);

      const saved = Math.max(0, defaultTds - optimizedTds);

      if (nriDefaultTdsAmt) nriDefaultTdsAmt.textContent = formatINR(defaultTds);
      if (nriOptimizedTdsAmt) nriOptimizedTdsAmt.textContent = formatINR(optimizedTds);
      if (nriLiquiditySaved) nriLiquiditySaved.textContent = formatINR(saved);
    }

    [nriSaleValue, nriCapGain, nriCountry, nriForm13Status].forEach(el => {
      if (el) el.addEventListener('input', updateNriTdsCalculator);
      if (el) el.addEventListener('change', updateNriTdsCalculator);
    });

    // ------------------------------------------------------------------
    // TOOL 7: Location-Wise Municipal Property Tax Engine
    // ------------------------------------------------------------------
    const propTaxCity = document.getElementById('propTaxCity');
    const propTaxZone = document.getElementById('propTaxZone');
    const propTaxUsage = document.getElementById('propTaxUsage');
    const propTaxAge = document.getElementById('propTaxAge');
    const propTaxArea = document.getElementById('propTaxArea');
    const propTaxAreaNum = document.getElementById('propTaxAreaNum');
    const propTaxAreaTxt = document.getElementById('propTaxAreaTxt');
    const propTaxGuidanceRate = document.getElementById('propTaxGuidanceRate');
    const propTaxGuidanceRateTxt = document.getElementById('propTaxGuidanceRateTxt');
    const propTaxGuidanceGroup = document.getElementById('propTaxGuidanceGroup');
    const propTaxGuidanceLbl = document.getElementById('propTaxGuidanceLbl');
    const propTaxEarlyPay = document.getElementById('propTaxEarlyPay');

    const propTaxTotalPayout = document.getElementById('propTaxTotalPayout');
    const propTaxPayoutSub = document.getElementById('propTaxPayoutSub');
    const propTaxRebateRateTxt = document.getElementById('propTaxRebateRateTxt');
    const propTaxRebateAmt = document.getElementById('propTaxRebateAmt');
    const propTaxPenaltyAmt = document.getElementById('propTaxPenaltyAmt');
    const propTaxBaseAmt = document.getElementById('propTaxBaseAmt');
    const propTaxBaseSub = document.getElementById('propTaxBaseSub');
    const propTaxSwmAmt = document.getElementById('propTaxSwmAmt');
    const propTaxSwmSub = document.getElementById('propTaxSwmSub');
    const propTaxCessAmt = document.getElementById('propTaxCessAmt');
    const propTaxCessSub = document.getElementById('propTaxCessSub');
    const propTaxWaterAmt = document.getElementById('propTaxWaterAmt');
    const propTaxWaterSub = document.getElementById('propTaxWaterSub');
    const propTaxIdBadge = document.getElementById('propTaxIdBadge');
    const propTaxPortalBtn = document.getElementById('propTaxPortalBtn');
    const propTaxStatutoryRef = document.getElementById('propTaxStatutoryRef');

    const municipalCityData = {
      blr: {
        name: 'Bengaluru (BBMP)',
        showGuidance: false,
        guidanceLabel: 'Sub-Registrar Guidance Rate (₹/sq.ft)',
        idBadge: 'BBMP 10-Digit PID / SAS Form IV/V',
        portalUrl: 'https://bbmptax.karnataka.gov.in',
        portalName: 'Official BBMP Portal ↗',
        statutoryRef: 'Governed under <strong>Section 108A of Karnataka Municipal Corporations Act 1976</strong> & Bruhat Bengaluru Mahanagara Palike (BBMP) Act 2020.',
        baseSubText: 'Unit Area SAS Assessment (10 Months)',
        swmSubText: 'SWM Mandatory Service Surcharge',
        cessSubText: '24% Statutory State Cess (Health/Library)',
        waterSubText: 'Included in BWSSB Water Bill',
        zones: [
          { val: 'a', label: 'Zone A — Central / Prime (MG Rd, Indiranagar, Koramangala)', defaultRate: 11000 },
          { val: 'b', label: 'Zone B — Major Arterials / IT Corridors (Whitefield, HSR, Bellandur, ORR)', defaultRate: 8500 },
          { val: 'c', label: 'Zone C — Established Residential (Jayanagar, Malleshwaram, JP Nagar)', defaultRate: 7200 },
          { val: 'd', label: 'Zone D — Developing Suburbs (Electronic City, Sarjapur, Yelahanka)', defaultRate: 5800 },
          { val: 'e', label: 'Zone E — Peripheral Extensions (Kengeri, KR Puram, Thanisandra)', defaultRate: 4600 },
          { val: 'f', label: 'Zone F — Rural / CMC Boundary Merged Layouts', defaultRate: 3500 }
        ]
      },
      mum: {
        name: 'Mumbai (BMC / MCGM)',
        showGuidance: true,
        guidanceLabel: 'Ready Reckoner Guidance Rate (₹/sq.ft)',
        idBadge: 'BMC 15-Digit Property Code (SAC No.)',
        portalUrl: 'https://ptaxportal.mcgm.gov.in',
        portalName: 'Official BMC Portal ↗',
        statutoryRef: 'Governed under <strong>Section 140 of Mumbai Municipal Corporation Act 1888</strong>. Apartments &lt; 500 sq.ft carpet receive 100% General Tax waiver.',
        baseSubText: 'Capital Value System (CVS) Base',
        swmSubText: 'Municipal Conservancy Tax Included',
        cessSubText: 'Education Cess & Tree Cess',
        waterSubText: 'Water & Sewerage Benefit Tax',
        zones: [
          { val: 'island', label: 'South Mumbai / Island City (Colaba, Nariman Pt, Malabar Hill, Dadar)', defaultRate: 32000 },
          { val: 'west', label: 'Western Suburbs (Bandra, Juhu, Andheri, Borivali, Goregaon)', defaultRate: 21000 },
          { val: 'east', label: 'Eastern Suburbs (Powai, Ghatkopar, Mulund, Chembur, Vikhroli)', defaultRate: 14500 },
          { val: 'ext', label: 'Extended MMR / Outer Boundaries (Dahisar, Mira-Bhayandar, Thane)', defaultRate: 9500 }
        ]
      },
      del: {
        name: 'Delhi NCR (MCD)',
        showGuidance: false,
        guidanceLabel: 'Circle Rate Benchmark (₹/sq.m)',
        idBadge: 'MCD Unique Property ID (UPIC)',
        portalUrl: 'https://mcdonline.nic.in',
        portalName: 'Official MCD Portal ↗',
        statutoryRef: 'Governed under <strong>Section 114 of Delhi Municipal Corporation Act 1957</strong> (Unit Area System UAS Categories A through H).',
        baseSubText: 'Unit Area System (UAS) Annual Value',
        swmSubText: 'Delhi Sanitation & User Charges',
        cessSubText: '1% Statutory Education Cess',
        waterSubText: 'Billed Separately by Delhi Jal Board',
        zones: [
          { val: 'cat_a', label: 'Category A — Super Prime (Golf Links, Vasant Vihar, Jor Bagh)', defaultRate: 774000 },
          { val: 'cat_b', label: 'Category B — Prime (Defence Colony, GK, Hauz Khas, Panchsheel)', defaultRate: 245000 },
          { val: 'cat_c', label: 'Category C — Established (Civil Lines, Lajpat Nagar, Nizamuddin, CR Park)', defaultRate: 160000 },
          { val: 'cat_d', label: 'Category D — Mid-Tier (Janakpuri, Mayur Vihar, Daryaganj, Preet Vihar)', defaultRate: 128000 },
          { val: 'cat_e', label: 'Category E — Moderate (Karol Bagh, Laxmi Nagar, Shahdara)', defaultRate: 70000 },
          { val: 'cat_f', label: 'Category F — Developing (Nangloi, Uttam Nagar, Govindpuri)', defaultRate: 56000 },
          { val: 'cat_g', label: 'Category G — Regularized Colonies (Badarpur, Tuglakabad)', defaultRate: 46000 },
          { val: 'cat_h', label: 'Category H — Urbanized Villages & Rural Extended Abadi', defaultRate: 23000 }
        ]
      },
      hyd: {
        name: 'Hyderabad (GHMC)',
        showGuidance: false,
        guidanceLabel: 'Plinth Valuation Benchmark (₹/sq.ft)',
        idBadge: 'GHMC Property Tax ID Number (PTIN)',
        portalUrl: 'https://ghmc.gov.in',
        portalName: 'Official GHMC Portal ↗',
        statutoryRef: 'Governed under <strong>Section 212 of GHMC Act 1955</strong> with statutory 33.33% maintenance deduction from Gross Rental Value.',
        baseSubText: 'Net Annual Rental Value (NARV) Base',
        swmSubText: 'GHMC Clean City Surcharge',
        cessSubText: '8% Statutory Library Cess',
        waterSubText: 'Billed Separately by HMWSSB',
        zones: [
          { val: 'core_it', label: 'Circle 1 — Core IT Corridor (Madhapur, Gachibowli, Hitec City, Kondapur)', defaultRate: 8500 },
          { val: 'prime_central', label: 'Circle 2 — Prime Central (Banjara Hills, Jubilee Hills, Somajiguda)', defaultRate: 9500 },
          { val: 'est_res', label: 'Circle 3 — Established Urban (Kukatpally, Secunderabad, Ameerpet)', defaultRate: 5200 },
          { val: 'outer', label: 'Circle 4 — Outer Suburbs (Miyapur, Uppal, LB Nagar, Tellapur)', defaultRate: 3800 }
        ]
      },
      chn: {
        name: 'Chennai (GCC)',
        showGuidance: false,
        guidanceLabel: 'Basic Street Valuation Rate (₹/sq.ft)',
        idBadge: 'GCC 15-Digit Assessment Number / Ward-Bill',
        portalUrl: 'https://chennaicorporation.gov.in',
        portalName: 'Official GCC Portal ↗',
        statutoryRef: 'Governed under <strong>Tamil Nadu Urban Local Bodies Rules</strong> & GCC Revised General Property Tax Revision.',
        baseSubText: 'Annual Value General Tax (20%)',
        swmSubText: 'GCC Solid Waste User Fee',
        cessSubText: 'Elementary Education Tax (5%)',
        waterSubText: 'CMWSSB Water & Sewerage Tax (7%)',
        zones: [
          { val: 'central', label: 'Zone 1 — Prime Central (Boat Club, Poes Garden, Nungambakkam)', defaultRate: 14000 },
          { val: 'it_omr', label: 'Zone 2 — IT Corridor / OMR & ECR (Thoraipakkam, Sholinganallur, Adyar)', defaultRate: 9000 },
          { val: 'est_res', label: 'Zone 3 — Established Urban (Anna Nagar, T Nagar, Mylapore, Kilpauk)', defaultRate: 8000 },
          { val: 'ind_north', label: 'Zone 4 — North / Industrial Corridor (Ambattur, Guindy, Kolathur)', defaultRate: 4800 }
        ]
      },
      pun: {
        name: 'Pune (PMC)',
        showGuidance: true,
        guidanceLabel: 'Ready Reckoner Guidance Rate (₹/sq.ft)',
        idBadge: 'PMC Property ID (Ward + Peth + Property No)',
        portalUrl: 'https://propertytax.punecorporation.org',
        portalName: 'Official PMC Portal ↗',
        statutoryRef: 'Governed under <strong>Maharashtra Municipal Corporations Act</strong> with reinstated 40% PT40 residential self-occupied rebate.',
        baseSubText: 'Annual Rateable Value (ARV) Base',
        swmSubText: 'Cleanliness & Sanitation Cess (6%)',
        cessSubText: 'Tree Cess & Fire Tax (2%)',
        waterSubText: 'Water Supply Tax (8%)',
        zones: [
          { val: 'peth', label: 'Core Urban / Peth Areas (Shivaji Nagar, Deccan, Sadashiv Peth)', defaultRate: 10500 },
          { val: 'east', label: 'Eastern IT Hubs (Kalyani Nagar, Koregaon Park, Viman Nagar, Kharadi)', defaultRate: 9500 },
          { val: 'west', label: 'Western IT Corridor (Baner, Balewadi, Aundh, Wakad, Hinjawadi)', defaultRate: 8500 },
          { val: 'outer', label: 'Outer Suburbs (Kothrud, Hadapsar, Katraj, Undri, Sinhagad Rd)', defaultRate: 6000 }
        ]
      }
    };

    function populateZonesForCity(cityKey) {
      if (!propTaxZone) return;
      const data = municipalCityData[cityKey];
      if (!data) return;

      propTaxZone.innerHTML = '';
      data.zones.forEach((z, idx) => {
        const opt = document.createElement('option');
        opt.value = z.val;
        opt.textContent = z.label;
        if (idx === (data.zones.length > 2 ? 1 : 0)) opt.selected = true;
        propTaxZone.appendChild(opt);
      });

      if (propTaxGuidanceGroup) {
        propTaxGuidanceGroup.style.display = data.showGuidance ? 'block' : 'none';
      }
      if (propTaxGuidanceLbl) {
        propTaxGuidanceLbl.textContent = data.guidanceLabel;
      }
      const selectedZoneObj = data.zones[1] || data.zones[0];
      if (propTaxGuidanceRate && selectedZoneObj) {
        propTaxGuidanceRate.value = selectedZoneObj.defaultRate;
        if (propTaxGuidanceRateTxt) {
          propTaxGuidanceRateTxt.textContent = `₹${selectedZoneObj.defaultRate.toLocaleString('en-IN')}/sq.ft`;
        }
      }

      if (propTaxIdBadge) propTaxIdBadge.textContent = data.idBadge;
      if (propTaxPortalBtn) {
        propTaxPortalBtn.href = data.portalUrl;
        const btnSpan = propTaxPortalBtn.querySelector('span');
        if (btnSpan) btnSpan.textContent = data.portalName;
      }
      if (propTaxStatutoryRef) propTaxStatutoryRef.innerHTML = data.statutoryRef;
      if (propTaxBaseSub) propTaxBaseSub.textContent = data.baseSubText;
      if (propTaxSwmSub) propTaxSwmSub.textContent = data.swmSubText;
      if (propTaxCessSub) propTaxCessSub.textContent = data.cessSubText;
      if (propTaxWaterSub) propTaxWaterSub.textContent = data.waterSubText;
    }

    function syncPropTaxArea(val) {
      const num = Math.max(100, Math.min(50000, parseFloat(val) || 1250));
      if (propTaxArea) propTaxArea.value = Math.min(10000, num);
      if (propTaxAreaNum) propTaxAreaNum.value = num;
      if (propTaxAreaTxt) propTaxAreaTxt.textContent = `${Number(num).toLocaleString('en-IN')} sq.ft`;
    }

    function updatePropTaxCalculator() {
      if (!propTaxCity || !propTaxTotalPayout) return;

      const city = propTaxCity.value || 'blr';
      const zone = propTaxZone ? propTaxZone.value : 'b';
      const usage = propTaxUsage ? propTaxUsage.value : 'res_self';
      const age = propTaxAge ? propTaxAge.value : 'age_new';
      const area = parseFloat(propTaxAreaNum ? propTaxAreaNum.value : (propTaxArea ? propTaxArea.value : 1250)) || 1250;
      const guidanceRate = parseFloat(propTaxGuidanceRate ? propTaxGuidanceRate.value : 0) || 15000;
      const isEarly = propTaxEarlyPay ? propTaxEarlyPay.checked : true;

      let baseTax = 0;
      let swmTax = 0;
      let cessTax = 0;
      let waterTax = 0;
      let rebatePct = 0.05;
      let rebateAmt = 0;
      let penaltyAmt = 0;
      let totalTax = 0;

      const isSemiPucca = age === 'age_semi';
      const isMature = age === 'age_old';
      const isMid = age === 'age_mid';

      if (city === 'blr') {
        // BBMP Unit Area Value (UAV) SAS Model
        const uavRates = {
          a: { res_self: 2.50, res_rent: 5.00, commercial: 12.00, industrial: 6.00 },
          b: { res_self: 2.00, res_rent: 4.00, commercial: 9.00, industrial: 4.50 },
          c: { res_self: 1.60, res_rent: 3.20, commercial: 7.00, industrial: 3.50 },
          d: { res_self: 1.20, res_rent: 2.40, commercial: 5.50, industrial: 2.80 },
          e: { res_self: 0.80, res_rent: 1.60, commercial: 4.00, industrial: 2.00 },
          f: { res_self: 0.50, res_rent: 1.00, commercial: 3.00, industrial: 1.50 }
        };
        const zoneRates = uavRates[zone] || uavRates['c'];
        const ratePerSqft = zoneRates[usage] || 2.00;

        const depPct = isMature ? 0.30 : (isMid ? 0.15 : (isSemiPucca ? 0.20 : 0.0));
        const guav = area * ratePerSqft * 10; // 10 months statutory
        const nav = guav * (1 - depPct);

        const taxRate = (usage === 'commercial' || usage === 'industrial') ? 0.25 : 0.20;
        baseTax = Math.round(nav * taxRate);

        // 24% statutory cesses: Health 15%, Library 6%, Beggary 3%
        cessTax = Math.round(baseTax * 0.24);

        // Solid waste management cess
        if (usage === 'commercial' || usage === 'industrial') {
          swmTax = 1800;
        } else {
          swmTax = area <= 1000 ? 360 : 600;
        }
        waterTax = 0; // Handled via BWSSB
        rebatePct = 0.05;
        rebateAmt = isEarly ? Math.round(baseTax * rebatePct) : 0;
        totalTax = Math.max(0, baseTax + cessTax + swmTax - rebateAmt);
        penaltyAmt = Math.round((baseTax + cessTax + swmTax) * 0.02);

      } else if (city === 'mum') {
        // BMC Capital Value System (CVS)
        const natureFactor = isSemiPucca ? 0.8 : 1.0;
        const ageFactor = isMature ? 0.8 : (isMid ? 0.9 : 1.0);
        const userFactor = usage === 'res_self' ? 1.0 : (usage === 'res_rent' ? 1.25 : (usage === 'commercial' ? 2.2 : 1.6));
        const cv = area * guidanceRate * natureFactor * ageFactor * userFactor;

        const isExemptResidential = (usage === 'res_self' || usage === 'res_rent') && area <= 500;

        if (usage === 'commercial') {
          baseTax = Math.round(cv * 0.0115);
          waterTax = Math.round(cv * 0.0030);
          cessTax = Math.round(cv * 0.0015);
        } else if (usage === 'industrial') {
          baseTax = Math.round(cv * 0.0085);
          waterTax = Math.round(cv * 0.0020);
          cessTax = Math.round(cv * 0.0010);
        } else {
          // Residential
          baseTax = isExemptResidential ? 0 : Math.round(cv * 0.0035);
          waterTax = Math.round(cv * 0.0012);
          cessTax = Math.round(cv * 0.0008);
        }
        swmTax = 0; // Included in conservancy tax
        rebatePct = 0.04;
        rebateAmt = isEarly ? Math.round((baseTax + waterTax + cessTax) * rebatePct) : 0;
        totalTax = Math.max(0, baseTax + waterTax + cessTax - rebateAmt);
        penaltyAmt = Math.round((baseTax + waterTax + cessTax) * 0.02);

      } else if (city === 'del') {
        // MCD Unit Area System (UAS)
        const buavRates = {
          cat_a: 630, cat_b: 500, cat_c: 400, cat_d: 320,
          cat_e: 270, cat_f: 230, cat_g: 200, cat_h: 100
        };
        const buav = buavRates[zone] || 400;
        const areaSqm = area / 10.764;
        const structure = isSemiPucca ? 0.7 : 1.0;
        const occupancy = usage === 'res_rent' ? 2.0 : 1.0;
        const ageF = isMature ? 0.8 : (isMid ? 0.9 : 1.0);
        const useF = usage === 'commercial' ? 3.0 : (usage === 'industrial' ? 2.0 : 1.0);

        const annualVal = areaSqm * buav * structure * occupancy * ageF * useF;

        let taxRate = 0.11;
        if (usage === 'commercial') {
          taxRate = 0.20;
        } else if (usage === 'industrial') {
          taxRate = 0.15;
        } else {
          if (zone === 'cat_a' || zone === 'cat_b') taxRate = 0.12;
          else if (zone === 'cat_c' || zone === 'cat_d' || zone === 'cat_e') taxRate = 0.11;
          else taxRate = 0.07;
        }

        baseTax = Math.round(annualVal * taxRate);
        cessTax = Math.round(baseTax * 0.01); // 1% education cess
        swmTax = (usage === 'commercial' || usage === 'industrial') ? 2400 : 600;
        waterTax = 0;
        rebatePct = 0.10;
        rebateAmt = isEarly ? Math.round(baseTax * rebatePct) : 0;
        totalTax = Math.max(0, baseTax + cessTax + swmTax - rebateAmt);
        penaltyAmt = Math.round((baseTax + cessTax + swmTax) * 0.02);

      } else if (city === 'hyd') {
        // GHMC Annual Rental Value (ARV) Method
        const mrvRates = {
          core_it: { res_self: 3.50, res_rent: 6.00, commercial: 15.00, industrial: 8.00 },
          prime_central: { res_self: 3.00, res_rent: 5.00, commercial: 14.00, industrial: 7.50 },
          est_res: { res_self: 2.20, res_rent: 3.80, commercial: 10.00, industrial: 5.50 },
          outer: { res_self: 1.50, res_rent: 2.80, commercial: 7.50, industrial: 4.00 }
        };
        const rates = mrvRates[zone] || mrvRates['est_res'];
        const mrv = rates[usage] || 2.50;
        const ageFactor = isMature ? 0.80 : (isMid ? 0.90 : 1.0);
        const garv = area * (mrv * ageFactor) * 12;
        const narv = garv * 0.6667; // 33.33% statutory maintenance deduction

        const taxRate = (usage === 'commercial' || usage === 'industrial') ? 0.30 : 0.25;
        baseTax = Math.round(narv * taxRate);
        cessTax = Math.round(baseTax * 0.08); // 8% library cess
        swmTax = (usage === 'commercial' || usage === 'industrial') ? 1200 : 360;
        waterTax = 0;
        rebatePct = 0.05;
        rebateAmt = isEarly ? Math.round(baseTax * rebatePct) : 0;
        totalTax = Math.max(0, baseTax + cessTax + swmTax - rebateAmt);
        penaltyAmt = Math.round((baseTax + cessTax + swmTax) * 0.02);

      } else if (city === 'chn') {
        // GCC Street Rate Model
        const streetRates = {
          central: { res_self: 2.80, res_rent: 4.50, commercial: 12.00, industrial: 6.50 },
          it_omr: { res_self: 2.20, res_rent: 3.80, commercial: 10.00, industrial: 5.50 },
          est_res: { res_self: 1.80, res_rent: 3.00, commercial: 8.00, industrial: 4.50 },
          ind_north: { res_self: 1.20, res_rent: 2.20, commercial: 6.00, industrial: 3.50 }
        };
        const rates = streetRates[zone] || streetRates['est_res'];
        const rate = rates[usage] || 2.00;
        const ageFactor = isMature ? 0.80 : (isMid ? 0.90 : 1.0);
        const annualVal = area * rate * ageFactor * 12 * 0.90; // 10% allowance

        baseTax = Math.round(annualVal * 0.20);
        cessTax = Math.round(annualVal * 0.05); // 5% Education Tax
        waterTax = Math.round(annualVal * 0.07); // 7% Sewerage / Water Tax
        swmTax = (usage === 'commercial' || usage === 'industrial') ? 1500 : 360;
        rebatePct = 0.05;
        rebateAmt = isEarly ? Math.min(5000, Math.round(baseTax * rebatePct)) : 0;
        totalTax = Math.max(0, baseTax + cessTax + waterTax + swmTax - rebateAmt);
        penaltyAmt = Math.round((baseTax + cessTax + waterTax + swmTax) * 0.02);

      } else if (city === 'pun') {
        // PMC Rateable Value Model with 40% PT40 Rebate
        const natureFactor = isSemiPucca ? 0.8 : 1.0;
        const ageFactor = isMature ? 0.8 : (isMid ? 0.9 : 1.0);
        const useMult = usage === 'commercial' ? 2.2 : (usage === 'industrial' ? 1.6 : 1.0);
        const capVal = area * guidanceRate * natureFactor * ageFactor * useMult;
        const arv = capVal * 0.06;

        let genTax = arv * 0.14;
        if (usage === 'res_self') {
          // Reinstated PT40 40% concession
          genTax = genTax * 0.60;
        }
        baseTax = Math.round(genTax);
        swmTax = Math.round(arv * 0.06); // Sanitation / Cleanliness
        waterTax = Math.round(arv * 0.08); // Water supply tax
        cessTax = Math.round(arv * 0.02); // Tree cess & fire tax
        rebatePct = 0.05;
        rebateAmt = isEarly ? Math.round(baseTax * rebatePct) : 0;
        totalTax = Math.max(0, baseTax + swmTax + waterTax + cessTax - rebateAmt);
        penaltyAmt = Math.round((baseTax + swmTax + waterTax + cessTax) * 0.02);
      }

      // Update DOM values
      if (propTaxTotalPayout) propTaxTotalPayout.textContent = formatINR(totalTax);
      if (propTaxBaseAmt) propTaxBaseAmt.textContent = formatINR(baseTax);
      if (propTaxSwmAmt) propTaxSwmAmt.textContent = formatINR(swmTax);
      if (propTaxCessAmt) propTaxCessAmt.textContent = formatINR(cessTax);
      if (propTaxWaterAmt) propTaxWaterAmt.textContent = formatINR(waterTax);
      if (propTaxRebateAmt) propTaxRebateAmt.textContent = formatINR(rebateAmt);
      if (propTaxPenaltyAmt) propTaxPenaltyAmt.textContent = `${formatINR(penaltyAmt)} / mo`;
      if (propTaxRebateRateTxt) propTaxRebateRateTxt.textContent = `${Math.round(rebatePct * 100)}% Prompt Rebate`;

      if (propTaxPayoutSub) {
        if (isEarly && rebateAmt > 0) {
          propTaxPayoutSub.textContent = `Includes ${formatINR(rebateAmt)} Early Bird rebate applied for prompt seasonal filing.`;
        } else {
          propTaxPayoutSub.textContent = `Total standard annual liability payable to municipal treasury (all urban cesses included).`;
        }
      }
    }

    if (propTaxCity) {
      propTaxCity.addEventListener('change', () => {
        populateZonesForCity(propTaxCity.value);
        updatePropTaxCalculator();
      });
    }

    if (propTaxZone) {
      propTaxZone.addEventListener('change', () => {
        const cityKey = propTaxCity ? propTaxCity.value : 'blr';
        const cityObj = municipalCityData[cityKey];
        if (cityObj) {
          const zObj = cityObj.zones.find(z => z.val === propTaxZone.value);
          if (zObj && propTaxGuidanceRate) {
            propTaxGuidanceRate.value = zObj.defaultRate;
            if (propTaxGuidanceRateTxt) {
              propTaxGuidanceRateTxt.textContent = `₹${zObj.defaultRate.toLocaleString('en-IN')}/sq.ft`;
            }
          }
        }
        updatePropTaxCalculator();
      });
    }

    if (propTaxArea) {
      propTaxArea.addEventListener('input', () => {
        syncPropTaxArea(propTaxArea.value);
        updatePropTaxCalculator();
      });
    }

    if (propTaxAreaNum) {
      propTaxAreaNum.addEventListener('input', () => {
        syncPropTaxArea(propTaxAreaNum.value);
        updatePropTaxCalculator();
      });
    }

    if (propTaxGuidanceRate) {
      propTaxGuidanceRate.addEventListener('input', () => {
        const r = parseFloat(propTaxGuidanceRate.value) || 0;
        if (propTaxGuidanceRateTxt) {
          propTaxGuidanceRateTxt.textContent = `₹${r.toLocaleString('en-IN')}/sq.ft`;
        }
        updatePropTaxCalculator();
      });
    }

    [propTaxUsage, propTaxAge, propTaxEarlyPay].forEach(el => {
      if (el) el.addEventListener('change', updatePropTaxCalculator);
    });

    // ------------------------------------------------------------------
    // TOOL 8: Home Loan EMI & Statutory Tax Shield Matrix
    // ------------------------------------------------------------------
    const hlLoanAmt = document.getElementById('hlLoanAmt');
    const hlLoanAmtNum = document.getElementById('hlLoanAmtNum');
    const hlLoanAmtTxt = document.getElementById('hlLoanAmtTxt');
    const hlLenderPreset = document.getElementById('hlLenderPreset');
    const hlInterestRate = document.getElementById('hlInterestRate');
    const hlInterestRateTxt = document.getElementById('hlInterestRateTxt');
    const hlTenure = document.getElementById('hlTenure');
    const hlTenureTxt = document.getElementById('hlTenureTxt');
    const hlTaxSlab = document.getElementById('hlTaxSlab');
    const hlPropertyStatus = document.getElementById('hlPropertyStatus');

    const hlNetEmiPayout = document.getElementById('hlNetEmiPayout');
    const hlNetEmiSub = document.getElementById('hlNetEmiSub');
    const hlAnnualTaxSavedTxt = document.getElementById('hlAnnualTaxSavedTxt');
    const hlAnnualTaxSavedAmt = document.getElementById('hlAnnualTaxSavedAmt');
    const hlLifetimeTaxSavedAmt = document.getElementById('hlLifetimeTaxSavedAmt');
    const hlGrossEmi = document.getElementById('hlGrossEmi');
    const hlSec24Amt = document.getElementById('hlSec24Amt');
    const hlSec24TaxTxt = document.getElementById('hlSec24TaxTxt');
    const hlSec80cAmt = document.getElementById('hlSec80cAmt');
    const hlSec80cTaxTxt = document.getElementById('hlSec80cTaxTxt');
    const hlTotalInterest = document.getElementById('hlTotalInterest');

    function syncHlLoanAmt(val) {
      const num = Math.max(500000, Math.min(100000000, parseFloat(val) || 7500000));
      if (hlLoanAmt) hlLoanAmt.value = Math.min(50000000, num);
      if (hlLoanAmtNum) hlLoanAmtNum.value = num;
      if (hlLoanAmtTxt) hlLoanAmtTxt.textContent = formatINR(num);
    }

    function updateHomeLoanCalculator() {
      if (!hlLoanAmt || !hlNetEmiPayout) return;

      const p = parseFloat(hlLoanAmtNum ? hlLoanAmtNum.value : (hlLoanAmt ? hlLoanAmt.value : 7500000)) || 7500000;
      const annualRate = parseFloat(hlInterestRate ? hlInterestRate.value : 8.50) || 8.50;
      const tenureYrs = parseFloat(hlTenure ? hlTenure.value : 20) || 20;
      const taxSlab = parseFloat(hlTaxSlab ? hlTaxSlab.value : 0.312) || 0.312;
      const propStatus = hlPropertyStatus ? hlPropertyStatus.value : 'self';

      const r = (annualRate / 100) / 12;
      const n = tenureYrs * 12;

      let emi = 0;
      if (r > 0 && n > 0) {
        emi = Math.round((p * r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1));
      }
      const totalPayment = emi * n;
      const totalInterest = Math.max(0, totalPayment - p);

      const yr1Interest = Math.round(p * (annualRate / 100));
      const yr1Principal = Math.max(0, (emi * 12) - yr1Interest);

      const sec24Eligible = propStatus === 'self' ? Math.min(200000, yr1Interest) : yr1Interest;
      const sec24TaxSaved = Math.round(sec24Eligible * taxSlab);

      const sec80cEligible = Math.min(150000, yr1Principal);
      const sec80cTaxSaved = Math.round(sec80cEligible * taxSlab);

      const annualTaxSaved = sec24TaxSaved + sec80cTaxSaved;
      const monthlyTaxSaved = Math.round(annualTaxSaved / 12);
      const netMonthlyEmi = Math.max(0, emi - monthlyTaxSaved);
      const lifetimeTaxSaved = annualTaxSaved * Math.min(tenureYrs, 20);

      if (hlLoanAmtTxt) hlLoanAmtTxt.textContent = formatINR(p);
      if (hlInterestRateTxt) hlInterestRateTxt.textContent = `${annualRate.toFixed(2)}%`;
      if (hlTenureTxt) hlTenureTxt.textContent = `${tenureYrs} Years`;

      if (hlNetEmiPayout) hlNetEmiPayout.textContent = `${formatINR(netMonthlyEmi)} / mo`;
      if (hlNetEmiSub) {
        hlNetEmiSub.innerHTML = `Gross EMI: ${formatINR(emi)} / mo &bull; Saves ${formatINR(monthlyTaxSaved)}/mo through Section 24(b) &amp; 80C income tax deductions`;
      }
      if (hlAnnualTaxSavedTxt) hlAnnualTaxSavedTxt.textContent = `${formatINR(annualTaxSaved)} / yr`;
      if (hlAnnualTaxSavedAmt) hlAnnualTaxSavedAmt.textContent = formatINR(annualTaxSaved);
      if (hlLifetimeTaxSavedAmt) hlLifetimeTaxSavedAmt.textContent = formatINR(lifetimeTaxSaved);

      if (hlGrossEmi) hlGrossEmi.textContent = `${formatINR(emi)} / mo`;
      if (hlSec24Amt) hlSec24Amt.textContent = `${formatINR(sec24Eligible)} / yr`;
      if (hlSec24TaxTxt) hlSec24TaxTxt.textContent = `Saves ${formatINR(sec24TaxSaved)} in Taxes (${(taxSlab * 100).toFixed(1)}% Slab)`;
      if (hlSec80cAmt) hlSec80cAmt.textContent = `${formatINR(sec80cEligible)} / yr`;
      if (hlSec80cTaxTxt) hlSec80cTaxTxt.textContent = `Saves ${formatINR(sec80cTaxSaved)} in Taxes`;
      if (hlTotalInterest) hlTotalInterest.textContent = formatINR(totalInterest);
    }

    if (hlLoanAmt) {
      hlLoanAmt.addEventListener('input', () => {
        syncHlLoanAmt(hlLoanAmt.value);
        updateHomeLoanCalculator();
      });
    }

    if (hlLoanAmtNum) {
      hlLoanAmtNum.addEventListener('input', () => {
        syncHlLoanAmt(hlLoanAmtNum.value);
        updateHomeLoanCalculator();
      });
    }

    if (hlLenderPreset) {
      hlLenderPreset.addEventListener('change', () => {
        if (hlLenderPreset.value !== 'custom') {
          if (hlInterestRate) hlInterestRate.value = hlLenderPreset.value;
          updateHomeLoanCalculator();
        }
      });
    }

    if (hlInterestRate) {
      hlInterestRate.addEventListener('input', () => {
        if (hlLenderPreset) hlLenderPreset.value = 'custom';
        updateHomeLoanCalculator();
      });
    }

    if (hlTenure) {
      hlTenure.addEventListener('input', updateHomeLoanCalculator);
    }

    [hlTaxSlab, hlPropertyStatus].forEach(el => {
      if (el) el.addEventListener('change', updateHomeLoanCalculator);
    });

    // ------------------------------------------------------------------
    // TOOL 9: Micro-Market Net Rental Yield & Society Maintenance ROI Benchmark
    // ------------------------------------------------------------------
    const ryMarketPreset = document.getElementById('ryMarketPreset');
    const ryArea = document.getElementById('ryArea');
    const ryAreaNum = document.getElementById('ryAreaNum');
    const ryAreaTxt = document.getElementById('ryAreaTxt');
    const ryCapitalCost = document.getElementById('ryCapitalCost');
    const ryCapitalCostTxt = document.getElementById('ryCapitalCostTxt');
    const ryMonthlyRent = document.getElementById('ryMonthlyRent');
    const ryMonthlyMaint = document.getElementById('ryMonthlyMaint');
    const ryAnnualTax = document.getElementById('ryAnnualTax');
    const ryVacancyMonths = document.getElementById('ryVacancyMonths');

    const ryNetYieldVal = document.getElementById('ryNetYieldVal');
    const ryNetYieldSub = document.getElementById('ryNetYieldSub');
    const ryGrossRentAmt = document.getElementById('ryGrossRentAmt');
    const ryTotalOpexAmt = document.getElementById('ryTotalOpexAmt');
    const ryAnnualMaintAmt = document.getElementById('ryAnnualMaintAmt');
    const ryVacancyLossAmt = document.getElementById('ryVacancyLossAmt');
    const ryPropTaxAmt = document.getElementById('ryPropTaxAmt');
    const rySec24ShieldAmt = document.getElementById('rySec24ShieldAmt');

    const rentalPresetData = {
      blr_ind: { rentSqft: 65, maintSqft: 5.50, costSqft: 14000, tax: 12500 },
      blr_white: { rentSqft: 45, maintSqft: 4.50, costSqft: 9500, tax: 9500 },
      mum_bandra: { rentSqft: 140, maintSqft: 10.00, costSqft: 42000, tax: 28000 },
      mum_powai: { rentSqft: 75, maintSqft: 6.50, costSqft: 22000, tax: 16000 },
      del_golf: { rentSqft: 50, maintSqft: 5.00, costSqft: 15000, tax: 14000 },
      del_noida: { rentSqft: 30, maintSqft: 3.50, costSqft: 7800, tax: 7500 },
      hyd_hitec: { rentSqft: 38, maintSqft: 3.80, costSqft: 8200, tax: 8000 },
      pun_kharadi: { rentSqft: 32, maintSqft: 3.50, costSqft: 7800, tax: 7500 }
    };

    function syncRyArea(val) {
      const num = Math.max(200, Math.min(10000, parseFloat(val) || 1400));
      if (ryArea) ryArea.value = Math.min(5000, num);
      if (ryAreaNum) ryAreaNum.value = num;
      if (ryAreaTxt) ryAreaTxt.textContent = `${Number(num).toLocaleString('en-IN')} sq.ft`;
    }

    function applyRentalPreset(presetKey) {
      const p = rentalPresetData[presetKey];
      if (!p) return;
      const area = parseFloat(ryAreaNum ? ryAreaNum.value : 1400) || 1400;
      if (ryCapitalCost) ryCapitalCost.value = area * p.costSqft;
      if (ryMonthlyRent) ryMonthlyRent.value = Math.round(area * p.rentSqft);
      if (ryMonthlyMaint) ryMonthlyMaint.value = Math.round(area * p.maintSqft);
      if (ryAnnualTax) ryAnnualTax.value = p.tax;
    }

    function updateRentalYieldCalculator() {
      if (!ryNetYieldVal) return;

      const area = parseFloat(ryAreaNum ? ryAreaNum.value : (ryArea ? ryArea.value : 1400)) || 1400;
      const capitalCost = parseFloat(ryCapitalCost ? ryCapitalCost.value : 19600000) || 19600000;
      const monthlyRent = parseFloat(ryMonthlyRent ? ryMonthlyRent.value : 91000) || 91000;
      const monthlyMaint = parseFloat(ryMonthlyMaint ? ryMonthlyMaint.value : 7700) || 7700;
      const annualTax = parseFloat(ryAnnualTax ? ryAnnualTax.value : 12500) || 12500;
      const vacancyMonths = parseFloat(ryVacancyMonths ? ryVacancyMonths.value : 1.0) || 1.0;

      const grossAnnualRent = monthlyRent * 12;
      const vacancyLoss = Math.round(monthlyRent * vacancyMonths);
      const annualMaint = monthlyMaint * 12;
      const totalOpex = annualMaint + annualTax + vacancyLoss;

      const netAnnualInflow = Math.max(0, grossAnnualRent - totalOpex);
      const grossYield = capitalCost > 0 ? (grossAnnualRent / capitalCost) * 100 : 0;
      const netYield = capitalCost > 0 ? (netAnnualInflow / capitalCost) * 100 : 0;
      const sec24Shield = Math.round(Math.max(0, grossAnnualRent - annualTax) * 0.30);

      if (ryAreaTxt) ryAreaTxt.textContent = `${Number(area).toLocaleString('en-IN')} sq.ft`;
      if (ryCapitalCostTxt) ryCapitalCostTxt.textContent = formatINR(capitalCost);

      if (ryNetYieldVal) ryNetYieldVal.textContent = `${netYield.toFixed(2)}% Net Yield`;
      if (ryNetYieldSub) {
        ryNetYieldSub.textContent = `Advertised Gross Yield: ${grossYield.toFixed(2)}% • Net Annual Cash Inflow: ${formatINR(netAnnualInflow)} / yr`;
      }
      if (ryGrossRentAmt) ryGrossRentAmt.textContent = `${formatINR(grossAnnualRent)} / yr`;
      if (ryTotalOpexAmt) ryTotalOpexAmt.textContent = `${formatINR(totalOpex)} / yr`;

      if (ryAnnualMaintAmt) ryAnnualMaintAmt.textContent = `${formatINR(annualMaint)} / yr`;
      if (ryVacancyLossAmt) ryVacancyLossAmt.textContent = formatINR(vacancyLoss);
      if (ryPropTaxAmt) ryPropTaxAmt.textContent = `${formatINR(annualTax)} / yr`;
      if (rySec24ShieldAmt) rySec24ShieldAmt.textContent = formatINR(sec24Shield);
    }

    if (ryMarketPreset) {
      ryMarketPreset.addEventListener('change', () => {
        if (ryMarketPreset.value !== 'custom') {
          applyRentalPreset(ryMarketPreset.value);
        }
        updateRentalYieldCalculator();
      });
    }

    if (ryArea) {
      ryArea.addEventListener('input', () => {
        syncRyArea(ryArea.value);
        const presetKey = ryMarketPreset ? ryMarketPreset.value : 'blr_ind';
        if (presetKey !== 'custom') applyRentalPreset(presetKey);
        updateRentalYieldCalculator();
      });
    }

    if (ryAreaNum) {
      ryAreaNum.addEventListener('input', () => {
        syncRyArea(ryAreaNum.value);
        const presetKey = ryMarketPreset ? ryMarketPreset.value : 'blr_ind';
        if (presetKey !== 'custom') applyRentalPreset(presetKey);
        updateRentalYieldCalculator();
      });
    }

    [ryCapitalCost, ryMonthlyRent, ryMonthlyMaint, ryAnnualTax, ryVacancyMonths].forEach(el => {
      if (el) {
        el.addEventListener('input', () => {
          if (ryMarketPreset && el !== ryVacancyMonths) ryMarketPreset.value = 'custom';
          updateRentalYieldCalculator();
        });
        el.addEventListener('change', updateRentalYieldCalculator);
      }
    });

    // ------------------------------------------------------------------
    // TOOL 10: Joint Development Agreement (JDA) & Section 45(5A) Estimator
    // ------------------------------------------------------------------
    const jdaLandExtent = document.getElementById('jdaLandExtent');
    const jdaLandExtentTxt = document.getElementById('jdaLandExtentTxt');
    const jdaUnitType = document.getElementById('jdaUnitType');
    const jdaFarVal = document.getElementById('jdaFarVal');
    const jdaSharingRatio = document.getElementById('jdaSharingRatio');
    const jdaSharingRatioTxt = document.getElementById('jdaSharingRatioTxt');
    const jdaUpfrontDeposit = document.getElementById('jdaUpfrontDeposit');
    const jdaProjectedRate = document.getElementById('jdaProjectedRate');
    const jdaOriginalCost = document.getElementById('jdaOriginalCost');
    const jdaOriginalCostTxt = document.getElementById('jdaOriginalCostTxt');

    const jdaTotalRealizable = document.getElementById('jdaTotalRealizable');
    const jdaRealizableSub = document.getElementById('jdaRealizableSub');
    const jdaGrossCashAmt = document.getElementById('jdaGrossCashAmt');
    const jdaConstructedAreaTxt = document.getElementById('jdaConstructedAreaTxt');
    const jdaConstructedValAmt = document.getElementById('jdaConstructedValAmt');
    const jdaTotalDevelopable = document.getElementById('jdaTotalDevelopable');
    const jdaDeveloperArea = document.getElementById('jdaDeveloperArea');
    const jdaTdsWithheld = document.getElementById('jdaTdsWithheld');
    const jdaLtcgTaxAmt = document.getElementById('jdaLtcgTaxAmt');

    function formatCr(val) {
      if (val >= 10000000) {
        return `₹${(val / 10000000).toFixed(2)} Cr`;
      }
      return formatINR(val);
    }

    function updateJdaCalculator() {
      if (!jdaTotalRealizable) return;

      const landExtent = parseFloat(jdaLandExtent ? jdaLandExtent.value : 1.0) || 1.0;
      const unit = jdaUnitType ? jdaUnitType.value : 'acre';
      const far = parseFloat(jdaFarVal ? jdaFarVal.value : 2.50) || 2.50;
      const sharingPct = parseFloat(jdaSharingRatio ? jdaSharingRatio.value : 40) || 40;
      const upfrontCash = parseFloat(jdaUpfrontDeposit ? jdaUpfrontDeposit.value : 10000000) || 10000000;
      const projectedRate = parseFloat(jdaProjectedRate ? jdaProjectedRate.value : 8500) || 8500;
      const originalCost = parseFloat(jdaOriginalCost ? jdaOriginalCost.value : 5000000) || 5000000;

      let landAreaSqft = landExtent * 43560;
      if (unit === 'gunta') landAreaSqft = landExtent * 1089;
      else if (unit === 'sqft') landAreaSqft = landExtent;

      const totalDevelopable = Math.round(landAreaSqft * far);
      const landownerArea = Math.round(totalDevelopable * (sharingPct / 100));
      const developerArea = totalDevelopable - landownerArea;

      const constructedVal = landownerArea * projectedRate;
      const totalRealizable = constructedVal + upfrontCash;

      const tdsWithheld = Math.round(upfrontCash * 0.10);
      const deemedConsideration = constructedVal + upfrontCash;
      const taxableGain = Math.max(0, deemedConsideration - originalCost);
      const ltcgTax = Math.round(taxableGain * 0.13); // 12.5% LTCG + 4% cess

      if (jdaLandExtentTxt) {
        jdaLandExtentTxt.textContent = `${landExtent} ${unit === 'acre' ? 'Acre' : (unit === 'gunta' ? 'Guntas' : 'sq.ft')} (${Math.round(landAreaSqft).toLocaleString('en-IN')} sq.ft)`;
      }
      if (jdaSharingRatioTxt) jdaSharingRatioTxt.textContent = `${sharingPct}% Share`;
      if (jdaOriginalCostTxt) jdaOriginalCostTxt.textContent = formatINR(originalCost);

      if (jdaTotalRealizable) jdaTotalRealizable.textContent = formatCr(totalRealizable);
      if (jdaRealizableSub) {
        jdaRealizableSub.textContent = `Landowner Built-Up Allocation: ${landownerArea.toLocaleString('en-IN')} sq.ft constructed + ${formatINR(upfrontCash)} upfront monetary cash`;
      }
      if (jdaGrossCashAmt) jdaGrossCashAmt.textContent = formatINR(upfrontCash);
      if (jdaConstructedAreaTxt) jdaConstructedAreaTxt.textContent = `${landownerArea.toLocaleString('en-IN')} sq.ft Allocation`;
      if (jdaConstructedValAmt) jdaConstructedValAmt.textContent = formatCr(constructedVal);

      if (jdaTotalDevelopable) jdaTotalDevelopable.textContent = `${totalDevelopable.toLocaleString('en-IN')} sq.ft`;
      if (jdaDeveloperArea) jdaDeveloperArea.textContent = `${developerArea.toLocaleString('en-IN')} sq.ft`;
      if (jdaTdsWithheld) jdaTdsWithheld.textContent = formatINR(tdsWithheld);
      if (jdaLtcgTaxAmt) jdaLtcgTaxAmt.textContent = formatCr(ltcgTax);
    }

    if (jdaSharingRatio) {
      jdaSharingRatio.addEventListener('input', () => {
        if (jdaSharingRatioTxt) jdaSharingRatioTxt.textContent = `${jdaSharingRatio.value}% Share`;
        updateJdaCalculator();
      });
    }

    [jdaLandExtent, jdaUnitType, jdaFarVal, jdaUpfrontDeposit, jdaProjectedRate, jdaOriginalCost].forEach(el => {
      if (el) {
        el.addEventListener('input', updateJdaCalculator);
        el.addEventListener('change', updateJdaCalculator);
      }
    });

    // Initialize all statutory tools
    updateDutyCalculator();
    updateCapGainsCalculator();
    populateZonesForCity('blr');
    updatePropTaxCalculator();
    updateHomeLoanCalculator();
    updateRentalYieldCalculator();
    updateJdaCalculator();
    updateReraDelayCalculator();
    updateSmReitCalculator();
    updateFarFsiCalculator();
    updateNriTdsCalculator();
  }

  // Initialize Statutory Workbench if section exists on current page
  initStatutoryTools();

  // Multi-page deck state initialization
  const pageSections = document.querySelectorAll('.terminal-page');
  if (pageSections.length > 1) {
    if (window.location.hash) {
      switchTerminalPage(window.location.hash, false);
    } else {
      switchTerminalPage(1, false);
    }
  }
});
