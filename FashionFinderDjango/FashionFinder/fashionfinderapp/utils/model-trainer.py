import os

import tensorflow as tf
import tensorflow.keras as keras

config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
tf.compat.v1.keras.backend.set_session(tf.compat.v1.Session(config=config))

# --------------------------------------

datasetdir = 'C:\\Users\\mdc20\\Downloads\\img'
os.chdir(datasetdir)

from tensorflow.keras.preprocessing.image import ImageDataGenerator

batch_size = 10


def DataLoad(shape, preprocessing):
    '''Create the training and validation datasets for 
    a given image shape.
    '''
    imgdatagen = ImageDataGenerator(
        preprocessing_function=preprocessing,
        horizontal_flip=True,
        validation_split=0.1,
    )

    height, width = shape

    # sub_dirs = [d for d in os.listdir(os.getcwd()) if os.path.isdir(os.path.join(datasetdir, d))]
    # print(sub_dirs)

    # for subdir

    train_dataset = imgdatagen.flow_from_directory(
        os.getcwd(),
        target_size=(height, width),
        batch_size=batch_size,
        class_mode='categorical',
        subset='training',
    )

    val_dataset = imgdatagen.flow_from_directory(
        os.getcwd(),
        target_size=(height, width),
        batch_size=batch_size,
        class_mode='categorical',
        subset='validation'
    )
    return train_dataset, val_dataset


# ---------------------------------

from keras.applications.vgg16 import preprocess_input

train_dataset, val_dataset = DataLoad((350, 350), preprocessing=preprocess_input)

print(type(train_dataset))
print(type(val_dataset))

X_train, y_train = next(train_dataset)

# ------------------
vgg16 = keras.applications.vgg16

# ---------------
conv_model = vgg16.VGG16(weights='imagenet', include_top=False, input_shape=(350, 350, 3))
conv_model = vgg16.VGG16(weights='imagenet', include_top=False)

# flatten the output of the convolutional part:
x = keras.layers.Flatten()(conv_model.output)
# three hidden layers
x = keras.layers.Dense(100, activation='relu')(x)
x = keras.layers.Dense(100, activation='relu')(x)
x = keras.layers.Dense(100, activation='relu')(x)
# final softmax layer with 15 categories
predictions = keras.layers.Dense(5620, activation='softmax')(x)

# creating the full model:
full_model = keras.models.Model(inputs=conv_model.input, outputs=predictions)
full_model.summary()

# -------------
for layer in conv_model.layers:
    layer.trainable = False

full_model.compile(loss='categorical_crossentropy',
                   optimizer=keras.optimizers.Adamax(lr=0.001),
                   metrics=['acc'])

# history = full_model.fit_generator(
#     train_dataset, 
#     validation_data = val_dataset,
#     workers=1,
#     epochs=3,
# )
