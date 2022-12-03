![Open in Codespaces](https://classroom.github.com/assets/open-in-codespaces-abfff4d4e15f9e1bd8274d9a39a0befe03a0632bb0f153d0ec72ff541cedbe34.svg)
<div align="center">

# Fashion Finder
[![Report Issue on Jira](https://img.shields.io/badge/Report%20Issues-Jira-0052CC?style=flat&logo=jira-software)](https://temple-cis-projects-in-cs.atlassian.net/jira/software/c/projects/DT/issues)
[![Deploy Docs](https://capstone-projects-2022-fall.github.io/project-fashion-finder/docs/)
[![Documentation Website Link](https://img.shields.io/badge/-Documentation%20Website-brightgreen)](https://applebaumian.github.io/tu-cis-4398-docs-template/)


</div>


## Keywords

Section 004, Recommendation Engine, Fashion, Django, MongoDB, React.js 

## Project Abstract

Fashion Finder is a web application for providing clothing and outfit recommendations based on
a user’s clothing interests. Many sites only suggest clothing items based on a user’s most recent search
history, as opposed to items in a user’s closet. With Fashion Finder, users will be able to upload photos of clothing items to their account’s “wardrobe”, from which Fashion Finder’s recommendation engine produces user-specific recommended clothing articles. As clothing recommendations are generated, they are split into two categories: similar items and complementary items. Similar items are clothing articles that resemble items uploaded to a user’s wardrobe in both color and style. Complementary items are clothing items that pair well with items in a user’s wardrobe, creating suggested outfits tailored to a user’s style. Fashion Finder aims to help its users find entire new clothing pieces that fit their style

## High Level Requirement

Describe the requirements – i.e., what the product does and how it does it from a user point of view – at a high level.

Fashion Finder offers all of the following functionality to its end users
* Authentication - The user is able register, login, and logout in the Fashion Finder application
* Item tracker - The user is able to upload photos of owned clothing pieces and track them from the home page
* Item labeler - The user is able to upload photos of owned clothing pieces and receive machine learning generated labels for those items.
* Item palette detection - The user is able to upload photos of owned clothing pieces and receive color palettes of the item.
* Similar Item Recommendations - The user is able to select a photo in their wardrobe and receive back 10 similar items.
* Complementary Item Recommendations - The user is able to select a photo in their wardrobe and receive back 10 complementary items.
* Item Discovery - The user is able to visit the discover page and "like" or "dislike" items. Their liked items are added to their homepage
* Recommendations on Discovered Items - Like the uploaded photos, the user is able to select a liked photo in their wardrobe and receive recommendations for both similar items and complementary items.

## Conceptual Design

Languages: Python 3.10.6 and Node 18

The frontend of the Fashion Finder application is written in React.js and compiled with Webpack into plain javascript files.
The backend of the Fahsion Finder apppliation is written in DJanbo. It serves as the authentication point of the user and as the middleman between the user and the user data.
The storage of the Fashion Finder application consists of two parts. User authentication data (usernames, passwords, etc.)  is stored in SQLite, which is hosted and managed by Django. User Fashion pieces and reference fashion pieces are hosted by MongoDB.

In terms of hardware resources, the project uses a free tier of MongoDB, which has 3 replicates and is hosted via MongoDB Atlas. Additionally, the project needs to be hosted on an AWS EC2 server, where Django and its managed SQLite database will be hosted.


## Background


### Commercial websites with Clothing recommendation systems
. Many sites, such as Amazon, Pinterest, and clothing retailers may track things such as the type of images that a user clicks on and spends time looking at an item. However, this is typically done to determine which items the user is most likely to buy, not to aid the user in finding new clothing. There are not any comercially viable sites out there that attempt to provide users recommendations based off of users uploaded images. Fashion Finder further distinguishes itself from these sites by putting the user in full control of the data they provide. 

#### Github Projects with a similar goal to Fashion finder
* https://github.com/sonu275981/Fashion-Recommender-system
* https://github.com/MsJacksonIYN/Mod5_FashionRecommendations

In searching for projects that serve as fashion recommendation systems, the two above projects appeared the closest to the goals of the Fashion Finder project. 

The first project, developed by sonu275891, uses ResNet 50 and trains on the Kaggle Fashion Product Images Dataset. 
![image](https://user-images.githubusercontent.com/47365682/205466156-05e4fe02-ec8e-443c-8175-19ee65cf584e.png)

There project uses K-nearest-neighbors on the features of the dataset (shown above) to determine which items to recommend. While it is able to consistently get items of the same category and sub-category as the inputted item, it struggles with color matching due to nature of the dataset being categorical. In the case of this project, there is no distinction between "Light red", "Dark red", and "red", since it uses human inputted color labels which are less precise than the color palette detection algorithm used in Fashion Finder. Fashion Finder further distinguishes itself from this project in that it allows a user to build a wardrobe out of their recommendations and uploaded photos

The second project, developed by MsJacksonIYN and shonfeld, uses ResNet 50 and the "Rent the Runway" dataset to generate recommendations for the end user. One of the issues in this project is the choice of the dataset "Rent the Runway", which is heavily skewed to luxury clothing. Using the DeepFashion dataset, as Fashion Finder does, allows for a model which will generalize better to most every day outfits. Additionally, this project does not provide any way for the user to save their recommendations nor does it provide any way for users to discover new fashion pieces and build outfits.

## Required Resources

As described above, the project utilizes an AWS EC2 instance and MongoDB Atlas as hardware resources.

An additional resource that was necessary for the development of the model was the Deep Fashion Dataset [which can be found here]([url](https://paperswithcode.com/dataset/deepfashion))

In order to develop the model, a large amount of GPU power will be necessary. A personal RTX 3060 will be used to aid in the training of the model.

## Collaborators

Mary Kathleen Durnan
Jonathan Slack
Kyle Hrinvak
Shah Popal
