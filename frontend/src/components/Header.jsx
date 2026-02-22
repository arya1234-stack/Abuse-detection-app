import React from "react";

export default function Header() {
  return (
    <div style={{ textAlign: "center", marginBottom: 10 }}>
      <h1
        style={{
          fontSize: "3rem",
          color: "#f83838ff",
          margin: 0,
          letterSpacing: "0.5px",
        }}
      >
        Social Media Abuse & Toxicity Detection with AI
      </h1>

      <p
        style={{
          marginTop: 6,
          color: "#e5e7eb",
          fontSize: "1rem",
          opacity: 0.9,
        }}
      >
        Real-time Abuse Detection • Sentiment • Toxicity Analytics
      </p>
    </div>
  );
}
