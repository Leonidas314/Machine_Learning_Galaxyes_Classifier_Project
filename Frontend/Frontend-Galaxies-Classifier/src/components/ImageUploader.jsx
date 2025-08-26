import { useState } from "react";
import "./ImageUploader.css"; // Importamos los estilos del componente

export default function ImageUploader() {
  const [images, setImages] = useState([]);

  const handleUpload = (e) => {
    const files = Array.from(e.target.files);
    const previews = files.map((file) => ({
      name: file.name,
      url: URL.createObjectURL(file),
    }));

    setImages((prev) => [...prev, ...previews]);
  };

  return (
    <div className="uploader">
      <input
        type="file"
        accept="image/*"
        multiple
        onChange={handleUpload}
        className="uploader-input"
      />

      <div className="uploader-grid">
        {images.map((img, idx) => (
          <div key={idx} className="uploader-item">
            <img src={img.url} alt={img.name} className="uploader-img" />
            <span className="uploader-name">{img.name}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
