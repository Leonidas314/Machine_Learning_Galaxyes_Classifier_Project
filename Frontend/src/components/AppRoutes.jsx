import { Routes,Route } from 'react-router-dom'
import App from './../App.jsx'
import About from './About.jsx'
import Home from './Home.jsx'

export default function AppRoutes() {
    return (
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/app" element={<App />} />
            <Route path="/about" element={<About />} />
        </Routes>
    );
}
