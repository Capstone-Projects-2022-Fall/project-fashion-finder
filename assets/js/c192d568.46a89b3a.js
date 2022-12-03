"use strict";(self.webpackChunktu_cis_4398_docs_template=self.webpackChunktu_cis_4398_docs_template||[]).push([[273],{3905:function(e,t,n){n.d(t,{Zo:function(){return c},kt:function(){return u}});var a=n(67294);function i(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function r(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,a)}return n}function o(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?r(Object(n),!0).forEach((function(t){i(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):r(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function l(e,t){if(null==e)return{};var n,a,i=function(e,t){if(null==e)return{};var n,a,i={},r=Object.keys(e);for(a=0;a<r.length;a++)n=r[a],t.indexOf(n)>=0||(i[n]=e[n]);return i}(e,t);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);for(a=0;a<r.length;a++)n=r[a],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(i[n]=e[n])}return i}var s=a.createContext({}),m=function(e){var t=a.useContext(s),n=t;return e&&(n="function"==typeof e?e(t):o(o({},t),e)),n},c=function(e){var t=m(e.components);return a.createElement(s.Provider,{value:t},e.children)},p={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},d=a.forwardRef((function(e,t){var n=e.components,i=e.mdxType,r=e.originalType,s=e.parentName,c=l(e,["components","mdxType","originalType","parentName"]),d=m(n),u=i,h=d["".concat(s,".").concat(u)]||d[u]||p[u]||r;return n?a.createElement(h,o(o({ref:t},c),{},{components:n})):a.createElement(h,o({ref:t},c))}));function u(e,t){var n=arguments,i=t&&t.mdxType;if("string"==typeof e||i){var r=n.length,o=new Array(r);o[0]=d;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l.mdxType="string"==typeof e?e:i,o[1]=l;for(var m=2;m<r;m++)o[m]=n[m];return a.createElement.apply(null,o)}return a.createElement.apply(null,n)}d.displayName="MDXCreateElement"},56563:function(e,t,n){n.r(t),n.d(t,{assets:function(){return c},contentTitle:function(){return s},default:function(){return u},frontMatter:function(){return l},metadata:function(){return m},toc:function(){return p}});var a=n(83117),i=n(80102),r=(n(67294),n(3905)),o=["components"],l={sidebar_position:1},s="Algorithms",m={unversionedId:"system-architecture/algorithms",id:"system-architecture/algorithms",title:"Algorithms",description:"There are several algorithms, big data techniques, and machine learning algorithms present in the Fashion Finder project.",source:"@site/docs/system-architecture/algorithms.md",sourceDirName:"system-architecture",slug:"/system-architecture/algorithms",permalink:"/project-fashion-finder/docs/system-architecture/algorithms",draft:!1,editUrl:"https://github.com/Capstone-Projects-2022-Fall/project-fashion-finder/edit/main/documentation/docs/system-architecture/algorithms.md",tags:[],version:"current",sidebarPosition:1,frontMatter:{sidebar_position:1},sidebar:"docsSidebar",previous:{title:"System Architecture",permalink:"/project-fashion-finder/docs/category/system-architecture"},next:{title:"design",permalink:"/project-fashion-finder/docs/system-architecture/design"}},c={},p=[{value:"Image Prediction",id:"image-prediction",level:2},{value:"Training",id:"training",level:3},{value:"Data Set",id:"data-set",level:4},{value:"Data Pre-processing",id:"data-pre-processing",level:4},{value:"Model",id:"model",level:4},{value:"Model Training",id:"model-training",level:4},{value:"Color Detection",id:"color-detection",level:2},{value:"Sampling algorithm",id:"sampling-algorithm",level:3},{value:"Recommendation Engine",id:"recommendation-engine",level:2},{value:"Similar Items",id:"similar-items",level:3},{value:"Palette similarity .",id:"palette-similarity-",level:4},{value:"Mongo Pipeline",id:"mongo-pipeline",level:4},{value:"Complementary Items",id:"complementary-items",level:3},{value:"Complementary Color detection",id:"complementary-color-detection",level:4}],d={toc:p};function u(e){var t=e.components,l=(0,i.Z)(e,o);return(0,r.kt)("wrapper",(0,a.Z)({},d,l,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h1",{id:"algorithms"},"Algorithms"),(0,r.kt)("p",null,"There are several algorithms, big data techniques, and machine learning algorithms present in the Fashion Finder project."),(0,r.kt)("h2",{id:"image-prediction"},"Image Prediction"),(0,r.kt)("h3",{id:"training"},"Training"),(0,r.kt)("h4",{id:"data-set"},"Data Set"),(0,r.kt)("p",null,"The deep fashion data set can be found ",(0,r.kt)("a",{parentName:"p",href:"https://drive.google.com/drive/folders/0B7EVK8r0v71pQ2FuZ0k0QnhBQnc?resourcekey=0-NWldFxSChFuCpK4nzAIGsg"},"here")),(0,r.kt)("p",null,"The dataset was populated from ",(0,r.kt)("inlineCode",{parentName:"p"},"Category and Attrribute Prediction Benchmark/Img/img_highres.zip")," subfolder, which includes >200,000 images of high resolution training data."),(0,r.kt)("h4",{id:"data-pre-processing"},"Data Pre-processing"),(0,r.kt)("p",null,"To prepare the model for pre-processing, a data loading routine had to be developed. The Data Loader routine that was used can be found ",(0,r.kt)("a",{target:"_blank",href:n(62549).Z},"here"),". "),(0,r.kt)("h4",{id:"model"},"Model"),(0,r.kt)("p",null,"The model that was chosen for use is the Keras VGG 16 model, which is well known for being used in the machine learning domain for image classification..\nThe structure of the model is shown below."),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"conv_model = vgg16.VGG16(weights='imagenet', include_top=False, input_shape=(224,224,3))\nfor layer in conv_model.layers:\n    layer.trainable = False\n\n# x = keras.layers.Dropout(0.25)(conv_model.output)\n \nx = keras.layers.Flatten()(conv_model.output)\nx = keras.layers.Dense(32, activation='relu')(x)\nx = keras.layers.Dense(32, activation='relu')(x)\nx = keras.layers.Dense(32, activation='relu')(x)\n\n# x = keras.layers.Dense(64, activation='relu')(x)\npredictions = keras.layers.Dense(len(CLASS_LIST), activation = 'sigmoid')(x)\nfull_model = keras.models.Model(inputs=conv_model.input, outputs=predictions)\nfull_model.summary()\n\n")),(0,r.kt)("h4",{id:"model-training"},"Model Training"),(0,r.kt)("p",null,'The model was trained on the Deep Fashion dataset described above. In its training, it completed 100 epochs (or "passovers"), meaning that it trained on each of the individual images 100 times. Since the original dataset is well over 200,000 images, this process took over 72 hours to fully train. Thankfully, VGG 16 is capable of "transfer learning" meaning that the training could be stopped and restarted without losing the models computed weights. '),(0,r.kt)("h2",{id:"color-detection"},"Color Detection"),(0,r.kt)("p",null,"The color detection algorithm has several different components. "),(0,r.kt)("p",null,"The goal is to prepare the image data to run a K-nearest-neighbors algorithm on it. However, just running KNN on all of the pixels would result in the dominant color of the background. To solve this, there is a custom sampling algorithm."),(0,r.kt)("h3",{id:"sampling-algorithm"},"Sampling algorithm"),(0,r.kt)("p",null,"The input to the sampling algorithm is a 256x256x3 RGB array. It uses the code below to construct a probability distribution. The distribution is the product of two 1D Gaussian arrays undergoing elementwise multiplication.The goal of the distribution is to increase the number of samples from the subject of the image (in the center of the image, as opposed to the background)"),(0,r.kt)("pre",null,(0,r.kt)("code",{parentName:"pre",className:"language-python"},"def gaussian_kernel(img_height, img_width, kernel_relative_size = 0.1, verbose=False):\n    xs = scipy.signal.gaussian(img_width, std= img_width * kernel_relative_size)\n    ys = scipy.signal.gaussian(img_height, std=img_height * kernel_relative_size)\n    kernel = np.array([[x*y for x in xs] for y in ys])\n    return kernel\n\ndef get_flatted_normalized_gaussian_kernel(kernel):\n    kernel = kernel.reshape(-1)\n    kernel = kernel / np.sum(kernel)\n    return kernel \n")),(0,r.kt)("p",null,'Using this probability distribution, it samples 1000 pixels (with replacement) from the image and then runs Scikit Learns K nearest neighbors algorithm. The "features" that Scikit Learn is fitting on is the RGB values of the pixels.'),(0,r.kt)("h2",{id:"recommendation-engine"},"Recommendation Engine"),(0,r.kt)("p",null,"The recommendation engine makes heavy use of MongoDB's ",(0,r.kt)("strong",{parentName:"p"},"Aggregation Pipelines"),". "),(0,r.kt)("h3",{id:"similar-items"},"Similar Items"),(0,r.kt)("p",null,"Two items are considered similar ",(0,r.kt)("strong",{parentName:"p"},"if and only if**")),(0,r.kt)("ol",null,(0,r.kt)("li",{parentName:"ol"},"They share at least one label class (E.g. Jeans, Blouse, Striped, TShirt, etc.)"),(0,r.kt)("li",{parentName:"ol"},"Their palette similarity is in the top 10 of all of the images that satisfy condition 1")),(0,r.kt)("h4",{id:"palette-similarity-"},"Palette similarity ."),(0,r.kt)("p",null,"The ",(0,r.kt)("em",{parentName:"p"},"Palette Similarity")," of IMG ",(0,r.kt)("em",{parentName:"p"},"target")," and ",(0,r.kt)("em",{parentName:"p"},"candidate_rec")," with 3 RGB values each, is calculated as follows"),(0,r.kt)("p",null,"For each of the colors in ",(0,r.kt)("em",{parentName:"p"},"target")," , calculate its similarity to a list of whites, greys, and skin tones to determine how much weight to give the color in the the recommendation. A color is considered less influential to match on if it is close to a white color, grey color, or a common skin tone color.\nThe similarity is calculated by a weighted average of the minimum euclidean distance between the (R,G,B) points of the ",(0,r.kt)("em",{parentName:"p"},"target")," IMG and the (R,G,B) points of the _candidate_rec image."),(0,r.kt)("h4",{id:"mongo-pipeline"},"Mongo Pipeline"),(0,r.kt)("p",null,"The Mongo Pipeline can be described as followed."),(0,r.kt)("p",null,"For all images in the pipeline, check if the image palette contains any of the RGB values from the ",(0,r.kt)("em",{parentName:"p"},"target")," IMG. Rank each of 3 values by how close they are (in euclidean distance) to any of the 3 values of the ",(0,r.kt)("em",{parentName:"p"},"target")," IMG."),(0,r.kt)("p",null,"Calculate a similarity score which is a weighted average of the above 3 metrics, depending on the weights calculated in the ",(0,r.kt)("em",{parentName:"p"},"Palette Similarity")," step."),(0,r.kt)("p",null,"Rank all of the images by this weighted similarity score, and return the top 10."),(0,r.kt)("p",null,"The recommendation query can be found ",(0,r.kt)("a",{target:"_blank",href:n(46504).Z+"#L96"},"here")),(0,r.kt)("h3",{id:"complementary-items"},"Complementary Items"),(0,r.kt)("p",null,'Complementary items recommendation is driven in a similar fashion to the "Similar Items" recommendation. The same Mongo Pipeline is used. However, since their are multiple different colors that would be considered "complementary" to the dominant color of the image, we must calculate those values and then search for images which contain at least one of those complementary values.'),(0,r.kt)("h4",{id:"complementary-color-detection"},"Complementary Color detection"),(0,r.kt)("p",null,"To determine complementary colors for a given input color, the first step is to represent the RGB values in HSV format (Hue, Saturation, Value)."),(0,r.kt)("p",null,"The relationships that were used to find complementary colors are to determine colors that are ",(0,r.kt)("strong",{parentName:"p"},"Analagous"),", ",(0,r.kt)("strong",{parentName:"p"},"Monochromatic"),", and ",(0,r.kt)("strong",{parentName:"p"},"Complementary")," to the given input color"),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Analagous"),"\nFor a color to be analagous to an inputted color, it must have similar values for ",(0,r.kt)("em",{parentName:"p"},"Saturation")," and ",(0,r.kt)("em",{parentName:"p"},"Value")," properties, and its ",(0,r.kt)("em",{parentName:"p"},"Hue")," property should differ by roughly 30 degrees.\n",(0,r.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/47365682/205463915-a5cf0bc9-f634-4067-a5bd-16f1bd2ff212.png",alt:"image"})),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Monochromatic"),"\nFor a color to be monochromatic to a given input color, it must have similar values for ",(0,r.kt)("em",{parentName:"p"},"Hue")," and ",(0,r.kt)("em",{parentName:"p"},"Value")," properties, with differening values for the ",(0,r.kt)("em",{parentName:"p"},"Saturation")," property. A color is considered to be monochromatic regardless of the difference in its ",(0,r.kt)("em",{parentName:"p"},"Saturation")," property.\n",(0,r.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/47365682/205463904-3dbbc011-c449-43ae-96b5-147d3c31df3d.png",alt:"image"})),(0,r.kt)("p",null,(0,r.kt)("strong",{parentName:"p"},"Complementary"),"\nFor a color be complementary to a given input color, it must have similar values for ",(0,r.kt)("em",{parentName:"p"},"Saturation")," and ",(0,r.kt)("em",{parentName:"p"},"Value")," properties, and its ",(0,r.kt)("em",{parentName:"p"},"Hue")," property should differ by roughly 180 degrees\n",(0,r.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/47365682/205463949-86a9be87-7e26-40de-b36a-23a5695e2424.png",alt:"image"})))}u.isMDXComponent=!0},46504:function(e,t,n){t.Z=n.p+"assets/files/upload_piece_to_mongo-fb1dc12600de7bdad4eb55169cf23a44.py"},62549:function(e,t,n){t.Z=n.p+"assets/files/ModelTraining3-48a5778b7ca8001680e05ddeee447f7c.ipynb"}}]);