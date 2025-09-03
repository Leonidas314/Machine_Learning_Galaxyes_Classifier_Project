import React from "react"
import { Link } from "react-router-dom"
import "./style/Header.css"

export default function Header() {
    const buttons = [
        {label: "Home", url: "/"},
        {label: "About", url: "/about"},
        {label: "Predict", url: "/predict"},
        {label: "Learn", url: "/learn"},
    ]

    return (
        <header className="header">
            { buttons.map((button,idx) => (
                <HeaderButton key={idx} label={button.label} url={button.url} />
            ))}
        </header>
    )
}

function HeaderButton({ label, url }) {
    return (
        <Link to={url}>
            {label}
        </Link>
    )
}
