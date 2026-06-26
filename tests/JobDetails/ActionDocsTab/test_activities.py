
class TestActivities:

    def test_tc93_click_activities_tab(self, activities_page):
        """TC-93:
        1. Click Activities sub-tab.
    
        """
        # Step 1 — click Activities sub-tab   
        activities_page.click_activities_tab()