import React, { useState } from 'react';

const Navbar = () => {
  const [isCollapsed, setIsCollapsed] = useState(true); // State to track the collapse status

  const handleToggle = () => {
    setIsCollapsed(!isCollapsed); // Toggle the collapse state
  };

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <div className="container">
        <a className="navbar-brand" href="#">Test Suite</a>
        <button 
          className="navbar-toggler" 
          type="button" 
          onClick={handleToggle} // Handle toggle click
          aria-controls="navbarNav" 
          aria-expanded={!isCollapsed} 
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className={`collapse navbar-collapse ${isCollapsed ? '' : 'show'}`} id="navbarNav">
          <ul className="navbar-nav ml-auto">
            <li className="nav-item">
              <a className="nav-link" href="/">NIST Statistical Tests</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="/dieharder_test">DieHarder Tests</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
