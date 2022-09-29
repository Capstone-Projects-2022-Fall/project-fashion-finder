"use strict";(self.webpackChunktu_cis_4398_docs_template=self.webpackChunktu_cis_4398_docs_template||[]).push([[273],{3905:function(e,t,r){r.d(t,{Zo:function(){return l},kt:function(){return m}});var n=r(67294);function o(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function i(e,t){var r=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),r.push.apply(r,n)}return r}function a(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{};t%2?i(Object(r),!0).forEach((function(t){o(e,t,r[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(r)):i(Object(r)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(r,t))}))}return e}function c(e,t){if(null==e)return{};var r,n,o=function(e,t){if(null==e)return{};var r,n,o={},i=Object.keys(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||(o[r]=e[r]);return o}(e,t);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);for(n=0;n<i.length;n++)r=i[n],t.indexOf(r)>=0||Object.prototype.propertyIsEnumerable.call(e,r)&&(o[r]=e[r])}return o}var s=n.createContext({}),u=function(e){var t=n.useContext(s),r=t;return e&&(r="function"==typeof e?e(t):a(a({},t),e)),r},l=function(e){var t=u(e.components);return n.createElement(s.Provider,{value:t},e.children)},p={inlineCode:"code",wrapper:function(e){var t=e.children;return n.createElement(n.Fragment,{},t)}},h=n.forwardRef((function(e,t){var r=e.components,o=e.mdxType,i=e.originalType,s=e.parentName,l=c(e,["components","mdxType","originalType","parentName"]),h=u(r),m=o,f=h["".concat(s,".").concat(m)]||h[m]||p[m]||i;return r?n.createElement(f,a(a({ref:t},l),{},{components:r})):n.createElement(f,a({ref:t},l))}));function m(e,t){var r=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var i=r.length,a=new Array(i);a[0]=h;var c={};for(var s in t)hasOwnProperty.call(t,s)&&(c[s]=t[s]);c.originalType=e,c.mdxType="string"==typeof e?e:o,a[1]=c;for(var u=2;u<i;u++)a[u]=r[u];return n.createElement.apply(null,a)}return n.createElement.apply(null,r)}h.displayName="MDXCreateElement"},56563:function(e,t,r){r.r(t),r.d(t,{assets:function(){return l},contentTitle:function(){return s},default:function(){return m},frontMatter:function(){return c},metadata:function(){return u},toc:function(){return p}});var n=r(83117),o=r(80102),i=(r(67294),r(3905)),a=["components"],c={sidebar_position:1},s=void 0,u={unversionedId:"system-architecture/algorithms",id:"system-architecture/algorithms",title:"algorithms",description:"Purpose",source:"@site/docs/system-architecture/algorithms.md",sourceDirName:"system-architecture",slug:"/system-architecture/algorithms",permalink:"/project-fashion-finder/docs/system-architecture/algorithms",draft:!1,editUrl:"https://github.com/Capstone-Projects-2022-Fall/project-fashion-finder/edit/main/documentation/docs/system-architecture/algorithms.md",tags:[],version:"current",sidebarPosition:1,frontMatter:{sidebar_position:1},sidebar:"docsSidebar",previous:{title:"System Architecture",permalink:"/project-fashion-finder/docs/category/system-architecture"},next:{title:"design",permalink:"/project-fashion-finder/docs/system-architecture/design"}},l={},p=[],h={toc:p};function m(e){var t=e.components,r=(0,o.Z)(e,a);return(0,i.kt)("wrapper",(0,n.Z)({},h,r,{components:t,mdxType:"MDXLayout"}),(0,i.kt)("p",null,(0,i.kt)("strong",{parentName:"p"},"Purpose")),(0,i.kt)("p",null,"The Design Document - Part I Architecture describes the software architecture and how the requirements are mapped into the design. This document will be a combination of diagrams and text that describes what the diagrams are showing."),(0,i.kt)("p",null,(0,i.kt)("strong",{parentName:"p"},"Requirements")),(0,i.kt)("p",null,"Describe algorithms employed in your project, e.g. neural network paradigm, training and training data set, etc."),(0,i.kt)("p",null,"The flow of data can be tracked beginning from the collection of unlabeled picture data of fashion items. The picture data may have tags relating to the context that it was collected in (i.e. type of clothing, style, color, other.)."),(0,i.kt)("p",null,"These images will then be passed through a trained Open CV model which will output both a label for the type of clothing as well as a geometric shape, representing the shape the of the clothing piece in the photo."),(0,i.kt)("p",null,"After the images have gone through this step, they can be uploaded to MongoDB for use in the Fashion Finder app."))}m.isMDXComponent=!0}}]);