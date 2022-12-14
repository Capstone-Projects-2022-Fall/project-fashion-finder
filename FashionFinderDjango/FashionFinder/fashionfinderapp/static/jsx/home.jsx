import React from "react";
import {useState} from 'react';
import Navbar from './navbar.jsx';
import Wardrobe from './wardrobe.jsx'

let context = JSON.parse(window._json);
let user_id = JSON.parse(context["user_id"]);

const PostStyle = () => {
    return (
        <style> {`
            .container {
                position: relative;
                width: 50%;
                height: 200px;
                margin-left: 25%;
                margin-right: 25%;
                margin-top: 25px;
                margin-bottom: 25px;
            }

            .imgContainer {
                position: absolute;
                left: 0;
                top: 0;
                bottom: 0;
                width: 30%;
                border: 1px solid black;
                border-right: 0px solid black;
                box-sizing: border-box;
                cursor: pointer;

                display: flex;
                justify-content: center;
                align-items: center;
            }

            .contentContainer {
                position: absolute;
                top: 0;
                right: 0;
                bottom: 0;
                width: 70%;
                box-sizing: border-box;
                border: 1px solid black;
                border-left: 0px solid black;
                padding: 20px;
                cursor: pointer;
            }

            .postImg {
                width: 100%;
                height: auto;
                max-height: 200px;
                max-width: 200px;
            }

            .postTitle {
                font-size: 32;
                margin-bottom: 5px;
                margin-top: 15px;
            }

            .postDesc {
                font-size: 24;
                margin-top: 20px;
            }

            .postUsername {
                font-size: 18;
            }

            @media only screen and (max-width: 768px) {
                .container {
                    position: relative;
                    width: 80%;
                    height: 300px;
                    margin-left: 10%;
                    margin-right: 10%;
                    margin-rop: 25px;
                    margin-bottom: 25px;
                }

                .imgContainer {
                    width: auto;
                    height: 45%;
                    position: absolute;
                    left: 0;
                    right: 0;
                    top: 0;
                    border: 1px solid black;
                    border-bottom: 0px solid black;
                    box-sizing: border-box;
                    cursor: pointer;

                    display: flex;
                    justify-content: center;
                    alignItems: center;
                }
                
                .contentContainer {
                    width: auto;
                    height: 55%;
                    position: absolute;
                    left: 0;
                    right: 0;
                    bottom: 0;
                    box-sizing: border-box;
                    border: 1px solid black;
                    border-top: 0px solid black;
                    padding: 20px;
                    cursor: pointer;

                    margin-top: 100px;
                }

                .postImg {
                    width: 100%;
                    height: auto;
                    max-height: 100px;
                    max-width: 100px;
                }

                .postTitle {
                    font-size: 32;
                    margin-top: 5px;
                    margin-bottom: 5px;
                }

                .postDesc {
                    font-size: 20;
                    margin-top: 15px;
                }
            }
        `}</style>
    );
}

const SearchStyle = () => {
    return (
        <style> {`
            .searchContainer {
                text-align: center;
            }

            .searchInput {
                width: 50%;
                padding: 12px 20px;
                margin: 8px 0px;
                box-sizing: border-box;
            }

            @media only screen and (max-width: 768px) {
                .searchInput {
                    width: 80%;
                    padding: 12px 20px;
                    margin: 8px 0px;
                    box-sizing: border-box;
                }
            }
        `}</style>
    );
}

const selectionStyle = {
    container: {
        textAlign: 'center'
    },

    btn: {
        width: '25%',
        height: '50px'
    },

    active: {
        height: '100%',
        background: 'linear-gradient(to right, #eee 50%, #aaa 50%)',

        "&:hover": {
            background: "#aaa"
        }
    },

    inactive: {
        height: '100%',
        background: 'linear-gradient(to right, #aaa 50%, #eee 50%)',

        "&:hover": {
            background: "#aaa"
        }
    },

    nameWrapper: {
        display: 'flex',
        justifyConent: 'space-between',
    },

    Wardrobe: {
        marginTop: '15px',
        width: '50%',
        height: '100%',
        textAlign: 'center'
    },

    Similar_Items: {
        marginTop: '15px',
        width: '50%',
        width: '50%',
        height: '100%',
        textAlign: 'center'
    },

    Complementary_Items: {
        marginTop: '15px',
        width: '50%',
        width: '50%',
        height: '100%',
        textAlign: 'center'
    }
}

const ItemPost = (props) => {
    const redirect = () => {
        window.location.replace('/item/' + props.id)
    }


    return <div className="container"> 
        <div className="imgContainer" onClick={redirect}><img src={props.img} className="postImg"/></div>
        <div className="contentContainer" onClick={redirect}>
            <h1 className="postTitle">{props.title}</h1>
            <span className="postUsername">{props.user}</span>
            <p className="postDesc">{props.desc}</p>
        </div>
    </div>;
};


const HomeStyle = () => {
    return (
        <style> {`
            .wardrobe-and-recommendations-container {
                display: flex;
            }
        `}</style>
    );
}


const Home = () => {
    const [elementToDisplay, setElementToDisplay] = useState("");
    const [active, setActiveTab] = useState(true);
    const activeSelction = () => setActiveTab(active => !active)

    const showWardrobe = () => {
      //Show Wardrobe Items
    //   {active && <Item items={items} /> }
    }
    const showSimilarItems = () => {
      //Show Recommendations: similar Items
    }
    const showComplementaryItems = () => {
      //Show Recommendations: complementary Items
    }

    return (
        <Navbar loggedIn={(user_id !== null)} user_id={user_id}>

            <HomeStyle/>
            <div className="wardrobe-and-recommendations-container">
                <Wardrobe>
                </Wardrobe>

            </div>
            
        </Navbar>

    );
}

export default Home;