import "./App.css";
import ImageUploader from "./components/ImageUploader";
import LinkToGalaxyZoo from "./components/LinkToGalaxyZoo";
function App() {
  return (
    <div className="app">
      <h1 className="app-title">Galaxy Classifier</h1>
      <p className="app-description">
        Subí imágenes de galaxias para su posterior análisis.
      </p>
      <ImageUploader />
      <div style={{ marginTop: "2rem" }}>
        <LinkToGalaxyZoo />
      </div>
    </div>
    
  );
}

export default App;
