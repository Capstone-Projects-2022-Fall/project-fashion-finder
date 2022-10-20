---
sidebar_position: 1
---




## Components and their interfaces


**Components** : Client, Server, Database, User-Interface
The **client** will be our web-user.  Due to the functionality of our software being used as a progressive web application it will be determined if the user is using a mobile application, or web application on how the user-interface is to be displayed.  When a client loads the website it will then call processDatas() which will determine the clientType and pass that to displayUserInterface.  
When displayUserInterface is called the client will be displayed with the correct **UserInterface** where their userData will be pulled from the server after login.  The user will be displayed images which are pulled from the pinterestAPI, and will allow a user to like an item.  When a user likes an item that item is added to our database where it can than be used in machine learning to provide a user with suggestions using displaySuggestions().  When displayPriceStats() is called a request will be sent to the StockXAPI to pull this data and display it to the user.  
When a user first logs in it will make a request to the **server** where getUserData() is called to obtain the data for that user from the **database**.  The server is also responsible for processing price data, grabbing images, and providing suggestions to the user.  

![Blank diagram](https://user-images.githubusercontent.com/89498580/192659599-5811a552-537f-4d47-81b0-d8c7803ed1e7.png)



![Database Entity-relationship Diagram](https://user-images.githubusercontent.com/71922448/194051565-f8a31cca-1d97-4e74-bd4d-dc2efda9b699.jpg)


