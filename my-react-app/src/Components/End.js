import React, { useState , createContext } from 'react';
import { runFrequencyTest } from '../api_frequency_test'; // Import the API function
import { runFrequencyBlockTest } from '../api_frequency_test'; // Import the API function
import './GridContainerEnd.css'; // Import CSS file for styling
import {runTest} from '../api_runs_test';
import {runlongestOneBlockTest} from '../api_run_longest_one_block_test';
import {runApproximateEntropyTest} from '../api_approximate_entropy_test';
import {runLinearComplexityTest} from '../api_linear_complexity_test';
import {runNonOverlappingTest} from '../api_template_matching_test';
import {runOverlappingTest} from '../api_template_matching_test';
import {runUniversalTest} from '../api_universal_test';
import {runSerialTest} from '../api_serial_test';
import {runCumulativeSumsTest} from '../api_cumulative_sums_test';
import {runRandomExcursionsTest} from '../api_random_excursions_test';
import {runRandomExcursionsVariantTest} from '../api_random_excursions_test';
import {runBinaryMatrixRankTest} from '../api_binary_matrix_rank_text';
import {runSpectralTest} from '../api_spectral_test';
import Down from './down';
import { TestContext, TestContextProvider } from './TestContext';

const GridContainer = ({binaryDataString}) => {
  
  const [binaryDataFile, setBinaryDataFile] = useState(null);//
  const [checkedTests, setCheckedTests] = useState([]);
  // Function to handle button clicks
  const handleButtonClick = (buttonName) => {
    // Handle button click actions
    
    if (buttonName === 'Report generation') {
      
        // Optionally, you can then redirect the user or perform other actions
        window.location.href = 'http://localhost:8000/pdf-report/';
       
      
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
    <TestContextProvider value={{ checkedTests, setCheckedTests }}>
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
    </TestContextProvider>
    
  );
}

export default GridContainer;
