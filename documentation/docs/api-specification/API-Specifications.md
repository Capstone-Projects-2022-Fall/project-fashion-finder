---
sidebar_position: 1
---

# API Specifications

API Documentation Document: 

## Classes - Web Interface
### HomePage
 Class Purpose: This is the first page that users will see when they visit the web page.  The purpose of this page is to give the user an understanding of the website, and to allow them to login or register to get access to the full functionality. 

#### Methods:
signUp()
Purpose: to allow a user to login to their account
Pre-Condition: The user must have an account
Post-Condition: none
Parameters:  email, password
Return Values: none
Exceptions Thrown: Invalid Credentials
signIn()
Purpose: to allow a user with an existing account to login
Pre-Condition:  the user does not have an account
Post Condition: the user will be notified through email of account creation.
Parameters: email, password, phoneNumber, firstName, lastName 
Return Values: none
Exceptions Thrown: user already exists


### SignUp

Class Purpose: This class is used for a user to sign up for an account.  They will enter their email, password, phoneNumber, firstName, and lastName to create their account. 

#### Data Fields:

##### Email

Type: string

Purpose: this is used to set the users email which will also be used for login.

##### Password

Type: string

Purpose: sets the password for account login

##### PhoneNumber
Type: string

Purpose:  a phone number to be held under the account

##### firstName

Type: string
Purpose: to have a name linked to each account

##### lastName:
Type: string
Purpose: to have a name linked to each account

#### Methods:
createAccount(email, password, phoneNumber, firstName, lastName)
Purpose:  this is to create an account for a user and store all of the information into the database.
Pre-Condition: valid email address (not used previously)
Post Condition: Verification email

### Account
Class Purpose: The Account class corresponds to a particular user. Account settings such as the username, password, email will be associated with an account upon sign-up, and linked with a unique userID.

#### Data Fields:

##### userID
Type: Int

Purpose: Primary Key

## Classes - ImgPredictionMicroservices

## ClassPredictor

#### Methods:
    predict_class(filepath):
    Purpose: Given an image at a given filepath, open it, process it, and run it through the deployed machine learning model. Return the result
    Returns: Dict obct with keys ['labels','hex_codes','rgb_0', 'rgb_1','rgb_2']

    hex_to_rgb(h):
    Purpose, given a hex-code, return the rgb values accordingly
    Returns: (R, G, B)

    binarizeOutput(y_pred, threshold=0.5):
    Given a tensor with probability values, round each element to 0 or 1 depending on the threshold value
    Returns: A binary tensor

## Mongo Driver
    create_user_fashion_piece_dock(data, img_bytes):
    Purpose: Creates a pyMongo document a python dictionary and raw image data
    Returns pyMongo document for creation

    insert_user_fashion_piece(mongo_doc):
    Params: mongo_doc (a pyMongo document type)
    Returns: If successful, returns ID of inserted piece. Otherwise, returns None

    get_wardrobe(user_id, user_name, n = 10, offset=0):
    Params: user_id, user_name (supplied from auth module).
    n: number of wardrobe items
    offset: page number (if applicable)

### Recommendation Mongo Driver
    def calculate_min_distance_from_banned_tones(rgb, tones):
    
    Purpose: We maintain a list of banned tones that we don't want the recommendation to recommend too heavily on hex values that is close to one of these tones. We block most grey values as well popular skin tones as to avoid matching on backgrounds and other factors in the photos.
    Arguments: rgb: integer array of dimension 2x3.
    Argument: tones: The list of banned tones

    def get_recommendations(piece_id, user_id, user_name, n = 10):
    Purpose: Find other pieces in the `LabeledFashionPiece` collection like the users selected piece
    Param: piece_id: The MongoDb id of the piece.
    Param: user_id: The users DJango id
    Param: user_name: The users name
    Param: n: The number of recommendations to generate


## Views Driver
The views.py files contains most of the response parsing and bundling logic. Not necessary to construct a Class doc for it.

## URLs driver
The urls.py driver file for both the FashionFinder proJect and the fashionfinderapp app is responsible for mapping the local paths to functions in views.py.
