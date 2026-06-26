# Cilio App — Test Case Analysis Sheet

---

## test_login.py — `TestLogin`

| TC ID | Method | Screen | Flow / What It Validates |
|-------|--------|--------|--------------------------|
| TC-01 | `test_tc01_empty_credentials` | Login | Empty username & password → user stays on login page |
| TC-02 | `test_tc02_valid_username_invalid_password` | Login | Valid username + wrong password → user stays on login page |
| TC-03 | `test_tc03_invalid_username_valid_password` | Login | Wrong username + valid password → user stays on login page |
| TC-04 | `test_tc04_invalid_credentials` | Login | Both fields invalid → user stays on login page |
| TC-05 | `test_tc05_valid_credentials` | Login | Valid credentials → login succeeds and navigates away from login page |

---

## test_my_work.py — `TestMyWork`

| TC ID | Method | Screen | Flow / What It Validates |
|-------|--------|--------|--------------------------|
| TC-06 | `test_tc06_header_always_visible` | My Work | Cilio logo and profile icon are always visible |
| TC-07 | `test_tc07_user_info_card_always_visible` | My Work | User name, role, View All Work, and My Badge are always visible |
| TC-08 | `test_tc08_refresh_button_always_visible` | My Work | Refresh button is always visible |
| TC-09 | `test_tc09_all_three_work_cards_visible` | My Work | Today, Tomorrow, and Yesterday work cards are all visible |
| TC-10 | `test_tc10_bottom_navigation_always_visible` | My Work | All bottom nav tabs (Home, Search, Schedule) are always visible |
| TC-11 | `test_tc11_no_job_sections_when_all_zero` | My Work | *(Scenario 1)* Job detail sections do NOT appear when all work card counts = 0 |
| TC-12 | `test_tc12_no_route_button_when_all_zero` | My Work | *(Scenario 1)* Route button does NOT appear when all work card counts = 0 |
| TC-13 | `test_tc13_card_with_jobs_is_visible` | My Work | *(Scenario 2)* Work card with count > 0 shows correct count and is tappable |
| TC-14 | `test_tc14_section_header_renders_only_for_cards_with_jobs` | My Work | *(Scenario 2)* Section header appears after tap only for cards with count > 0 |
| TC-15 | `test_tc15_log_work_card_summary` | My Work | Reads all work cards via card-reader utility; logs names/counts; asserts cards are visible |
| TC-16 | `test_tc16_pickup_report_visible_when_jobs_exist` | My Work | *(Scenario 2)* Pickup Report button is visible after tapping a card with jobs |
| TC-17 | `test_tc17_job_card_name_and_pay_visible` | My Work | *(Scenario 2)* Job card name and crew pay are visible after tapping a card with jobs |
| TC-18 | `test_tc18_expand_job_details_shows_all_fields` | My Work | *(Scenario 2)* Every expanded Job Detail card shows all expected labels (Name, Crew Pay, Labor Category, Customer City, Company, Start/End/Duration, Scope of Work) |
| TC-19 | `test_tc19_scroll_down_reveals_job_detail_and_route_button` | My Work | *(Scenario 2)* Scrolling down reveals job detail section and route button |
| TC-20 | `test_tc20_scroll_up_restores_header` | My Work | *(Scenario 2)* Scrolling back up brings Cilio logo (header) back into view |
| TC-21 | `test_tc21_tap_pickup_report_button` | My Work | *(Scenario 2)* Pickup Report, Job Section Card, and Route Button all rendered; taps Pickup Report |
| TC-22 | `test_tc22_tap_job_section_card` | My Work | *(Scenario 2)* Job section card rendered; tapping it navigates to Job Detail; back arrow returns |
| TC-23 | `test_tc23_tap_route_button` | My Work | *(Scenario 2)* Route button rendered; tapping it navigates to route screen; back arrow returns |
| TC-24 | `test_tc24_tap_profile_icon_navigates_to_profile` | My Work | Tapping the profile icon navigates to Profile screen |

---

## test_profile.py — `TestProfile`

| TC ID | Method | Screen | Flow / What It Validates |
|-------|--------|--------|--------------------------|
| TC-25 | `test_tc25_profile_screen_elements` | Profile | All expected elements are present on the Profile screen |
| TC-26 | `test_tc26_my_badge_navigation` | Profile | Tapping My Badge navigates to My Badge screen; back arrow returns |
| TC-27 | `test_tc27_my_account_navigation` | Profile | Tapping My Account navigates to My Account screen; scroll and back arrow returns |
| TC-28 | `test_tc28_view_cilio_dashboard_navigation` | Profile | Tapping View Cilio Dashboard opens dashboard/external link; returns via profile icon |
| TC-29 | `test_tc29_privacy_policy_page` | Profile | Privacy Policy page opens; scroll actions work; back arrow returns |
| TC-30 | `test_tc30_terms_conditions_page` | Profile | Terms & Conditions page opens; scroll actions work; back arrow returns |
| TC-31 | `test_tc31_logout_functionality` | Profile | Tapping Logout shows confirmation dialog; Cancel dismisses it without logging out |
| TC-32 | `test_tc32_logout_functionality` | Profile | Tapping Logout shows confirmation dialog; Confirm completes the logout |
| TC-33 | `test_tc33_valid_credentials` | Login | Re-login with valid credentials after logout succeeds |
| TC-34 | `test_tc34_tap_my_work_navigates_to_my_work` | Profile | Tapping My Work button navigates to My Work screen |
| TC-35 | `test_tc35_tap_home_nav_navigates_to_home` | Profile | Tapping Home nav icon navigates to Home screen |
| TC-36 | `test_tc36_tap_search_nav_navigates_to_search` | Profile | Tapping Search nav icon navigates to Search screen |
| TC-37 | `test_tc37_tap_schedule_nav_navigates_to_schedule` | Profile | Tapping Schedule nav icon navigates to Schedule screen |
| TC-38 | `test_tc38_tap_home_nav_navigates_to_home_from_schedule` | Profile | Tapping Home nav from Schedule screen navigates to Home screen |
| TC-39 | `test_tc_39_tap_view_all_work_navigates_to_view_all_work` | Profile | Tapping View All Work button navigates to View All Work screen |

---

## test_view_all_work.py — `TestViewAllWork`

| TC ID | Method | Screen | Flow / What It Validates |
|-------|--------|--------|--------------------------|
| TC-40 | `test_tc40_header_always_visible` | View All Work | Cilio logo and profile icon are always visible |
| TC-41 | `test_tc41_user_info_card_always_visible` | View All Work | User name, role, My Work button, and My Badge are always visible |
| TC-42 | `test_tc42_find_jobs_by_type_cards_visible` | View All Work | All "Find Jobs by Types" cards are visible; names and counts are logged |
| TC-43 | `test_tc43_bottom_navigation_always_visible` | View All Work | Home and Search nav tabs visible; Schedule tab is disabled |
| TC-44 | `test_tc44_tap_profile_icon_navigates_to_profile` | View All Work | Tapping profile icon navigates to Profile screen; back arrow returns |

---

## test_job_status.py — `TestJobStatus`

| TC ID | Method | Screen | Flow / What It Validates |
|-------|--------|--------|--------------------------|
| TC-45 | `test_tc45_tap_job_type_card_shows_job_status_screen` | View All Work → Job Status | Tapping a Job Type card with count > 0 navigates to Job Status screen with matching header |
| TC-46 | `test_tc46_tap_job_status_card_with_count` | Job Status | Taps the first status sub-card that has count > 0 |

---

## test_global_search.py — `TestGlobalSearch`

| TC ID | Method | Screen | Flow / What It Validates |
|-------|--------|--------|--------------------------|
| TC-47 | `test_tc45_search_screen_loaded` | Search | Cilio logo and search bar are visible on Search screen |
| TC-48 | `test_tc46_search_bar_placeholder_visible` | Search | "Search..." placeholder text is visible in the search bar |
| TC-49 | `test_tc47_find_jobs_by_filters_label_visible` | Search | "Find Jobs by Filters" section label is visible |
| TC-50 | `test_tc50_bottom_navigation_visible` | Search | Home and Search nav tabs visible; Schedule tab disabled |
| TC-51 | `test_tc51_tap_search_bar_opens_input` | Search | Tapping the search bar opens the search input |
| TC-52 | `test_tc52_enter_search_text` | Search | Typing "testing" in the search bar sets the input field value correctly |
| TC-55 | `test_tc55_tap_random_three_search_result_cards` | Search → Job Detail | Taps 3 random result cards from "testing" query; back arrow returns after each |
| TC-56 | `test_tc56_tap_clear_search` | Search | Tapping the clear button clears the search input |
| TC-57 | `test_tc57_tap_search_back_arrow` | Search | Tapping the back arrow inside the search input navigates back |

---

## test_basic_Advance_Search.py — `TestBasicAndAdvancedSearch`

| TC ID | Method | Screen | Flow / What It Validates |
|-------|--------|--------|--------------------------|
| TC-58 | `test_tc45_search_screen_loaded` | Search | Cilio logo and search bar are visible |
| TC-59 | `test_tc46_search_bar_placeholder_visible` | Search | "Search..." placeholder text is visible |
| TC-60 | `test_tc47_find_jobs_by_filters_label_visible` | Search | "Find Jobs by Filters" label is visible |
| TC-61 | `test_tc48_basic_filter_button_visible` | Search | "Basic" filter button is visible |
| TC-62 | `test_tc49_advanced_filter_button_visible` | Search | "Advanced" filter button is visible |
| TC-63 | `test_tc50_bottom_navigation_visible` | Search | Bottom nav tabs visible; Schedule disabled |
| TC-64 | `test_tc51_tap_basic_search_navigates_to_basic_search` | Search | Tapping "Basic" filter button navigates to Basic Search screen |
| TC-65 | `test_tc52_basic_search_fields_and_go` | Basic Search | Go and Clear buttons visible; logs all enabled filter fields for current user |
| TC-66 | `test_tc53_enter_customer_first_name_and_go` | Basic Search | Enters "testing" in Customer First Name field and taps Go |
| TC-67 | `test_tc54_tap_random_basic_search_result_cards` | Basic Search Results | Taps up to 2 random result cards; back arrow returns to Basic Search |
| TC-68 | `test_tc55_tap_clear_shows_confirmation_dialog_ok_clear` | Basic Search | Tapping Clear shows confirmation dialog; taps Ok to clear |
| TC-69 | `test_tc56_enter_city_and_go` | Basic Search | Enters "city" in City field and taps Go |
| TC-70 | `test_tc57_tap_random_cards_after_city_search` | Basic Search Results | Taps up to 2 random cards from City search; back arrow returns |
| TC-71 | `test_tc58_tap_clear_shows_confirmation_dialog_ok_clear` | Basic Search | Tapping Clear shows confirmation dialog; taps Ok to clear |
| TC-72 | `test_tc59_enter_phone_number_and_go` | Basic Search | Enters "1234567890" in Phone Number field and taps Go |
| TC-73 | `test_tc60_tap_random_cards_after_phone_search` | Basic Search Results | Taps up to 2 random cards from Phone Number search; back arrow returns |
| TC-74 | `test_tc61_tap_clear_shows_confirmation_dialog_ok_clear` | Basic Search | Tapping Clear shows confirmation dialog; taps Ok to clear |
| TC-75 | `test_tc62_navigate_back_from_basic_search` | Basic Search | Back arrow on Basic Search returns to main Search screen |
| TC-76 | `test_tc63_tap_advanced_search_navigates_to_advanced_search` | Search | Tapping "Advanced" filter button navigates to Advanced Search screen |
| TC-77 | `test_tc64_advanced_search_status_and_go` | Advanced Search | Logs all enabled Job Statuses; selects "New"; taps Go; taps 2 random result cards |
| TC-78 | `test_tc65_advanced_search_type_and_go` | Advanced Search | Logs all enabled Job Types; selects "Assessment"; taps Go; taps 2 random result cards |

---

## tests/JobDetails/test_base_jobpage.py — `TestJobDetailsBasePage`

| TC ID | Method | Screen | Flow / What It Validates |
|-------|--------|--------|--------------------------|
| TC-79 | `test_tc59_job_details_header_visible` | Job Details | Header, Hot Buttons, Measures button, dynamic name, and Lead Safe button are all visible |
| TC-80 | `test_tc60_hot_buttons_and_navigation` | Job Details | Tapping Hot Buttons navigates to that screen; back arrow returns to Job Details |
| TC-81 | `test_tc61_measures_button_disabled` | Job Details | Measures button is visible but disabled (not interactable) |
| TC-82 | `test_tc62_cust_site_and_job_sched_buttons` | Job Details | Cust/Site, Job/Sched, and Actions/Docs tab buttons are all visible |
| TC-83 | `test_tc63_measures_button_and_navigation` | Job Details | Taps the disabled Measures button; back arrow returns to Job Details |
| TC-84 | `test_tc64_tap_profile_icon` | Job Details | Tapping profile icon navigates away; back arrow returns |

---

## tests/JobDetails/CustSiteTab/test_seller_info.py — `TestSellerInfoTab`

| TC ID | Method | Screen | Flow / What It Validates |
|-------|--------|--------|--------------------------|
| TC-85 | `test_tc65_seller_info_tab_visible` | Job Details → Cust/Site | The Seller Info tab is visible on the Job Details screen |
| TC-86 | `test_tc66_tap_seller_info_tab` | Seller Info tab | Tapping Seller Info tab displays non-empty store name and store address |

---

## tests/JobDetails/CustSiteTab/test_site_info.py — `TestSiteInfoPage`

| TC ID | Method | Screen | Flow / What It Validates |
|-------|--------|--------|--------------------------|
| TC-87 | `test_tc64_site_info_fields_visible` | Site Info tab | Distance to Seller, Avg. Time to Seller, Built Pre-1978, and Lead Safe Job fields are visible |
| TC-88 | `test_tc65_zillow_button_info` | Site Info → Zillow bottom sheet | Tapping Zillow icon opens bottom sheet with title, data, link, and close button |
| TC-89 | `test_tc66_zillow_button_navigation` | Site Info → Zillow webview | Tapping the Zillow ToS link and then back arrow returns to Site Info tab |
| TC-90 | `test_tc65_is_lead_safe_job_checkbox_checked` | Site Info tab | *(Checked path)* Lead Safe checkbox checked → related questions, dropdowns, Lead Collection Form, and Responsible User elements are visible |
| TC-91 | `test_tc66_is_lead_safe_job_checkbox_unchecked` | Site Info tab | *(Unchecked path)* Lead Safe checkbox unchecked → related questions and dropdowns are NOT visible; Lead Collection Form and Responsible User still present |
| TC-92 ⚠️ | `test_tc67_select_random_option_dropdown_built_pre` | Site Info tab | Opens Built Pre-1978 dropdown and selects a random option (method name says TC-67, docstring says TC-68) |
| TC-93 ⚠️ | `test_tc69_tap_lead_collection_form_button` | Site Info → Lead Collection Form | Taps Lead Collection Form button; verifies navigation away; back arrow returns (method says TC-69, docstring says TC-70) |
| TC-94 ⚠️ | `test_tc70_tap_responsible_user_icon` | Site Info → Responsible User | Tapping Responsible User icon opens the bottom sheet; closing returns to Site Info tab (method says TC-70, docstring says TC-67) |

> ⚠️ **TC ID Mismatch Note**: In `test_site_info.py`, the last three methods have inconsistencies between the method name TC number and the docstring TC number. Review and align these before final reporting.

---

## Summary

| Module | TC Range | Total TCs |
|--------|----------|-----------|
| test_login.py | TC-01 – TC-05 | 5 |
| test_my_work.py | TC-06 – TC-24 | 19 |
| test_profile.py | TC-25 – TC-39 | 15 |
| test_view_all_work.py | TC-40 – TC-44 | 5 |
| test_job_status.py | TC-45 – TC-46 | 2 |
| test_global_search.py | TC-45 – TC-57 | 9 |
| test_basic_Advance_Search.py | TC-45 – TC-65 | 21 |
| test_base_jobpage.py | TC-59 – TC-64 | 6 |
| test_seller_info.py | TC-65 – TC-66 | 2 |
| test_site_info.py | TC-64 – TC-70 | 8 |
| **Total** | | **94** |
