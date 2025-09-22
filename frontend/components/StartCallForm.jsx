import React, { useState, useEffect } from "react";
import axios from "../api/axios";

export default function StartCallForm({ setCallResult }) {
  const [driverName, setDriverName] = useState("");
  const [driverPhone, setDriverPhone] = useState("");
  const [loadNumber, setLoadNumber] = useState("");
  const [configs, setConfigs] = useState([]);
  const [selectedConfig, setSelectedConfig] = useState("");

  useEffect(() => {
    axios.get("/configs").then(res => setConfigs(res.data));
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("/start_call", {
        driver_name: driverName,
        driver_phone: driverPhone,
        load_number: loadNumber,
        config_id: selectedConfig,
      });
      setCallResult(res.data);
    } catch (err) {
      console.error(err);
      setCallResult({ error: err.response?.data || "Call failed" });
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-3 mb-4">
      <div>
        <label>Driver Name:</label>
        <input className="border p-1 ml-2" value={driverName} onChange={e => setDriverName(e.target.value)} required />
      </div>
      <div>
        <label>Driver Phone:</label>
        <input className="border p-1 ml-2" value={driverPhone} onChange={e => setDriverPhone(e.target.value)} required />
      </div>
      <div>
        <label>Load Number:</label>
        <input className="border p-1 ml-2" value={loadNumber} onChange={e => setLoadNumber(e.target.value)} required />
      </div>
      <div>
        <label>Config:</label>
        <select className="border p-1 ml-2" value={selectedConfig} onChange={e => setSelectedConfig(e.target.value)} required>
          <option value="">Select Config</option>
          {configs.map(cfg => <option key={cfg.id} value={cfg.id}>{cfg.name}</option>)}
        </select>
      </div>
      <button type="submit" className="bg-blue-600 text-white px-3 py-1 rounded">Start Call</button>
    </form>
  );
}
