import { Routes,Route } from 'react-router-dom'
import Predict from './Predict.jsx'
import About from './About.jsx'
import Home from './Home.jsx'

export default function AppRoutes() {
    return (
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/predict" element={<Predict />} />
            <Route path="/about" element={<About />} />
        </Routes>
    );
}
