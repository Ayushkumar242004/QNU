import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Grid = ({ binaryData }) => {
  // State to store the digit value
  const [digit, setDigit] = useState(1);
  const [isChecked, setIsChecked] = useState(false);
  const [runRandomExcursionsVariantTestResponse, setrunRandomExcursionsVariantTestResponse] = useState('');


  useEffect(() => {
    const fetchrunRandomExcursionsVariantTestData = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/random_excursions_variant_test/?binary_data=${binaryData}`);
        setrunRandomExcursionsVariantTestResponse(response.data);
      } catch (error) {
        console.error('Error executing Random Excursions test:', error);
      }
    };
    fetchrunRandomExcursionsVariantTestData();
  }, [binaryData]);

  // Function to handle incrementing or decrementing the digit value
  const handleButtonClick = (operation) => {
    if (operation === 'increment') {
      setDigit(digit + 1);
    } else if (operation === 'decrement' && digit > 1) {
      setDigit(digit - 1);
    }
  };

  // Function to handle checkbox change
  const handleCheckboxChange = () => {
    setIsChecked(!isChecked);
  };

  return (
    <div style={{
      display: 'grid',
      gridTemplateColumns: '1fr', // One column in the first row
      gridTemplateRows: '1fr 1fr', // Two rows, first row with one row, second and third rows with four columns each
      // black border
    }}>
      {/* First row */}
      <div style={{ border: '1px solid black', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>

        <div style={{ marginLeft: '5px', textAlign: 'center' }}>17. Random Excursion Variant Test</div>
      </div>
      {/* Second row */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: '1fr 1fr 1fr 1fr', // Four columns in the second row
        border: '1px solid black', // black border
      }}>
        {['State', 'Count', 'p-value', 'Result'].map((columnName, index) => (
          <div key={`column-${index}`} style={{ border: '1px solid black', textAlign: 'center', background: 'blue', color: 'white' }}>
            {columnName}
          </div>
        ))}
      </div>
      {/* Third row */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: '1fr 1fr 1fr 1fr', // Four columns in the third row
        border: '1px solid black', // black border
      }}>
        {['Digit', 'Chi^2', 'p-value', 'Result'].map((columnName, index) => {
          if (index === 0) {
            return (
              <div key={index} style={{ border: '1px solid black', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
                <button onClick={() => handleButtonClick('decrement')}>-</button>
                <span style={{ border: '1px solid black', paddingLeft: '5px', paddingRight: '5px' }}>{digit}</span>
                <button onClick={() => handleButtonClick('increment')}>+</button>
              </div>
            );
          } else if (index === 1) {
            return (
              <div key={index} style={{ border: '1px solid black', textAlign: 'center', color: 'red', }}>
                {runRandomExcursionsVariantTestResponse ? runRandomExcursionsVariantTestResponse['chi^2'] : ''}
              </div>
            );
          } else if (index === 2) {
            return (
              <div key={index} style={{ border: '1px solid black', textAlign: 'center', color: 'red', }}>
                {runRandomExcursionsVariantTestResponse ? runRandomExcursionsVariantTestResponse.p_value : ''}
              </div>
            );
          } else if (index === 3) {
            return (
              <div key={index} style={{ border: '1px solid black', textAlign: 'center', color: 'red', }}>
                {runRandomExcursionsVariantTestResponse ? runRandomExcursionsVariantTestResponse.result : ''}
              </div>
            );
          }
        })}

        <div style={{ border: '1px solid black' }}></div>
        <div style={{ border: '1px solid black' }}></div>
        <div style={{ border: '1px solid black' }}></div>
        <div style={{ border: '1px solid black' }}></div>
      </div>
    </div>
  );
}

export default Grid;
