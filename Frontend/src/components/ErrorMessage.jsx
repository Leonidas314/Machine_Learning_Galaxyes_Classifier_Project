import React from "react";
import { useNavigate } from "react-router-dom";

export default function ErrorMessage({ message }) {
  const navigate = useNavigate();

  const handleRedirect = () => {
    navigate("/predict"); // redirige al endpoint /predict
  };

  return (
    <div className="error-box">
      <h2>❌ Error</h2>
      <p>{message || "Ha ocurrido un error inesperado."}</p>
      <button onClick={handleRedirect}>Ir a /predict</button>
    </div>
  );
}

