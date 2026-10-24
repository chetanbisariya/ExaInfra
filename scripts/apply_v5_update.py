import json

with open("/Users/chetanbisariya/.gemini/antigravity-ide/scratch/exainfra-in/bangalore_verified_listings.json") as f:
    listings = json.load(f)

with open("/Users/chetanbisariya/.gemini/antigravity-ide/scratch/exainfra-in/app.js") as f:
    code = f.read()

# 1. Update defaultApartments
start_marker = "  let defaultApartments = ["
end_marker = "  // Load from localStorage or defaults"

start_idx = code.find(start_marker)
end_idx = code.find(end_marker)
assert start_idx != -1 and end_idx != -1, "defaultApartments markers not found!"

js_listings = json.dumps(listings, indent=4)
new_defaults = f"  let defaultApartments = {js_listings};\n\n  "
code = code[:start_idx] + new_defaults + code[end_idx:]

# 2. Update cache key
code = code.replace("exainfra_multiportal_blr_v4_live_real_feed", "exainfra_multiportal_blr_v5_verified_bengaluru")
code = code.replace("exainfra_multiportal_blr_v3", "exainfra_multiportal_blr_v5_verified_bengaluru")

# 3. Update Card Action Buttons in renderApartments()
old_card_buttons = """            <div class="apt-card-actions-clean">
              <button class="btn btn-chat-owner btn-sm btn-action-chat" data-id="${apt.id}">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
                <span>Chat with Landlord</span>
              </button>
              <button class="btn btn-secondary btn-sm btn-action-view" data-id="${apt.id}">
                <span>Schedule Visit</span>
              </button>
            </div>

            <div>
              <button class="btn btn-reserve-flat btn-sm btn-full btn-action-confirm" data-id="${apt.id}">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                <span>${apt.isReserved ? 'Locked & Reserved' : 'Confirm & Reserve Flat (₹10K Token)'}</span>
              </button>
            </div>"""

new_card_buttons = """            <div class="apt-card-actions-clean">
              <button class="btn btn-schedule-visit btn-full btn-action-view" data-id="${apt.id}" title="Schedule property tour & move-in assistance">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                <span>Schedule Property Visit & Assistance</span>
              </button>
            </div>"""

assert old_card_buttons in code, "old_card_buttons not found!"
code = code.replace(old_card_buttons, new_card_buttons, 1)

# Remove unused card listeners for chat and confirm
old_listeners = """    document.querySelectorAll('.btn-action-chat').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const aptId = e.currentTarget.getAttribute('data-id');
        openInAppChatModal(aptId);
      });
    });

    document.querySelectorAll('.btn-action-confirm').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const aptId = e.currentTarget.getAttribute('data-id');
        openConfirmRentalModal(aptId);
      });
    });"""

if old_listeners in code:
    code = code.replace(old_listeners, "// Chat and Confirm buttons removed as per aggregator architecture", 1)

# 4. Update filterCity listener for Coming Soon handling
old_filter_city = """  if (filterCity) {
    filterCity.addEventListener('change', (e) => {
      activeFilters.city = e.target.value;
      if (quickCitySelect) quickCitySelect.value = e.target.value;
      renderApartments();
    });
  }"""

new_filter_city = """  if (filterCity) {
    filterCity.addEventListener('change', (e) => {
      const selectedCity = e.target.value;
      if (selectedCity !== 'Bengaluru') {
        openCityComingSoonModal(selectedCity);
        filterCity.value = 'Bengaluru';
        activeFilters.city = 'Bengaluru';
        return;
      }
      activeFilters.city = 'Bengaluru';
      renderApartments();
    });
  }"""

assert old_filter_city in code, "old_filter_city not found!"
code = code.replace(old_filter_city, new_filter_city, 1)

# 5. Replace openApartmentDetailModal with comprehensive seeker information & tentative move-in date form
detail_start_marker = "  function openApartmentDetailModal(aptId) {"
detail_end_marker = "  const closeModalDetail = document.getElementById('closeModalDetail');"

d_start = code.find(detail_start_marker)
d_end = code.find(detail_end_marker)
assert d_start != -1 and d_end != -1, "detail modal markers not found!"

new_detail_modal_func = """  function openApartmentDetailModal(aptId) {
    const apt = apartments.find(a => a.id === aptId) || apartments[0];
    selectedApartment = apt;

    const detailContainer = document.getElementById('detailModalContent');
    if (!detailContainer) return;

    let portalClass = 'nobroker';
    if (apt.source === 'Housing.com') portalClass = 'housing';
    else if (apt.source === 'MagicBricks') portalClass = 'magicbricks';
    else if (apt.source === '99acres') portalClass = 'acres99';
    else if (apt.source === 'ExaInfra Direct') portalClass = 'exadirect';

    // Calculate tentative default dates
    const today = new Date();
    const todayYMD = today.toISOString().split('T')[0];
    const defaultMoveIn = new Date();
    defaultMoveIn.setDate(today.getDate() + 7);
    const defaultMoveInYMD = defaultMoveIn.toISOString().split('T')[0];

    detailContainer.innerHTML = `
      <div>
        <div class="detail-img-box" style="position:relative;">
          <a href="${apt.externalUrl || '#'}" target="_blank" rel="noopener noreferrer" title="View original listing on ${apt.source}">
            <img src="${apt.image}" alt="${apt.title}" loading="lazy" referrerpolicy="no-referrer" onerror="this.onerror=null; this.src='https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=800&q=80';">
          </a>
          <div class="card-img-credit-pill" style="bottom:12px; left:12px; font-size:0.75rem; padding:0.3rem 0.7rem; max-width:85%;">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path><circle cx="12" cy="13" r="4"></circle></svg>
            <span>${apt.imageCredit || 'Verified Aggregator Photo'}</span>
          </div>
        </div>
        <div style="background:#F8FAFC; border:1px solid #E2E8F0; padding:0.85rem; border-radius:10px; margin-bottom:0.85rem;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
            <span style="font-size:0.75rem; font-weight:700; color:#FD3752;">SOURCE: ${apt.source} (Verified Direct Listing)</span>
            <span style="font-size:0.7rem; font-weight:700; color:#059669; background:#ECFDF5; padding:0.15rem 0.45rem; border-radius:4px;">ZERO BROKERAGE</span>
          </div>
          <div style="font-size:0.88rem; font-weight:700; color:#0F172A; margin-bottom:4px;">${apt.title}</div>
          <div style="font-size:0.82rem; color:#475569; margin-bottom:6px;">📍 ${apt.locality}, ${apt.city}</div>
          
          <div style="display:flex; gap:1rem; border-top:1px dashed #CBD5E1; padding-top:6px; margin-top:6px; font-size:0.8rem;">
            <div>Rent: <strong style="color:#0F172A;">${formatINR(apt.rent)}/mo</strong></div>
            <div>Deposit: <strong style="color:#0F172A;">${formatINR(apt.deposit)}</strong></div>
            <div>Size: <strong style="color:#0F172A;">${apt.area} sq.ft</strong></div>
          </div>
        </div>
      </div>

      <div>
        <div style="margin-bottom:0.85rem;">
          <a href="${apt.externalUrl || '#'}" target="_blank" rel="noopener noreferrer" class="btn btn-portal-ext ${portalClass} btn-full" style="padding:0.65rem 1rem; font-size:0.86rem; text-decoration:none;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
            <span>View Full Details & Photos on ${apt.source} ↗</span>
          </a>
        </div>

        <div class="visit-form-box" id="visitFormWrapper">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.4rem;">
            <h4 style="font-size:1rem; font-weight:800; color:#0F172A; margin:0;">Schedule Visit & Move-In Assistance</h4>
            <span style="font-size:0.7rem; font-weight:700; color:#059669; background:#ECFDF5; padding:0.2rem 0.5rem; border-radius:4px;">100% FREE</span>
          </div>
          <p style="font-size:0.8rem; color:#64748B; margin-bottom:0.85rem; line-height:1.4;">
            Submit your contact info and tentative move-in date. Our Bengaluru rental concierge will coordinate your visit and verify keys with ${apt.source}.
          </p>

          <form id="formBookVisit">
            <div class="visit-form-grid-2">
              <div class="form-group" style="margin-bottom:0.6rem;">
                <label for="visitName" style="font-size:0.75rem; font-weight:700; color:#334155;">Your Full Name *</label>
                <input type="text" id="visitName" class="form-control-clean" style="font-size:0.85rem; padding:0.5rem 0.75rem;" value="${currentUser.name}" required>
              </div>
              <div class="form-group" style="margin-bottom:0.6rem;">
                <label for="visitPhone" style="font-size:0.75rem; font-weight:700; color:#334155;">WhatsApp / Mobile Number *</label>
                <input type="tel" id="visitPhone" class="form-control-clean" style="font-size:0.85rem; padding:0.5rem 0.75rem;" value="${currentUser.phone}" required>
              </div>
            </div>

            <div class="visit-form-grid-2">
              <div class="form-group" style="margin-bottom:0.6rem;">
                <label for="visitEmail" style="font-size:0.75rem; font-weight:700; color:#334155;">Email Address *</label>
                <input type="email" id="visitEmail" class="form-control-clean" style="font-size:0.85rem; padding:0.5rem 0.75rem;" value="${currentUser.email || 'aditya@tenant.com'}" required>
              </div>
              <div class="form-group" style="margin-bottom:0.6rem;">
                <label for="visitTenantType" style="font-size:0.75rem; font-weight:700; color:#334155;">Tenant Profile *</label>
                <select id="visitTenantType" class="form-control-clean" style="font-size:0.85rem; padding:0.5rem 0.75rem;">
                  <option value="Working Professional">Working Professional</option>
                  <option value="Family">Family</option>
                  <option value="Couple">Couple</option>
                  <option value="Students / Roommates">Students / Roommates</option>
                </select>
              </div>
            </div>

            <div class="form-group" style="margin-bottom:0.6rem;">
              <label for="visitMoveInDate" style="font-size:0.75rem; font-weight:700; color:#334155;">Tentative Move-In Date *</label>
              <input type="date" id="visitMoveInDate" class="form-control-clean" style="font-size:0.85rem; padding:0.5rem 0.75rem;" min="${todayYMD}" value="${defaultMoveInYMD}" required>
              <div class="movein-quick-pills" id="moveInQuickPills">
                <span class="movein-pill" data-days="3">Immediate (Next 3 Days)</span>
                <span class="movein-pill active" data-days="7">Within 1 Week</span>
                <span class="movein-pill" data-days="15">Within 15 Days</span>
                <span class="movein-pill" data-days="30">Within 30 Days</span>
              </div>
            </div>

            <div class="visit-form-grid-2">
              <div class="form-group" style="margin-bottom:0.6rem;">
                <label for="visitSlot" style="font-size:0.75rem; font-weight:700; color:#334155;">Preferred Visit Slot *</label>
                <select id="visitSlot" class="form-control-clean" style="font-size:0.85rem; padding:0.5rem 0.75rem;">
                  <option value="Saturday Morning (10:00 AM - 1:00 PM)">Saturday Morning (10 AM - 1 PM)</option>
                  <option value="Saturday Afternoon (2:00 PM - 5:00 PM)">Saturday Afternoon (2 PM - 5 PM)</option>
                  <option value="Sunday Morning (10:00 AM - 1:00 PM)">Sunday Morning (10 AM - 1 PM)</option>
                  <option value="Sunday Evening (4:00 PM - 7:00 PM)">Sunday Evening (4 PM - 7 PM)</option>
                  <option value="Weekday Morning (9:00 AM - 12:00 PM)">Weekday Morning (9 AM - 12 PM)</option>
                  <option value="Weekday Evening (5:00 PM - 8:00 PM)">Weekday Evening (5 PM - 8 PM)</option>
                </select>
              </div>
              <div class="form-group" style="margin-bottom:0.6rem;">
                <label for="visitCompany" style="font-size:0.75rem; font-weight:700; color:#334155;">Workplace / Employer</label>
                <input type="text" id="visitCompany" class="form-control-clean" style="font-size:0.85rem; padding:0.5rem 0.75rem;" placeholder="e.g. Infosys, TCS, Google, Startup">
              </div>
            </div>

            <div class="form-group" style="margin-bottom:0.85rem;">
              <label for="visitNotes" style="font-size:0.75rem; font-weight:700; color:#334155;">Specific Preferences / Notes</label>
              <input type="text" id="visitNotes" class="form-control-clean" style="font-size:0.85rem; padding:0.5rem 0.75rem;" placeholder="e.g. 1 car parking required, pet dog, preferred floor">
            </div>

            <button type="submit" class="btn btn-primary btn-full btn-lg" style="font-size:0.92rem; padding:0.75rem 1rem;">
              <span>Submit Free Visit & Move-In Request 🚀</span>
            </button>
          </form>
        </div>
      </div>
    `;

    openModal(modalApartmentDetail);

    // Quick move-in pills
    const moveInInput = document.getElementById('visitMoveInDate');
    document.querySelectorAll('.movein-pill').forEach(pill => {
      pill.addEventListener('click', () => {
        document.querySelectorAll('.movein-pill').forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        const days = parseInt(pill.getAttribute('data-days'), 10);
        const targetDate = new Date();
        targetDate.setDate(targetDate.getDate() + days);
        if (moveInInput) {
          moveInInput.value = targetDate.toISOString().split('T')[0];
        }
      });
    });

    const formBookVisit = document.getElementById('formBookVisit');
    if (formBookVisit) {
      formBookVisit.addEventListener('submit', (e) => {
        e.preventDefault();

        const vName = document.getElementById('visitName').value.trim();
        const vPhone = document.getElementById('visitPhone').value.trim();
        const vEmail = document.getElementById('visitEmail').value.trim();
        const vMoveIn = document.getElementById('visitMoveInDate').value;
        const vSlot = document.getElementById('visitSlot').value;
        const vTenantType = document.getElementById('visitTenantType').value;
        const vCompany = document.getElementById('visitCompany') ? document.getElementById('visitCompany').value.trim() : '';
        const vNotes = document.getElementById('visitNotes') ? document.getElementById('visitNotes').value.trim() : '';

        // Save lead to backend database
        try {
          fetch('api/leads.php', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              action: 'schedule_visit',
              name: vName,
              phone: vPhone,
              email: vEmail,
              apartmentId: apt.id,
              apartmentTitle: apt.title,
              portalSource: apt.source,
              moveInDate: vMoveIn,
              preferredSlot: vSlot,
              tenantType: vTenantType,
              companyName: vCompany,
              specialNotes: vNotes
            })
          }).catch(() => {});
        } catch (err) {}

        // Save to local storage
        try {
          let visits = JSON.parse(localStorage.getItem('exainfra_visit_requests') || '[]');
          visits.push({
            apartmentId: apt.id,
            apartmentTitle: apt.title,
            source: apt.source,
            name: vName,
            phone: vPhone,
            email: vEmail,
            moveInDate: vMoveIn,
            slot: vSlot,
            submittedAt: new Date().toISOString()
          });
          localStorage.setItem('exainfra_visit_requests', JSON.stringify(visits));
        } catch (err) {}

        // Render Success State in Modal
        detailContainer.innerHTML = `
          <div style="grid-column: 1 / -1; text-align:center; padding: 2.2rem 1.2rem; background:#FFFFFF; border-radius:12px;">
            <div style="width:64px; height:64px; background:#ECFDF5; color:#059669; border-radius:50%; display:inline-flex; align-items:center; justify-content:center; font-size:2rem; margin-bottom:1rem;">
              ✓
            </div>
            <h3 style="font-size:1.35rem; font-weight:800; color:#0F172A; margin-bottom:0.4rem;">Visit & Move-In Request Confirmed!</h3>
            <p style="font-size:0.9rem; color:#475569; max-width:520px; margin:0 auto 1.2rem auto; line-height:1.5;">
              Thank you, <strong>${vName}</strong>! Your visit request for <strong>${apt.title}</strong> has been logged with our Bengaluru team.
            </p>

            <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:10px; max-width:480px; margin:0 auto 1.25rem auto; padding:1.1rem; text-align:left;">
              <div style="display:flex; justify-content:space-between; margin-bottom:0.45rem; font-size:0.85rem;">
                <span style="color:#64748B;">Tentative Move-In:</span>
                <strong style="color:#0F172A;">${vMoveIn}</strong>
              </div>
              <div style="display:flex; justify-content:space-between; margin-bottom:0.45rem; font-size:0.85rem;">
                <span style="color:#64748B;">Preferred Slot:</span>
                <strong style="color:#0F172A;">${vSlot}</strong>
              </div>
              <div style="display:flex; justify-content:space-between; margin-bottom:0.45rem; font-size:0.85rem;">
                <span style="color:#64748B;">Contact WhatsApp:</span>
                <strong style="color:#0F172A;">${vPhone}</strong>
              </div>
              <div style="display:flex; justify-content:space-between; font-size:0.85rem; border-top:1px dashed #CBD5E1; padding-top:0.45rem; margin-top:0.45rem;">
                <span style="color:#64748B;">Source Portal:</span>
                <span style="font-weight:700; color:#FD3752;">${apt.source} (Zero Brokerage)</span>
              </div>
            </div>

            <p style="font-size:0.82rem; color:#64748B; margin-bottom:1.25rem;">
              Our Bengaluru rental concierge will WhatsApp you at <strong>${vPhone}</strong> within 2 hours to confirm your visit time.
            </p>

            <div style="display:flex; gap:0.75rem; justify-content:center; max-width:480px; margin:0 auto;">
              <a href="${apt.externalUrl || '#'}" target="_blank" rel="noopener noreferrer" class="btn btn-portal-ext ${portalClass}" style="flex:1; text-decoration:none; padding:0.65rem 1rem;">
                <span>View on ${apt.source} ↗</span>
              </a>
              <button class="btn btn-secondary" id="btnCloseSuccessModal" style="flex:1; padding:0.65rem 1rem;">
                <span>Done / Close</span>
              </button>
            </div>
          </div>
        `;

        const btnCloseSuccessModal = document.getElementById('btnCloseSuccessModal');
        if (btnCloseSuccessModal) {
          btnCloseSuccessModal.addEventListener('click', () => closeModal(modalApartmentDetail));
        }

        showToast(`📅 Visit request sent! We will WhatsApp you at ${vPhone} within 2 hours.`);
      });
    }
  }

  """

code = code[:d_start] + new_detail_modal_func + code[d_end:]

# 6. Add modalCityComingSoon logic before the final closing bracket
city_modal_logic = """
  // ====================================================================
  // 12. City Coming Soon Modal Logic
  // ====================================================================
  const modalCityComingSoon = document.getElementById('modalCityComingSoon');
  const comingSoonCityName = document.getElementById('comingSoonCityName');
  const btnCityNotifyLabel = document.getElementById('btnCityNotifyLabel');
  const formCityNotify = document.getElementById('formCityNotify');
  const closeModalCityComingSoon = document.getElementById('closeModalCityComingSoon');
  const btnExploreBangaloreNow = document.getElementById('btnExploreBangaloreNow');

  function openCityComingSoonModal(cityName) {
    if (comingSoonCityName) comingSoonCityName.textContent = cityName;
    if (btnCityNotifyLabel) btnCityNotifyLabel.textContent = cityName;
    openModal(modalCityComingSoon);
  }

  if (closeModalCityComingSoon) {
    closeModalCityComingSoon.addEventListener('click', () => closeModal(modalCityComingSoon));
  }

  if (btnExploreBangaloreNow) {
    btnExploreBangaloreNow.addEventListener('click', () => {
      closeModal(modalCityComingSoon);
      const el = document.getElementById('explore-apartments');
      if (el) el.scrollIntoView({ behavior: 'smooth' });
    });
  }

  if (formCityNotify) {
    formCityNotify.addEventListener('submit', (e) => {
      e.preventDefault();
      const contactInput = document.getElementById('cityNotifyContact');
      const contact = contactInput ? contactInput.value.trim() : '';
      const city = comingSoonCityName ? comingSoonCityName.textContent : 'Mumbai';

      try {
        fetch('api/leads.php', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ action: 'city_waitlist', city: city, contact: contact })
        }).catch(() => {});
      } catch (err) {}

      closeModal(modalCityComingSoon);
      showToast(`🎉 You are on the early access VIP list for ${city}! We will notify you on launch.`);
      if (contactInput) contactInput.value = '';
    });
  }
"""

last_closing = code.rfind("});")
assert last_closing != -1, "Last closing not found!"
code = code[:last_closing] + city_modal_logic + "\n" + code[last_closing:]

with open("/Users/chetanbisariya/.gemini/antigravity-ide/scratch/exainfra-in/app.js", "w") as f:
    f.write(code)

print("Successfully updated app.js with v5 verified Bengaluru listings and seeker visit flow!")
