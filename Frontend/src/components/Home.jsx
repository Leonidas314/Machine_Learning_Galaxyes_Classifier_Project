import "./style/Home.css"
import Header from "./Header.jsx"

export default function Home() {
    const play = { 
        name: "Play",
        desc: "Play against our ML model."
    }
    const predict = { 
        name: "Predict",
        desc: "Give a galaxy image to our ML model to see its morphology."
    }

    return (
        <div className="home">
            <h1> ChadIA- Galaxy Classifier </h1>
            <div className="home-applications">
                <ApplicationButton name={play.name} desc={play.desc} />
                <ApplicationButton name={predict.name} desc={predict.desc} />
            </div>
        </div>
    )
}

function ApplicationButton({ name, desc }) {
    return (
        <div className="application-button">
            <h3> {name} </h3>
            <p>
                {desc}
            </p>
        </div>
    )
}
