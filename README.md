# AEG B2B – Playwright + Behave (BDD) Framework — UAT-A

BDD UI automation for the AEG B2B site (German **UAT-A** environment), built with
**Behave** (Gherkin) + **Playwright** (sync API) using the **Page Object Model**,
with **Allure** reporting. The structure mirrors the `BehavePOPlaywright` reference project.

**Target site:** https://t1-aeg-uat-a.eluxmkt.com/de-de/b2b/pre-login/

---

## Folder structure

```
Playwrite- UAT-A/
├── ConfigurationData/
│   └── conf.ini                 # site URL, browser choice, and all locators
├── Logs/                        # auto-generated daily log files
├── allure_reports/              # Allure results (generated on run)
├── Utilities/
│   ├── configReader.py          # reads conf.ini  ->  readConfig(section, key)
│   └── LogUtil.py               # Logger class (file logging)
├── features/
│   ├── environment.py           # Behave hooks: browser open/close + screenshot on fail
│   ├── prelogin.feature         # Gherkin scenarios
│   ├── pageobjects/
│   │   ├── BasePage.py          # reusable actions (click, type, select, ...)
│   │   └── PreLoginPage.py      # pre-login page object (extends BasePage)
│   └── steps/
│       └── prelogin_step.py     # step definitions (Given/When/Then)
├── requirements.txt
└── README.md
```

---

## One-time setup (Windows / PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium
```

> If `Activate.ps1` is blocked by policy, run this once in the same window:
> `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

---

## Run the tests

Run all commands from the project root (this folder), with the venv activated.

```powershell
behave                                  # run everything
behave --tags=@smoke                    # only the smoke scenario (passes out of the box)
behave --tags=@login                    # the login scenario (after you add real locators)
behave features/prelogin.feature        # a single feature file
```

### Allure report

```powershell
behave -f allure_behave.formatter:AllureFormatter -o allure_reports
allure serve allure_reports
```

---

## How to extend it (add a new page / test)

1. **Add locators** under `[locators]` in `ConfigurationData/conf.ini`.
2. **Create a page object** in `features/pageobjects/` that extends `BasePage`
   and exposes business methods (e.g. `set_email`, `submit_form`).
3. **Write a `.feature` file** in `features/` with your Gherkin scenarios.
4. **Bind the steps** in `features/steps/` — each step calls a page-object method.

---

## Notes

- The locators in `conf.ini` are **placeholders**. Replace them with the real ones:
  `playwright codegen https://t1-aeg-uat-a.eluxmkt.com/de-de/b2b/pre-login/`
  (or DevTools → Inspect → Copy XPath).
- Switch the browser in `conf.ini` → `[basic info] browser = chrome` (or `firefox`).
  Tests run **headed** so you can watch them.
- The `@login` scenario is tagged `@wip` (work in progress) — finish the locators,
  then remove the tag.
