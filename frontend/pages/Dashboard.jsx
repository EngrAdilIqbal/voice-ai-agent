import React, { useState } from "react";
import StartCallForm from "../components/StartCallForm";
import Results from "../components/Results";

export default function Dashboard() {
  const [callResult, setCallResult] = useState(null);

  return (
    <div>
      <h1 className="text-3xl font-bold mb-4">AI Voice Agent Dashboard</h1>
      <StartCallForm setCallResult={setCallResult} />
      {callResult && <Results result={callResult} />}
    </div>
  );
}
