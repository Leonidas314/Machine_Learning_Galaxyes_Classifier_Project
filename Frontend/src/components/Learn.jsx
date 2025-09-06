import Header from "./Header"
import React, { useState, useEffect } from "react";
import "./style/Learn.css"

export default function Learn(){
    return (
        <div className="learn">
            <h1> Learn About the Universe </h1>
            <Articles />
        </div>
    )
}

function Articles() {
    const [articles, setData] = useState([]);

    useEffect(() => {
        fetch("http://127.0.0.1:5000/articles")
            .then(response => response.json())
            .then(data => {
                setData(data);
            })
            .catch(error => {
                console.error("Error loading the data: ", error);
            });
    }, []);

    return (
        <div>
            <ul>
                {articles.map((item,idx) => (
                    <Article key={idx} name={item.name} resume={item.resume} />
                ))}
            </ul>
    
        </div>
    )
}

function Article({ name, resume }) {
    return (
        <li>
            <h1>{name}</h1>
            <p>{resume}</p>
        </li>
    )
}
