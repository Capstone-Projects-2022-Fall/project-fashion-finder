"use strict";(self.webpackChunktu_cis_4398_docs_template=self.webpackChunktu_cis_4398_docs_template||[]).push([[3961],{3905:function(e,t,n){n.d(t,{Zo:function(){return d},kt:function(){return m}});var o=n(67294);function r(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function i(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var o=Object.getOwnPropertySymbols(e);t&&(o=o.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,o)}return n}function a(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?i(Object(n),!0).forEach((function(t){r(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):i(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,o,r=function(e,t){if(null==e)return{};var n,o,r={},i=Object.keys(e);for(o=0;o<i.length;o++)n=i[o],t.indexOf(n)>=0||(r[n]=e[n]);return r}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(o=0;o<i.length;o++)n=i[o],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(r[n]=e[n])}return r}var l=o.createContext({}),c=function(e){var t=o.useContext(l),n=t;return e&&(n="function"==typeof e?e(t):a(a({},t),e)),n},d=function(e){var t=c(e.components);return o.createElement(l.Provider,{value:t},e.children)},p={inlineCode:"code",wrapper:function(e){var t=e.children;return o.createElement(o.Fragment,{},t)}},u=o.forwardRef((function(e,t){var n=e.components,r=e.mdxType,i=e.originalType,l=e.parentName,d=s(e,["components","mdxType","originalType","parentName"]),u=c(n),m=r,h=u["".concat(l,".").concat(m)]||u[m]||p[m]||i;return n?o.createElement(h,a(a({ref:t},d),{},{components:n})):o.createElement(h,a({ref:t},d))}));function m(e,t){var n=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var i=n.length,a=new Array(i);a[0]=u;var s={};for(var l in t)hasOwnProperty.call(t,l)&&(s[l]=t[l]);s.originalType=e,s.mdxType="string"==typeof e?e:r,a[1]=s;for(var c=2;c<i;c++)a[c]=n[c];return o.createElement.apply(null,a)}return o.createElement.apply(null,n)}u.displayName="MDXCreateElement"},55531:function(e,t,n){n.r(t),n.d(t,{assets:function(){return d},contentTitle:function(){return l},default:function(){return m},frontMatter:function(){return s},metadata:function(){return c},toc:function(){return p}});var o=n(83117),r=n(80102),i=(n(67294),n(3905)),a=["components"],s={sidebar_position:1},l=void 0,c={unversionedId:"system-architecture/design",id:"system-architecture/design",title:"design",description:"Components and their interfaces",source:"@site/docs/system-architecture/design.md",sourceDirName:"system-architecture",slug:"/system-architecture/design",permalink:"/project-fashion-finder/docs/system-architecture/design",draft:!1,editUrl:"https://github.com/Capstone-Projects-2022-Fall/project-fashion-finder/edit/main/documentation/docs/system-architecture/design.md",tags:[],version:"current",sidebarPosition:1,frontMatter:{sidebar_position:1},sidebar:"docsSidebar",previous:{title:"Algorithms",permalink:"/project-fashion-finder/docs/system-architecture/algorithms"},next:{title:"class_diagram",permalink:"/project-fashion-finder/docs/system-architecture/class_diagram"}},d={},p=[{value:"Components and their interfaces",id:"components-and-their-interfaces",level:2},{value:"Component Diagram",id:"component-diagram",level:3},{value:"Storage Components",id:"storage-components",level:2},{value:"MongoDB Storage Component",id:"mongodb-storage-component",level:3},{value:"Collections",id:"collections",level:4},{value:"SQL Storage Component",id:"sql-storage-component",level:3},{value:"Backend Components",id:"backend-components",level:2},{value:"Django FS",id:"django-fs",level:3},{value:"Fashion Finder app",id:"fashion-finder-app",level:3},{value:"Auth module",id:"auth-module",level:4},{value:"CRUD module",id:"crud-module",level:4},{value:"Web server",id:"web-server",level:4},{value:"ImgPredMicroservice",id:"imgpredmicroservice",level:3},{value:"Palette Detection module",id:"palette-detection-module",level:4},{value:"Class Detection module",id:"class-detection-module",level:4},{value:"Frontend Components",id:"frontend-components",level:2},{value:"React Development Environment",id:"react-development-environment",level:3},{value:"Webpack",id:"webpack",level:3},{value:"NPM",id:"npm",level:2}],u={toc:p};function m(e){var t=e.components,n=(0,r.Z)(e,a);return(0,i.kt)("wrapper",(0,o.Z)({},u,n,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("h2",{id:"components-and-their-interfaces"},"Components and their interfaces"),(0,i.kt)("p",null,(0,i.kt)("strong",{parentName:"p"},"Components")," : Storage, Backend, Frontend"),(0,i.kt)("p",null,(0,i.kt)("strong",{parentName:"p"},"Storage sub-components:")," MongoDB Atlas and Django ORM SQLite"),(0,i.kt)("p",null,(0,i.kt)("strong",{parentName:"p"},"Backend Sub-components:"),"  Fashion Finder App, Image Prediction Microservice, Django Static File Server"),(0,i.kt)("p",null,(0,i.kt)("strong",{parentName:"p"},"Frontend Sub-compoonents:")," React development environment, Babel production build, Django Static File Server hosts js files"),(0,i.kt)("p",null,"The relation of the components can be found in the diagram below."),(0,i.kt)("h3",{id:"component-diagram"},"Component Diagram"),(0,i.kt)("p",null,(0,i.kt)("img",{parentName:"p",src:"https://user-images.githubusercontent.com/47365682/202888272-3d578fcf-64fe-4ea3-9dbd-c85dcd542445.png",alt:"FFSystemdiagram"})),(0,i.kt)("h2",{id:"storage-components"},"Storage Components"),(0,i.kt)("h3",{id:"mongodb-storage-component"},"MongoDB Storage Component"),(0,i.kt)("p",null,"The MongoDB Storage Component is hosted by the free tier of MongoDB atlas which includes 3 replication instances and up to 4 GB of data storage. In the MongoDB storage, we were able to store over 1000 User uploaded pieces and 40,000 reference pieces to be used for the recommendation algorithm."),(0,i.kt)("h4",{id:"collections"},"Collections"),(0,i.kt)("p",null,(0,i.kt)("strong",{parentName:"p"},"UserFashionPiece"),": This collection tracks the labels, colors, descriptors and raw image data of user uploaded photos."),(0,i.kt)("p",null,(0,i.kt)("strong",{parentName:"p"},"LabeledFashionPiece"),": This collection is the reference source for the recommendation algorithm"),(0,i.kt)("p",null,(0,i.kt)("strong",{parentName:"p"},"Votes"),": This collection is for tracking a users likes/dislikes on items in the ",(0,i.kt)("strong",{parentName:"p"},"LabeledFashionPiece")," collection"),(0,i.kt)("h3",{id:"sql-storage-component"},"SQL Storage Component"),(0,i.kt)("p",null,"Django ships by default with SQLite3. While it is not used for the storage of our images or like/dislike data, it is used to keep track of django users and to serve the django admin portal."),(0,i.kt)("h2",{id:"backend-components"},"Backend Components"),(0,i.kt)("h3",{id:"django-fs"},"Django FS"),(0,i.kt)("p",null,"The Django file system handles several jobs for the application. The static HTML/CSS/JS folders house plain javascript generated by webpack. Those static files are then served to the user when they visit the site.\nAdditionally, the Django file system caches files that it receives from the Mongo Data storage. Django does not have to store all 40,000+ images related to the application. Instead, the application will pull the image data once and cache the result as a file in the django static folder."),(0,i.kt)("h3",{id:"fashion-finder-app"},"Fashion Finder app"),(0,i.kt)("h4",{id:"auth-module"},"Auth module"),(0,i.kt)("p",null,"The Auth module is in charge of enforcing users credential rules across the sight.\nThe Sign Up and Login Forms are tied to the django user object and use the auth module to verify the users credentials"),(0,i.kt)("h4",{id:"crud-module"},"CRUD module"),(0,i.kt)("p",null,"The CRUD module is in charge of handling user uploads, creating new Fashion piece document collections through the mongo driver, the creation and deletion of reference data. It is also in charge of saving image to data to static folders upon retrieval from storage."),(0,i.kt)("h4",{id:"web-server"},"Web server"),(0,i.kt)("p",null,"The web servers primary purpose is to repsond to the request of the user. Depending on the request, it will handle it internally or make a second call the the ",(0,i.kt)("inlineCode",{parentName:"p"},"ImgPredMicroService")," app which is described below."),(0,i.kt)("h3",{id:"imgpredmicroservice"},"ImgPredMicroservice"),(0,i.kt)("p",null,"The ",(0,i.kt)("inlineCode",{parentName:"p"},"ImgPredMicroservice")," app is responsible for hosting the trained machine learning kernel, the pallet detection algorithm, and the recommendation engine. These algorithms are explained in more detail in the ",(0,i.kt)("a",{parentName:"p",href:"/project-fashion-finder/docs/system-architecture/algorithms"},"algorithms.md")," file."),(0,i.kt)("h4",{id:"palette-detection-module"},"Palette Detection module"),(0,i.kt)("p",null,"Responsible for taking in a 3x256x256 bit array and producing 3 hex values representing the 3 most shown colors in the fashion piece.\nUses a variety of python modules including ",(0,i.kt)("strong",{parentName:"p"},"scikitlearn, pillow, opencv-python")," to pre-precoess an image and compute the 3 centroids of the processed image."),(0,i.kt)("h4",{id:"class-detection-module"},"Class Detection module"),(0,i.kt)("p",null,'The class dection module hosts the machine learning kernel. The kernel is a multiclass 21-class kernel, meaning that it will predict yes/no to 21 different questions where the question is "Does the image belong to class X?"'),(0,i.kt)("h2",{id:"frontend-components"},"Frontend Components"),(0,i.kt)("h3",{id:"react-development-environment"},"React Development Environment"),(0,i.kt)("p",null,"The frontend is developed in a react development environment."),(0,i.kt)("h3",{id:"webpack"},"Webpack"),(0,i.kt)("p",null,"React code is compiled into plain javascript, which is then served by the Django file server."),(0,i.kt)("h2",{id:"npm"},"NPM"),(0,i.kt)("p",null,"The project uses node@18 and webpack to compile react code into production javascript"))}m.isMDXComponent=!0}}]);