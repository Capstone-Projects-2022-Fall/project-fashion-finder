---
sidebar_position: 1
---

# Activities

## Requirements Gathering
### Functional Requirements
- Fashion Finder will have a scrollable recommended clothing content feed
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
     - Fashion Finder will have a easy to use UI on a web browser and a mobile app
- Fashion Finder will have price tracking for users that an item has liked and is interested in buying
     - When an item that a user has liked drops to a price that is recognized as a reasonable price by our price analysis tool the user will recieve a notification that it is a good time to buy that product
     - All price tracking will be saved to our database and will begin as soon as a user likes an item suggesting that they might purchase that item.
- Fashion Finder will use machine learning to constantly recreate a users content feed, and suggestion feed
     - The more pictures that a user either uploads or likes on the infinite Pinterest content feed, the further there results will be tailored based off that data
     - Individual clothing or wardrobe suggestions will be constantly different as long as a user continues to add liked clothing to their account.

 &nbsp;   In order to create the requirements listed in this document our team had to gather information relating to the issues an individual commonly faces when trying to find new clothing and outfit suggestions.  Firstly a user typically shops on multiple websites, therefore the suggestions on each of those websites are completely different and typically based just off the last few items that they have browsed.  For this reason Fashion Finder takes a different approach by collecting data and saving it to a users account on every item that they have liked for the time-being on their Fashion Finder account.  Another issue users typically face is finding items that go with a specific item that they already own.  To resolve this issue Fashion Finder provides a feature to upload clothing that they own and add that to their Fashion Finder account wardrobe.  Based off the items they already own suggestions can be made to match their current clothing.  
     
&nbsp;    From the analysis our group conducted users also face issues when trying to find the best price of an item.  For the majority of individuals finding a cheap and cost efficient way to shop is something that they are all interested in.  For this reason Fashion Finder provides a price analysis tool for users to know how often the price of an item flucuates and to alert them on the best possible time to purchase an item.  

## Top-Level Design
1. Create progressive web app UI
2. Develop UI for Web Browser functionality
3. Create UI for Mobile Device Functionality
4. Make UI for creating login/register system
5. Create layout for content feed where users can like items
6. Create layout for suggestions feed that will be recommended to users
7. Create layout for price analysis 
8. Notifications for price alerts
9. Create an account user interface so users can removed and see their liked items

## Detailed Design


## Tests

### Unit Tests

The Python Standard Library unittest module will be used to validate template rendering.

### Integration

The Postman API platform will be used to test HTTP requests.

### Acceptance

Use Case Acceptance testing will be conducted to evaluate user experience.