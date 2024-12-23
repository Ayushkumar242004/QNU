import './GridContainerUp.css'; // Import CSS file for styling
import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import End from "./End";
const MAX_STACK_SIZE_ESTIMATE = 1 * 1024 * 1024 ;
const DieharderTest = ({ getData, onBinaryDataChange }) => {
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


  // extra functions for new tests
  /////////////////////////////////////
  const [frequencyTestChecked, setFrequencyTestChecked] = useState(false);

  const [runBinarySpacingsTestResponse, setrunBinarySpacingsTestResponse] = useState("");
  const [runParkingLotTestResponse, setrunParkingLotTestResponse] = useState("");
  const [runOverlapping5PermutationTestResponse, setrunOverlapping5PermutationTestResponse] = useState("");
  const [runMinimumDistanceTestResponse, setrunMinimumDistanceTestResponse] = useState("");
  const [run31MatrixTestResponse, setrun31MatrixTestResponse] = useState("");
  const [runSpeheresTestResponse, setrunSpeheresTestResponse] = useState("");
  const [run32MatrixTestResponse, setrun32MatrixTestResponse] = useState("");
  const [runCrapsTestResponse, setrunCrapsTestResponse] = useState("");
  const [runBitstreamTestResponse, setrunBitstreamTestResponse] = useState("");
  const [rungcdTestResponse, setrungcdTestResponse] = useState("");
  const [runopsoTestResponse, setrunopsoTestResponse] = useState("");
  const [runoqsoTestResponse, setrunoqsoTestResponse] = useState("");
  const [rundnaTestResponse, setrundnaTestResponse] = useState("");
  const [runoneStreamTestResponse, setrunoneStreamTestResponse] = useState("");
  const [runoneByteTestResponse, setrunoneByteTestResponse] = useState("");
  const [rungcdSimpleTestResponse, setrungcdSimpleTestResponse] = useState("");
  const [rungeneralisedMinimumTestResponse, setrungeneralisedMinimumTestResponse] = useState("");
  const [runu01LinearComplexityTestResponse, setrunu01LinearComplexityTestResponse] = useState("");
  const [runu01LongestSubstringTestResponse, setrunu01LongestSubstringTestResponse] = useState("");
  const [runmatrixRankTestResponse, setrunmatrixRankTestResponse] = useState("");

  // Function to handle checkbox change
  const handleFrequencyTestCheckboxChange = () => {
    setFrequencyTestChecked(!frequencyTestChecked);
  };

  // useEffect(() => {
  //   const runBinarySpacingsTestData = async () => {
  //     try {
  //       const response = await axios.get(
  //         `http://localhost:8000/run_binary_spacings_test/?binary_data=${initialInputData}`
  //       );
  //       setrunBinarySpacingsTestResponse(response.data);
  //     } catch (error) {
  //       console.error("Error executing frequency test:", error);
  //     }
  //   };

  //   runBinarySpacingsTestData();
  // }, [initialInputData]);

  useEffect(() => {
    const runBinarySpacingsTestData = async () => {
      try {
        console.log(initialInputData)
        const response = await axios.post(
          'http://localhost:8000/run_binary_spacings_test/', // POST endpoint
          { binary_data: initialInputData } // JSON payload
        );
        console.log("hi hello spacing test", response);
        setrunBinarySpacingsTestResponse(response.data); // Update response state
      } catch (error) {
        console.error("Error executing binary spacings test:", error);
      }
    };
  
    runBinarySpacingsTestData();
  }, [initialInputData]); // Dependency array
  

  useEffect(() => {
    const runParkingLotTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_parking_lot_test/', // The POST endpoint
          { binary_data: initialInputData } // Data sent in the POST request body
        );
        setrunParkingLotTestResponse(response.data);
      } catch (error) {
        console.error("Error executing parking lot test:", error);
      }
    };
  
    if (initialInputData) {
      runParkingLotTestData();
    }
  }, [initialInputData]);
  

  useEffect(() => {
    const runOverlapping5PermutationTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_overlapping_5_test/',
          { binary_data: initialInputData }
        );
        setrunOverlapping5PermutationTestResponse(response.data);
      } catch (error) {
        console.error("Error executing overlapping 5 test:", error);
      }
    };

    if (initialInputData){
    runOverlapping5PermutationTestData();
    }
  }, [initialInputData]);

  useEffect(() => {
    const runMinimumDistanceTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_minimum_distance_test/',
          { binary_data: initialInputData }
        );
        setrunMinimumDistanceTestResponse(response.data);
      } catch (error) {
        console.error("Error executing minimum distance test:", error);
      }
    };

    runMinimumDistanceTestData();
  }, [initialInputData]);

  useEffect(() => {
    const run31MatrixTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_31matrix_test/',
          { binary_data: initialInputData }
        );
        setrun31MatrixTestResponse(response.data);
      } catch (error) {
        console.error("Error executing 31 matrix test:", error);
      }
    };

    run31MatrixTestData();
  }, [initialInputData]);

  useEffect(() => {
    const runSpheresTestData = async () => {
      try {
        const response = await axios.post(
        'http://localhost:8000/run_spheres_test/',
        { binary_data: initialInputData }
        );
        setrunSpeheresTestResponse(response.data);
      } catch (error) {
        console.error("Error executing spheres test:", error);
      }
    };

    runSpheresTestData();
  }, [initialInputData]);



  useEffect(() => {
    const run32MatrixTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_32matrix_test/',
          { binary_data: initialInputData }
        );
        setrun32MatrixTestResponse(response.data);
      } catch (error) {
        console.error("Error executing 32 matrix test:", error);
      }
    };

    run32MatrixTestData();
  }, [initialInputData]);

  useEffect(() => {
    const runCrapsTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_craps_test/',
          { binary_data: initialInputData }
        );
        setrunCrapsTestResponse(response.data);
      } catch (error) {
        console.error("Error executing craps test:", error);
      }
    };

    runCrapsTestData();
  }, [initialInputData]);




  useEffect(() => {
    const runBitstreamTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_bitstream_test/',
          { binary_data: initialInputData }
        );
        setrunBitstreamTestResponse(response.data);
      } catch (error) {
        console.error("Error executing bitstream test:", error);
      }
    };

    runBitstreamTestData();
  }, [initialInputData]);



  useEffect(() => {
    const rungcdTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_gcd_test/',
          { binary_data: initialInputData }
        );
        setrungcdTestResponse(response.data);
      } catch (error) {
        console.error("Error executing gcd test:", error);
      }
    };

    rungcdTestData();
  }, [initialInputData]);



  useEffect(() => {
    const runopsoTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_opso_test/',
          { binary_data: initialInputData }
        );
        setrunopsoTestResponse(response.data);
      } catch (error) {
        console.error("Error executing opso test:", error);
      }
    };

    runopsoTestData();
  }, [initialInputData]);

  useEffect(() => {
    const runoqsoTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_oqso_test/',
          { binary_data: initialInputData }
        );
        setrunoqsoTestResponse(response.data);
      } catch (error) {
        console.error("Error executing oqso test:", error);
      }
    };

    runoqsoTestData();
  }, [initialInputData]);

  useEffect(() => {
    const runoneStreamTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_count_one_test/',
          { binary_data: initialInputData }
        );
        setrunoneStreamTestResponse(response.data);
      } catch (error) {
        console.error("Error executing one stream test:", error);
      }
    };

    runoneStreamTestData();
  }, [initialInputData]);


  useEffect(() => {
    const rundnaTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_dna_test/',
          { binary_data: initialInputData }
        );
        setrundnaTestResponse(response.data);
      } catch (error) {
        console.error("Error executing dna test:", error);
      }
    };

    rundnaTestData();
  }, [initialInputData]);



  useEffect(() => {
    const runoneByteTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_count_one_byte_test/',
          { binary_data: initialInputData }
        );
        setrunoneByteTestResponse(response.data);
      } catch (error) {
        console.error("Error executing one byte test:", error);
      }
    };

    runoneByteTestData();
  }, [initialInputData]);



  useEffect(() => {
    const rungcdSimpleTestData = async () => {
      try {
        const response = await axios.post(
        'http://localhost:8000/run_simple_gcd_test/',
        { binary_data: initialInputData }
        );
        setrungcdSimpleTestResponse(response.data);
      } catch (error) {
        console.error("Error executing gcd simple test:", error);
      }
    };

    rungcdSimpleTestData();
  }, [initialInputData]);



  useEffect(() => {
    const rungeneralisedMinimumDistanceTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_general_minimum_distance_test/',
          { binary_data: initialInputData }
        );
        setrungeneralisedMinimumTestResponse(response.data);
      } catch (error) {
        console.error("Error executing generalised minimum test:", error);
      }
    };

    rungeneralisedMinimumDistanceTestData();
  }, [initialInputData]);



  useEffect(() => {
    const runu01LinearComplexityTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_u01_linear_complexity_test/',
          { binary_data: initialInputData }
        );
        setrunu01LinearComplexityTestResponse(response.data);
      } catch (error) {
        console.error("Error executing linear complexity test:", error);
      }
    };

    runu01LinearComplexityTestData();
  }, [initialInputData]);




  useEffect(() => {
    const runu01LongestSubstringTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_u01_longest_repeated_substring_test/',
          { binary_data: initialInputData }
        );
        setrunu01LongestSubstringTestResponse(response.data);
      } catch (error) {
        console.error("Error executing longest substring test:", error);
      }
    };

    runu01LongestSubstringTestData();
  }, [initialInputData]);




  useEffect(() => {
    const runmatrixRankTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_matrix_rank_test/',
          { binary_data: initialInputData }
        );
        setrunmatrixRankTestResponse(response.data);
      } catch (error) {
        console.error("Error executing matrix rank test:", error);
      }
    };

    runmatrixRankTestData();
  }, [initialInputData]);

  const handleButtonClickGraph = (buttonName) => {
    // Handle button click actions
    
    // if (buttonName === 'Report generation') {
      
    //    window.open(`http://localhost:8000/pdf-report-dieharder/?binary_data=${encodeURIComponent(initialInputData[0])}`, '_blank');
      
    // }

    if (buttonName === 'Report generation') {
      const binaryData = initialInputData[0]; // Get the binary data
  
      // Send a POST request with binary data
      fetch('http://localhost:8000/pdf-report-dieharder/', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ binary_data: binaryData }), // Send the binary data as JSON
      })
      .then(response => response.blob())  // Get the response as a Blob (binary data)
      .then(blob => {
          // Create a URL for the Blob object (this will represent the PDF file)
          const pdfUrl = URL.createObjectURL(blob);
  
          // Open the PDF in a new tab
          window.open(pdfUrl, '_blank');
      })
      .catch(error => {
          console.error('Error generating report:', error);
      });
  }
    // else if (buttonName === 'Graph generation') {
    //     console.log("hi my binary data is: ",initialInputData[0])
     
    //     window.open(`http://localhost:8000/graph-generaion-dieharder/?binary_data=${encodeURIComponent(initialInputData[0])}`, '_blank');
    // }

    else if (buttonName === 'Graph generation') {
      const binaryData = initialInputData[0]; // Use actual binary data
  
      // Send a POST request with binary data
      fetch('http://localhost:8000/graph-generaion-dieharder/', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ binary_data: binaryData }),
      })
      .then(response => response.blob())  // Get the image data as a Blob
      .then(blob => {
          // Create a URL for the Blob object
          const imageUrl = URL.createObjectURL(blob);
  
          // Open the image URL in a new tab
          window.open(imageUrl, '_blank');
      })
      .catch(error => {
          console.error('Error generating graph:', error);
      });
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
    <div>

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

    


        <div
          style={{
            display: "grid",
            gridTemplateColumns: "20% 20% auto 20% 20%  auto", // 6 columns of equal width
            gridTemplateRows: "repeat(12, 100px)", // 10 rows of equal height (added one extra row)
            width: "100%", // Set width to 100%
            
          }}
        >
          {/* Row with "Randomness testing" */}
          <div
            style={{
              gridColumn: "1 / -1", // Span the entire grid width
              gridRow: "1", // First row
              background: "black",
              color: "white",
              
              textAlign: "center",
              
            }}
          >
            <div style={{ marginTop:'37px'}}>

              Randomness testing
            </div>
          </div>

          {/* Header cells for Test type, p-value, and Result */}
          <div
                        style={{
                            textAlign: "center",
                            border: "1px solid black",
                            color: "white",
                            backgroundColor: "blue",
                            
                        }}
                    >
                        <div style={{marginTop:'37px'}}>
                            Test Type
                        </div>
                    </div>
                    <div
                        style={{
                            textAlign: "center",
                            border: "1px solid black",
                            color: "white",
                            backgroundColor: "blue",
                        }}
                    >
                        <div style={{marginTop:'37px'}}>
                           p-value
                        </div>
                    </div>
                    <div
                        style={{
                            textAlign: "center",
                            border: "1px solid black",
                            color: "white",
                            backgroundColor: "blue",
                        }}
                    >
                        <div style={{marginTop:'37px'}}>
                           Result
                        </div>
                    </div>
                    <div
                        style={{
                            textAlign: "center",
                            border: "1px solid black",
                            color: "white",
                            backgroundColor: "blue",
                        }}
                    >
                        <div style={{marginTop:'37px'}}>
                            Test Type
                        </div>
                    </div>
                    <div
                        style={{
                            textAlign: "center",
                            border: "1px solid black",
                            color: "white",
                            backgroundColor: "blue",
                        }}
                    >
                        <div style={{marginTop:'37px'}}>
                           p-value
                        </div>
                    </div>
                    <div
                        style={{
                            textAlign: "center",
                            border: "1px solid black",
                            color: "white",
                            backgroundColor: "blue",
                        }}
                    >
                        <div style={{marginTop:'37px'}}>
                           Result
                        </div>
                    </div>


          {/* Content for the remaining grid cells */}
          {Array.from({ length: 60 }).map((_, index) => {
            if (index === 0) {
              // Check if it's the cell below "Test type"
              return (
                <div
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >

                  <div
                    style={{
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                    }}
                  >
                    <span style={{}}>1. Birthday Spacings Test                </span>
                  </div>
                </div>
              );
            } else if (index === 6) {
              // Check if it's the cell below "Test type"
              return (
                <div
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >

                  <div
                    style={{
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                    }}
                  >
                    3. Overlapping 5-Permutation Test

                  </div>
                </div>
              );
            } else if (index === 12) {
              // Check if it's the cell below "Test type"
              return (
                <div
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >

                  <div
                    style={{
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                    }}
                  >
                    5. Ranks of 31x31 Matrices Test
                  </div>
                </div>
              );
            } else if (index === 18) {
              // Check if it's the cell below "Test type"
              return (
                <div
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >

                  <div
                    style={{
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                    }}
                  >
                    7. Ranks of 32x32 Matrices Test
                  </div>
                </div>
              );
            } else if (index === 24) {
              // Check if it's the cell below "Test type"
              return (
                <div
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >

                  <div
                    style={{
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                    }}
                  >
                    9. Bitstream Test

                  </div>
                </div>
              );
            } else if (index === 30) {
              // Check if it's the cell below "Test type"
              return (
                <div
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >

                  <div
                    style={{
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                    }}
                  >
                    11. Overlapping-Pairs-Sparse-Occupancy (OPSO) Test

                  </div>
                </div>
              );
            } else if (index === 33) {
              // Check if it's the cell below "Test type"
              return (
                <div
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >

                  <div
                    style={{
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                    }}
                  >
                    12. Overlapping-Quadruples-Sparse-Occupancy (OQSO) Test

                  </div>
                </div>
              );
            } else if (index === 36) {
              // Check if it's the cell below "Test type"
              return (
                <div
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >

                  <div
                    style={{
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                    }}
                  >
                    13. DNA Test

                  </div>
                </div>
              );
            }
            else if (index === 39) {
              // Check if it's the cell below "Test type"
              return (
                <div
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >

                  <div
                    style={{
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                    }}
                  >
                    14. Count-the-1s (stream) Test

                  </div>
                </div>
              );
            }
            else if (index === 42) {
              // Check if it's the cell below "Test type"
              return (
                <div
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >

                  <div
                    style={{
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                    }}
                  >
                    15. Count-the-1s (byte) Test

                  </div>
                </div>
              );
            }
            else if (index === 3) {
              // Check if it's the cell below "Test type"
              return (
                <div
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >

                  <div
                    style={{
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                    }}
                  >
                    2. Parking Lot Test
                  </div>
                </div>
              );
            } else if (index === 9) {
              // Check if it's the cell below "Test type"
              return (
                <div
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >

                  <div
                    style={{
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                    }}
                  >
                    4. Minimum Distance Test
                  </div>
                </div>
              );
            } else if (index === 15) {
              // Check if it's the cell below "Test type"
              return (
                <div
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >

                  <div
                    style={{
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                    }}
                  >
                    6. 3d Spheres Test

                  </div>
                </div>
              );
            } else if (index === 21) {
              // Check if it's the cell below "Test type"
              return (
                <div
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >

                  <div
                    style={{
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                    }}
                  >
                    8. Craps Test
                  </div>
                </div>
              );
            } else if (index === 27) {
              // Check if it's the cell below "Test type"
              return (
                <div
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >

                  <div
                    style={{
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                    }}
                  >
                    10. Marsaglia-Tsang GCD Test

                  </div>
                </div>
              );
            }
            else if (index === 45) {
              // Check if it's the cell below "Test type"
              return (
                <div
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >

                  <div
                    style={{
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                    }}
                  >
                    16. Marsaglia-Tsang Simple GCD Test


                  </div>
                </div>
              );
            }

            else if (index === 48) {
              // Check if it's the cell below "Test type"
              return (
                <div
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >

                  <div
                    style={{
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                    }}
                  >
                    17. Generalized Minimum Distance Test


                  </div>
                </div>
              );
            }
            else if (index === 51) {
              // Check if it's the cell below "Test type"
              return (
                <div
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    
                  }}
                >

                  <div
                    style={{
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                    }}
                  >
                    18. TestU01 Linear Complexity Test



                  </div>
                </div>
              );
            }
            else if (index === 54) {
              // Check if it's the cell below "Test type"
              return (
                <div
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    
                  }}
                >

                  <div
                    style={{
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                    }}
                  >
                    19. TestU01 Longest Repeated Substring Test


                  </div>
                </div>
              );
            }
            else if (index === 57) {
              // Check if it's the cell below "Test type"
              return (
                <div
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",

                  }}
                >

                  <div
                    style={{
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                    }}
                  >
                    20. TestU01 Matrix Rank Test


                  </div>
                </div>
              );
            }

            else if (index === 33 || index === 39) {
              return <div key={index} style={{ border: "1px solid black" }}></div>;
            } else if (index === 1) {
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runBinarySpacingsTestResponse.p_value}
                    </span>
                  </div>
                </div>
              );
            } else if (index === 2) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runBinarySpacingsTestResponse.result}
                    </span>
                  </div>
                </div>
              );
            } else if (index === 4) {
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runParkingLotTestResponse.p_value}
                    </span>
                  </div>
                </div>
              );
            } else if (index === 5) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runParkingLotTestResponse.result}
                    </span>
                  </div>
                </div>
              );
            } else if (index === 7) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>{runOverlapping5PermutationTestResponse.p_value}</span>
                  </div>
                </div>
              );
            } else if (index === 8) {
              
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>{runOverlapping5PermutationTestResponse.result}</span>
                  </div>
                </div>
              );
            } else if (index === 10) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runMinimumDistanceTestResponse.p_value}
                    </span>
                  </div>
                </div>
              );
            } else if (index === 11) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runMinimumDistanceTestResponse.result}
                    </span>
                  </div>
                </div>
              );
            } else if (index === 13) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {run31MatrixTestResponse.p_value}
                    </span>
                  </div>
                </div>
              );
            } else if (index === 14) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {run31MatrixTestResponse.result}
                    </span>
                  </div>
                </div>
              );
            } else if (index === 16) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runSpeheresTestResponse.p_value}
                    </span>
                  </div>
                </div>
              );
            } else if (index === 17) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runSpeheresTestResponse.result}
                    </span>
                  </div>
                </div>
              );
            } else if (index === 28) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {rungcdTestResponse.p_value}
                    </span>
                  </div>
                </div>
              );
            } else if (index === 29) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {rungcdTestResponse.result}
                    </span>
                  </div>
                </div>
              );
            } else if (index === 34) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runoqsoTestResponse.p_value}
                    </span>
                  </div>
                </div>
              );
            } else if (index === 35) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runoqsoTestResponse.result}
                    </span>
                  </div>
                </div>
              );
            }
            //runNonOverlappingTest
            else if (index === 19) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {run32MatrixTestResponse.p_value}
                    </span>
                  </div>
                </div>
              );
            } else if (index === 20) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {run32MatrixTestResponse.result}
                    </span>
                  </div>
                </div>
              );
            } else if (index === 22) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runCrapsTestResponse.p_value}
                    </span>
                  </div>
                </div>
              );
            } else if (index === 23) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runCrapsTestResponse.result}
                    </span>
                  </div>
                </div>
              );
            } else if (index === 25) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runBitstreamTestResponse.p_value}
                    </span>
                  </div>
                </div>
              );
            } else if (index === 26) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runBitstreamTestResponse.result}
                    </span>
                  </div>
                </div>
              );
            } else if (index === 31) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runopsoTestResponse.p_value}
                    </span>
                  </div>
                </div>
              );
            } else if (index === 32) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runopsoTestResponse.result}
                    </span>
                  </div>
                </div>
              );
            } else if (index === 37) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {rundnaTestResponse.p_value}
                    </span>
                  </div>
                </div>
              );
            } else if (index === 38) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {rundnaTestResponse.result}
                    </span>
                  </div>
                </div>
              );
            }

            else if (index === 40) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runoneStreamTestResponse.p_value}
                    </span>
                  </div>
                </div>
              );
            }

            else if (index === 41) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runoneStreamTestResponse.result}
                    </span>
                  </div>
                </div>
              );
            }

            else if (index === 43) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runoneByteTestResponse.p_value}
                    </span>
                  </div>
                </div>
              );
            }

            else if (index === 44) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runoneByteTestResponse.result}
                    </span>
                  </div>
                </div>
              );
            }


            else if (index === 46) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {rungcdSimpleTestResponse.p_value}
                    </span>
                  </div>
                </div>
              );
            }


            else if (index === 47) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {rungcdSimpleTestResponse.result}
                    </span>
                  </div>
                </div>
              );
            }



            else if (index === 49) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {rungeneralisedMinimumTestResponse.p_value}
                    </span>
                  </div>
                </div>
              );
            }

            else if (index === 50) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {rungeneralisedMinimumTestResponse.result}
                    </span>
                  </div>
                </div>
              );
            }



            else if (index === 52) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runu01LinearComplexityTestResponse.p_value}
                    </span>
                  </div>
                </div>
              );
            }


            else if (index === 53) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runu01LinearComplexityTestResponse.result}
                    </span>
                  </div>
                </div>
              );
            }



            else if (index === 55) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runu01LongestSubstringTestResponse.p_value}
                    </span>
                  </div>
                </div>
              );
            }

            else if (index === 56) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runu01LongestSubstringTestResponse.result}
                    </span>
                  </div>
                </div>
              );
            }

            else if (index === 58) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runmatrixRankTestResponse.p_value}
                    </span>
                  </div>
                </div>
              );
            }

            else if (index === 59) {
              // Check if it's the cell below "Result"
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}>
                      {runmatrixRankTestResponse.result}
                    </span>
                  </div>
                </div>
              );
            }
            {
              return (
                <div
                  key={index}
                  style={{
                    border: "1px solid black",
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  <div
                    style={{ width: "100%", height: "20px", textAlign: "center" }}
                  >
                    <span style={{ color: "red" }}></span>
                  </div>
                </div>
              );
            }
          })}
        </div>


      </div>

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

export default DieharderTest;
