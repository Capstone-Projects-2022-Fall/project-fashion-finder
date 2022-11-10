import React from "react";
import ReactDOM from 'react-dom';
import Navbar from "./navbar.jsx";
import {useState} from "react";

let context = JSON.parse(window._json);
let responseErr = (context["error"] === undefined) ? false : JSON.parse(context["error"]);
console.log(responseErr)

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const ErrMsg = () => {
    const errKeys = Object.keys(responseErr)

    return (
        <div>
            {errKeys.map((errKey) => {
                <p>{errKey}</p>
            })}
        </div>
    );
};

const LoginStyle = () => {
    return (
        <style> {`
            .loginContainer {
                text-align: center;
            }

            .loginTitle {
                font-size: 32;
            }

            .loginInputContainer {
                width: 100%;
            }

            .loginInput {
                width: 50%;
                padding: 12px 20px;
                margin: 8px 0px;
                box-sizing: border-box;
            }

            .loginBtn {
                width: 25%;
                height: 3em;
                text-align: center;
            }

            @media only screen and (max-width: 768px) {
                .loginInput {
                    width: 80%;
                    padding: 12px 20px;
                    margin: 8px 0px;
                    box-sizing: border-box;
                }
            }
        `}</style>
    );
}
const Login = () => {
    return <Navbar> 
        <LoginStyle />
        <ErrMsg />
        <div className="loginContainer">
            <h1 className="loginTitle">Sign Up</h1>

            <form method="POST">
                <div className="loginInputContainter"><input className="loginInput" placeholder="Username" name="username" id="username-input" /></div>
                <div className="loginInputContainter"><input className="loginInput" placeholder="Password" name="password" id="password-input" type="password" /></div>
                <input className="loginBtn" type="submit" />
            </form>
        </div>
    </Navbar>;
};

ReactDOM.render(<Login />, document.getElementById('root'));