(self.webpackChunktu_cis_4398_docs_template=self.webpackChunktu_cis_4398_docs_template||[]).push([[2876],{71441:function(e,t,n){"use strict";n.r(t),n.d(t,{assets:function(){return h},contentTitle:function(){return d},default:function(){return m},frontMatter:function(){return c},metadata:function(){return l},toc:function(){return p}});var a=n(83117),s=n(80102),r=(n(67294),n(3905)),i=n(93456),o=["components"],c={},d=void 0,l={unversionedId:"system-architecture/class_diagram",id:"system-architecture/class_diagram",title:"class_diagram",description:"Class Diagram for Django API Backend",source:"@site/docs/system-architecture/class_diagram.md",sourceDirName:"system-architecture",slug:"/system-architecture/class_diagram",permalink:"/project-fashion-finder/docs/system-architecture/class_diagram",draft:!1,editUrl:"https://github.com/Capstone-Projects-2022-Fall/project-fashion-finder/edit/main/documentation/docs/system-architecture/class_diagram.md",tags:[],version:"current",frontMatter:{},sidebar:"docsSidebar",previous:{title:"design",permalink:"/project-fashion-finder/docs/system-architecture/design"},next:{title:"data_flow",permalink:"/project-fashion-finder/docs/system-architecture/data_flow"}},h={},p=[{value:"Class Diagram for Django API Backend",id:"class-diagram-for-django-api-backend",level:2},{value:"The <strong>FashionPiece</strong> interface",id:"the-fashionpiece-interface",level:3},{value:"The <strong>LabeledFashionPiece</strong> interface",id:"the-labeledfashionpiece-interface",level:3},{value:"The <strong>ReferenceFashionPiece</strong> class",id:"the-referencefashionpiece-class",level:3},{value:"The <strong>UserFashionPiece</strong> class",id:"the-userfashionpiece-class",level:3},{value:"The <strong>Wardrobe</strong> class",id:"the-wardrobe-class",level:3},{value:"The <strong>User</strong> class",id:"the-user-class",level:3},{value:"The <strong>Vote</strong> class",id:"the-vote-class",level:3}],g={toc:p};function m(e){var t=e.components,n=(0,s.Z)(e,o);return(0,r.kt)("wrapper",(0,a.Z)({},g,n,{components:t,mdxType:"MDXLayout"}),(0,r.kt)("h2",{id:"class-diagram-for-django-api-backend"},"Class Diagram for Django API Backend"),(0,r.kt)(i.Mermaid,{config:{},chart:'classDiagram\n    class FashionPiece {\n      <<interface>>\n      +String descriptor\n      +bytearray img_data\n\n      +ObjectId mongo_object_id\n      -create_fashion_piece()\n      -delete_fashion_piece()\n      -update_fashion_piece()\n    }\n\n    FashionPiece .. LabeledFashionPiece\n\n    class LabeledFashionPiece {\n      <<interface>>\n      +List[String] Hex_Codes [predicted]\n      +List[String] Labels [predicted]\n      +List[int] rgb_0 [predicted]\n      +List[int] rgb_1 [predicted]\n      +List[int] rgb_2 [predicted]\n    }\n    LabeledFashionPiece .. UserFashionPiece\n\n    class UserFashionPiece{\n      +String django_user_name\n      +Int django_user_id\n    }\n    LabeledFashionPiece .. ReferenceFashionPiece\n    class ReferenceFashionPiece {\n      +List[String] Hex_Codes [predicted]\n      +List[String] Labels [true]\n      +List[int] rgb_0 [predicted]\n      +List[int] rgb_1 [predicted]\n      +List[int] rgb_2 [predicted]\n    }\n\n    class User {\n        +String username\n        +Int id\n        +String email\n        +String hashed_password\n        +String first_name\n        +String last_name\n        +django_login() User \n        +django_logout() User \n        +django_register() bool \n        +django_authenticate() bool \n    }\n\n    User "1" -- "1..*" UserFashionPiece \n    User "1" -- "1" Wardrobe \n    Wardrobe "1" o-- "1..*" UserFashionPiece \n    class Wardrobe {\n        +List[id] pieces:UserFashionPiece[id]\n        +Int user_id:User[id]\n        +add_item_to_wardrobe(id) bool \n        +remove_item_from_wardrobe(id) bool \n        +view_wardrobe(id) bool \n    }\n\n    class Vote {\n        +Objectid MongoID\n        +id UserId\n        +String vote_value\n        +cast_vote() bool\n    }\n    Vote "1" -- "1" ReferenceFashionPiece\n    Vote "1" -- "1..*" User\n',mdxType:"Mermaid"}),(0,r.kt)("p",null,"The above diagram shows 1 Interface and 6 classes"),(0,r.kt)("h3",{id:"the-fashionpiece-interface"},"The ",(0,r.kt)("strong",{parentName:"h3"},"FashionPiece")," interface"),(0,r.kt)("p",null,"requires that the implementing class have a description, binary image data, and Mongo's ObjectID."),(0,r.kt)("h3",{id:"the-labeledfashionpiece-interface"},"The ",(0,r.kt)("strong",{parentName:"h3"},"LabeledFashionPiece")," interface"),(0,r.kt)("p",null,"extends the ",(0,r.kt)("strong",{parentName:"p"},"FashionPiece")," interface. It also adds the attributes ",(0,r.kt)("strong",{parentName:"p"},"Hex_Codes, labels, rgb_0, rgb_1 and rgb_2")," which represent the labels and color palette. "),(0,r.kt)("h3",{id:"the-referencefashionpiece-class"},"The ",(0,r.kt)("strong",{parentName:"h3"},"ReferenceFashionPiece")," class"),(0,r.kt)("p",null,"implements the ",(0,r.kt)("strong",{parentName:"p"},"LabeledFashionPiece")," interface. It contains the same labels as ",(0,r.kt)("strong",{parentName:"p"},"LabeledFashionPiece"),", but its labels come directly from the Deep Fashion dataset labels, instead of the labels generated by the machine learning pipelines. Its color palette is predicted by the custom color palette detection algorithm."),(0,r.kt)("h3",{id:"the-userfashionpiece-class"},"The ",(0,r.kt)("strong",{parentName:"h3"},"UserFashionPiece")," class"),(0,r.kt)("p",null,"implements the ",(0,r.kt)("strong",{parentName:"p"},"LabeledFashionPiece")," interface. It adds the attributes ",(0,r.kt)("strong",{parentName:"p"},"django_user_name")," and ",(0,r.kt)("strong",{parentName:"p"},"django_user_id"),". These values represent the owner of the fashion piece."),(0,r.kt)("h3",{id:"the-wardrobe-class"},"The ",(0,r.kt)("strong",{parentName:"h3"},"Wardrobe")," class"),(0,r.kt)("p",null,"tracks the fashion pieces that a user has uploaded for later retrieval. It is constructed as a mongoDB aggregation by grouping on the ",(0,r.kt)("strong",{parentName:"p"},"django_user_name")," and",(0,r.kt)("strong",{parentName:"p"},"django_user_id")," in the ",(0,r.kt)("strong",{parentName:"p"},"UserFahsionPiece")," class."),(0,r.kt)("h3",{id:"the-user-class"},"The ",(0,r.kt)("strong",{parentName:"h3"},"User")," class"),(0,r.kt)("p",null,"is a barebones implementation of the Django ",(0,r.kt)("strong",{parentName:"p"},"User")," class, with the attributes of ",(0,r.kt)("strong",{parentName:"p"},"username, id, email, hashed_password, first_name and last_name"),". It relies on the builtin ",(0,r.kt)("inlineCode",{parentName:"p"},"login()"),", ",(0,r.kt)("inlineCode",{parentName:"p"},"logout()"),", ",(0,r.kt)("inlineCode",{parentName:"p"},"autenticate()")," and ",(0,r.kt)("inlineCode",{parentName:"p"},"register()")," functions in the ",(0,r.kt)("inlineCode",{parentName:"p"},"django.auth")," libary "),(0,r.kt)("h3",{id:"the-vote-class"},"The ",(0,r.kt)("strong",{parentName:"h3"},"Vote")," class"),(0,r.kt)("p",null,"is relationship class for tracking which users have liked which reference fashion pieces."),(0,r.kt)("p",null,"The ",(0,r.kt)("strong",{parentName:"p"},"MongoID")," field is a foreign key on the ",(0,r.kt)("strong",{parentName:"p"},"ReferenceFashionPiece")," id field."),(0,r.kt)("p",null,"The ",(0,r.kt)("strong",{parentName:"p"},"UserId")," field is a foreign key on the ",(0,r.kt)("strong",{parentName:"p"},"User")," id field"))}m.isMDXComponent=!0},11748:function(e,t,n){var a={"./locale":89234,"./locale.js":89234};function s(e){var t=r(e);return n(t)}function r(e){if(!n.o(a,e)){var t=new Error("Cannot find module '"+e+"'");throw t.code="MODULE_NOT_FOUND",t}return a[e]}s.keys=function(){return Object.keys(a)},s.resolve=r,e.exports=s,s.id=11748}}]);