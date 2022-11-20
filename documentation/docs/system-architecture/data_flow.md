**Data Flow**

The data flow can be found below

## Data Flow Diagram
![DataFlow drawio](https://user-images.githubusercontent.com/47365682/202894408-38c5d8c6-1a2b-40b2-8649-4d21369a8d84.png)

### FF App
The application has several jobs in relation to data flow
1. Handle user upload events
2. Process user images with label prediction (through the ImgPredictionMicroservice) 
3. Process user images with palette prediction (through the ImgPredictionMicroservice)
4. Process CRUD actions on data of class **UserFashionPiece** through the mongo driver
5. Process CRUD actions on data of class **User** through the djang auth driver

### Img Pred
The image prediction microservice takes in an image of format .jpg or .png of any size. It then processes the data as follows.

First, it will resize the data to be 512x512x3 in size, using tensorflows `DataLoader()` class. It will then pass the input tensor into the loaded model, and the model will output a list of classes where the p>0.4. In this case, p represents the probability that the input belongs to class x.

The Img Pred microservice will then call the Color Prediction class's get_dominant_colors() to get the palette of the image.

More details on these services can be found in [algorithms.md](algorithms.md)

The Img Pred microservice will then return both the label and the color codes to the FF App.

### Rec Eng.
The recommendation engine takes in requests from the FF App and in turn calls a Mongo Aggregation pipeline.

The recommendation engine is responsible for calculating the weights for each color in the source image.
The recommendation engine is responsible for calculating complementatry colors to feed into the mongo aggregation pipeline.

## Data Lakes
### User Pieces
Hosts the labels, color codes, and raw image data of users uploaded files.
### Rec Pieces
Hosts the labels, color codes, and raw image data of recommendation reference data files.
### Django Static
Hosts static JPG/PNG files that have been cached due to calls for those files.
