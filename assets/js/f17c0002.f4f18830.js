"use strict";(self.webpackChunktu_cis_4398_docs_template=self.webpackChunktu_cis_4398_docs_template||[]).push([[3157],{3905:function(e,t,n){n.d(t,{Zo:function(){return u},kt:function(){return f}});var i=n(67294);function o(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function a(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);t&&(i=i.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,i)}return n}function r(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?a(Object(n),!0).forEach((function(t){o(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):a(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function s(e,t){if(null==e)return{};var n,i,o=function(e,t){if(null==e)return{};var n,i,o={},a=Object.keys(e);for(i=0;i<a.length;i++)n=a[i],t.indexOf(n)>=0||(o[n]=e[n]);return o}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(i=0;i<a.length;i++)n=a[i],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(o[n]=e[n])}return o}var c=i.createContext({}),l=function(e){var t=i.useContext(c),n=t;return e&&(n="function"==typeof e?e(t):r(r({},t),e)),n},u=function(e){var t=l(e.components);return i.createElement(c.Provider,{value:t},e.children)},p={inlineCode:"code",wrapper:function(e){var t=e.children;return i.createElement(i.Fragment,{},t)}},d=i.forwardRef((function(e,t){var n=e.components,o=e.mdxType,a=e.originalType,c=e.parentName,u=s(e,["components","mdxType","originalType","parentName"]),d=l(n),f=o,m=d["".concat(c,".").concat(f)]||d[f]||p[f]||a;return n?i.createElement(m,r(r({ref:t},u),{},{components:n})):i.createElement(m,r({ref:t},u))}));function f(e,t){var n=arguments,o=t&&t.mdxType;if("string"==typeof e||o){var a=n.length,r=new Array(a);r[0]=d;var s={};for(var c in t)hasOwnProperty.call(t,c)&&(s[c]=t[c]);s.originalType=e,s.mdxType="string"==typeof e?e:o,r[1]=s;for(var l=2;l<a;l++)r[l]=n[l];return i.createElement.apply(null,r)}return i.createElement.apply(null,n)}d.displayName="MDXCreateElement"},40099:function(e,t,n){n.r(t),n.d(t,{assets:function(){return u},contentTitle:function(){return c},default:function(){return f},frontMatter:function(){return s},metadata:function(){return l},toc:function(){return p}});var i=n(83117),o=n(80102),a=(n(67294),n(3905)),r=["components"],s={sidebar_position:1},c="API Specifications",l={unversionedId:"api-specification/API-Specifications",id:"api-specification/API-Specifications",title:"API Specifications",description:"API Documentation Document:",source:"@site/docs/api-specification/API-Specifications.md",sourceDirName:"api-specification",slug:"/api-specification/API-Specifications",permalink:"/project-fashion-finder/docs/api-specification/API-Specifications",draft:!1,editUrl:"https://github.com/Capstone-Projects-2022-Fall/project-fashion-finder/edit/main/documentation/docs/api-specification/API-Specifications.md",tags:[],version:"current",sidebarPosition:1,frontMatter:{sidebar_position:1},sidebar:"docsSidebar",previous:{title:"API Specification",permalink:"/project-fashion-finder/docs/category/api-specification"},next:{title:"Class Diagram of API",permalink:"/project-fashion-finder/docs/api-specification/classDiagram"}},u={},p=[{value:"Classes - Web Interface",id:"classes---web-interface",level:2},{value:"HomePage",id:"homepage",level:3},{value:"Methods:",id:"methods",level:4},{value:"SignUp",id:"signup",level:3},{value:"Data Fields:",id:"data-fields",level:4},{value:"Email",id:"email",level:5},{value:"Password",id:"password",level:5},{value:"PhoneNumber",id:"phonenumber",level:5},{value:"firstName",id:"firstname",level:5},{value:"lastName:",id:"lastname",level:5},{value:"Methods:",id:"methods-1",level:4}],d={toc:p};function f(e){var t=e.components,n=(0,o.Z)(e,r);return(0,a.kt)("wrapper",(0,i.Z)({},d,n,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"api-specifications"},"API Specifications"),(0,a.kt)("p",null,"API Documentation Document: "),(0,a.kt)("h2",{id:"classes---web-interface"},"Classes - Web Interface"),(0,a.kt)("h3",{id:"homepage"},"HomePage"),(0,a.kt)("p",null," Class Purpose: This is the first page that users will see when they visit the web page.  The purpose of this page is to give the user an understanding of the website, and to allow them to login or register to get access to the full functionality. "),(0,a.kt)("h4",{id:"methods"},"Methods:"),(0,a.kt)("p",null,"signUp()\nPurpose: to allow a user to login to their account\nPre-Condition: The user must have an account\nPost-Condition: none\nParameters:  email, password\nReturn Values: none\nExceptions Thrown: Invalid Credentials\nsignUp()\nPurpose: to allow a user with an existing account to login\nPre-Condition:  the user does not have an account\nPost Condition: the user will be notified through email of account creation.\nParameters: email, password, phoneNumber, firstName, lastName\nReturn Values: none\nExceptions Thrown: user already exists"),(0,a.kt)("h3",{id:"signup"},"SignUp"),(0,a.kt)("p",null,"Class Purpose: This class is used for a user to sign up for an account.  They will enter their email, password, phoneNumber, firstName, and lastName to create their account. "),(0,a.kt)("h4",{id:"data-fields"},"Data Fields:"),(0,a.kt)("h5",{id:"email"},"Email"),(0,a.kt)("p",null,"Type: string"),(0,a.kt)("p",null,"Purpose: this is used to set the users email which will also be used for login."),(0,a.kt)("h5",{id:"password"},"Password"),(0,a.kt)("p",null,"Type: string"),(0,a.kt)("p",null,"Purpose: sets the password for account login"),(0,a.kt)("h5",{id:"phonenumber"},"PhoneNumber"),(0,a.kt)("p",null,"Type: string"),(0,a.kt)("p",null,"Purpose:  a phone number to be held under the account"),(0,a.kt)("h5",{id:"firstname"},"firstName"),(0,a.kt)("p",null,"Type: string\nPurpose: to have a name linked to each account"),(0,a.kt)("h5",{id:"lastname"},"lastName:"),(0,a.kt)("p",null,"Type: string\nPurpose: to have a name linked to each account"),(0,a.kt)("h4",{id:"methods-1"},"Methods:"),(0,a.kt)("p",null,"createAccount(email, password, phoneNumber, firstName, lastName)\nPurpose:  this is to create an account for a user and store all of the information into the database.\nPre-Condition: valid email address (not used previously)\nPost Condition: Verification email"))}f.isMDXComponent=!0}}]);