import './GridContainerUp.css'; // Import CSS file for styling
import React, { useState, useEffect, useRef } from "react";
import axios from "axios";

const MAX_STACK_SIZE_ESTIMATE = 1 * 1024 * 1024;
const ServerLink = () => {
  
   

    ////////////////////////////////////////////////////////

    // const [initialInputData, setInitialInputData] = useState(""); // Stores the binary number from API
    // const [url, setUrl] = useState(""); // Stores the input URL
    // const [isFetching, setIsFetching] = useState(false); // Track if API fetching is active
    // const [intervalId, setIntervalId] = useState(null); // Stores the interval ID to clear it later

    // // Function to handle URL input change
    // const handleUrlChange = (e) => {
    //     setUrl(e.target.value);
    // };

    // // Function to start fetching random numbers
    // const startFetching = () => {
    //     if (url.trim() === "") {
    //         alert("Please enter a valid URL");
    //         return;
    //     }
    //     setIsFetching(true);
    // };

    // const stopFetching = () => {
    //     if (isFetching && intervalId) {
    //         clearInterval(intervalId); // Clear the interval to stop fetching
    //         setIsFetching(false);
    //     }
    // };


    // const fetchRandomNumber = async () => {
    //     try {
    //         const response = await fetch(url);

    //         if (!response.ok) {
    //             throw new Error("Network response was not ok");
    //         }

    //         const data = await response.json();
    //         // console.log(' hi fetching dudes',data);
    //         // Handle the specific API response format
    //         if (data && data.binary_data) {
    //             setInitialInputData(data.binary_data); // Update the binary value
    //         } else {
    //             throw new Error("Invalid API response format");
    //         }
    //     } catch (error) {
    //         console.error("Error fetching the random number:", error);
    //         setInitialInputData("Error fetching data");
    //     }
    // };

    // // useEffect to fetch number every 2 seconds when fetching is active
    // useEffect(() => {
    //     if (isFetching && url) {
    //         const id = setInterval(fetchRandomNumber, 2000); // Fetch every 2 seconds
    //         setIntervalId(id); // Save the interval ID
    //     }
    //     return () => clearInterval(intervalId); // Clear interval on cleanup
    // }, [isFetching, url]);



    const [initialInputData, setInitialInputData] = useState(""); // Stores the binary number from API
    const [url, setUrl] = useState("http://localhost:3003/proxy"); // Default URL for the Proxy API (update to your proxy server URL)
    const [isFetching, setIsFetching] = useState(false); // Track if API fetching is active
    const [intervalId, setIntervalId] = useState(null); // Stores the interval ID to clear it later

    // Function to handle URL input change (if you want to allow custom URLs)
    const handleUrlChange = (e) => {
        setUrl(e.target.value);
    };

    // Function to start fetching random binary data
    const startFetching = () => {
        if (url.trim() === "") {
            alert("Please enter a valid URL");
            return;
        }
        setIsFetching(true);
    };

    const stopFetching = () => {
        if (isFetching && intervalId) {
            clearInterval(intervalId); // Clear the interval to stop fetching
            setIsFetching(false);
        }
    };

    // Function to fetch random binary data from the proxy server
    const fetchRandomNumber = async () => {
        try {
            const response = await fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    API_Key: "6625a404-fcf7-aa22-595f-1ce908fc5ebb",
                    APISalt: "$2a$04$nArWqsGVKLmYJ3ob48c2/.fL8hULjZTJLWdtTEstM4Ss8oqagInmu",
                    Rand_type: 1, // Request binary data
                    Length: 64, // Example length of binary data (you can customize)
                }),
            });

            console.log("Server response:", response);
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }

            const data = await response.json();
            if (data && data.random) {
                setInitialInputData(data.random); // Update with fetched binary data
            } else {
                throw new Error("Invalid API response format");
            }
        } catch (error) {
            console.error("Error fetching the random number:", error);
            setInitialInputData("Error fetching data");
        }
    };

    // useEffect to fetch data every 2 seconds when fetching is active
    useEffect(() => {
        if (isFetching && url) {
            const id = setInterval(fetchRandomNumber, 2000); // Fetch every 2 seconds
            setIntervalId(id); // Save the interval ID
        }
        return () => clearInterval(intervalId); // Cleanup the interval on unmount
    }, [isFetching, url]);

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


    const [frequencyTestResponse, setFrequencyTestResponse] = useState("");
    const [frequencyBlockTestResponse, setFrequencyBlockTestResponse] =
        useState("");
    const [runTestResponse, setrunTestResponse] = useState("");
    const [ApproximateEntropyTestResponse, setApproximateEntropyTestResponse] =
        useState("");
    const [runLinearComplexityTestResponse, setrunLinearComplexityTestResponse] =
        useState("");
    const [runNonOverlappingTestResponse, setrunNonOverlappingTestResponse] =
        useState("");
    const [runOverlappingTestResponse, setrunOverlappingTestResponse] =
        useState("");
    const [runUniversalTestResponse, setrunUniversalTestResponse] = useState("");
    const [runSerialTestResponse, setrunSerialTestResponse] = useState("");
    const [runCumulativeSumsTestResponse, setrunCumulativeSumsTestResponse] =
        useState("");
    const [runlongestOneBlockTestResponse, setrunlongestOneBlockTestResponse] =
        useState("");
    const [runBinaryMatrixRankTestResponse, setrunBinaryMatrixRankTestResponse] =
        useState("");
    const [runSpectralTestResponse, setrunSpectralTestResponse] = useState("");

    const [runAutoCorrelationtResponse, setrunAutoCorrelationtResponse] = useState("");

    const [runAdaptiveStatisticalTestResponse, setrunAdaptiveStatisticalTestResponse] = useState("");


    const [runRandomExcursionsTestResponse, setrunRandomExcursionsTestResponse] = useState('');


    const [link, setLink] = useState('');

    const handleInputChangeLink = (e) => {
        setLink(e.target.value);
    };


    useEffect(() => {
        const fetchrunRandomExcursionsTestData = async () => {
          try {
            const response = await axios.post(
              'http://localhost:8000/random_excursions_test/', 
              { binary_data: initialInputData }
            );
            setrunRandomExcursionsTestResponse(response.data);
          } catch (error) {
            console.error('Error executing Random Excursions test:', error);
          }
        };
      
        fetchrunRandomExcursionsTestData();
      }, [initialInputData]);


    const [runRandomExcursionsVariantTestResponse, setrunRandomExcursionsVariantTestResponse] = useState('');


    useEffect(() => {
        const fetchRunRandomExcursionsVariantTestData = async () => {
          try {
            const response = await axios.post(
              'http://localhost:8000/random_excursions_variant_test/', 
              { binary_data: initialInputData } // Sending binary data in the request body
            );
            setrunRandomExcursionsVariantTestResponse(response.data); // Update state with response
          } catch (error) {
            console.error('Error executing Random Excursions Variant test:', error);
          }
        };
      
        fetchRunRandomExcursionsVariantTestData();
      }, [initialInputData]); 




      useEffect(() => {
        const runBinarySpacingsTestData = async () => {
          try {
            // console.log("hi birthday spacing test data :  ", initialInputData);
            const response = await axios.post(
              'http://localhost:8000/run_binary_spacings_test/', // POST endpoint
              { binary_data: initialInputData } // JSON payload
            );
            // console.log("hi birthday spacing test:  ", response.data);
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
        console.log("hi parking lot test:  ", response.data);
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
    ///////////////////////////////////////////////////////////////////////////////////////////////////////




    useEffect(() => {
        const fetchFrequencyTestData = async () => {
          try {
            const response = await axios.post(
              'http://localhost:8000/run_frequency_test/', 
              { binary_data: initialInputData }  // Send the binary data in the request body
            );
            console.log(response)
            setFrequencyTestResponse(response.data);
          } catch (error) {
            console.error("Error executing frequency test:", error);
          }
        };
      
        fetchFrequencyTestData();
      }, [initialInputData]);
      
      useEffect(() => {
        const fetchFrequencyBlockTestData = async () => {
          try {
            const response = await axios.post(
              'http://localhost:8000/run_frequency_block_test/',
              { binary_data: initialInputData }
            );
            setFrequencyBlockTestResponse(response.data);
          } catch (error) {
            console.error("Error executing frequency block test:", error);
          }
        };
    
        fetchFrequencyBlockTestData();
      }, [initialInputData]);

      useEffect(() => {
        const fetchrunTestData = async () => {
          try {
            const response = await axios.post(
              'http://localhost:8000/run_runs_test/',
              { binary_data: initialInputData }
            );
            setrunTestResponse(response.data);
          } catch (error) {
            console.error("Error executing run test:", error);
          }
        };
    
        fetchrunTestData();
      }, [initialInputData]);

      useEffect(() => {
        const fetchrunlongestOneBlockTestData = async () => {
          try {
            const response = await axios.post(
              'http://localhost:8000/run_longest_one_block_test/',
              { binary_data: initialInputData }
            );
            setrunlongestOneBlockTestResponse(response.data);
          } catch (error) {
            console.error("Error executing run test:", error);
          }
        };
    
        fetchrunlongestOneBlockTestData();
      }, [initialInputData]);


    useEffect(() => {
    const fetchApproximateEntropyTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_approximate_entropy_test/',
          { binary_data: initialInputData }
        );
        setApproximateEntropyTestResponse(response.data);
      } catch (error) {
        console.error("Error executing Approximate Entropy test:", error);
      }
    };
    fetchApproximateEntropyTestData();
  }, [initialInputData]);

  useEffect(() => {
    const fetchrunLinearComplexityTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_linear_complexity_test/',
          { binary_data: initialInputData }
        );
        setrunLinearComplexityTestResponse(response.data);
      } catch (error) {
        console.error("Error executing linear complexity test:", error);
      }
    };
    fetchrunLinearComplexityTestData();
  }, [initialInputData]);


    useEffect(() => {
    const fetchrunNonOverlappingTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_non_overlapping_test/',
          { binary_data: initialInputData }
        );
        setrunNonOverlappingTestResponse(response.data);
      } catch (error) {
        console.error("Error executing Non-overlapping test:", error);
      }
    };
    fetchrunNonOverlappingTestData();
  }, [initialInputData]);

  useEffect(() => {
    const fetchrunOverlappingTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_overlapping_test/',
          { binary_data: initialInputData }
        );
        setrunOverlappingTestResponse(response.data);
      } catch (error) {
        console.error("Error executing Overlapping test:", error);
      }
    };
    fetchrunOverlappingTestData();
  }, [initialInputData]);

  useEffect(() => {
    const fetchrunUniversalTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_statistical_test/',
          {binary_data: initialInputData}
        );
        setrunUniversalTestResponse(response.data);
      } catch (error) {
        console.error("Error executing Universal test:", error);
      }
    };
    fetchrunUniversalTestData();
  }, [initialInputData]);

  useEffect(() => {
    const fetchrunSerialTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_serial_test/',
          {binary_data: initialInputData}
        );
        setrunSerialTestResponse(response.data);
      } catch (error) {
        console.error("Error executing Serial test:", error);
      }
    };
    fetchrunSerialTestData();
  }, [initialInputData]);


    useEffect(() => {
    const fetchrunCumulativeSumsTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_cumulative_sums_test/',
          {binary_data: initialInputData}
        );
        setrunCumulativeSumsTestResponse(response.data);
      } catch (error) {
        console.error("Error executing Cumulative Sums test:", error);
      }
    };
    fetchrunCumulativeSumsTestData();
  }, [initialInputData]);

  useEffect(() => {
    const fetchrunBinaryMatrixRankTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_binary_matrix_rank_text/',
          {binary_data: initialInputData}
        );
        setrunBinaryMatrixRankTestResponse(response.data);
      } catch (error) {
        console.error("Error executing Cumulative Sums test:", error);
      }
    };
    fetchrunBinaryMatrixRankTestData();
  }, [initialInputData]);

  useEffect(() => {
    const fetchrunSpectralTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_spectral_test/',
          {binary_data: initialInputData}
        );
        setrunSpectralTestResponse(response.data);
      } catch (error) {
        console.error("Error executing Cumulative Sums test:", error);
      }
    };
    fetchrunSpectralTestData();
  }, [initialInputData]);

  useEffect(() => {
    const fecthrunAutoCorrelationtData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_autocorrelation_test/',
          {binary_data: initialInputData}
        );
        setrunAutoCorrelationtResponse(response.data);
      } catch (error) {
        console.error("Error executing auto correlation test:", error);
      }
    };
    fecthrunAutoCorrelationtData();
  }, [initialInputData]);


    useEffect(() => {
    const fetchrunSpectralTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_spectral_test/',
          {binary_data: initialInputData}
        );
        setrunSpectralTestResponse(response.data);
      } catch (error) {
        console.error("Error executing Cumulative Sums test:", error);
      }
    };
    fetchrunSpectralTestData();
  }, [initialInputData]);

    useEffect(() => {
    const fetchrunAdaptiveStatisticalTestData = async () => {
      try {
        const response = await axios.post(
          'http://localhost:8000/run_adaptive_statistical_test/',
          {binary_data: initialInputData}
        );
        setrunAdaptiveStatisticalTestResponse(response.data);
      } catch (error) {
        console.error("Error executing adaptive statistical test:", error);
      }
    };
    fetchrunAdaptiveStatisticalTestData();
  }, [initialInputData]);


    return (

        <div >
            <div style={{ textAlign: "center", justifyContent: 'center', marginTop: '30px', height: '150px' }}>
                <h1>Random Number Generator</h1>
                <input
                    type="text"
                    placeholder="Enter API URL"
                    value={url}
                    onChange={handleUrlChange}
                />
                <button onClick={startFetching}>Start Generating</button>
                <button onClick={stopFetching} disabled={!isFetching}>Stop Generating</button>
                <h3>Binary Number: {initialInputData}</h3>
            </div>


            <div className="gridContainer">

                <div
                    style={{
                        display: "grid",
                        gridTemplateColumns: "20% 20% auto 20% 20%  auto", // 6 columns of equal width
                        gridTemplateRows: "repeat(21, 100px)", // 10 rows of equal height (added one extra row)
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

                   
                    {Array.from({ length: 114 }).map((_, index) => {
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
                        }

                        // ////////////////////////////////////////////////////////////////////////


                        if (index === 60) {
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
                                        <span style={{}}>21. Frequency Test</span>
                                    </div>
                                </div>
                            );
                        } else if (index === 63) {
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
                                        22. Runs Test
                                    </div>
                                </div>
                            );
                        } else if (index === 66) {
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
                                        23. Binary Matrix Rank Test
                                    </div>
                                </div>
                            );
                        } else if (index === 69) {
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
                                        24. Non-overlapping Template match
                                    </div>
                                </div>
                            );
                        } else if (index === 72) {
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
                                        25. Maurer's Universal Statistical Test
                                    </div>
                                </div>
                            );
                        } else if (index === 75) {
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
                                        26. Serial Test
                                    </div>
                                </div>
                            );
                        } else if (index === 78) {
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
                                        27. Approximate Entropy Test
                                    </div>
                                </div>
                            );
                        } else if (index === 81) {
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
                                        28. Cumulative Sums Test
                                    </div>
                                </div>
                            );
                        }
                        else if (index === 84) {
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
                                        29. Autocorrelation Test
                                    </div>
                                </div>
                            );
                        }
                        else if (index === 87) {
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
                                        30. Adaptive Statistical Test
                                    </div>
                                </div>
                            );
                        }
                        else if (index === 90) {
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
                                        31. Frequency Test within a Block
                                    </div>
                                </div>
                            );
                        } else if (index === 93) {
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
                                        32. Test for the longest Run of Ones
                                    </div>
                                </div>
                            );
                        } else if (index === 96) {
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
                                        33. Discrete Fourier Transform Test
                                    </div>
                                </div>
                            );
                        } else if (index === 99) {
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
                                        34. Overlapping Template Matching Test
                                    </div>
                                </div>
                            );
                        } else if (index === 102) {
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
                                        35. Linear Complexity Test
                                    </div>
                                </div>
                            );
                        }




                        ////////////////////////////////////////////////////






                        else if (index === 1) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>{runOverlapping5PermutationTestResponse.p_value}</span>
                                    </div>
                                </div>
                            );
                        } else if (index === 8) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {runmatrixRankTestResponse.result}
                                        </span>
                                    </div>
                                </div>
                            );
                        }


                        ////////////////////////////////////////////////////////////////////

                        else if (index === 61) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {frequencyTestResponse.p_value}
                                        </span>
                                    </div>
                                </div>
                            );
                        } else if (index === 62) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {frequencyTestResponse.result}
                                        </span>
                                    </div>
                                </div>
                            );
                        } else if (index === 91) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {frequencyBlockTestResponse.p_value}
                                        </span>
                                    </div>
                                </div>
                            );
                        } else if (index === 92) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {frequencyBlockTestResponse.result}
                                        </span>
                                    </div>
                                </div>
                            );
                        } else if (index === 64) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>{runTestResponse.p_value}</span>
                                    </div>
                                </div>
                            );
                        } else if (index === 65) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>{runTestResponse.result}</span>
                                    </div>
                                </div>
                            );
                        } else if (index === 94) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {runlongestOneBlockTestResponse.p_value}
                                        </span>
                                    </div>
                                </div>
                            );
                        } else if (index === 95) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {runlongestOneBlockTestResponse.result}
                                        </span>
                                    </div>
                                </div>
                            );
                        } else if (index === 67) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {runBinaryMatrixRankTestResponse.p_value}
                                        </span>
                                    </div>
                                </div>
                            );
                        } else if (index === 68) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {runBinaryMatrixRankTestResponse.result}
                                        </span>
                                    </div>
                                </div>
                            );
                        } else if (index === 97) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {runSpectralTestResponse.p_value}
                                        </span>
                                    </div>
                                </div>
                            );
                        } else if (index === 98) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {runSpectralTestResponse.result}
                                        </span>
                                    </div>
                                </div>
                            );
                        } else if (index === 103) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {runLinearComplexityTestResponse.p_value}
                                        </span>
                                    </div>
                                </div>
                            );
                        } else if (index === 104) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {runLinearComplexityTestResponse.result}
                                        </span>
                                    </div>
                                </div>
                            );
                        } else if (index === 79) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {ApproximateEntropyTestResponse.p_value}
                                        </span>
                                    </div>
                                </div>
                            );
                        } else if (index === 80) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {ApproximateEntropyTestResponse.result}
                                        </span>
                                    </div>
                                </div>
                            );
                        }
                        //runNonOverlappingTest
                        else if (index === 70) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {runNonOverlappingTestResponse.p_value}
                                        </span>
                                    </div>
                                </div>
                            );
                        } else if (index === 71) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {runNonOverlappingTestResponse.result}
                                        </span>
                                    </div>
                                </div>
                            );
                        } else if (index === 100) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {runOverlappingTestResponse.p_value}
                                        </span>
                                    </div>
                                </div>
                            );
                        } else if (index === 101) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {runOverlappingTestResponse.result}
                                        </span>
                                    </div>
                                </div>
                            );
                        } else if (index === 73) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {runUniversalTestResponse.p_value}
                                        </span>
                                    </div>
                                </div>
                            );
                        } else if (index === 74) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {runUniversalTestResponse.result}
                                        </span>
                                    </div>
                                </div>
                            );
                        } else if (index === 76) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {runSerialTestResponse.p_value}
                                        </span>
                                    </div>
                                </div>
                            );
                        } else if (index === 77) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {runSerialTestResponse.result}
                                        </span>
                                    </div>
                                </div>
                            );
                        } else if (index === 82) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {runCumulativeSumsTestResponse.p_value}
                                        </span>
                                    </div>
                                </div>
                            );
                        } else if (index === 83) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {runCumulativeSumsTestResponse.result}
                                        </span>
                                    </div>
                                </div>
                            );
                        }

                        else if (index === 85) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {runAutoCorrelationtResponse.p_value}
                                        </span>
                                    </div>
                                </div>
                            );
                        }

                        else if (index === 86) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {runAutoCorrelationtResponse.result}
                                        </span>
                                    </div>
                                </div>
                            );
                        }

                        else if (index === 88) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {runAdaptiveStatisticalTestResponse.p_value}
                                        </span>
                                    </div>
                                </div>
                            );
                        }

                        else if (index === 89) {
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
                                        style={{ width: "100%", height: "50px", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}>
                                            {runAdaptiveStatisticalTestResponse.result}
                                        </span>
                                    </div>
                                </div>
                            );
                        }

                        else if (index === 105) {
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
                                        36. Random Excursion Variant Test

                                    </div>
                                </div>
                            );
                        }

                        else if (index === 106) {
                            return (
                                
                                <div key={index} style={{ border: '1px solid black', textAlign: 'center', color: 'red', }}>
                                    {runRandomExcursionsVariantTestResponse ? runRandomExcursionsVariantTestResponse.p_value : ''}
                                </div>
                            );
                        } else if (index === 107) {
                            return (
                                <div key={index} style={{ border: '1px solid black', textAlign: 'center', color: 'red', }}>
                                    {runRandomExcursionsVariantTestResponse ? runRandomExcursionsVariantTestResponse.result : ''}
                                </div>
                            );
                        }



                        else if (index === 108) {
                            // Check if it's the cell below "Test type"
                            return (
                                <div
                                style={{
                                    border: "1px solid black",
                                    display: "flex",
                                    alignItems: "center",
                                    justifyContent: "center",
                                    height:'100px'
                                }}
                                >

                                    <div
                                        style={{
                                            display: "flex",
                                            justifyContent: "center",
                                            alignItems: "center",
                                        }}
                                    >
                                        37. Random Excursion  Test

                                    </div>
                                </div>
                            );
                        }

                        else if (index === 109) {
                            return (
                                <div key={index} style={{ border: '1px solid black', textAlign: 'center', color: 'red', }}>
                                    {runRandomExcursionsTestResponse ? runRandomExcursionsTestResponse.p_value : ''}
                                </div>
                            );
                        } else if (index === 110) {
                            return (
                                <div key={index} style={{ border: '1px solid black', textAlign: 'center', color: 'red', }}>
                                    {runRandomExcursionsTestResponse ? runRandomExcursionsTestResponse.result : ''}
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
                                        style={{ width: "100%", textAlign: "center" }}
                                    >
                                        <span style={{ color: "red" }}></span>
                                    </div>
                                </div>


                            );
                        }
                    })}


                </div>


            </div>


            <div>



            </div>


        </div>
    );
}

export default ServerLink;
