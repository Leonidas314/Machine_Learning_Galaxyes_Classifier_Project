import "./style/Predict.css";
import ImageUploader from "./ImageUploader";
import LinkToGalaxyZoo from "./LinkToGalaxyZoo";
import ImageGallery from "./ImageGallery";
import Header from "./Header";

export default function Predict() {
   const mockImages = [
    { url: "https://placehold.co/200x200/000000/FFFFFF?text=Galaxy+1", name: "Galaxy 1" },
    { url: "https://placehold.co/200x200/222222/FFFFFF?text=Galaxy+2", name: "Galaxy 2" },
    { url: "https://placehold.co/200x200/444444/FFFFFF?text=Galaxy+3", name: "Galaxy 3" },
    { url: "https://placehold.co/200x200/666666/FFFFFF?text=Galaxy+4", name: "Galaxy 4" },
  ];
  return (
    <div className="app">
      <Header />
      <h1 className="app-title">Galaxy Classifier</h1>
      <p className="app-description">
        Subí imágenes de galaxias para su posterior análisis.
      </p>
      <ImageUploader />
       <h2 style={{ marginTop: "2rem" }}>Galaxias similares</h2>
      <ImageGallery images={mockImages} />
      
    </div>
    
  );
}

