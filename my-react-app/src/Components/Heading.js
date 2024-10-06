import React from "react";

const Heading = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-secondary" style={{ maxWidth: "100%", height: "40px" }}>
      <div className="container d-flex justify-content-center align-items-center">
        <span className="navbar-text">
          Test Suites for NIST Random numbers
        </span>
      </div>
    </nav>
  );
};

export default Heading;
