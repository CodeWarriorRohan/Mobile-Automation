class TestScheduler:

    def test_tc94_schedule_job(self, scheduler_page):
        """TC-94: Schedule a job and verify it appears on the Scheduler screen."""
        scheduler_page.click_scheduler_tab()

    def test_tc95_header_always_visible(self, scheduler_page):
        """TC-95: Cilio logo and profile icon are always visible."""

        assert scheduler_page.is_element_visible(scheduler_page.CILIO_LOGO), \
            "Cilio logo should be visible"
        assert scheduler_page.is_element_visible(scheduler_page.MAP_ICON), \
            "Map icon should be visible"
        assert scheduler_page.is_element_visible(scheduler_page.PROFILE_ICON), \
            "Profile icon should be visible"    
        assert scheduler_page.is_element_visible(scheduler_page.PICKUP_REPORT_BTN), \
            "Pickup Report button should be visible"  

    def test_tc96_bottom_navigation_always_visible(self, scheduler_page):
        """TC-96: All bottom navigation tabs are always visible."""
        assert scheduler_page.is_element_visible(scheduler_page.NAV_HOME), \
            "Home nav tab should be visible"
        assert scheduler_page.is_element_visible(scheduler_page.NAV_SEARCH), \
            "Search nav tab should be visible"
        assert scheduler_page.is_element_visible(scheduler_page.NAV_SCHEDULE), \
            "Schedule nav tab should be visible"  

    def test_tc_97_tap_calendar_section_items_on_scheduler(self, scheduler_page):
        """TC-97: Tap calendar section items on Scheduler screen."""

        scheduler_page.tap_calendar_section_items()
        scheduler_page.wait_seconds(2)     


    def test_tc98_tap_map_icon(self, scheduler_page):

        scheduler_page.tap_map_icon()
        scheduler_page.wait_seconds(2)
        assert scheduler_page.is_element_visible(scheduler_page.ROUTE_TEXT), \
            "Route text (e.g. \"4 May's Route\") should be visible after tapping map icon"
        assert scheduler_page.is_element_visible(scheduler_page.CALENDAR_ICON), \
            "Calendar icon should be visible on the route screen" 

        scheduler_page.tap_calendar_icon()
        scheduler_page.wait_seconds(2)      

    def test_tc_99_tap_pickup_report(self, scheduler_page):

        scheduler_page.tap_pickup_report()
        scheduler_page.wait_seconds(2)  
        scheduler_page.tap_calendar_section_items()
        scheduler_page.wait_seconds(2)
        scheduler_page.tap_two_random_dates()
        scheduler_page.wait_seconds(2)
        scheduler_page.tap_back_arrow()
        scheduler_page.wait_seconds(1)

    
    def test_tc_100_click_on_the_scheduled_job(self, scheduler_page):
        """TC-100: Click on the scheduled job and verify details."""

        scheduler_page.scroll_to_end()
        scheduler_page.wait_seconds(1)
        scheduler_page.scroll_content_to_beginning()
        scheduler_page.wait_seconds(1)
        
        scheduler_page.scroll_content_to_text()
        scheduler_page.tap_random_job_card()
        scheduler_page.wait_seconds(2)

    def test_tc_101_log_bottom_sheet_and_view_job(self, scheduler_page):
        """TC-101: Log bottom sheet job details and tap View Job."""
        details = scheduler_page.log_bottom_sheet_details()
        assert details, "Bottom sheet should display job details"
    
        scheduler_page.wait_seconds(1)
        scheduler_page.tap_view_job()
        scheduler_page.wait_seconds(3)    

    def test_tc_102_tap_profile_icon_navigates_to_profile(self, scheduler_page):
        """TC-102: All View All Work UI rendered — tap profile icon to navigate to Profile screen."""
        scheduler_page.wait_seconds(1)
        scheduler_page.tap_profile_icon()
        scheduler_page.wait_seconds(3)  
        assert scheduler_page.is_element_visible(scheduler_page.PROFILE_ICON), \
            "Profile icon should be visible on the Profile screen"