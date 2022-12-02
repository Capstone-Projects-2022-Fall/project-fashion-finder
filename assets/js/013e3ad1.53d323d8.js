"use strict";(self.webpackChunktu_cis_4398_docs_template=self.webpackChunktu_cis_4398_docs_template||[]).push([[5052],{3905:function(e,t,r){r.d(t,{Zo:function(){return p},kt:function(){return m}});var a=r(67294);function n(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function o(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);t&&(a=a.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,a)}return r}function i(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?o(Object(r),!0).forEach((function(t){n(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):o(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function l(e,t){if(null==e)return{};var r,a,n=function(e,t){if(null==e)return{};var r,a,n={},o=Object.keys(e);for(a=0;a<o.length;a++)r=o[a],t.indexOf(r)>=0||(n[r]=e[r]);return n}(e,t);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);for(a=0;a<o.length;a++)r=o[a],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(n[r]=e[r])}return n}var s=a.createContext({}),c=function(e){var t=a.useContext(s),r=t;return e&&(r="function"==typeof e?e(t):i(i({},t),e)),r},p=function(e){var t=c(e.components);return a.createElement(s.Provider,{value:t},e.children)},d={inlineCode:"code",wrapper:function(e){var t=e.children;return a.createElement(a.Fragment,{},t)}},u=a.forwardRef((function(e,t){var r=e.components,n=e.mdxType,o=e.originalType,s=e.parentName,p=l(e,["components","mdxType","originalType","parentName"]),u=c(r),m=n,f=u["".concat(s,".").concat(m)]||u[m]||d[m]||o;return r?a.createElement(f,i(i({ref:t},p),{},{components:r})):a.createElement(f,i({ref:t},p))}));function m(e,t){var r=arguments,n=t&&t.mdxType;if("string"==typeof e||n){var o=r.length,i=new Array(o);i[0]=u;var l={};for(var s in t)hasOwnProperty.call(t,s)&&(l[s]=t[s]);l.originalType=e,l.mdxType="string"==typeof e?e:n,i[1]=l;for(var c=2;c<o;c++)i[c]=r[c];return a.createElement.apply(null,i)}return a.createElement.apply(null,r)}u.displayName="MDXCreateElement"},89892:function(e,t,r){r.r(t),r.d(t,{assets:function(){return p},contentTitle:function(){return s},default:function(){return m},frontMatter:function(){return l},metadata:function(){return c},toc:function(){return d}});var a=r(83117),n=r(80102),o=(r(67294),r(3905)),i=["components"],l={},s=void 0,c={unversionedId:"system-architecture/data_flow",id:"system-architecture/data_flow",title:"data_flow",description:"Data Flow",source:"@site/docs/system-architecture/data_flow.md",sourceDirName:"system-architecture",slug:"/system-architecture/data_flow",permalink:"/project-fashion-finder/docs/system-architecture/data_flow",draft:!1,editUrl:"https://github.com/Capstone-Projects-2022-Fall/project-fashion-finder/edit/main/documentation/docs/system-architecture/data_flow.md",tags:[],version:"current",frontMatter:{},sidebar:"docsSidebar",previous:{title:"class_diagram",permalink:"/project-fashion-finder/docs/system-architecture/class_diagram"},next:{title:"API Specification",permalink:"/project-fashion-finder/docs/category/api-specification"}},p={},d=[{value:"Data Flow Diagram",id:"data-flow-diagram",level:2},{value:"FF App",id:"ff-app",level:3},{value:"Img Pred",id:"img-pred",level:3},{value:"Rec Eng.",id:"rec-eng",level:3},{value:"Data Lakes",id:"data-lakes",level:2},{value:"User Pieces",id:"user-pieces",level:3},{value:"Rec Pieces",id:"rec-pieces",level:3},{value:"Django Static",id:"django-static",level:3}],u={toc:d};function m(e){var t=e.components,r=(0,n.Z)(e,i);return(0,o.kt)("wrapper",(0,a.Z)({},u,r,{components:t,mdxType:"MDXLayout"}),(0,o.kt)("p",null,(0,o.kt)("strong",{parentName:"p"},"Data Flow")),(0,o.kt)("p",null,"The data flow can be found below"),(0,o.kt)("h2",{id:"data-flow-diagram"},"Data Flow Diagram"),(0,o.kt)("p",null,(0,o.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/47365682/202894408-38c5d8c6-1a2b-40b2-8649-4d21369a8d84.png",alt:"DataFlow drawio"})),(0,o.kt)("h3",{id:"ff-app"},"FF App"),(0,o.kt)("p",null,"The application has several jobs in relation to data flow"),(0,o.kt)("ol",null,(0,o.kt)("li",{parentName:"ol"},"Handle user upload events"),(0,o.kt)("li",{parentName:"ol"},"Process user images with label prediction (through the ImgPredictionMicroservice) "),(0,o.kt)("li",{parentName:"ol"},"Process user images with palette prediction (through the ImgPredictionMicroservice)"),(0,o.kt)("li",{parentName:"ol"},"Process CRUD actions on data of class ",(0,o.kt)("strong",{parentName:"li"},"UserFashionPiece")," through the mongo driver"),(0,o.kt)("li",{parentName:"ol"},"Process CRUD actions on data of class ",(0,o.kt)("strong",{parentName:"li"},"User")," through the djang auth driver")),(0,o.kt)("h3",{id:"img-pred"},"Img Pred"),(0,o.kt)("p",null,"The image prediction microservice takes in an image of format .jpg or .png of any size. It then processes the data as follows."),(0,o.kt)("p",null,"First, it will resize the data to be 512x512x3 in size, using tensorflows ",(0,o.kt)("inlineCode",{parentName:"p"},"DataLoader()")," class. It will then pass the input tensor into the loaded model, and the model will output a list of classes where the p>0.4. In this case, p represents the probability that the input belongs to class x."),(0,o.kt)("p",null,"The Img Pred microservice will then call the Color Prediction class's get_dominant_colors() to get the palette of the image."),(0,o.kt)("p",null,"More details on these services can be found in ",(0,o.kt)("a",{parentName:"p",href:"/project-fashion-finder/docs/system-architecture/algorithms"},"algorithms.md")),(0,o.kt)("p",null,"The Img Pred microservice will then return both the label and the color codes to the FF App."),(0,o.kt)("h3",{id:"rec-eng"},"Rec Eng."),(0,o.kt)("p",null,"The recommendation engine takes in requests from the FF App and in turn calls a Mongo Aggregation pipeline."),(0,o.kt)("p",null,"The recommendation engine is responsible for calculating the weights for each color in the source image.\nThe recommendation engine is responsible for calculating complementatry colors to feed into the mongo aggregation pipeline."),(0,o.kt)("h2",{id:"data-lakes"},"Data Lakes"),(0,o.kt)("h3",{id:"user-pieces"},"User Pieces"),(0,o.kt)("p",null,"Hosts the labels, color codes, and raw image data of users uploaded files."),(0,o.kt)("h3",{id:"rec-pieces"},"Rec Pieces"),(0,o.kt)("p",null,"Hosts the labels, color codes, and raw image data of recommendation reference data files."),(0,o.kt)("h3",{id:"django-static"},"Django Static"),(0,o.kt)("p",null,"Hosts static JPG/PNG files that have been cached due to calls for those files."))}m.isMDXComponent=!0}}]);