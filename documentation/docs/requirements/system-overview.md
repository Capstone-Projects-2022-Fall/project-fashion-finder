---
sidebar_position: 1
---

# System Overview
## Project Abstract
The Fashion Finder Web App will be an application for identifying pieces of clothing and gaining inspiration for outfits and fashion pieces. It serves as a multi-tool for users to find fashion pieces that fit their style and existing wardrobe.do
ck.
The Features of the Fashion Finder web app can be found in the [Features and Requirements Document](features-and-requirements.md). This document will instead cover the main architectural hurdles that are required to get to the features described above

## Data Requirements
In order to get a model that would generalize well, a lot of data was necessary. The training set consists of 30 GB of high resolution image data, containing a wide variety of images obtained from retailers, marketers, and photo collections. All of these files had brief descriptors.
# Conceptual Design
### Data Cleaning process
A data cleaning system will prepare the raw data from Fashion Deep (our training set) and the VGG 16 model.

Of all of the classes present in the data, we selected a subset of classes which were believed to be capable of having strong predictive power.

```
CLASS_LIST_21 = ["Tee","Tank","Dress","Shorts","Skirt","Hoodie","Jumpsuit","Sweater","Blazer","Striped","Cardigan","Blouse","Jacket","Jeans","Maxi","Floral","Denim","Sweatshorts","Polka","Shawl","Bodycon"]
```


## Model Training
The code for the model training can be found here [here](../../../model/src/ModelTraining3.ipynb).
A Data Loader utility is used to batch process image files alongside their labels and feed them into the neural network. The neural network would take in batches of 32 images at a time, guess a prediction, and then propogate. The best model trained took 50 batches over 20 samples of the data and took 29 hours to train. It achieved an accuracy of score of 84% on a class list size of 14. The model that is actually deployed achieved an accuracy of 79% on a class list size of 21. Given the quantity of data and lack of time for manual data cleansing, these are high accuracy scores.

## Model Deployment Process

In order for the machine learning microservice to be deployed it had to be hosted by django. Instead of making it part of the django web-app, it is deployed as a separate app, `ImgPredMicroservice`. This means that it does not share the same thread as the web server and does not risk hanging the web server when it needs to make heavy calculations.

The model is loaded once when the web server starts. To actually process newly uploaded data, routines where written to read a file from Django's `InMemoryUploadedFile` data type and transform it into a 2D RGB-valued array.

## Front-End Development
Using the package manager npm@18, front-end components are written in react, compiled as javascript, and then served as static files by the Django file server.

## Back-End Development
Back-end development occurs in two different areas.
1. CRUD operations for users items
2. Data transformation and Machine learning algorthms
  
In (1) , most routes represent the creation, retrieval, and deletion of models described below
In (2), most routes depend on the core instantiation of the `model` variable, which is read in from `src/model/artifacts/` when the webserver is botoed 

### Models
#### Like
```  
    user_id::str (ref to django user id)
    user_name::str (ref to django user name)
    fashion_piece::ObjectID (ref to piece from `LabeledFashionPiece` collection)
  User
    id, username, fname, lname, hashed_password
```
#### UserFashionPiece
    descriptor::str (Description)
    hex_codes::List[List[int]] Hex codes for palette
    rgb::List[List[int]] RGB representations of pallete
    labels::List[str] List of labels provided by machine learning kernel.
## Background
While there are lots of different fashion sites out that let users upload photos and share that data, Fashion Finder distinguishes itself by from those sites by running machine learning algorithms, color detection algorithms, and customized recommendation algorithms to give users more of what they want. Sites like pinterest allow users to somewhat customize their feed, but only by giving feedback on existing content.

<!-- The Fashion Finder progressive web application is for individuals who are interested in finding a more efficient and cost effective way to shop online. Fashion Finder's main purpose is to provide clothing recommendations based on items they have expressed interest in or photos they have uploaded. In addition, if the item is on available on StockX, the user will be able to see the price history for the item. Then, the user will be able to decide if the items they are interested in are being sold at a fair price. Fashion Finder will also serve features that are not available anywhere else, which is to help its users find entire outfit recommendations, rather than just suggested items based on their most recent search history.

In order to acquire the data needed to provide accurate outfit suggestions users will be displayed content pulled from Pinterest. When they scroll through the content that is displayed they will be able to like the items that they are interested, which will help us to create a content feed more tailored to each specific user. The more content a user likes the better our algorithms will be able to create accurate outfit suggestions for each user. Along with creating completely new outfit suggestions and displaying those to a user, Fashion Finder will also be axle to take items that a user already owns, and be able to match those articles of clothing to other pieces that would go well together in an outfit. All items suggested will be cross checked with StockX to see if they are available on their website and a price evaluation will be done on each item. Some of these items might not be available on StockX, but they will still be suggested to the user if that user has selected the option to view outsider products also, where they can then look around to find where to purchase that item themselves.  The user will then be able to add their recommendations to a My Closet section.

After an item has been cross checked with StockX to see if it is available on their website, you can select that you are interested in that item to continue tracking the price of the item. As soon as you start to track an item our software begins to collect data in order to find out when an item is at a good price for you to make a purchase. Initially when you track an item Fashion Finder will be able to provide several statistics to a user on the price of that item such as its 12 month trade price, all-time trade range, the volatility, number of sales, price premium, and the average sale price. The longer you track an item the more accurate these statistics will become along with being able to view a graphic chart showing exactly every sale of that item. If you are tracking an item and decide to receive notifications once an item in your size drops to a fair market price you will be the first to receive an update and this will help you to save money on the clothing your most interested in.

The main goal behind this project is to help our users to shop in the most efficient way possible.  Through the help of our users by liking all the clothing they are interested in we use machine learning to then put together outfits that go well together, but also that they will be highly interested in.  Along with figuring out the correct clothing that each user desires our goal is to help them to find the best price to buy each of these products.  Fashion finder will not only eliminate the need to search multiple websites for clothing options, but also eliminates the need to second guess if you are getting a good deal on the clothing your interested in buying.  For the ease of the user Fashion Finder is a progressive web application, meaning our software will be able to run on both a web browser, or as a mobile application.  -->

<!-- 
# Conceptual Design
 This progressive web application will be developed with the purpose of being used on Android or Google mobile devices. The back-end API will be a Django REST API. It will handle modeling the relevant data and the needed CRUD operations. The Django REST API will be integrated with MongoDB by making use of the pymongo driver. Linked are examples of using MongoDB with Django:
○	https://www.mongodb.com/compatibility/mongodb-and-django 
○	https://github.com/mongodb-developer/django-pymongo 
The MongoDB database will be hosted via the MongoDB Atlas service and its schema will be controlled by Django.
We will be using ResNet and Tensorflow to recognize and categorize clothing items as well as label the data, and then Scikit learn’s K nearest neighbor algorithm to generate a similarity score and provide the final recommendation. The design of our user interface will be done using the MatPlotLib python library, along with the use of bootstrap's web development toolkit. For the purpose of generating content to our users we plan to use the PinterestAPI (https://developers.pinterest.com/), and for grabbing data off StockX we will be using an open source StockX api created by a fellow GitHub user (https://github.com/matthew1232/stockx-api).  The front end will be done with React.JS. -->

<!-- ## Background
  There is no software relatable to Fashion Finder except for many basic versions which are implemented on nearly every retail website.  Most retail websites use simple algorithms to make suggestions to their users, typically collecting a cache of all of their recently viewed products, and forming suggestions based on similar brand, article of clothing, or color.  Unlike typical retail websites we plan to create an application that will pull fashion ideas from the millions of creaters on Pinterest, instead of just one specific website.  Through our users liking specific items of content we display we can tailor their content feed closer to what they want, while also suggesting entire outfit ideas instead of single articles of clothing.  Along with doing this we will provide a price analysis on the products that are listed on StockX, something that no retail company would ever do.  Most retail websites only collect data on a users cache which has to do with their current browsing session.  We plan to allow users to create accounts to collect data over a period of time to fully understand the clothing they actually like.     -->
  
<!-- The custom model includes additional dense layers and custom activation functions. -->