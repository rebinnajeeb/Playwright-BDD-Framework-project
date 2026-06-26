# AEG B2B Playwright (Python) — Build Roadmap

This is my plan to rebuild the **chiron-b2b-automation** Java Selenium test suite
in **Playwright + Python + Behave**. I follow the same conventions I already use in
`PreLoginPage.py`.

---

## Build Style (same as PreLoginPage)

- **Selectors live directly inside each page-object method** — NOT in conf.ini.
  ```python
  def go_to_login(self):
      self.page.locator("a.btn...[href*='SciProxyCaller']").click()
  ```
- **conf.ini holds ONLY:** browser, market, and per-market URLs.
- **Excel (LoginData.xlsx)** holds credentials per market sheet.
- **Step definitions call page methods** — they never contain selectors.
- **Action steps (When/And)** need no assertion (Playwright throws if element missing).
  **Verification steps (Then)** use one explicit `assert` or `expect(...).to_be_visible()`.
- For waiting on a result, prefer `expect(locator).to_be_visible(timeout=10000)`.

### Folder layout (target)
```
features/
  pageobjects/
    BasePage.py          (done - shared navigate/log helpers)
    PreLoginPage.py      (done)
    HomePage.py          (TODO - top nav, category menu, search btn, profile dropdown)
    PLPPage.py           (TODO - ONE page for ALL category listings + core range)
    PDPPage.py           (TODO - product detail)
    BasketPage.py        (TODO)
    WishlistPage.py      (TODO)
    ComparePage.py       (TODO)
    SearchPage.py        (TODO)
    MyAccountPage.py     (TODO)
    ContactUsPage.py     (TODO)
  steps/
    prelogin_step.py     (done)
    <one *_step.py per feature>
  <one *.feature per functionality>
```

> KEY: There is NO page per category. Oven / Washing Machine / Cooking / Core Range
> are just different category URLs that all reuse the SAME `PLPPage`.

---

## Page Objects to Create (mirrors Java)

| Python Page | Java equivalent | Responsibility |
|---|---|---|
| `HomePage.py` | AegHomePage + PartnerPortalHomePage | top nav menus, category menu, search button, profile/logout dropdown, brand pop-up |
| `PLPPage.py` | PLPpage | product listing: filters, sort, add-to-basket, add-to-wishlist, compare |
| `PDPPage.py` | PDPpage | product detail: add to basket, accessories block, model/PNC/EAN read |
| `BasketPage.py` | BasketPage | view/clear basket, verify product added |
| `WishlistPage.py` | WishListPage | view/empty wishlist, verify product added |
| `ComparePage.py` | ComparePage | compare 2 products, remove, add-to-basket |
| `SearchPage.py` | SearchPage | search results, load more, view product |
| `MyAccountPage.py` | MyAccount | account edits, delivery, brand setting |
| `ContactUsPage.py` | ContactUsPage | contact + service-repair forms |

---

## Test Cases — full inventory (from the Java project)

> Skip these (they were commented-out / inactive in Java):
> NavigationMenus, OrderStatus, FocusRange, PremierLine, PriceDisplay, Sets.

### PHASE 1 — Auth
- [x] **Login** — valid credentials → lands on partner portal *(DONE)*
- [ ] **Login** — invalid credentials → error message shown
- [ ] **Logout** — click profile dropdown → logout → back on prelogin page

### PHASE 2 — Navigation menus (easy: click + verify)
- [ ] **Sales & Marketing** — link shown / submenus shown / submenu pages open
- [ ] **Orders** — link shown / submenus shown / submenu pages open
- [ ] **Training** — link shown / submenus shown / submenu pages open
- [ ] **Tools & Services** — link shown / submenus shown / submenu pages open
- [ ] **Footer** — first & third footer column links navigate correctly

### PHASE 3 — Product browsing
- [ ] **Categories** — click category menu → list of product categories shown
- [ ] **Search** — by category + load more
- [ ] **Search** — by Model ID → verify model id on PDP
- [ ] **Search** — by PNC number → verify PNC on PDP
- [ ] **Search** — by EAN number → verify EAN on PDP
- [ ] **Filters** — toggle filters on oven PLP
- [ ] **Filters** — toggle filters on washing-machine PLP
- [ ] **Filters** — dropdown filters on oven PLP
- [ ] **Filters** — dropdown filters on washing-machine PLP
- [ ] **Filters** — apply dropdown filters + reset
- [ ] **Sorting** — highest rating
- [ ] **Sorting** — highest price
- [ ] **Sorting** — lowest price
- [ ] **Sorting** — new label
- [ ] **Core Range** — dropdown filters / reset / sorting / add-to-basket / add-to-wishlist / no compare icon

### PHASE 4 — Cart & Wishlist
- [ ] **Add to Basket** — from PLP
- [ ] **Add to Basket** — from PDP
- [ ] **Add to Basket** — from Wishlist
- [ ] **Add to Basket** — from Accessories block (PDP)
- [ ] **Add to Basket** — from Search results
- [ ] **Add to Wishlist** — from PLP
- [ ] **Add to Wishlist** — from PDP
- [ ] **Add to Wishlist** — from Accessories block
- [ ] **Add to Wishlist** — from Search results
- [ ] **Compare** — single product → compare button hidden
- [ ] **Compare** — 2 products → compare page shows price & stock
- [ ] **Compare** — remove a product from compare page
- [ ] **Compare** — add to basket from compare page

### PHASE 5 — Account & Forms (advanced)
- [ ] **My Account** — navigate to My Account page
- [ ] **My Account** — menu options shown
- [ ] **My Account** — registered email NOT editable
- [ ] **My Account** — edit phone number → save → success
- [ ] **My Account** — password reset link → success message
- [ ] **My Account** — edit communication email → save → shows in basket
- [ ] **My Account** — confirm-order / get-notification checkboxes checked
- [ ] **My Account** — delivery option visibility per user
- [ ] **My Account** — ship full / partial order → reflected in basket
- [ ] **My Account** — order status view (line / header)
- [ ] **My Account** — default brand setting + switch
- [ ] **Contact Us** — submit valid form → confirmation
- [ ] **Contact Us** — submit empty → description error
- [ ] **Service Repair** — submit valid → confirmation
- [ ] **Service Repair** — invalid phone → error
- [ ] **Service Repair** — empty → description error
- [ ] **Fast Order** — navigate to fast order page

### PHASE 6 — Store / Brand (Super User)
- [ ] **Brand Switching** — switch AEG ↔ Electrolux; basket persists
- [ ] **Store Switching** — switch store; basket persists

---

## Recommended order
1. Logout (quick win)
2. Navigation menus (Phase 2)
3. Categories → PLP → Basket (core flow)
4. Search
5. Filters & Sorting
6. Wishlist & Compare
7. My Account / User Management / Forms
8. Brand / Store switching

## Per-feature checklist (repeat for each)
1. Create/extend the page object (selectors inline, in its method).
2. Write the `.feature` file (Gherkin scenarios).
3. Write the matching `*_step.py` (steps call page methods only).
4. Run: `behave --tags=@<tag>`
5. Fix selectors using DevTools / `playwright codegen` when they differ.
6. Tick the box above.

## Notes / gotchas seen so far
- Cookie banner: `#onetrust-accept-btn-handler` (its dark overlay blocks clicks until accepted).
- Login button is generic — needed `[href*='SciProxyCaller']` to pick the right one.
- "Log On" matched title + heading + button → used `get_by_role("button", name="Log On")`.
- Home welcome text: `Willkommen im AEG Partner Portal - Schön, dass Sie da sind` (market-specific!).
- `is_visible()` does NOT auto-wait; use `expect(...).to_be_visible(timeout=...)` to wait.
