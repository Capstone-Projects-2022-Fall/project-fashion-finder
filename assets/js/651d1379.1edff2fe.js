(self.webpackChunktu_cis_4398_docs_template=self.webpackChunktu_cis_4398_docs_template||[]).push([[7607],{4757:function(e,n,i){"use strict";i.r(n),i.d(n,{assets:function(){return p},contentTitle:function(){return l},default:function(){return F},frontMatter:function(){return c},metadata:function(){return d},toc:function(){return m}});var a=i(83117),t=i(80102),s=(i(67294),i(3905)),o=i(93456),r=["components"],c={sidebar_position:5},l="Use-case descriptions",d={unversionedId:"requirements/use-case-descriptions",id:"requirements/use-case-descriptions",title:"Use-case descriptions",description:"Use case 1: Item tracker",source:"@site/docs/requirements/use-case-descriptions.md",sourceDirName:"requirements",slug:"/requirements/use-case-descriptions",permalink:"/project-fashion-finder/docs/requirements/use-case-descriptions",draft:!1,editUrl:"https://github.com/Capstone-Projects-2022-Fall/project-fashion-finder/edit/main/documentation/docs/requirements/use-case-descriptions.md",tags:[],version:"current",sidebarPosition:5,frontMatter:{sidebar_position:5},sidebar:"docsSidebar",previous:{title:"Features and Requirements",permalink:"/project-fashion-finder/docs/requirements/features-and-requirements"},next:{title:"Software Development Plan",permalink:"/project-fashion-finder/docs/category/software-development-plan"}},p={},m=[{value:"Use case 1: Item tracker",id:"use-case-1-item-tracker",level:2},{value:"Use case 2: Item labeler",id:"use-case-2-item-labeler",level:2},{value:"Use case 3: Color labeler",id:"use-case-3-color-labeler",level:2},{value:"Use case 4: Finding similar items",id:"use-case-4-finding-similar-items",level:2},{value:"Use case 5: Finding complementary items",id:"use-case-5-finding-complementary-items",level:2},{value:"Use case 6: Liking / Dislking items",id:"use-case-6-liking--dislking-items",level:2}],h={toc:m};function F(e){var n=e.components,i=(0,t.Z)(e,r);return(0,s.kt)("wrapper",(0,a.Z)({},h,i,{components:n,mdxType:"MDXLayout"}),(0,s.kt)("h1",{id:"use-case-descriptions"},"Use-case descriptions"),(0,s.kt)("h2",{id:"use-case-1-item-tracker"},"Use case 1: Item tracker"),(0,s.kt)("p",null,"A user navigates to Fashion Finder and is fully authenticated\nThey want to keep track of clothes in their closet.\nThey uploads photos of each fashion piece they own.\nThe user is then able to view their uploaded pieces"),(0,s.kt)(o.Mermaid,{config:{},chart:"sequenceDiagram\n    title: Use case 1 -Item tracker\n    actor U as User\n    participant F as Fashion Finder React App\n    %% participant DM as Fashion Finder Django ML Backend\n    participant DC as Fashion Finder Django API Backend\n    participant DFS as Django File Server\n    participant DB as MongoDB\n    U->>+F: Requests route /upload\n    U->>+DFS: Uploads file\n    U->>F: GET /home\n    F->>+DC: Get /async/wardrobe\n    DC->>+F: JSON of User pieces\n    F->>+F: Renders HTML from JSON representation \n    F->>+U: Home Page presented",mdxType:"Mermaid"}),(0,s.kt)("h2",{id:"use-case-2-item-labeler"},"Use case 2: Item labeler"),(0,s.kt)("p",null,"A user navigates to Fashion Finder and is fully authenticated\nThey have pictures of their closet and want to find out how many of each type of clothing they own\nThey upload photos of each fashion piece they own.\nThe user is then able to see their wardrobe with labels generated from a machine learning model\nThese labels will tell the user the type of clothing for each image uploaded "),(0,s.kt)(o.Mermaid,{chart:"sequenceDiagram\n    title: Use case 2 - Item labeler\n    actor U as User\n    participant F as Fashion Finder React App\n    %% participant DM as Fashion Finder Django ML Backend\n    participant DMC as Fashion Finder Django ML Backend\n    participant DC as Fashion Finder Django API Backend\n    participant DFS as Django File Server\n    participant DB as MongoDB\n    U->>+F: Requests route /upload\n    F->>+U: Returns upload form\n    U->>+DFS: Uploads file\n    DFS->>+DC: Notify of new upload\n    DC->>+DMC: Send image file\n    DMC->>+DMC: Run palette detection\n    DMC->>+DC: Redirect user to /home\n    DC->>+F: User redirect\n    F->>+U: Redirect to /home\n    U->>+F: GET /home\n    F->>+DC: Get /async/wardrobe\n    DC->>+DB: Get pieces from UserFashionPiece collection\n    DB->>+DC: Send pieces from USerFashionPiece collection.\n    DC->>+F: JSON of User pieces containing labels\n    F->>+F: Renders HTML from JSON representation containing labels\n    F->>+U: Rendered home page returned to user, which contains colors\n\n\n",mdxType:"Mermaid"}),(0,s.kt)("h2",{id:"use-case-3-color-labeler"},"Use case 3: Color labeler"),(0,s.kt)("p",null,'A user navigates to Fashion Finder and is fully authenticated\nThey have pictures of their closet and want to find out how often different colors appear in their wardrobe.\nThey upload photos of each fashion piece they own.\nThe user is then able to see their wardrobe with labels of the primary colors appearing in each photo.\nThese labels will tell the user the primary "palette" of the fashion piece.'),(0,s.kt)(o.Mermaid,{chart:"sequenceDiagram\n    title: Use case 3 - Color labeler\n    actor U as User\n    participant F as Fashion Finder React App\n    %% participant DM as Fashion Finder Django ML Backend\n    participant DMC as Fashion Finder Django Color Backend\n    participant DC as Fashion Finder Django API Backend\n    participant DFS as Django File Server\n    participant DB as MongoDB\n    U->>+F: Requests route /upload\n    F->>+U: Returns upload form\n    U->>+DFS: Uploads file\n    DFS->>+DC: Notify of new upload\n    DC->>+DMC: Send image file\n    DMC->>+DMC: Run palette detection\n    DMC->>+DC: Redirect user to /home\n    DC->>+F: User redirect\n    F->>+U: Redirect to /home\n    U->>+F: GET /home\n    F->>+DC: Get /async/wardrobe\n    DC->>+DB: Get pieces from UserFashionPiece collection\n    DB->>+DC: Send pieces from USerFashionPiece collection.\n    DC->>+F: JSON of User pieces containing colors\n    F->>+F: Renders HTML from JSON representation containing colors\n    F->>+U: Rendered home page returned to user, which contains colors\n\n",mdxType:"Mermaid"}),(0,s.kt)("h2",{id:"use-case-4-finding-similar-items"},"Use case 4: Finding similar items"),(0,s.kt)("p",null,'A user navigates to Fashion Finder and is fully authenticated.\nThey have a fashion piece that they like and want to find more items like it.\nThey upload the fashion piece image to the Fashion Finder Database.\nThey navigate to a "See more like this" section, where they can see other fashion pieces in the same categories and fashion pieces with similar color palettes. '),(0,s.kt)(o.Mermaid,{chart:'sequenceDiagram\n    title: Use case 4 - Finding similar items\n    actor U as User\n    participant F as Fashion Finder React App\n    %% participant DM as Fashion Finder Django ML Backend\n    %% participant DMC as Fashion Finder Django Color Backend\n    participant DC as Fashion Finder Django API Backend\n    participant DFS as Django File Server\n    participant DB as MongoDB\n\n    U->>+F: Upload file or like/dislike from Discover page\n    F->>+DC: Add item to user wardrobe\n    U->>+F: GET /home\n    F->>+DC: GET /async/wardrobe\n    DC->>+DB: Get UserFashionPiece collection items\n    DB->>+DC: Return UserFashionPiece collection items\n    DC->>+DFS: Store local copy of image data\n    DFS->>+DC: Indicate success or failure on storage \n    DC->>+F: Return JSON of Users pieces\n    F->>+F: Renders HTML from JSON\n    F->>+U: HTML is rendered on the users page\n    F->>+DFS: Get static images\n    U->>+F: Select an item from wardrobe\n    F->>+DC: GET /async/recommendations/<piece_id>\n    DC->>+DB: Call MongoDB aggregation pipeline for recommendations\n    DB->>+DC: Return 10 Mongo documents representing similar items\n    DC->>+DFS: Store local copy of image data\n    DFS->>+DC: Indicate success or failure on storage\n    DC->>+F: Return JSON of Mongo documents, minus image data\n    F->>+DFS: Get static images for recommendations\n    DFS->>+F: Serve static images\n    F->>+U: Renders images on DOM in "Pieces like this" section.',mdxType:"Mermaid"}),(0,s.kt)("h2",{id:"use-case-5-finding-complementary-items"},"Use case 5: Finding complementary items"),(0,s.kt)("p",null,'A user navigates to Fashion Finder and is fully authenticated.\nThey are able to view their wardrobe of uploaded items.\nThey want to be able to find other items that would go well with their item\nFor any of the items in their wardrobe, they can click on a "See items that would good well with this" section\nThey are then prompted with the most similar items, ranked by label similarity and color palette similarity. '),(0,s.kt)(o.Mermaid,{chart:'sequenceDiagram\n    title: Use case 5 - Finding complementary items\n    actor U as User\n    participant F as Fashion Finder React App\n    %% participant DM as Fashion Finder Django ML Backend\n    %% participant DMC as Fashion Finder Django Color Backend\n    participant DC as Fashion Finder Django API Backend\n    participant DFS as Django File Server\n    participant DB as MongoDB\n\n    U->>+F:  Upload file or like/dislike from Discover page\n    F->>+DC: Add item to user wardrobe\n    U->>+F: GET /home\n    F->>+DC: GET /async/wardrobe\n    DC->>+DB: Get UserFashionPiece collection items\n    DB->>+DC: Return UserFashionPiece collection items\n    DC->>+DFS: Store local copy of image data\n    DFS->>+DC: Indicate success or failure on storage \n    DC->>+F: Return JSON of Users pieces\n    F->>+F: Renders HTML from JSON\n    F->>+U: HTML is rendered on the users page\n    F->>+DFS: Get static images\n    U->>+F: Select an item from wardrobe\n    F->>+DC: GET /async/recommendations/complementary/<piece_id>\n    DC->>+DB: Call MongoDB aggregation pipeline for complementary recommendations\n    DB->>+DC: Return 10 Mongo documents representing similar items\n    DC->>+DFS: Store local copy of image data\n    DFS->>+ DC: Indicate success or failure on storage\n    DC->>+F: Return JSON of Mongo documents, minus image data\n    F->>+DFS: Get static images for complementary recommendations\n    DFS->>+F: Serve static images\n    F->>+U: Renders images on DOM in "Pieces that would go well with this" section.\n',mdxType:"Mermaid"}),(0,s.kt)("h2",{id:"use-case-6-liking--dislking-items"},"Use case 6: Liking / Dislking items"),(0,s.kt)("p",null,'A user navigates to Fashion Finder and is fully authenticated.\nThey are able to navigate to a "Like/Dislike" page, where they will be prompted with random fashion pieces\nThey will be able to like or dislike different pieces\nThe user will be able to view a list of their liked pieces'),(0,s.kt)(o.Mermaid,{chart:"sequenceDiagram\n    title: Use case 6 - Liking / Disliking items\n    actor U as User\n    participant F as Fashion Finder React App\n    %% participant DM as Fashion Finder Django ML Backend\n    %% participant DMC as Fashion Finder Django Color Backend\n    participant DC as Fashion Finder Django API Backend\n    participant DFS as Django File Server\n    participant DB as MongoDB\n    U->>+F: GET /discover\n    F->>+DC: GET /discover\n    DC->>+DB: Get random piece from LabeledFashionPiece collection\n    DB->>+DC: Return Mongo Doc of random piece\n    DC->>+DFS: Store image in local file system\n    DFS->>+DC: Indicate success of storage operation\n    DC->>+F: Return JSON with image file path\n    F->>+DFS: Get image from file server\n    DFS->>+F: Send image\n    F->>+U: Update DOM with new image\n    U->>+F: Like piece with id <piece_id>\n    F->>+DC: POST /async/like/<piece_id>\n    DC->>+DB: Add piece_id to UserLikedPieces collection for the given user\n    DB->>DC: Indicate succcess of operation \n    DC->>+F: Return JSON indicating success\n    F->>+U: Update DOM with new image and repeat ",mdxType:"Mermaid"}))}F.isMDXComponent=!0},11748:function(e,n,i){var a={"./locale":89234,"./locale.js":89234};function t(e){var n=s(e);return i(n)}function s(e){if(!i.o(a,e)){var n=new Error("Cannot find module '"+e+"'");throw n.code="MODULE_NOT_FOUND",n}return a[e]}t.keys=function(){return Object.keys(a)},t.resolve=s,e.exports=t,t.id=11748}}]);