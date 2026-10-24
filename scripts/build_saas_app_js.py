# Build clean, high-performance app.js focused on Landlord SaaS, Legal Leases & HRA Studio

js_content = """/**
 * ExaInfra Landlord SaaS & Legal Studio (exainfra.in)
 * Proprietary property management, UPI rent collection, and court-admissible lease deeds
 */

document.addEventListener('DOMContentLoaded', () => {

  // ====================================================================
  // 1. Toast Notification System
  // ====================================================================
  function showToast(message, type = 'emerald') {
    const container = document.getElementById('toastContainer');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `toast-item toast-${type}`;
    toast.innerHTML = `
      <div class="toast-content">${message}</div>
      <button class="toast-close" onclick="this.parentElement.remove()">&times;</button>
    `;

    container.appendChild(toast);
    setTimeout(() => {
      toast.classList.add('fade-out');
      setTimeout(() => toast.remove(), 300);
    }, 4000);
  }
  window.showToast = showToast;

  // ====================================================================
  // 2. Modal Helper Functions
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

  // ====================================================================
  // 3. Landlord SaaS Dashboard Workbench
  // ====================================================================
  const saasTabButtons = document.querySelectorAll('.saas-tab-btn');
  const saasPanes = {
    rent: document.getElementById('saasTabRent'),
    leases: document.getElementById('saasTabLeases'),
    tickets: document.getElementById('saasTabTickets')
  };

  saasTabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      saasTabButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const tabKey = btn.getAttribute('data-saas-tab');
      Object.keys(saasPanes).forEach(k => {
        if (saasPanes[k]) {
          saasPanes[k].style.display = (k === tabKey) ? 'block' : 'none';
        }
      });
    });
  });

  // Sneha Rao UPI Reminder Simulation
  const btnSendSnehaReminder = document.getElementById('btnSendSnehaReminder');
  if (btnSendSnehaReminder) {
    btnSendSnehaReminder.addEventListener('click', () => {
      btnSendSnehaReminder.innerHTML = `<span>Sent ✓</span>`;
      btnSendSnehaReminder.style.background = '#059669';
      btnSendSnehaReminder.disabled = true;

      showToast('💬 WhatsApp Rent Invoice with UPI link delivered to Sneha Rao ()');
    });
  }

  // Send WhatsApp Links to All Units
  const btnSimulateCollectAll = document.getElementById('btnSimulateCollectAll');
  if (btnSimulateCollectAll) {
    btnSimulateCollectAll.addEventListener('click', () => {
      btnSimulateCollectAll.innerHTML = `<span>Sending...</span>`;
      btnSimulateCollectAll.disabled = true;

      setTimeout(() => {
        btnSimulateCollectAll.innerHTML = `<span>✓ Rent Links Sent to All Units</span>`;
        showToast('⚡ WhatsApp UPI payment links sent to all 4 tenant units!');
      }, 900);
    });
  }

  // Maintenance Ticket Resolution
  const ticketCountBadge = document.getElementById('ticketCountBadge');
  window.resolveTicket = function(btn) {
    const row = btn.closest('tr');
    if (row) {
      const statusCell = row.children[4];
      if (statusCell) {
        statusCell.innerHTML = `<span class="saas-badge-paid">✓ Resolved</span>`;
      }
      btn.remove();
      if (ticketCountBadge) {
        let count = parseInt(ticketCountBadge.textContent, 10) || 1;
        ticketCountBadge.textContent = Math.max(0, count - 1);
      }
      showToast('✓ Maintenance ticket marked as Resolved!');
    }
  };

  // Log New Maintenance Issue
  const btnLogNewTicket = document.getElementById('btnLogNewTicket');
  const saasTicketsTableBody = document.getElementById('saasTicketsTableBody');
  if (btnLogNewTicket && saasTicketsTableBody) {
    btnLogNewTicket.addEventListener('click', () => {
      const issue = prompt("Enter tenant repair or maintenance issue:", "Balcony Geyser Sensor & Heating Coil Check");
      if (!issue) return;

      const newId = "TCK-" + Math.floor(800 + Math.random() * 100);
      const newRow = document.createElement('tr');
      newRow.innerHTML = `
        <td><strong>${newId}</strong></td>
        <td>UNIT-112 (Arjun)</td>
        <td>${issue}</td>
        <td>Today</td>
        <td><span class="saas-badge-due">⚙ In Progress</span></td>
        <td>
          <button class="btn btn-xs btn-primary" onclick="resolveTicket(this)">
            Mark Resolved ✓
          </button>
        </td>
      `;
      saasTicketsTableBody.prepend(newRow);
      if (ticketCountBadge) {
        let count = parseInt(ticketCountBadge.textContent, 10) || 0;
        ticketCountBadge.textContent = count + 1;
      }
      showToast(`✓ Ticket ${newId} created and dispatched to vendor!`);
    });
  }

  // Add Managed Unit Modal
  const modalAddUnit = document.getElementById('modalAddUnit');
  const formAddUnit = document.getElementById('formAddUnit');
  const closeModalAddUnit = document.getElementById('closeModalAddUnit');
  const btnNavAddUnit = document.getElementById('btnNavAddUnit');
  const btnAddUnitPrompt = document.getElementById('btnAddUnitPrompt');
  const saasRentTableBody = document.getElementById('saasRentTableBody');
  const saasKpiUnits = document.getElementById('saasKpiUnits');

  if (btnNavAddUnit) {
    btnNavAddUnit.addEventListener('click', () => openModal(modalAddUnit));
  }
  if (btnAddUnitPrompt) {
    btnAddUnitPrompt.addEventListener('click', () => openModal(modalAddUnit));
  }
  if (closeModalAddUnit) {
    closeModalAddUnit.addEventListener('click', () => closeModal(modalAddUnit));
  }

  if (formAddUnit && saasRentTableBody) {
    formAddUnit.addEventListener('submit', (e) => {
      e.preventDefault();

      const unitCode = document.getElementById('newUnitCode').value.toUpperCase();
      const society = document.getElementById('newSociety').value;
      const tenantName = document.getElementById('newTenantName').value;
      const tenantPhone = document.getElementById('newTenantPhone').value;
      const rentAmt = parseInt(document.getElementById('newMonthlyRent').value, 10);
      const dueDay = document.getElementById('newDueDate').value;

      const newRow = document.createElement('tr');
      newRow.innerHTML = `
        <td><strong>${unitCode}</strong><br><span style="font-size:0.75rem; color:#94A3B8;">${society}</span></td>
        <td>${tenantName}<br><span style="font-size:0.75rem; color:#94A3B8;">${tenantPhone}</span></td>
        <td><strong>₹${rentAmt.toLocaleString('en-IN')}</strong></td>
        <td><span class="saas-badge-due">Due on ${dueDay}th</span></td>
        <td>${dueDay} Nov 2026</td>
        <td>
          <button class="btn-upi-action" onclick="this.innerHTML='Sent ✓'; this.style.background='#059669'; showToast('💬 WhatsApp Rent Link dispatched to ${tenantName}!');">
            <span>Send UPI Link 💬</span>
          </button>
        </td>
      `;

      saasRentTableBody.prepend(newRow);
      closeModal(modalAddUnit);
      formAddUnit.reset();

      if (saasKpiUnits) {
        let current = parseInt(saasKpiUnits.textContent, 10) || 4;
        saasKpiUnits.textContent = `${current + 1} Units`;
      }

      showToast(`🎉 Unit ${unitCode} (${society}) registered! Automated UPI invoicing active.`);
    });
  }

  // ====================================================================
  // 4. Legal Lease Deeds & Tax Studio
  // ====================================================================
  const btnToggleLeaseMode = document.getElementById('btnToggleLeaseMode');
  const btnToggleHraMode = document.getElementById('btnToggleHraMode');
  const studioLeaseView = document.getElementById('studioLeaseView');
  const studioHraView = document.getElementById('studioHraView');

  if (btnToggleLeaseMode && btnToggleHraMode) {
    btnToggleLeaseMode.addEventListener('click', () => {
      btnToggleLeaseMode.classList.add('active');
      btnToggleLeaseMode.style.background = 'var(--coral-500)';
      btnToggleLeaseMode.style.color = '#FFFFFF';

      btnToggleHraMode.classList.remove('active');
      btnToggleHraMode.style.background = 'none';
      btnToggleHraMode.style.color = '#475569';

      if (studioLeaseView) studioLeaseView.style.display = 'grid';
      if (studioHraView) studioHraView.style.display = 'none';
    });

    btnToggleHraMode.addEventListener('click', () => {
      btnToggleHraMode.classList.add('active');
      btnToggleHraMode.style.background = 'var(--coral-500)';
      btnToggleHraMode.style.color = '#FFFFFF';

      btnToggleLeaseMode.classList.remove('active');
      btnToggleLeaseMode.style.background = 'none';
      btnToggleLeaseMode.style.color = '#475569';

      if (studioLeaseView) studioLeaseView.style.display = 'none';
      if (studioHraView) studioHraView.style.display = 'grid';
    });
  }

  // 11-Month Lease Drafter Form
  const formAgreementDraft = document.getElementById('formAgreementDraft');
  const modalAgreementPreview = document.getElementById('modalAgreementPreview');
  const legalDocumentPaper = document.getElementById('legalDocumentPaper');
  const closeModalAgrPreview = document.getElementById('closeModalAgrPreview');
  const btnPrintAgreement = document.getElementById('btnPrintAgreement');
  const btnProceedAadhaarSign = document.getElementById('btnProceedAadhaarSign');

  if (closeModalAgrPreview) {
    closeModalAgrPreview.addEventListener('click', () => closeModal(modalAgreementPreview));
  }

  if (formAgreementDraft && legalDocumentPaper) {
    formAgreementDraft.addEventListener('submit', (e) => {
      e.preventDefault();

      const ownerName = document.getElementById('agrOwnerName').value;
      const tenantName = document.getElementById('agrTenantName').value;
      const propAddr = document.getElementById('agrPropertyAddress').value;
      const monthlyRent = parseInt(document.getElementById('agrMonthlyRent').value, 10);
      const deposit = parseInt(document.getElementById('agrDeposit').value, 10);
      const duration = document.getElementById('agrDuration').value;
      const notice = document.getElementById('agrNotice').value;

      legalDocumentPaper.innerHTML = `
        <div class="estamp-banner-clean">
          <div class="estamp-top-row">
            <div class="govt-seal">
              <strong>GOVERNMENT OF KARNATAKA</strong><br>
              <span>e-Stamp Certificate of Stamp Duty & Registration</span>
            </div>
            <div class="estamp-code">
              <strong>CERT NO: IN-KA29108420194098T</strong><br>
              <span>Stamp Duty Paid: ₹500.00 &bull; 24-Oct-2026</span>
            </div>
          </div>
          <div class="estamp-divider"></div>
          <div class="estamp-parties-row">
            <span>First Party: <strong>${ownerName}</strong> (Lessor)</span>
            <span>Second Party: <strong>${tenantName}</strong> (Lessee)</span>
          </div>
        </div>

        <div class="legal-body-text">
          <h3 style="text-align:center; text-transform:uppercase; font-size:1.25rem; font-weight:800; margin:1.5rem 0 1rem 0; letter-spacing:0.5px;">
            RESIDENTIAL RENTAL & LEASE AGREEMENT
          </h3>

          <p>
            THIS RESIDENTIAL LEASE AGREEMENT is made and entered into on this <strong>24th day of October 2026</strong>, by and between:
          </p>

          <p>
            <strong>${ownerName}</strong>, residing at Bangalore, Karnataka, hereinafter referred to as the <strong>"LESSOR" / OWNER</strong> (which expression shall include his/her legal heirs, successors and assigns) of the ONE PART;
          </p>
          <p style="text-align:center; font-weight:700;">- AND -</p>
          <p>
            <strong>${tenantName}</strong>, residing at Bangalore, Karnataka, hereinafter referred to as the <strong>"LESSEE" / TENANT</strong> (which expression shall include his/her legal heirs, successors and assigns) of the OTHER PART.
          </p>

          <h4 style="margin:1rem 0 0.5rem 0; font-size:1rem; font-weight:700; color:#0F172A;">1. SUBJECT PREMISES</h4>
          <p>The Lessor hereby lets out and the Lessee agrees to take on lease the premises situated at: <strong>${propAddr}</strong>.</p>

          <h4 style="margin:1rem 0 0.5rem 0; font-size:1rem; font-weight:700; color:#0F172A;">2. TENURE & LOCK-IN PERIOD</h4>
          <p>The lease shall be in effect for a tenure of <strong>${duration}</strong> commencing immediately. Both parties agree to a mandatory lock-in period of 3 months.</p>

          <h4 style="margin:1rem 0 0.5rem 0; font-size:1rem; font-weight:700; color:#0F172A;">3. MONTHLY RENT & UTILITIES</h4>
          <p>The Lessee shall pay to the Lessor a monthly rental of <strong>₹${monthlyRent.toLocaleString('en-IN')}</strong> payable on or before the 5th day of every calendar month via UPI / Net Banking. Electricity and water consumption charges shall be paid directly by the Lessee.</p>

          <h4 style="margin:1rem 0 0.5rem 0; font-size:1rem; font-weight:700; color:#0F172A;">4. INTEREST-FREE SECURITY DEPOSIT</h4>
          <p>The Lessee has paid a sum of <strong>₹${deposit.toLocaleString('en-IN')}</strong> as an interest-free refundable security deposit, refundable upon handover of keys subject to 1-month painting deduction.</p>

          <h4 style="margin:1rem 0 0.5rem 0; font-size:1rem; font-weight:700; color:#0F172A;">5. TERMINATION & NOTICE</h4>
          <p>Either party may terminate this agreement by providing a minimum of <strong>${notice}</strong> written notice.</p>

          <div class="legal-sign-grid" style="display:grid; grid-template-columns:1fr 1fr; gap:2rem; margin-top:2.5rem; padding-top:1.5rem; border-top:1px dashed #CBD5E1;">
            <div class="sign-col">
              <span style="font-size:0.8rem; color:#64748B;">LESSOR / OWNER SIGNATURE</span>
              <div style="font-family:'JetBrains Mono', monospace; font-size:1.1rem; color:#0F172A; margin:0.75rem 0 0.25rem 0; font-weight:700;">${ownerName}</div>
              <span style="font-size:0.75rem; color:#059669;">✓ Verified Landlord Identity</span>
            </div>
            <div class="sign-col">
              <span style="font-size:0.8rem; color:#64748B;">LESSEE / TENANT SIGNATURE</span>
              <div style="font-family:'JetBrains Mono', monospace; font-size:1.1rem; color:#0F172A; margin:0.75rem 0 0.25rem 0; font-weight:700;">${tenantName}</div>
              <span style="font-size:0.75rem; color:#0284C7;">⏳ Ready for Aadhaar eSign</span>
            </div>
          </div>
        </div>
      `;

      openModal(modalAgreementPreview);
    });
  }

  if (btnPrintAgreement) {
    btnPrintAgreement.addEventListener('click', () => {
      window.print();
    });
  }

  if (btnProceedAadhaarSign) {
    btnProceedAadhaarSign.addEventListener('click', () => {
      btnProceedAadhaarSign.innerHTML = `<span>Simulating Aadhaar OTP...</span>`;
      btnProceedAadhaarSign.disabled = true;

      setTimeout(() => {
        btnProceedAadhaarSign.innerHTML = `<span>✓ Agreement Digitally eSigned</span>`;
        btnProceedAadhaarSign.style.background = '#059669';
        showToast('🎉 Digital Lease Agreement successfully eSigned and E-Stamped!');
      }, 1200);
    });
  }

  // 12-Month HRA Tax Receipts Generator
  const formHraGenerate = document.getElementById('formHraGenerate');
  const modalHraPreview = document.getElementById('modalHraPreview');
  const hraReceiptsContainer = document.getElementById('hraReceiptsContainer');
  const closeModalHraPreview = document.getElementById('closeModalHraPreview');
  const btnPrintHraReceipts = document.getElementById('btnPrintHraReceipts');

  if (closeModalHraPreview) {
    closeModalHraPreview.addEventListener('click', () => closeModal(modalHraPreview));
  }

  if (formHraGenerate && hraReceiptsContainer) {
    formHraGenerate.addEventListener('submit', (e) => {
      e.preventDefault();

      const tenant = document.getElementById('hraTenantName').value;
      const landlord = document.getElementById('hraLandlordName').value;
      const rentAmt = parseInt(document.getElementById('hraRentAmount').value, 10);
      const landlordPan = document.getElementById('hraLandlordPan').value.toUpperCase();
      const address = document.getElementById('hraAddress').value;
      const fy = document.getElementById('hraFinancialYear').value;

      const months = [
        { name: 'April', year: fy.split('-')[0] },
        { name: 'May', year: fy.split('-')[0] },
        { name: 'June', year: fy.split('-')[0] },
        { name: 'July', year: fy.split('-')[0] },
        { name: 'August', year: fy.split('-')[0] },
        { name: 'September', year: fy.split('-')[0] },
        { name: 'October', year: fy.split('-')[0] },
        { name: 'November', year: fy.split('-')[0] },
        { name: 'December', year: fy.split('-')[0] },
        { name: 'January', year: fy.split('-')[1] },
        { name: 'February', year: fy.split('-')[1] },
        { name: 'March', year: fy.split('-')[1] }
      ];

      hraReceiptsContainer.innerHTML = months.map((m, idx) => `
        <div class="hra-receipt-paper" style="background:#FFFFFF; border:1px solid #CBD5E1; border-radius:10px; padding:1.25rem; margin-bottom:1rem; box-shadow:0 2px 4px rgba(0,0,0,0.04);">
          <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #E2E8F0; padding-bottom:0.6rem; margin-bottom:0.75rem;">
            <div>
              <span style="font-size:0.75rem; color:#64748B; font-weight:700;">HRA TAX RENT RECEIPT #${idx + 1}</span>
              <h4 style="margin:0; font-size:1.1rem; color:#0F172A; font-weight:800;">${m.name} ${m.year}</h4>
            </div>
            <div style="text-align:right;">
              <span style="font-size:0.75rem; color:#64748B;">Section 10(13A) Exemption</span>
              <div style="font-size:1.2rem; font-weight:800; color:#059669;">₹${rentAmt.toLocaleString('en-IN')}</div>
            </div>
          </div>

          <p style="font-size:0.88rem; color:#334155; line-height:1.6; margin:0 0 0.75rem 0;">
            Received with thanks from <strong>${tenant}</strong> a sum of <strong>₹${rentAmt.toLocaleString('en-IN')}</strong> towards house rent for the month of <strong>${m.name} ${m.year}</strong> for residential premises situated at: <strong>${address}</strong>.
          </p>

          <div style="display:flex; justify-content:space-between; align-items:flex-end; padding-top:0.5rem; border-top:1px dashed #E2E8F0;">
            <div>
              <span style="font-size:0.75rem; color:#64748B; display:block;">LANDLORD DECLARATION:</span>
              <strong style="font-size:0.9rem; color:#0F172A;">${landlord}</strong>
              <div style="font-size:0.75rem; color:#475569; font-family:'JetBrains Mono', monospace;">PAN: <strong>${landlordPan}</strong></div>
            </div>

            <div class="hra-stamp-box" style="border:2px solid #E11D48; padding:0.4rem 0.6rem; text-align:center; border-radius:4px; transform:rotate(-4deg); background:#FFF1F2;">
              <span style="font-size:0.65rem; color:#E11D48; font-weight:800; display:block;">REVENUE STAMP</span>
              <span style="font-size:0.8rem; font-weight:800; color:#E11D48;">₹1.00</span>
              <div style="font-size:0.65rem; color:#E11D48; font-style:italic;">${landlord}</div>
            </div>
          </div>
        </div>
      `).join('');

      openModal(modalHraPreview);
      showToast(`✓ Generated 12 official HRA rent receipts for ${fy}!`);
    });
  }

  if (btnPrintHraReceipts) {
    btnPrintHraReceipts.addEventListener('click', () => {
      window.print();
    });
  }

  // ====================================================================
  // 5. Rent & Yield Intelligence Estimator
  // ====================================================================
  const estLocality = document.getElementById('estLocality');
  const estBhk = document.getElementById('estBhk');
  const estFurnishing = document.getElementById('estFurnishing');
  const estCarpetArea = document.getElementById('estCarpetArea');
  const estAmenities = document.getElementById('estAmenities');
  const estRangeDisplay = document.getElementById('estRangeDisplay');
  const estYieldDisplay = document.getElementById('estYieldDisplay');

  function calculateRentEstimate() {
    if (!estRangeDisplay) return;

    let baseRent = 35000;
    const bhk = estBhk ? estBhk.value : '2 BHK';
    if (bhk === '1 BHK') baseRent = 20000;
    else if (bhk === '2 BHK') baseRent = 38000;
    else if (bhk === '3 BHK') baseRent = 58000;
    else if (bhk === '4+ BHK') baseRent = 95000;

    const loc = estLocality ? estLocality.value : 'Bellandur';
    let locMultiplier = 1.0;
    if (loc.includes('Bellandur') || loc.includes('Indiranagar')) locMultiplier = 1.2;
    else if (loc.includes('Whitefield') || loc.includes('Koramangala')) locMultiplier = 1.15;
    else if (loc.includes('Electronic')) locMultiplier = 0.85;

    const furn = estFurnishing ? estFurnishing.value : 'Semi Furnished';
    let furnMultiplier = 1.0;
    if (furn === 'Fully Furnished') furnMultiplier = 1.25;
    else if (furn === 'Unfurnished') furnMultiplier = 0.85;

    const calculated = Math.round(baseRent * locMultiplier * furnMultiplier / 1000) * 1000;
    const low = Math.round(calculated * 0.92 / 1000) * 1000;
    const high = Math.round(calculated * 1.12 / 1000) * 1000;

    estRangeDisplay.textContent = `₹${low.toLocaleString('en-IN')} - ₹${high.toLocaleString('en-IN')} / mo`;
    if (estYieldDisplay) estYieldDisplay.textContent = '4.5% - 5.1% p.a.';
  }

  [estLocality, estBhk, estFurnishing, estCarpetArea, estAmenities].forEach(el => {
    if (el) el.addEventListener('change', calculateRentEstimate);
  });

  // ====================================================================
  // 6. SaaS Pricing Handlers
  // ====================================================================
  const btnBuyLandlordPro = document.getElementById('btnBuyLandlordPro');
  if (btnBuyLandlordPro) {
    btnBuyLandlordPro.addEventListener('click', () => {
      showToast('🎉 Landlord Pro SaaS Activated (₹999/yr)! Unlimited Units & Automated WhatsApp Reminders Active.');
    });
  }

});
"""

with open('/Users/chetanbisariya/.gemini/antigravity-ide/scratch/exainfra-in/app.js', 'w') as f:
    f.write(js_content)

print(f"Generated clean SaaS app.js ({len(js_content)} bytes) successfully.")
