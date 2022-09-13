---
sidebar_position: 4
---

# Features and Requirements

## User Accounts

### Login Page

Users will be able to create a new account or login to an existing account. Login security will be managed using Django's authentication module, which can be leveraged to handle unsuccessful logins as well as password resets.

### Account Home Page

Active users will be redirected to a (personalized home page?) upon a successful login. At the top of the home screen will be a naviagation bar with item search functionality, a greeting to the user_name, and an option to logout. The majority of the home page below the navigation bar will be devoted to item recommendations.

## Favorited Items

Users will be able to save items they find into a favorited items list. Information about the items color, category, and brand will be stored in a database tracking user preferences.

## Recommended Items

Items will be recommended to user accounts. Recommendations will be made using ResNet and Tensorflow to recognize and categorize clothing items as well as label the data, and then Scikit learn’s K nearest neighbor algorithm to generate a similarity score and provide the final recommendation.