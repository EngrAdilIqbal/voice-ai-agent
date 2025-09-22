import React from "react";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Configs from "./pages/Configs";

export default function App() {
  return (
    <BrowserRouter>
      <div className="p-4">
        <nav className="mb-4">
          <Link className="mr-4 text-blue-600" to="/">Dashboard</Link>
          <Link className="text-blue-600" to="/configs">Configs</Link>
        </nav>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/configs" element={<Configs />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}
