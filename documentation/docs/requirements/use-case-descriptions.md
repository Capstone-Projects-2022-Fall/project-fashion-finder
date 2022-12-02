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
graph TD
    A[User arrives at homepage] -->|Click Upload photo button| B
    A-->|Navigate back to home page| C
    B[Upload page] --> A
    C[User views uploaded items]
```
## Use case 2: Item labeler

A user navigates to Fashion Finder and is fully authenticated
They have pictures of their closet and want to find out how many of each type of clothing they own
They upload photos of each fashion piece they own.
The user is then able to see their wardrobe with labels generated from a machine learning model
These labels will tell the user the type of clothing for each image uploaded 

```mermaid
graph TD
    A[User arrives at homepage] -->|Click Upload photo button| B
    A-->|View main content| C
    B[Upload page] --> A
    C[User views uploaded items]
    C-->D
    D[User views labels of items]

```
## Use case 3: Color labeler

A user navigates to Fashion Finder and is fully authenticated
They have pictures of their closet and want to find out how often different colors appear in their wardrobe.
They upload photos of each fashion piece they own.
The user is then able to see their wardrobe with labels of the primary colors appearing in each photo.
These labels will tell the user the primary "palette" of the fashion piece.
```mermaid
graph TD
    A[User arrives at homepage] -->|Click Upload photo button| B
    A-->|View main content| C
    B[Upload page] --> A
    C[User views uploaded items]
    C-->D
    D[User views color palette of items]
```


## Use case 4: Finding similar items
A user navigates to Fashion Finder and is fully authenticated.
They have a fashion piece that they like and want to find more items like it.
They upload the fashion piece image to the Fashion Finder Database.
They navigate to a "See more like this" section, where they can see other fashion pieces in the same categories and fashion pieces with similar color palettes. 
```mermaid
graph TD
    A[User arrives at homepage] -->|Click Upload photo button| B
    A-->|View main content| F
    F[User has different items to select from]
    F-->|User selects item| C
    B[Upload page] --> A
    C[Item is selected on page]
    D[User has view of similar items ot selected item]
    C-->|Similar items section updates| D
    C-->|User changes selected item| C
    %% D[User views color palette of items]
```
## Use case 5: Finding complementary items
A user navigates to Fashion Finder and is fully authenticated.
They are able to view their wardrobe of uploaded items.
They want to be able to find other items that would go well with their item
For any of the items in their wardrobe, they can click on a "See items that would good well with this" section
They are then prompted with the most similar items, ranked by label similarity and color palette similarity. 
```mermaid
graph TD
    A[User arrives at homepage] -->|Click Upload photo button| B
    A-->|View main content| F
    F[User has different items to select from]
    F-->|User selects item| C
    B[Upload page] --> A
    C[Item is selected on page]
    D[User has view of complementary items of selected item]
    C-->|Complementary items section updates| D
    C-->|User changes selected item| C
```
## Use case 6: Liking / Dislking items  
A user navigates to Fashion Finder and is fully authenticated.
They are able to navigate to a "Like/Dislike" page, where they will be prompted with random fashion pieces
They will be able to like or dislike different pieces
The user will be able to view a list of their liked pieces

![FashionFinderLogin](/img/Fashion Finder Login (1).png)
```mermaid
graph TD
    A[User arrives at homepage] -->|Click Discover button| B
    A-->|View main content| F
    F[User has different items to select from]
    F-->|User selects item| C
    B[Discover page] --> A
    B-->|User action Like/dislike| B2
    B2-->|User like adds item to home page| F
    B2[Discover page loads new photo] 
    C[Item is selected on page]
    D[User has view of recommended items of selected item]
    C-->|Recommended items section updates| D
    C-->|User changes selected item| C
```