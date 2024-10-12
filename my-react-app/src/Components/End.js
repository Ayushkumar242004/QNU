import React, { useState , createContext } from 'react';
import './GridContainerEnd.css'; // Import CSS file for styling


const GridContainer = ({binaryDataString}) => {
  

  // Function to handle button clicks
  const handleButtonClick = (buttonName) => {
    // Handle button click actions
    
    if (buttonName === 'Report generation') {
      
        // Optionally, you can then redirect the user or perform other actions
        window.location.href = 'http://localhost:8000/pdf-report/?binary_data=${encodeURIComponent(binaryData)}';
       
      
    }
    else if (buttonName === 'Graph generation') {
      // Example binary data
      const binaryData = '1101010101010101'; // Replace with actual binary data
      
      // Redirect with binary data as query parameter
      window.location.href = `http://localhost:8000/graph-generation/?binary_data=${encodeURIComponent(binaryData)}`;
    }
    
   
  };

  // Define button names
  const buttonNames = [
    
    // 'Execute Test',
    // 'Reset',
    // 'Exit Program'
    'Graph generation',
    'Report generation'
  ];

  return (
    
    <div>
      {/* Render buttons */}
      
      <div className="button-container">
        {buttonNames.map((name, index) => (
          <button
            key={index}
            className="action-btn"
            onClick={() => handleButtonClick(name)}
          >
            {name}
          </button>
        ))}
      </div>

      
    </div>
 
    
  );
}

export default GridContainer;
