# Cilio App — Automation Work Done

## App Under Test
Cilio — React Native Android field service management app (`io.cilio.cio.qa`)

---

## Screens Completed

1. **Login Screen** — User authentication with valid/invalid credential handling
2. **My Work Screen (Home)** — Work cards (Today / Tomorrow / Yesterday), job counts, job detail expansion, Route & Pickup Report buttons
3. **Profile Screen** — User info, My Badge, My Account, Cilio Dashboard, Privacy Policy, Terms & Conditions, Logout flow
4. **View All Work Screen** — "Find Jobs by Types" cards with job counts
5. **Job Status Screen** — Job status sub-cards after selecting a job type (e.g. Active, New)
6. **Global Search Screen** — Search bar, result cards, random card navigation, clear search
7. **Basic & Advanced Search Screen** — Filter button navigation, enabled filter field enumeration, Go/Clear actions
8. **Hybrid WebView** — Context switching between native app and embedded WebView
9. **Job Details — Base Page** — Job details header, Hot Buttons, Measures, tab bar (Cust/Site, Job/Sched, Actions/Docs), dynamic job name, Lead Safe button
10. **Job Details — Seller Info Tab** — Seller Info tab navigation, Store Name and Store Address fields
11. **Job Details — Site Info Tab** — Distance/Time to Seller fields, Lead Safe checkbox with conditional fields, Built Pre-1978 & Lead Safe dropdowns, Zillow bottom sheet & webview, Responsible User bottom sheet, Lead Collection Form navigation

---

## Utilities Built

- **Card Reader** — Scrollable multi-pass card list reader with deduplication (parses name + count from `content-desc`)
- **Field Reader** — Scrollable multi-pass input field hint reader with deduplication
- **Wait Helpers** — WebDriverWait wrappers for visible, present, clickable, disappear, and text conditions
- **Logger** — Named logger factory with timestamped console output
- **Screenshot Handler** — Auto-saves failure screenshots to `Screenshots/` on test failure
- **Constants** — Central locator and timeout definitions shared across all pages

---

## Infrastructure

- **Driver Factory** — Builds Appium session from YAML device profiles (emulator / real device), 600s HTTP timeout
- **Config System** — Profile-based device/capabilities config via `device_config.yaml` + `.env`
- **Session-Scoped Driver** — Single Appium session reused across the entire test run
- **Auto Screenshot on Failure** — Root `conftest.py` hook captures PNG for every failing test
- **pytest Setup** — Markers (`smoke`, `regression`, `hybrid`), 120s test timeout, HTML report output
