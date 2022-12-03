---
sidebar_position: 1
---

# Algorithms
There are several algorithms, big data techniques, and machine learning algorithms present in the Fashion Finder project.

## Image Prediction

### Training

#### Data Set
The deep fashion data set can be found [here](https://drive.google.com/drive/folders/0B7EVK8r0v71pQ2FuZ0k0QnhBQnc?resourcekey=0-NWldFxSChFuCpK4nzAIGsg)

The dataset was populated from `Category and Attrribute Prediction Benchmark/Img/img_highres.zip` subfolder, which includes >200,000 images of high resolution training data.

#### Data Pre-processing
To prepare the model for pre-processing, a data loading routine had to be developed. The Data Loader routine that was used can be found [here](../../../model/src/ModelTraining3.ipynb). 
#### Model
The model that was chosen for use is the Keras VGG 16 model, which is well known for being used in the machine learning domain for image classification..
The structure of the model is shown below.
```python
conv_model = vgg16.VGG16(weights='imagenet', include_top=False, input_shape=(224,224,3))
for layer in conv_model.layers:
    layer.trainable = False

# x = keras.layers.Dropout(0.25)(conv_model.output)
 
x = keras.layers.Flatten()(conv_model.output)
x = keras.layers.Dense(32, activation='relu')(x)
x = keras.layers.Dense(32, activation='relu')(x)
x = keras.layers.Dense(32, activation='relu')(x)

# x = keras.layers.Dense(64, activation='relu')(x)
predictions = keras.layers.Dense(len(CLASS_LIST), activation = 'sigmoid')(x)
full_model = keras.models.Model(inputs=conv_model.input, outputs=predictions)
full_model.summary()

```

#### Model Training
The model was trained on the Deep Fashion dataset described above. In its training, it completed 100 epochs (or "passovers"), meaning that it trained on each of the individual images 100 times. Since the original dataset is well over 200,000 images, this process took over 72 hours to fully train. Thankfully, VGG 16 is capable of "transfer learning" meaning that the training could be stopped and restarted without losing the models computed weights. 


## Color Detection
The color detection algorithm has several different components. 

The goal is to prepare the image data to run a K-nearest-neighbors algorithm on it. However, just running KNN on all of the pixels would result in the dominant color of the background. To solve this, there is a custom sampling algorithm.

### Sampling algorithm
The input to the sampling algorithm is a 256x256x3 RGB array. It uses the code below to construct a probability distribution. The distribution is the product of two 1D Gaussian arrays undergoing elementwise multiplication.The goal of the distribution is to increase the number of samples from the subject of the image (in the center of the image, as opposed to the background)
```python
def gaussian_kernel(img_height, img_width, kernel_relative_size = 0.1, verbose=False):
    xs = scipy.signal.gaussian(img_width, std= img_width * kernel_relative_size)
    ys = scipy.signal.gaussian(img_height, std=img_height * kernel_relative_size)
    kernel = np.array([[x*y for x in xs] for y in ys])
    return kernel

def get_flatted_normalized_gaussian_kernel(kernel):
    kernel = kernel.reshape(-1)
    kernel = kernel / np.sum(kernel)
    return kernel 
```

Using this probability distribution, it samples 1000 pixels (with replacement) from the image and then runs Scikit Learns K nearest neighbors algorithm. The "features" that Scikit Learn is fitting on is the RGB values of the pixels.

## Recommendation Engine

The recommendation engine makes heavy use of MongoDB's **Aggregation Pipelines**. 

### Similar Items
Two items are considered similar **if and only if****
1. They share at least one label class (E.g. Jeans, Blouse, Striped, TShirt, etc.)
2. Their palette similarity is in the top 10 of all of the images that satisfy condition 1

#### Palette similarity .

The _Palette Similarity_ of IMG _target_ and _candidate_rec_ with 3 RGB values each, is calculated as follows

For each of the colors in _target_ , calculate its similarity to a list of whites, greys, and skin tones to determine how much weight to give the color in the the recommendation. A color is considered less influential to match on if it is close to a white color, grey color, or a common skin tone color.
The similarity is calculated by a weighted average of the minimum euclidean distance between the (R,G,B) points of the _target_ IMG and the (R,G,B) points of the _candidate_rec image.
#### Mongo Pipeline
The Mongo Pipeline can be described as followed.

For all images in the pipeline, check if the image palette contains any of the RGB values from the _target_ IMG. Rank each of 3 values by how close they are (in euclidean distance) to any of the 3 values of the _target_ IMG.

Calculate a similarity score which is a weighted average of the above 3 metrics, depending on the weights calculated in the _Palette Similarity_ step.

Rank all of the images by this weighted similarity score, and return the top 10.

The recommendation query can be found [here](../../../FashionFinderDjango/FashionFinder/ImgPredMicroservice/upload_piece_to_mongo.py#L96)


### Complementary Items

Complementary items recommendation is driven in a similar fashion to the "Similar Items" recommendation. The same Mongo Pipeline is used. However, since their are multiple different colors that would be considered "complementary" to the dominant color of the image, we must calculate those values and then search for images which contain at least one of those complementary values.

#### Complementary Color detection

To determine complementary colors for a given input color, the first step is to represent the RGB values in HSV format (Hue, Saturation, Value).

The relationships that were used to find complementary colors are to determine colors that are **Analagous**, **Monochromatic**, and **Complementary** to the given input color

**Analagous**
For a color to be analagous to an inputted color, it must have similar values for _Saturation_ and _Value_ properties, and its _Hue_ property should differ by roughly 30 degrees.
![image](https://user-images.githubusercontent.com/47365682/205463915-a5cf0bc9-f634-4067-a5bd-16f1bd2ff212.png)



**Monochromatic**
For a color to be monochromatic to a given input color, it must have similar values for _Hue_ and _Value_ properties, with differening values for the _Saturation_ property. A color is considered to be monochromatic regardless of the difference in its _Saturation_ property.
![image](https://user-images.githubusercontent.com/47365682/205463904-3dbbc011-c449-43ae-96b5-147d3c31df3d.png)

**Complementary**
For a color be complementary to a given input color, it must have similar values for _Saturation_ and _Value_ properties, and its _Hue_ property should differ by roughly 180 degrees
![image](https://user-images.githubusercontent.com/47365682/205463949-86a9be87-7e26-40de-b36a-23a5695e2424.png)

