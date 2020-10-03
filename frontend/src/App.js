import React, { useState } from "react";
import "./App.css";

function App() {
  const [fixedAcidity, setFixedAcidity] = useState("");
  const [volatileAcidity, setVolatileAcidity] = useState("");
  const [citricAcid, setCitricAcid] = useState("");
  const [residualSugar, setResidualSugar] = useState("");
  const [chlorides, setChlorides] = useState("");
  const [freeSulfurDioxide, setFreeSulfurDioxide] = useState("");
  const [totalSulfurDioxide, setTotalSulfurDioxide] = useState("");
  const [density, setDensity] = useState("");
  const [sulphates, setSulphates] = useState("");
  const [pH, setPH] = useState("");
  const [alcohol, setAlcohol] = useState("");
  const [wineType, setWineType] = useState("");

  const handleSubmit = () => {
    //call Api after installing axuse package
    if (
      fixedAcidity === "" ||
      volatileAcidity === "" ||
      citricAcid === "" ||
      residualSugar === "" ||
      chlorides === "" ||
      freeSulfurDioxide === "" ||
      totalSulfurDioxide === "" ||
      density === "" ||
      sulphates === "" ||
      pH === "" ||
      alcohol === "" ||
      wineType === ""
    ) {
      alert("empty field");
    } else if (!/^[0-9\b]+$/.test(fixedAcidity)) {
      alert("Should Enter a Number");
    }
  };

  return (
    <div className="container" style={{ paddingTop: 20, paddingBottom: 20 }}>
      <form>
        <div className="form-group">
          <label>Fixed Acidity</label>
          <input
            type="text"
            className="form-control"
            onChange={(e) => setFixedAcidity(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label>Volatile Acidity</label>
          <input
            type="text"
            className="form-control"
            onChange={(e) => setVolatileAcidity(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label>Citric Acid</label>
          <input
            type="text"
            className="form-control"
            onChange={(e) => setCitricAcid(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label>Residual Sugar</label>
          <input
            type="text"
            className="form-control"
            onChange={(e) => setResidualSugar(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label>Chlorides</label>
          <input
            type="text"
            className="form-control"
            onChange={(e) => setChlorides(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label>Free Sulfur Dioxide</label>
          <input
            type="text"
            className="form-control"
            onChange={(e) => setFreeSulfurDioxide(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label>Total Sulfur Dioxide</label>
          <input
            type="text"
            className="form-control"
            onChange={(e) => setTotalSulfurDioxide(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label>Density</label>
          <input
            type="text"
            className="form-control"
            onChange={(e) => setDensity(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label>PH</label>
          <input
            type="text"
            className="form-control"
            onChange={(e) => setPH(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label>Sulphates</label>
          <input
            type="text"
            className="form-control"
            onChange={(e) => setSulphates(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label>Alcohol</label>
          <input
            type="text"
            className="form-control"
            onChange={(e) => setAlcohol(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label>Wine Type</label>
          <select
            className="form-control"
            onChange={(e) => setWineType(e.target.value)}
          >
            <option>Select Wine Type</option>
            <option>Red</option>
            <option>White</option>
          </select>
        </div>
      </form>
      <button className="btn btn-success" onClick={handleSubmit}>
        Submit
      </button>
    </div>
  );
}

export default App;
