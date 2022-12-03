"use strict";(self.webpackChunktu_cis_4398_docs_template=self.webpackChunktu_cis_4398_docs_template||[]).push([[3196],{3905:function(e,t,n){n.d(t,{Zo:function(){return c},kt:function(){return m}});var r=n(67294);function a(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function o(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,r)}return n}function i(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?o(Object(n),!0).forEach((function(t){a(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):o(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,r,a=function(e,t){if(null==e)return{};var n,r,a={},o=Object.keys(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||(a[n]=e[n]);return a}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(r=0;r<o.length;r++)n=o[r],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(a[n]=e[n])}return a}var l=r.createContext({}),d=function(e){var t=r.useContext(l),n=t;return e&&(n="function"==typeof e?e(t):i(i({},t),e)),n},c=function(e){var t=d(e.components);return r.createElement(l.Provider,{value:t},e.children)},p={inlineCode:"code",wrapper:function(e){var t=e.children;return r.createElement(r.Fragment,{},t)}},u=r.forwardRef((function(e,t){var n=e.components,a=e.mdxType,o=e.originalType,l=e.parentName,c=s(e,["components","mdxType","originalType","parentName"]),u=d(n),m=a,f=u["".concat(l,".").concat(m)]||u[m]||p[m]||o;return n?r.createElement(f,i(i({ref:t},c),{},{components:n})):r.createElement(f,i({ref:t},c))}));function m(e,t){var n=arguments,a=t&&t.mdxType;if("string"==typeof e||a){var o=n.length,i=new Array(o);i[0]=u;var s={};for(var l in t)hasOwnProperty.call(t,l)&&(s[l]=t[l]);s.originalType=e,s.mdxType="string"==typeof e?e:a,i[1]=s;for(var d=2;d<o;d++)i[d]=n[d];return r.createElement.apply(null,i)}return r.createElement.apply(null,n)}u.displayName="MDXCreateElement"},21317:function(e,t,n){n.r(t),n.d(t,{assets:function(){return c},contentTitle:function(){return l},default:function(){return m},frontMatter:function(){return s},metadata:function(){return d},toc:function(){return p}});var r=n(83117),a=n(80102),o=(n(67294),n(3905)),i=["components"],s={sidebar_position:1},l="System Overview",d={unversionedId:"requirements/system-overview",id:"requirements/system-overview",title:"System Overview",description:"Project Abstract",source:"@site/docs/requirements/system-overview.md",sourceDirName:"requirements",slug:"/requirements/system-overview",permalink:"/project-fashion-finder/docs/requirements/system-overview",draft:!1,editUrl:"https://github.com/Capstone-Projects-2022-Fall/project-fashion-finder/edit/main/documentation/docs/requirements/system-overview.md",tags:[],version:"current",sidebarPosition:1,frontMatter:{sidebar_position:1},sidebar:"docsSidebar",previous:{title:"Requirements Specification",permalink:"/project-fashion-finder/docs/category/requirements-specification"},next:{title:"System Block Diagram",permalink:"/project-fashion-finder/docs/requirements/system-block-diagram"}},c={},p=[{value:"Project Abstract",id:"project-abstract",level:2},{value:"Data Requirements",id:"data-requirements",level:2},{value:"Data Cleaning process",id:"data-cleaning-process",level:3},{value:"Model Training",id:"model-training",level:2},{value:"Model Deployment Process",id:"model-deployment-process",level:2},{value:"Front-End Development",id:"front-end-development",level:2},{value:"Back-End Development",id:"back-end-development",level:2},{value:"Models",id:"models",level:3},{value:"Like",id:"like",level:4},{value:"UserFashionPiece",id:"userfashionpiece",level:4},{value:"Background",id:"background",level:2}],u={toc:p};function m(e){var t=e.components,s=(0,a.Z)(e,i);return(0,o.kt)("wrapper",(0,r.Z)({},u,s,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("h1",{id:"system-overview"},"System Overview"),(0,o.kt)("h2",{id:"project-abstract"},"Project Abstract"),(0,o.kt)("p",null,"The Fashion Finder Web App will be an application for identifying pieces of clothing and gaining inspiration for outfits and fashion pieces. It serves as a multi-tool for users to find fashion pieces that fit their style and existing wardrobe."),(0,o.kt)("p",null,"The Features of the Fashion Finder web app can be found in the ",(0,o.kt)("a",{parentName:"p",href:"/project-fashion-finder/docs/requirements/features-and-requirements"},"Features and Requirements Document"),". This document will instead cover the main architectural hurdles that are required to get to the features described above."),(0,o.kt)("h2",{id:"data-requirements"},"Data Requirements"),(0,o.kt)("p",null,"In order to get a model that would generalize well, a lot of data was necessary. The training set (Deep Fashion) consists of 30 GB of high resolution image data, containing a wide variety of images obtained from retailers, marketers, and photo collections. All of these files had brief descriptors."),(0,o.kt)("h1",{id:"conceptual-design"},"Conceptual Design"),(0,o.kt)("h3",{id:"data-cleaning-process"},"Data Cleaning process"),(0,o.kt)("p",null,"A data cleaning system will prepare the raw data from Deep Fashion (our training set) and the VGG 16 model."),(0,o.kt)("p",null,"Of all of the classes present in the data, we selected a subset of classes capable of having strong predictive power."),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre"},'CLASS_LIST_21 = ["Tee","Tank","Dress","Shorts","Skirt","Hoodie","Jumpsuit","Sweater","Blazer","Striped","Cardigan","Blouse","Jacket","Jeans","Maxi","Floral","Denim","Sweatshorts","Polka","Shawl","Bodycon"]\n')),(0,o.kt)("h2",{id:"model-training"},"Model Training"),(0,o.kt)("p",null,"The code for the model training can be found here ",(0,o.kt)("a",{target:"_blank",href:n(62549).Z},"here"),".\nA Data Loader utility is used to batch process image files alongside their labels and feed them into the neural network. The neural network takes in batches of 32 images at a time, guess a prediction, and then propogate. The best model training took 29 hours and involved 50 batches over 20 samples of the data. It achieved an accuracy of score of 84% on a class list size of 14. The model that is actually deployed achieved an accuracy of 79% on a class list size of 21. Given the quantity of data and lack of time for manual data cleansing, these are high accuracy scores."),(0,o.kt)("h2",{id:"model-deployment-process"},"Model Deployment Process"),(0,o.kt)("p",null,"In order for the machine learning microservice to be deployed it had to be hosted by django. Instead of making it part of the django web-app, it is deployed as a separate app, ",(0,o.kt)("inlineCode",{parentName:"p"},"ImgPredMicroservice"),". This means that it does not share the same thread as the web server and does not risk hanging the web server when it needs to make heavy calculations."),(0,o.kt)("p",null,"The model is loaded once when the web server starts. To actually process newly uploaded data, routines where written to read a file from Django's ",(0,o.kt)("inlineCode",{parentName:"p"},"InMemoryUploadedFile")," data type and transform it into a 2D RGB-valued array."),(0,o.kt)("h2",{id:"front-end-development"},"Front-End Development"),(0,o.kt)("p",null,"Using the package manager npm@18, front-end components are written in react, compiled as javascript, and then served as static files by the Django file server."),(0,o.kt)("h2",{id:"back-end-development"},"Back-End Development"),(0,o.kt)("p",null,"Back-end development occurs in two different areas."),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},"CRUD operations for users items"),(0,o.kt)("li",{parentName:"ol"},"Data transformation and Machine learning algorthms")),(0,o.kt)("p",null,"In (1) , most routes represent the creation, retrieval, and deletion of models described below.\nIn (2), most routes depend on the core instantiation of the ",(0,o.kt)("inlineCode",{parentName:"p"},"model")," variable, which is read in from ",(0,o.kt)("inlineCode",{parentName:"p"},"src/model/artifacts/")," when the webserver is booted."),(0,o.kt)("h3",{id:"models"},"Models"),(0,o.kt)("h4",{id:"like"},"Like"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre"},"    user_id::str (ref to django user id)\n    user_name::str (ref to django user name)\n    fashion_piece::ObjectID (ref to piece from `LabeledFashionPiece` collection)\n  User\n    id, username, fname, lname, hashed_password\n")),(0,o.kt)("h4",{id:"userfashionpiece"},"UserFashionPiece"),(0,o.kt)("pre",null,(0,o.kt)("code",{parentName:"pre"},"descriptor::str (Description)\nhex_codes::List[List[int]] Hex codes for palette\nrgb::List[List[int]] RGB representations of pallete\nlabels::List[str] List of labels provided by machine learning kernel.\n")),(0,o.kt)("h2",{id:"background"},"Background"),(0,o.kt)("p",null,"While there are lots of different fashion sites out that let users upload photos and share that data, Fashion Finder distinguishes itself by from those sites by running machine learning algorithms, color detection algorithms, and customized recommendation algorithms to give users more of what they want. Sites like pinterest allow users to somewhat customize their feed, but they only give feedback on existing content. "))}m.isMDXComponent=!0},62549:function(e,t,n){t.Z=n.p+"assets/files/ModelTraining3-48a5778b7ca8001680e05ddeee447f7c.ipynb"}}]);