import React, { useState, useEffect } from 'react';
import axios from 'axios';

//1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000
const Grid = ({binaryData}) => {
  // State to store the digit value
  const [digit, setDigit] = useState(1);
  const [isChecked, setIsChecked] = useState(false);
  const [runRandomExcursionsTestResponse, setrunRandomExcursionsTestResponse] = useState('');


  // useEffect(() => {
  //   const fetchrunRandomExcursionsTestData = async () => {
  //     try {
  //       const response = await axios.get(`http://localhost:8000/random_excursions_test/?binary_data=${binaryData}`);
  //       setrunRandomExcursionsTestResponse(response.data);
  //     } catch (error) {
  //       console.error('Error executing Random Excursions test:', error);
  //     }
  //   };
  //   fetchrunRandomExcursionsTestData();
  // }, [binaryData]);


  useEffect(() => {
    const fetchrunRandomExcursionsTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/random_excursions_test/', 
          { binary_data: binaryData }
        );
        setrunRandomExcursionsTestResponse(response.data);
      } catch (error) {
        console.error('Error executing Random Excursions test:', error);
      }
    };
  
    fetchrunRandomExcursionsTestData();
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
      gridTemplateRows: '1fr 1fr', 
      // position:'relative'
      marginTop:'268px'
    }}>
      {/* First row */}
      <div style={{ border: '1px solid black', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
       
        <div style={{ marginLeft: '5px', textAlign: 'center' }}>16. Random Excursion Test</div>
      </div>
      {/* Second row */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: '1fr 1fr 1fr 1fr', // Four columns in the second row
        border: '1px solid black', // black border
      }}>
        {['State', 'Chi^2', 'p-value', 'Result'].map((columnName, index) => (
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
          {/* <button onClick={() => handleButtonClick('decrement')}>-</button> */}
          <span style={{ border: '1px solid black', paddingLeft: '5px', paddingRight: '5px' }}>1</span>
          {/* <button onClick={() => handleButtonClick('increment')}>+</button> */}
        </div>
      );
    } else if (index === 1) {
      return (
        <div key={index} style={{ border: '1px solid black', textAlign: 'center',color:'red', }}>
           {runRandomExcursionsTestResponse ? runRandomExcursionsTestResponse['chi^2'] : ''}
        </div>
      );
    } else if (index === 2) {
      return (
        <div key={index} style={{ border: '1px solid black', textAlign: 'center',color:'red', }}>
          {runRandomExcursionsTestResponse ? runRandomExcursionsTestResponse.p_value : ''}
        </div>
      );
    } else if (index === 3) {
      return (
        <div key={index} style={{ border: '1px solid black', textAlign: 'center', color:'red',}}>
          {runRandomExcursionsTestResponse ? runRandomExcursionsTestResponse.result : ''}
        </div>
      );
    }
  })}
        
      </div>
    </div>
  );
}

export default Grid;
