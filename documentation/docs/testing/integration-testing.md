---
sidebar_position: 2
---
# Integration tests

Tests to demonstrate each use-case based on the use-case descriptions and the sequence diagrams. External input should be provided via mock objects and results verified via mock objects. Integration tests should not require manual entry of data nor require manual interpretation of results.


## FF Views Integration Authenticated Tests
This test suite contains all of the tests necessary to test whether a properly authenticated user is able to access the pages that they should have access to, and that the data is coming back in the correct format (HTML or JSON, depending on the route)

This test suite makes use of `django.test.Client`, which is a sandbox client for making request to the django server. In this case, the client is mocking the behavior of the React.js application. 
### Tests

* `test_authenticated_user_can_access_async_complementary_recommendations_routine` 
  * Tests than an authenticated user can access the "complementary pieces" API. Expected result is allowed access.
* `test_authenticated_user_can_access_async_recommendations_routine` 
  * Tests than an authenticated user can access the "pieces like ths" API.  Expected result is allowed access.
* `test_authenticated_user_can_access_async_wardrobe_routine` 
  * Tests than an authenticated user can access the "wardrobe" API.  Expected result is allowed access.
* `test_authenticated_user_can_access_upload_page`
  * Tests than an authenticated user can access the page to upload a new file.  Expected result is allowed access.
* `test_authenticated_user_can_access_home_page`
  * Tests than an authenticated user can access the home page.  Expected result is allowed access.

## FF Views Integration Unauthenticated Tests
This test suite contains all of the tests necessary to test whether an unauthenticated user is able to visit the site and authenticate themselves. It tests that the unauthenticated user able to visit the site, 

Like the suite above, test suite makes use of `django.test.Client`, which is a sandbox client for making request to the django server. Again, the client is mocking the behavior of the React.js application. 
### Tests
* `test_unauthenticated_user_index`
  * Tests than an unauthenticated user can navigate to the site. Expected result is redirect to login
* `test_unauthenticated_user_index_receives_cookie`
  * Tests than an unauthenticated user receives a cookie upon navigating to the site. Expected result is `csrftoken` cookie being present in the browser.
* `test_unauthenticated_user_login_user_does_not_exist`
  * Tests than an unauthenticated user is not authenticated when attempting to login with a user that does not exist. Expected result is redirection to login page.
* `test_unauthenticated_user_login_wrong_password`
  * Tests than an unauthenticated user is not authenticated when attempting to login with a correct user and incorrect password. Expected result is redirection to login page.
* `test_unauthenticated_user_login_wrong_password_with_email`
  *  Tests than an unauthenticated user is not authenticated when attempting to login with a correct email and incorrect password. Expected result is redirection to login page.
* `test_unauthenticated_user_login_correct_password`
  * Tests than an unauthenticated user is authenticated when attempting to login with a correct username and password. Expected result is redirection to home page.
