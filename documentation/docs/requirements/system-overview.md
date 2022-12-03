---
sidebar_position: 1
---

# System Overview
## Project Abstract
The Fashion Finder Web App will be an application for identifying pieces of clothing and gaining inspiration for outfits and fashion pieces. It serves as a multi-tool for users to find fashion pieces that fit their style and existing wardrobe.

The Features of the Fashion Finder web app can be found in the [Features and Requirements Document](features-and-requirements.md). This document will instead cover the main architectural hurdles that are required to get to the features described above.

## Data Requirements
In order to get a model that would generalize well, a lot of data was necessary. The training set (Deep Fashion) consists of 30 GB of high resolution image data, containing a wide variety of images obtained from retailers, marketers, and photo collections. All of these files had brief descriptors.
# Conceptual Design
### Data Cleaning process
A data cleaning system will prepare the raw data from Deep Fashion (our training set) and the VGG 16 model.

Of all of the classes present in the data, we selected a subset of classes capable of having strong predictive power.

The inputted data was filtered to train only on items which fit in at least one of the classes below

```
CLASS_LIST = ["Tee","Tank","Dress","Shorts","Skirt","Hoodie","Jumpsuit","Sweater","Blazer","Striped","Cardigan","Blouse","Jacket","Jeans","Maxi","Floral","Denim","Sweatshorts","Polka","Shawl","Bodycon"]
```


## Model Training
The code for the model training can be found here [here](../../../model/src/ModelTraining3.ipynb).
A Data Loader utility is used to batch process image files alongside their labels and feed them into the neural network. The neural network takes in batches of 32 images at a time, guess a prediction, and then use backpropogatation ot update model weights. The best model training took 72 hours and involved 50 batches over 20 samples of the data. It achieved an accuracy of score of 84% on a class list size of 14. The model that is actually deployed achieved a sample-weighted accuracy of 79% on a class list size of 21. Given the quantity of data and lack of time for manual data cleansing, these are high accuracy scores.

## Model Deployment Process

In order for the machine learning microservice to be deployed it had to be hosted by Django. Instead of making it part of the django web-app, it is deployed as a separate app, named `ImgPredMicroservice`. This means that it does not share the same thread as the web server and does not risk hanging the web server when it needs to make heavy calculations. 

The model is loaded once when the web server starts. To actually process newly uploaded data, routines were written to read a file from Django's `InMemoryUploadedFile` data type and transform it into a 2D RGB-valued array. With the new array of shape (m,n,3), it can be inputted into the trained model and receive labels back.

## Front-End Development
Using the package manager npm@18, front-end components are written in react, compiled as javascript, and then served as static files by the Django file server.

## Back-End Development
Back-end development occurs in three different areas.
1. CRUD operations for users items
2. Data transformation and Machine learning algorthms
3. Storage and retrieval of images
  
In (1), most routes represent the creation, retrieval, and deletion of models described below.
In (2), most routes depend on the core instantiation of the `model` variable, which is read in from `src/model/artifacts/` when the webserver is booted.
In (3), most routines will make use of in-memory representations of images, and when they need to be stored permanently, they will be stored in MongoDB.
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
While there are lots of different fashion sites out that let users upload photos and share that data, Fashion Finder distinguishes itself from those sites by running machine learning algorithms, color detection algorithms, and customized recommendation algorithms to give users more of what they want. Sites like pinterest allow users to somewhat customize their feed, but they only give feedback on existing content. 

# Conceptual Design
 This progressive web application will be developed with the purpose of being used on Android or Google mobile devices. The back-end API will be a Django REST API. It will handle modeling the relevant data and the needed CRUD operations. The Django REST API will be integrated with MongoDB by making use of the pymongo driver. Linked are examples of using MongoDB with Django:
○	https://www.mongodb.com/compatibility/mongodb-and-django 
○	https://github.com/mongodb-developer/django-pymongo 
The MongoDB database will be hosted via the MongoDB Atlas service and its schema will be controlled by Django.
We will be using VGG16 and Tensorflow to recognize and categorize clothing items as well as label the data. We will also use Scikit learn’s K-nearest-neighbor algorithm to generate a similarity score and provide the final recommendation. The design of our user interface will have two main pages. The "Home" page, and the "Discover" page. The home page will serve as a place for users to get recommendations, and the discover page will serve as a place for users to indicate to the site their style preferences by "Liking" or "Disliking" items.
