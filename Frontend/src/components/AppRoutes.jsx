import { Routes,Route } from 'react-router-dom'
import App from './../App.jsx'
import About from './About.jsx'

function AppRoutes() {
    return (
        <Routes>
            <Route path="/" element={<App />} />
            <Route path="/about" element={<About />} />
        </Routes>
    );
}

export default AppRoutes;
