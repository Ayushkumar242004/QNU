import React, { useState, useRef } from 'react';
import './GridContainerUp.css'; // Import CSS file for styling
import RandomTest from './RandomTest';
import RandomVariantTest from './RandomVariantTest';
import Down from './down';

const MAX_STACK_SIZE_ESTIMATE = 1 * 1024 * 1024;
const GridContainer1 = ({ getData, onBinaryDataChange }) => {
  const [initialInputData, setInitialInputData] = useState(['', '', '']); // Initialize with 3 empty strings
  const fileInputRefs = useRef([null, null, null]);

  const handleInputChange = (index, value) => {
    const newData = [...initialInputData]; // Create a copy of the current state
    newData[index] = value; // Update the value at the specified index
    setInitialInputData(newData); // Update the state
    // Pass the binary data to the parent component
    if (onBinaryDataChange && index === 0) {
      onBinaryDataChange(value);
      getData(value);
    }
  };

  const handleButtonClick = (index) => {
    // Trigger click on the respective file input
    if (index === 1 || index === 2) {
      fileInputRefs.current[index].click();
    }
  };



  const handleFileInputChange = (event, index) => {
    const selectedFile = event.target.files[0];
    if (selectedFile.size > MAX_STACK_SIZE_ESTIMATE) {
      alert('Warning: The selected file is too large. Please choose a smaller file.');
      return;
    }
  
    const reader = new FileReader();
    reader.onload = (e) => {
      const binaryData = e.target.result; // ArrayBuffer
      const byteArray = new Uint8Array(binaryData); // Convert ArrayBuffer to Uint8Array
      
      const decoder = new TextDecoder(); // Create a TextDecoder to interpret the data
      const textData = decoder.decode(byteArray).trim(); // Convert Uint8Array to string
  
      console.log(textData); // Logs "100" (or whatever the content of the file is)
  
      
      
      handleInputChange(0, textData); // Update input value with the binary data
    };
    reader.readAsArrayBuffer(selectedFile);
  };


  const handleButtonClickGraph = (buttonName) => {
    // Handle button click actions
    
    if (buttonName === 'Report generation') {
      
        // Optionally, you can then redirect the user or perform other actions
        window.location.href = `http://localhost:8000/pdf-report/?binary_data=${encodeURIComponent(initialInputData[0])}`;
       
      
    }
    else if (buttonName === 'Graph generation') {
      // Example binary data
    //   const binaryData = '1101010101010101'; // Replace with actual binary data
      
      // Redirect with binary data as query parameter
      console.log("hi my binary data is: ",initialInputData[0])
      window.location.href = `http://localhost:8000/graph-generation/?binary_data=${encodeURIComponent(initialInputData[0])}`;
    }
    
   
  };

  // Define button names
  const buttonNamesGraph = [
    
    // 'Execute Test',
    // 'Reset',
    // 'Exit Program'
    'Graph generation',
    'Report generation'
  ];
  


  return (
    <div className="grid-container">
      {/* Input Data in the first row */}
      <div className="header">Input Data</div>

      {/* Content for the remaining grid cells */}
      {initialInputData.map((value, index) => (
        <div key={index + 1} className="input-row">
          <div className="label">
            {index === 0 ? 'Binary data ' : index === 1 ? 'Binary data file' : 'Binary string file'}
          </div>
          <input
            type="string"
            value={index === 0 ? value : String.fromCharCode.apply(null, new Uint8Array(value))}
            onChange={(e) => handleInputChange(0, e.target.value)}
            className="text-input"
            placeholder={index === 0 ? 'Enter data here' : ''}
            disabled={index !== 0}
          />
          {/* Add file input */}
          {index === 1 && (
            <input
              type="file"
              ref={(el) => fileInputRefs.current[index] = el}
              style={{ display: 'none' }}
              onChange={(e) => handleFileInputChange(e, index)}
            />
          )}
          {/* Add buttons adjacent to the input boxes */}
          {index === 1 && (
            <button className="select-btn" onClick={() => handleButtonClick(index)}>Select binary data file</button>
          )}
          {index === 2 && (
            <input
              type="file"
              ref={(el) => fileInputRefs.current[index] = el}
              style={{ display: 'none' }}
              onChange={(e) => handleFileInputChange(e, index)}
            />
          )}
          {index === 2 && (
            <button className="select-btn" onClick={() => handleButtonClick(index)}>Select string data file</button>
          )}
        </div>
      ))}
      
     
      { <Down binaryData={initialInputData[0]} />}
      { <RandomTest binaryData={initialInputData[0]} />}
      { <RandomVariantTest binaryData={initialInputData[0]} />}

      <div className="button-container">
        {buttonNamesGraph.map((name, index) => (
          <button
            key={index}
            className="action-btn"
            onClick={() => handleButtonClickGraph(name)}
          >
            {name}
          </button>
        ))}
      </div>
    </div>
  );
}

export default GridContainer1;
