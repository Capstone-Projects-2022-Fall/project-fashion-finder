---
sidebar_position: 1
---

**Purpose**

The Design Document - Part I Architecture describes the software architecture and how the requirements are mapped into the design. This document will be a combination of diagrams and text that describes what the diagrams are showing.

**Requirements**


Describe algorithms employed in your project, e.g. neural network paradigm, training and training data set, etc.

The flow of data can be tracked beginning from the collection of unlabeled picture data of fashion items. The picture data may have tags relating to the context that it was collected in (i.e. type of clothing, style, color, other.).

These images will then be passed through a trained Open CV model which will output both a label for the type of clothing as well as a geometric shape, representing the shape the of the clothing piece in the photo.

After the images have gone through this step, they can be uploaded to MongoDB for use in the Fashion Finder app.
