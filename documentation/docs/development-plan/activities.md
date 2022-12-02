---
sidebar_position: 1
---

# Activities

## Requirements Gathering
### Functional Requirements
- Fashion Finder will have a randomized clothing content feed
     - Content will be pulled from the Pinterest API
     - Users will be able to like content in the feed and it will be saved to their account
     - The more content a user likes the better Fashion Finder will tailor recommendations to that user
- Fashion Finder will have an upload picture feature 
     - Users can upload clothing that is already in their wardrobe that they like 
     - Users can upload clothing that they found online and like
     - The clothing users upload will be used the same way liked clothing from the content is used to further tailor suggestions shown to that specific user.
- Fashion Finder will have a UI to provide outfit or clothing suggestions to the user
     - Suggestions will be based off of content liked on the content feed
     - Suggestions will be based off of content that has been uploaded by the user
     - The more content that a user uploads the better we can tailor results to that user
     - Users can either get suggestions on specific pieces of clothing, or users can get suggestions on entire outfits.
     - An outfit pairing or matching feature will available to the user, so they can find other pieces of clothing that go with items they already own.
- Fashion Finder will provide a price analysis tool to the user
     - The price analysis tool will be based off prices that are available on StockX
     - All outfit suggestions will be cross-checked with StockX to see if that specific item is available on Stockx.com
     - If an item is available on StockX a UI will be shown to show all recent purchases of that item, a price analysis chart, 12-month trade range, 3-month trade range, volitality, and price premium of that specific item. 
### Nonfunctional Requirements
- Fashion Finder will have a user-friendly interface 
     - The user interface will be easily navigatable, and will give clear instructions from the beginning on how a user can recieve the best outfit suggestions.
     - If any errors do occur the user will be prompted of the error
- Fashion Finder will be a progressive web application
     - Fashion Finder will have a easy to use UI on a web browser.
- Fashion Finder will use machine learning and big data to find similar items and complementary items
     - Individual clothing or wardrobe suggestions will be personalized to the users upload files.

 &nbsp;   In order to create the requirements listed in this document our team had to gather information relating to the issues an individual commonly faces when trying to find new clothing and outfit suggestions.  Firstly a user typically shops on multiple websites, therefore the suggestions on each of those websites are completely different and typically based just off the last few items that they have browsed.  For this reason Fashion Finder takes a different approach by collecting data and saving it to a users account on every item that they have liked for the time-being on their Fashion Finder account.  Another issue users typically face is finding items that go with a specific item that they already own.  To resolve this issue Fashion Finder provides a feature to upload clothing that they own and add that to their Fashion Finder account wardrobe.  Based off the items they already own suggestions can be made to match their current clothing.  
     

## Top-Level Design
1. Create progressive web app UI
2. Develop UI for Web Browser functionality
3. Make UI for creating login/register system
5. Create layout for content feed where users can like items
6. Create layout for suggestions feed that will be recommended to users based on liked/uploaded items

## Detailed Design
To deliver the above functionality, the app will use Django, React.js, and MongoDB. Additionally, Webpack will be used to compile React.js code and Selenium will be used for automated testing.

Django will be responsible for...
* Authenticating users
* Creation of new users
* Handling uploads
* Hosting static images to be served to the end user
* Hosting compiled js to be served to the end user
* Serve as middle-man between MongoDB and the end user.
  
MongoDB will be responsible for...
* Storing a new users fashion piece
* Storing a users votes on recommendation pieces.
* Storing all reference images
* Providing an aggregation pipeline for recommendations of similar items
* Providing an aggregation pipeline for recommendations of complementary items

React.js will be responsible for...
* Providing asynchronous behavior on the front end
* Displaying user images
* Providing interfaces for the user to interact with
## Tests

### Unit Tests

The Django test library will be used to perform units tests on the business logic in the Fashion Finder app and the Image prediction microservice app. 

### Integration

Integrations tests will be implemented using Djangos test library. Specifically, they will use the `Django.test.Client` class to emulate the end user

### Acceptance

Acceptance testing will be performed using Selenium. The functionality that is tested can be found in the acceptance-testing doc.