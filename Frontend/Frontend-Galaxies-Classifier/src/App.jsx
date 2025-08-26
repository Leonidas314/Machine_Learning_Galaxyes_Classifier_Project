import { useState } from 'react'
import './App.css'
import ImageUploader from './components/ImageUploader';
function App() {
  const [count, setCount] = useState(0)

  return (
     <div className="min-h-screen flex flex-col items-center justify-center bg-gray-900 text-white p-6">
      <h1 className="text-3xl font-bold mb-6">Galaxy Classifier</h1>
      <p className="mb-6 text-gray-300">
        Subí imágenes de galaxias para su posterior análisis.
      </p>
      <ImageUploader />
    </div>   
  );
}

export default App
