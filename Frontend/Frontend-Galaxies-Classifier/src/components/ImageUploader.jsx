import { useState } from "react";

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
    <div className="flex flex-col items-center gap-4">
      <input
        type="file"
        accept="image/*"
        multiple
        onChange={handleUpload}
        className="border p-2 rounded"
      />

      <div className="grid grid-cols-2 md:grid-cols-3 gap-4 mt-4">
        {images.map((img, idx) => (
          <div key={idx} className="flex flex-col items-center">
            <img
              src={img.url}
              alt={img.name}
              className="w-40 h-40 object-cover rounded shadow"
            />
            <span className="text-sm mt-1">{img.name}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
