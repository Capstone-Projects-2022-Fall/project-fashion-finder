---
sidebar_position: 5
---

# Use-case descriptions

## Use case 1: Item tracker  

A user navigates to Fashion Finder and is fully authenticated
They want to keep track of clothes in their closet.
They uploads photos of each fashion piece they own.
The user is then able to view their uploaded pieces
```mermaid
sequenceDiagram
    title Use case 1: Item tracker
    actor U as User
    participant F as Fashion Finder React App
    %% participant DM as Fashion Finder Django ML Backend
    participant DC as Fashion Finder Django API Backend
    participant DFS as Django File Server
    participant DB as MongoDB
    U->>+F: Requests route /upload
    U->>+DFS: Uploads file
    U->>F: GET /home
    F->>DC: Get /async/wardrobe
    DC-->>F: JSON of User pieces
    F-->>F: Renders HTML from JSON representation 
    F-->>-U: Home Page presented
```
## Use case 2: Item labeler

A user navigates to Fashion Finder and is fully authenticated
They have pictures of their closet and want to find out how many of each type of clothing they own
They upload photos of each fashion piece they own.
The user is then able to see their wardrobe with labels generated from a machine learning model
These labels will tell the user the type of clothing for each image uploaded 

```mermaid
sequenceDiagram
    title Use case 3: Item labeler
    actor U as User
    participant F as Fashion Finder React App
    %% participant DM as Fashion Finder Django ML Backend
    participant DMC as Fashion Finder Django ML Backend
    participant DC as Fashion Finder Django API Backend
    participant DFS as Django File Server
    participant DB as MongoDB
    U->>+F: Requests route /upload
    F->>+U: Returns upload form
    U->>+DFS: Uploads file
    DFS->DC: Notify of new upload
    DC->>+DMC: Send image file
    DMC->>+DMC: Run palette detection
    DMC->>DC: Redirect user to /home
    DC->>F: User redirect
    F->>U: Redirect to /home
    U->>F: GET /home
    F->>DC: Get /async/wardrobe
    DC->>DB: Get pieces from UserFashionPiece collection
    DB->>DC: Send pieces from USerFashionPiece collection.
    DC-->>F: JSON of User pieces containing labels
    F-->>F: Renders HTML from JSON representation containing labels
    F-->>-U: Rendered home page returned to user, which contains colors



```
## Use case 3: Color labeler

A user navigates to Fashion Finder and is fully authenticated
They have pictures of their closet and want to find out how often different colors appear in their wardrobe.
They upload photos of each fashion piece they own.
The user is then able to see their wardrobe with labels of the primary colors appearing in each photo.
These labels will tell the user the primary "palette" of the fashion piece.
```mermaid
sequenceDiagram
    title Use case 3: Color labeler
    actor U as User
    participant F as Fashion Finder React App
    %% participant DM as Fashion Finder Django ML Backend
    participant DMC as Fashion Finder Django Color Backend
    participant DC as Fashion Finder Django API Backend
    participant DFS as Django File Server
    participant DB as MongoDB
    U->>+F: Requests route /upload
    F->>+U: Returns upload form
    U->>+DFS: Uploads file
    DFS->DC: Notify of new upload
    DC->>+DMC: Send image file
    DMC->>+DMC: Run palette detection
    DMC->>DC: Redirect user to /home
    DC->>F: User redirect
    F->>U: Redirect to /home
    U->>F: GET /home
    F->>DC: Get /async/wardrobe
    DC->>DB: Get pieces from UserFashionPiece collection
    DB->>DC: Send pieces from USerFashionPiece collection.
    DC-->>F: JSON of User pieces containing colors
    F-->>F: Renders HTML from JSON representation containing colors
    F-->>-U: Rendered home page returned to user, which contains colors


```


## Use case 4: Finding similar items
A user navigates to Fashion Finder and is fully authenticated.
They have a fashion piece that they like and want to find more items like it.
They upload the fashion piece image to the Fashion Finder Database.
They navigate to a "See more like this" section, where they can see other fashion pieces in the same categories and fashion pieces with similar color palettes. 
```mermaid
sequenceDiagram
    title Use case 4: Finding similar items
    actor U as User
    participant F as Fashion Finder React App
    %% participant DM as Fashion Finder Django ML Backend
    %% participant DMC as Fashion Finder Django Color Backend
    participant DC as Fashion Finder Django API Backend
    participant DFS as Django File Server
    participant DB as MongoDB

    U-->+F: Upload file or like/dislike from Discover page
    F-->+DC: Add item to user wardrobe
    U-->+F: GET /home
    F-->+DC: GET /async/wardrobe
    DC-->+DB: Get UserFashionPiece collection items
    DB-->+DC: Return UserFashionPiece collection items
    DC-->+DFS: Store local copy of image data
    DFS-->+DC: Indicate success or failure on storage 
    DC-->+F: Return JSON of Users pieces
    F-->+F: Renders HTML from JSON
    F-->U: HTML is rendered on the users page
    F-->DFS: Get static images
    U-->F: Select an item from wardrobe
    F-->DC: GET /async/recommendations/<piece_id>
    DC-->DB: Call MongoDB aggregation pipeline for recommendations
    DB-->DC: Return 10 Mongo documents representing similar items
    DC-->DFS: Store local copy of image data
    DFS--> DC: Indicate success or failure on storage
    DC-->F: Return JSON of Mongo documents, minus image data
    F-->DFS: Get static images for recommendations
    DFS-->F: Serve static images
    F-->U: Renders images on DOM in "Pieces like this" section.

```
## Use case 5: Finding complementary items
A user navigates to Fashion Finder and is fully authenticated.
They are able to view their wardrobe of uploaded items.
They want to be able to find other items that would go well with their item
For any of the items in their wardrobe, they can click on a "See items that would good well with this" section
They are then prompted with the most similar items, ranked by label similarity and color palette similarity. 
```mermaid
sequenceDiagram
    title Use case 5: Finding complementary items
    actor U as User
    participant F as Fashion Finder React App
    %% participant DM as Fashion Finder Django ML Backend
    %% participant DMC as Fashion Finder Django Color Backend
    participant DC as Fashion Finder Django API Backend
    participant DFS as Django File Server
    participant DB as MongoDB

    U-->+F: Upload file or like/dislike from Discover page
    F-->+DC: Add item to user wardrobe
    U-->+F: GET /home
    F-->+DC: GET /async/wardrobe
    DC-->+DB: Get UserFashionPiece collection items
    DB-->+DC: Return UserFashionPiece collection items
    DC-->+DFS: Store local copy of image data
    DFS-->+DC: Indicate success or failure on storage 
    DC-->+F: Return JSON of Users pieces
    F-->+F: Renders HTML from JSON
    F-->U: HTML is rendered on the users page
    F-->DFS: Get static images
    U-->F: Select an item from wardrobe
    F-->DC: GET /async/recommendations/complementary/<piece_id>
    DC-->DB: Call MongoDB aggregation pipeline for complementary recommendations
    DB-->DC: Return 10 Mongo documents representing similar items
    DC-->DFS: Store local copy of image data
    DFS--> DC: Indicate success or failure on storage
    DC-->F: Return JSON of Mongo documents, minus image data
    F-->DFS: Get static images for complementary recommendations
    DFS-->F: Serve static images
    F-->U: Renders images on DOM in "Pieces that would go well with this" section.

```
## Use case 6: Liking / Dislking items  
A user navigates to Fashion Finder and is fully authenticated.
They are able to navigate to a "Like/Dislike" page, where they will be prompted with random fashion pieces
They will be able to like or dislike different pieces
The user will be able to view a list of their liked pieces

![FashionFinderLogin](/img/Fashion Finder Login (1).png)
```mermaid
sequenceDiagram
    title Use case 6: Liking / Disliking items
    actor U as User
    participant F as Fashion Finder React App
    %% participant DM as Fashion Finder Django ML Backend
    %% participant DMC as Fashion Finder Django Color Backend
    participant DC as Fashion Finder Django API Backend
    participant DFS as Django File Server
    participant DB as MongoDB
    U-->+F: GET /discover
    F-->+DC: GET /discover
    DC-->DB: Get random piece from LabeledFashionPiece collection
    DB-->DC: Return Mongo Doc of random piece
    DC-->DFS: Store image in local file system
    DFS-->DC: Indicate success of storage operation
    DC-->F: Return JSON with image file path
    F-->DFS: Get image from file server
    DFS-->F: Send image
    F-->U: Update DOM with new image
    U-->F: Like piece with id <piece_id>
    F--> DC: POST /async/like/<piece_id>
    DC--> DB: Add piece_id to UserLikedPieces collection for the given user
    DB-->DC: Indicate succcess of operation 
    DC-->F: Return JSON indicating success
    F-->U: Update DOM with new image and repeat 
```
