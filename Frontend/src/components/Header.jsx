import React from "react"
import "./style/Header.css"

function Header({ buttons }) {
    return (
        <header className="header">
            { buttons.map((label,idx) => (
                <button key={idx} className="header-btn">{label}</button>
            ))}
        </header>
    )
}

export default Header;
