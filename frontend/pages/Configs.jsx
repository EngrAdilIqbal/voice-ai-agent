import React, { useEffect, useState } from "react";
import axios from "../api/axios";

export default function Configs() {
  const [configs, setConfigs] = useState([]);

  useEffect(() => {
    axios.get("/configs")
      .then(res => setConfigs(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Agent Configs</h2>
      <ul className="space-y-3">
        {configs.map(cfg => (
          <li key={cfg.id} className="p-4 border rounded shadow-sm">
            <h3 className="font-semibold">{cfg.name}</h3>
            <p>{cfg.description}</p>
            <pre className="bg-gray-100 p-2 mt-2 rounded text-sm overflow-auto">
              {JSON.stringify(cfg.prompt, null, 2)}
            </pre>
          </li>
        ))}
      </ul>
    </div>
  );
}
