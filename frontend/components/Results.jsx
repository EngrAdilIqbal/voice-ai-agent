import React from "react";

export default function Results({ result }) {
  if (!result) return null;

  return (
    <div className="mt-4 p-4 border rounded shadow">
      <h2 className="text-xl font-semibold mb-2">Call Summary</h2>
      <pre className="bg-gray-100 p-2 rounded overflow-auto">
        {JSON.stringify(result, null, 2)}
      </pre>
    </div>
  );
}
