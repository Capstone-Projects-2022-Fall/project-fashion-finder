import React from "react";
import {useState} from 'react';

const style = {
    navbar: { 
        position: 'fixed',
        top: '0px',
        left: '0px', 
        zIndex: 1,
        width: '100%',

        backgroundColor: '#00ff',
        color: 'black',
        padding: '5px',
        fontFamily: 'Arial',
        fontSize: '40px',
        letterSpacing: '1.5px'
    },
            
    title: {
        fontWeight: 900,
        textAlign: 'center',
        paddingTop: '3px',
        paddingBottom: '3px',
    },

    nav: { 
        position: 'fixed',
        top: '0px',
        right: '0px',
        textAlign: 'right',
        fontSize: '18px',
        padding: '12px',
        paddingTop: '22px'
    },

    navLink: { 
        textDecoration: 'none',
        color: '#686868',
        paddingRight: '7px',
        paddingLeft: '7px'
    },

    dropdown: {
        position: 'relative',
        display: 'inline-block'
    },

    dropdownContent: {
        display: 'none',
        position: 'absolute',
        backgroundColor: '#f9f9f9',
        boxShadow: '0px 8px 16px 0px rgba(0,0,0,0.2)',
        minWidth: '90px',
        zIndex: 1,
        marginTop: '11px'
    },

    dropdownContentLink: {
        color: 'black', 
        textDecoration: 'none', 
        display: 'block'
    }
};

const Navbar = ({children, loggedIn: _loggedIn}) => {
    const [isActive, setActive] = useState(false);

    const loggedIn = _loggedIn && _loggedIn !== 'false';

    const toggleClass = () => {
        setActive(!isActive);
    }

    const redirect = () => {
        let url = new URL(window.location.href);
        let params = new URLSearchParams(url.search);
        params.delete('search');
    }

    return <>
        <header className={isActive ? "header header-active" : "header"}>
            <nav className="navbar">
                <a href="/" className="nav-logo" onClick={redirect}>Fashion Finder</a>
                <ul className={isActive ? "nav-menu active" : "nav-menu"}>
                    {loggedIn && <>
                    <li className="nav-item">
                        <a href="/upload" className="nav-link">New Upload</a>
                    </li>
                    <li className="nav-item">
                        <a href="/profile" className="nav-link">Profile</a>
                    </li>
                    <li className="nav-item">
                        <a href="/accounts/logout/" className="nav-link">Logout</a>
                    </li>
                    <li className="nav-item">
                        <a href="/discover" className="nav-link">Discover</a>
                    </li>
                    </>}
                    {!loggedIn && <>
                    <li className="nav-item">
                        <a href="/accounts/login/" className="nav-link">Upload Photo</a>
                    </li>
                    <li className="nav-item">
                        <a href="/accounts/login/" className="nav-link">Log in</a>
                    </li>
                    <li className="nav-item">
                        <a href="/accounts/register/" className="nav-link">Sign Up</a>
                    </li>
                     </>}
                </ul>
                <div className={isActive ? "hamburger active" : "hamburger"} onClick={toggleClass}>
                    <span className="bar"></span>
                    <span className="bar"></span>
                    <span className="bar"></span>
                </div>
            </nav>
        </header>

        <div className="content">
            {children}
        </div>
    </>;
}

export default Navbar;