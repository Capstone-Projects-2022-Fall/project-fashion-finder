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
  * Tests that the selenium web driver is working
* `test_home_page`
  * Tests that an unauthenticated user is able to access the home page with nav bar 
* `test_home_page_attempt_upload`
  * Tests that an unauthenticated user not able to access the upload page
* `test_attempt_login`
  * Tests than an unauthenticated user is able to login with correct credentials
* `test_attempt_register`
  * Tests that an unathenticated user is able to register a new account
## Authenticated Automated Tests

This test suite  (located at `FashionFinderAutomatedTests/authenticated_automated_tests.py`) also makes use of the selenium webdriver to run functional tests. The suite focuses on automating the actions of the authenticated user, and tests the user stories laid out in [use-case-descriptions.md](../requirements/use-case-descriptions.md)

### Tests
* `test_google`
  * Tests that selenium webdriver is working
* `test_home_page`
  * Tests that an authenticated user
* `test_home_page_attempt_access_upload`
  * Tests than an authenticated user can access the upload page
* `test_home_page_attempt_upload`
  * Tests that an authenticated user can upload a file from local storage.
* `test_home_page_can_view_items`
  * Tests the "Item tracker" use-case
* `test_home_page_can_view_item_labels`
  * Tests the "Item labeler" use-case
* `test_home_page_can_view_color_labels`
  * Tests the "Color labeler" use-case
* `test_home_page_can_view_similar_items`
  * Tests the "Finding similar items" use-case
* `test_home_page_can_view_complementary_items`
  * Tests the "Finding complementary items" use-case

There is no test case for the "Like/Dislike" functionality as the functionality was not delivered.
