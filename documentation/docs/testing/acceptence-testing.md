---
sidebar_position: 3
---
# Acceptance test

Demonstration of all of the functional and non-functional requirements. This can be a combination of automated tests derived from the use-cases (user stories) and manual tests with recorded observation of the results.

<!-- ## Selenium/pytest  -->

## Unauthenticated Automated Tests
This test suite (located at `FashionFinderAutomatedTests/unauthenticated_automated_tests.py`) makes use of the selenium webdriver to run functional tests on the fashion finder application. The suite focuses on automating the actions of the unauthenticated user, and tests whether they are able to properly authenticate with the server. 
### Tests
* `test_google`
  * Tests that the selenium web driver is working. Expected result is to navigate to google.com
* `test_home_page`
  * Tests that an unauthenticated user is able to access the home page with nav bar. Expected result is that the home page renders 
* `test_home_page_attempt_upload`
  * Tests that an unauthenticated user not able to access the upload page. Expected result is redirect to login
* `test_attempt_login`
  * Tests than an unauthenticated user is able to login with correct credentials. Expected result is redirection home page
* `test_attempt_register`
  * Tests that an unathenticated user is able to register a new account. Expected result is is redirection to home page.
## Authenticated Automated Tests

This test suite  (located at `FashionFinderAutomatedTests/authenticated_automated_tests.py`) also makes use of the selenium webdriver to run functional tests. The suite focuses on automating the actions of the authenticated user, and tests the user stories laid out in [use-case-descriptions.md](../requirements/use-case-descriptions.md)

### Tests
* `test_google`
  * Tests that selenium webdriver is working. Expected result is accessing google.com
* `test_home_page`
  * Tests that an authenticated user is able to access the home page. Expected result is no redirection.
* `test_home_page_attempt_access_upload`
  * Tests than an authenticated user can access the upload page. Expected result is no redirection.
* `test_home_page_attempt_upload`
  * Tests that an authenticated user can upload a file from local storage. Expected result is redirection to the home page and the view the uploaded item
* `test_home_page_can_view_items`
  * Tests the "Item tracker" use-case. Expected result is that the user can view their uploaded items
* `test_home_page_can_view_item_labels`
  * Tests the "Item labeler" use-case. Expected result is that the user can view the labels assigned to their items.
* `test_home_page_can_view_color_labels`
  * Tests the "Color labeler" use-case. Expected result is that the user can view the colors assigned to their items
* `test_home_page_can_view_similar_items`
  * Tests the "Finding similar items" use-case. Expected result is that the user can view similar items to items in their wardrobe.
* `test_home_page_can_view_complementary_items`
  * Tests the "Finding complementary items" use-case. Expected result is that the user can view complementary items in their wardrobe.

There is no test case for the "Like/Dislike" functionality as the functionality was not delivered at the time of developing the test suite.
