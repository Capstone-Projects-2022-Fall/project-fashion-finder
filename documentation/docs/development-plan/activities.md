---
sidebar_position: 1
---

# Activities

## Requirements Gathering

To gather requirements, the team performed research on other popular sites for images and fashion, such as Pinterest, Depop, Instagram, and multiple different clothing retailers. While many of them had ways to filter and sort between different clothing types, we found that it would be difficult for a user to try and build a wardrobe using any of these platforms.

To determine what features were desireable in the application, the team asked family members and friends about how they go about finding new pieces of clothing.

Of those surveyed, many users expressed interest in being able to get recommendations from pieces that they already have in their wardrobe. Additionally, they wanted to be able to discover new pieces.

From the above conversations, it was determined that the requirements laid out below would lead to the best experience for the end user.

To achieve the above desired outcomes, a plan in JIRA was laid out, creating several different Epics and populating stories for those epics.


### Functional Requirements
- Fashion Finder will have a scrollable recommended clothing content feed
     - Content will be pulled from the Deep Fashion dataset
     - Users will be able to like content in the feed and it will be saved to their personal wardrobe
     - Fashion Finder will tailor recommendations based off of a users wardrobe.
- Fashion Finder will have an upload picture feature 
     - Users can upload clothing that is already in their wardrobe that they like 
     - Users can upload clothing that they found online and like or dislike pieces of clothing
     - The clothing users upload will be used the same way liked clothing from the content is used to further tailor suggestions shown to that specific user.
- Fashion Finder will have a UI to provide outfit or clothing suggestions to the user
     - Suggestions will be based off of content liked on the content feed
     - Suggestions will be based off of content that has been uploaded by the user
     - Users can get suggestions on a specific piece of clothing
     - An outfit pairing or matching feature will available to the user, so they can find other pieces of clothing that go with items they already own.
### Nonfunctional Requirements
- Fashion Finder will have a user-friendly interface 
     - The user interface will be easily navigatable, and will give clear instructions from the beginning on how a user can recieve the best outfit suggestions.
     - If any errors do occur the user will be prompted of the error
- Fashion Finder will be a progressive web application
     - Fashion Finder will have a easy to use UI on a web browser

 &nbsp;   In order to create the requirements listed in this document our team had to gather information relating to the issues an individual commonly faces when trying to find new clothing and outfit suggestions.  
 Firstly, a user typically shops on multiple websites, therefore the suggestions on each of those websites are isolated to the data stored on those websites.  For this reason, Fashion Finder takes a different approach by collecting users photos and saving it to a users account. Every item that a user has liked on the "Discover section" will also appear on their Fashion Finder account.  Another issue users typically face is finding items that go with a specific item that they already own.  
 To resolve this issue, Fashion Finder provides a feature to upload clothing that they own and add that to their Fashion Finder account wardrobe. Based off the items they already own, suggestions will be made to match their current clothing.  
     

## Top-Level Design
1. Create progressive web app UI
2. Develop UI for Web Browser functionality
4. Make UI for creating login/register system
5. Create layout for content feed where users can like items
6. Create layout for suggestions feed that will be recommended to users
7. Create an account user interface so users can see their liked items
8. Create an accout user interface so users can get recommendations based on their liked items

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