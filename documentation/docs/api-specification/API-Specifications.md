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
