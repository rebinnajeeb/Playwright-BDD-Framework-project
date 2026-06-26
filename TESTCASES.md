# AEG B2B — Full Test Case List (from chiron-b2b-automation Java suite)

**~90 distinct scenarios.** Most are Scenario Outlines that run once per user/brand row
(mostly AEG + Electrolux = x2), so total test runs ≈ **175**.

You implement the **90 scenarios**; the "x2 AEG/Electrolux" + extra users come free by
adding rows to a Behave `Examples:` table under each `Scenario Outline` (same as Java).

Legend: `[ ]` = to do, `(xN)` = number of Examples rows (data variations) in Java.

---

## PHASE 1 — AUTH

**Login.feature** (`@Loginfunctionality`)
- [x] 1. Login with valid credentials -> land on B2B homepage, email shown top-right (x8 users: Admin/Advanced/Medium/Basic x AEG/Electrolux) *(DONE for de-de Admin)*
- [ ] 2. Login with invalid credentials -> error message shown (x1, Invalid_user)

**Logout.feature** (`@Logoutfunctionality`)
- [ ] 3. Logout from profile dropdown -> back to prelogin, cannot access logged pages (x2)

---

## PHASE 2 — NAVIGATION MENUS

**Sales&Marketing.feature** (`@SalesandmarketingNavigation`)
- [ ] 4. Sales & Marketing link is displayed (x2)
- [ ] 5. Submenus shown on clicking the menu (x2)
- [ ] 6. Navigate to each submenu page + verify content (x2)

**Orders.feature** (`@OrdersNavigation`)
- [ ] 7. Orders link is displayed (x2)
- [ ] 8. Submenus shown on clicking Orders (x2)
- [ ] 9. Navigate to each orders submenu page + verify content (x2)

**Training.feature** (`@TrainingNavigation`)
- [ ] 10. Training link is displayed (x2)
- [ ] 11. Submenus shown on clicking Training (x2)
- [ ] 12. Navigate to each training submenu page + verify content (x2)

**Tools&Services.feature** (`@ToolsandservicesNavigation`)
- [ ] 13. Tools & Services link is displayed (x2)
- [ ] 14. Submenus shown on clicking Tools & Services (x2)
- [ ] 15. Navigate to each tools submenu page + verify content (x2)

**Footer.feature** (`@Footer`)
- [ ] 16. Footer 1st & 3rd column links navigate correctly — from Partner Portal page (x2)
- [ ] 17. Footer 1st & 3rd column links navigate correctly — from PLP page (x2)
- [ ] 18. Footer 1st & 3rd column links navigate correctly — from iframe (order status) page (x2)

---

## PHASE 3 — PRODUCT BROWSING

**Categories&SubCategories.feature** (`@CategoriesNavigation`)
- [ ] 19. Click category menu -> list of product categories shown (x2)

**Search.feature** (`@Searchfunctionality`)
- [ ] 20. Search by product category + click "load more" (x2)
- [ ] 21. Search by Model ID -> view product -> verify Model ID on PDP (x2)
- [ ] 22. Search by PNC number -> view product -> verify PNC on PDP (x2)
- [ ] 23. Search by EAN number -> view product -> verify EAN on PDP (x2)

**Filters.feature** (`@Filters`)
- [ ] 24. Apply toggle filters on oven PLP (x2)
- [ ] 25. Apply toggle filters on washing machine PLP (x2)
- [ ] 26. Apply dropdown filters on oven PLP (x2)
- [ ] 27. Apply dropdown filters on washing machine PLP (x2)
- [ ] 28. Apply dropdown filters + reset on oven PLP (x2)

**ProductSorting.feature** (`@ProductSorting`)
- [ ] 29. Sort by highest rating (x2)
- [ ] 30. Sort by highest price (x2)
- [ ] 31. Sort by lowest price (x2)
- [ ] 32. Sort by new label (x2)

**CoreRange.feature** (`@CoreRange`)
- [ ] 33. Dropdown filters in core range (x2)
- [ ] 34. Dropdown filters + reset in core range (x2)
- [ ] 35. Sort highest rating (core range) (x2)
- [ ] 36. Sort highest price (core range) (x2)
- [ ] 37. Sort lowest price (core range) (x2)
- [ ] 38. Sort new label (core range) (x2)
- [ ] 39. Add to basket from core range PLP (x2)
- [ ] 40. Add to wishlist from core range PLP (x2)
- [ ] 41. No compare icon shown on core range PLP (x2)

---

## PHASE 4 — CART & WISHLIST

**AddToBasket.feature** (`@Addtobasket`)
- [ ] 42. Add to basket from PLP (x2)
- [ ] 43. Add to basket from PDP (x2)
- [ ] 44. Add to basket from Wishlist (x2)
- [ ] 45. Add to basket from Accessories block (PDP) (x2)
- [ ] 46. Add to basket from Search results (Model ID) (x2)

**AddToWishlist.feature** (`@Addtowishlist`)
- [ ] 47. Add to wishlist from PLP (x2)
- [ ] 48. Add to wishlist from PDP (x2)
- [ ] 49. Add to wishlist from Accessories block (x2)
- [ ] 50. Add to wishlist from Search results (x2)

**Compare.feature** (`@Compare`)
- [ ] 51. Add 1 product -> compare button stays hidden (x2)
- [ ] 52. Compare 2 products -> compare page shows price & stock (x2)
- [ ] 53. Remove a product from compare page (x2)
- [ ] 54. Add to basket from compare page (x2)

---

## PHASE 5 — ACCOUNT & FORMS

**MyAccount.feature** (`@MyAccount`)
- [ ] 55. Navigate to My Account page (x2)
- [ ] 56. See menu options from My Account (x2)
- [ ] 57. Registered email field is NOT editable (x2)
- [ ] 58. Edit phone number -> save -> success message (x2)
- [ ] 59. Password reset link -> success message (x2)
- [ ] 60. Edit communication email -> save (x2)
- [ ] 61. Updated communication email shows in Basket page (x2)
- [ ] 62. Confirm-order-via-mail & get-notification checkboxes are checked (x2)
- [ ] 63. Delivery option NOT visible for specific users (Basic/Medium) (x2)
- [ ] 64. Ship full order / ship partial order -> reflected in basket (x2)
- [ ] 65. Order status view: line view / header view -> reflected in order status page (x2)
- [ ] 66. Default brand setting + switch + re-login pop-up behavior (x1)

**UserManagement.feature** (`@UserManagement`) — admin/Super_User
- [ ] 67. Non-admin users cannot see User Management page (x2)
- [ ] 68. Navigate to User Management page (x2)
- [ ] 69. Create + delete a user (x2)
- [ ] 70. Change access right of a user (x2)
- [ ] 71. Reset password of a user -> success message (x2)
- [ ] 72. Search users by username (x2)
- [ ] 73. Search users by email (x2)
- [ ] 74. Sort by name / email / access right (asc + desc) (x2)
- [ ] 75. Validate created user persists after brand switch (x2)
- [ ] 76. Validate access-right change persists after brand switch (x2)

**ContactUs.feature** (`@Contactusform`)
- [ ] 77. Submit contact us form with valid info -> confirmation message (x2)
- [ ] 78. Submit empty -> Description field error message (x2)

**ServiceRepair.feature** (`@Servicerepairform`)
- [ ] 79. Submit service repair form valid -> confirmation (x2)
- [ ] 80. Invalid phone number -> error message (x2)
- [ ] 81. Submit empty -> Description field error (x2)

**FastOrder.feature** (`@FastOrder`)
- [ ] 82. Navigate to Fast Order page (x2)

---

## PHASE 6 — STORE / BRAND SWITCHING (Super_User)

**BrandSwitching.feature** (`@BrandSwitching`)
- [ ] 83. Different brand shown in switch dropdown (x1)
- [ ] 84. Switch brand from dropdown (x1)
- [ ] 85. Switch brand from pop-up (x1)
- [ ] 86. Basket products persist when returning to brand after switch (x1)

**StoreSwitching.feature** (`@StoreSwitching`)
- [ ] 87. Store switching dropdown shown for multi-store user (x1)
- [ ] 88. Switch store from dropdown (x1)
- [ ] 89. Switch store from pop-up (x1)
- [ ] 90. Basket products persist when returning to store after switch (x1)

---

## INACTIVE in Java (commented out — optional extras)
These files exist but are fully commented. The original team disabled them. Add only if you want extra coverage:
- NavigationMenus (2 scenarios)
- OrderStatus (2: see orders in status page, order details page)
- FocusRange (9: filters/sort/basket/wishlist/footer/compare — like Core Range but "Focus Range")
- PremierLine (9: same pattern, AEG Premium users)
- PriceDisplay (2: Net Invoice Price vs RRP radio button)
- Sets (4: sets PLP/PDP/basket/order)

---

## Count summary
| | Scenarios | ~ Test runs (with Examples) |
|---|---|---|
| Active (build these) | 90 | ~175 |
| Inactive (optional) | ~28 | ~50 |

## Common step phrasing used across features (reuse these step defs!)
- `Given the "<user>" logon to B2B partner portal`
- `And the user lands on partner portal homepage`
- `When the user is applicable to switch the "<brand>"`
- `When the user lands on oven plp` / `washing machine plp` / `core range page`
- `And the user clears basket` / `And the user empties wishlist page`
- `Then the product should be added in basket` / `... in wishlist`

> These shared steps mean: write the login + "land on homepage" + "switch brand" steps ONCE,
> and every other feature reuses them. Build those foundation steps first.

Feature files:

#	Feature File	Status	Scenarios
1	Login.feature	✅ Active	2
2	Logout.feature	✅ Active	1
3	Categories&SubCategories.feature	✅ Active	1 (1 commented)
4	Search.feature	✅ Active	4
5	Filters.feature	✅ Active	5
6	ProductSorting.feature	✅ Active	4
7	CoreRange.feature	✅ Active	9
8	AddToBasket.feature	✅ Active	5
9	AddToWishlist.feature	✅ Active	4
10	Compare.feature	✅ Active	4
11	Orders.feature	✅ Active	3
12	Sales&Marketing.feature	✅ Active	3
13	Tools&Services.feature	✅ Active	3
14	Training.feature	✅ Active	3
15	Footer.feature	✅ Active	3
16	MyAccount.feature	✅ Active	12
17	UserManagement.feature	✅ Active	10
18	ContactUs.feature	✅ Active	2
19	ServiceRepair.feature	✅ Active	3
20	FastOrder.feature	✅ Active	1
21	BrandSwitching.feature	✅ Active	4
22	StoreSwitching.feature	✅ Active	4
23	NavigationMenus.feature	❌ Commented	(2)
24	OrderStatus.feature	❌ Commented	(2)
25	FocusRange.feature	❌ Commented	(9)
26	PremierLine.feature	❌ Commented	(9)
27	PriceDisplay.feature	❌ Commented	(2)
28	Sets.feature	❌ Commented	(4)
29	Prelogin_contactus_login.feature	❌ Commented	(3)
30	PreloginContactUsForm.feature	❌ Commented	(3)
22 active feature files = 90 scenarios (all in your TESTCASES.md). 8 are commented out.

