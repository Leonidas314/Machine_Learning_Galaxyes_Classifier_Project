import { useState } from "react";
import "./style/ImageUploader.css";
import ErrorMessage from "./ErrorMessage"
export default function ImageUploader() {
  const [images, setImages] = useState([]);
  const [error, setError] = useState(null);
  // Guardar archivos seleccionados para preview y envío
  const handleFileSelect = (e) => {
    const files = Array.from(e.target.files);
    const previews = files.map((file) => ({
      file, // mantenemos el archivo para enviar
      name: file.name,
      url: URL.createObjectURL(file),
    }));

    setImages((prev) => [...prev, ...previews]);
  };

  // Enviar imágenes al backend
  const handleUpload = async () => {
    if (images.length === 0) return;

    const formData = new FormData();
    images.forEach((img) => formData.append("images", img.file));

    try {
      const response = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) throw new Error("Error al subir las imágenes");

      const data = await response.json();
      console.log("Respuesta del backend:", data);

      if (data.error) {
      // 🔹 si el backend devuelve { error: ... }
        setError(data.error);
      } else {
        alert("Imágenes enviadas correctamente!");
      }
      } catch (err) {
        console.error("Error en la subida:", err);
        setError(err.message); // 🔹 guarda el mensaje de error
      }
  };

  return (
    error ? (
      <ErrorMessage message={error}  onRetry={() => setError(null)}/>
    ):(
      <div className="uploader">
        <input
          type="file"
          accept="image/*"
          multiple
          onChange={handleFileSelect}
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
        
      <button onClick={handleUpload} className="uploader-btn">
        Enviar al backend
      </button>
    </div>        
    )
  );
}
