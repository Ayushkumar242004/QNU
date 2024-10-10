import React, { useState, useEffect, useContext, createContext } from "react";
import axios from "axios";
import End from "./End";

const GridContainer = ({ binaryData }) => {
  const [frequencyTestChecked, setFrequencyTestChecked] = useState(false);
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

  // Function to handle checkbox change
  const handleFrequencyTestCheckboxChange = () => {
    setFrequencyTestChecked(!frequencyTestChecked);
  };
  // 1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000
  useEffect(() => {
    const fetchFrequencyTestData = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/run_frequency_test/?binary_data=${binaryData}`
        );
        setFrequencyTestResponse(response.data);
      } catch (error) {
        console.error("Error executing frequency test:", error);
      }
    };

    fetchFrequencyTestData();
  }, [binaryData]);

  useEffect(() => {
    const fetchFrequencyBlockTestData = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/run_frequency_block_test/?binary_data=${binaryData}`
        );
        setFrequencyBlockTestResponse(response.data);
      } catch (error) {
        console.error("Error executing frequency block test:", error);
      }
    };

    fetchFrequencyBlockTestData();
  }, [binaryData]);

  useEffect(() => {
    const fetchrunTestData = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/run_runs_test/?binary_data=${binaryData}`
        );
        setrunTestResponse(response.data);
      } catch (error) {
        console.error("Error executing run test:", error);
      }
    };

    fetchrunTestData();
  }, [binaryData]);

  useEffect(() => {
    const fetchrunlongestOneBlockTestData = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/run_longest_one_block_test/?binary_data=${binaryData}`
        );
        setrunlongestOneBlockTestResponse(response.data);
      } catch (error) {
        console.error("Error executing run test:", error);
      }
    };

    fetchrunlongestOneBlockTestData();
  }, [binaryData]);
  useEffect(() => {
    const fetchApproximateEntropyTestData = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/run_approximate_entropy_test/?binary_data=${binaryData}`
        );
        setApproximateEntropyTestResponse(response.data);
      } catch (error) {
        console.error("Error executing Approximate Entropy test:", error);
      }
    };
    fetchApproximateEntropyTestData();
  }, [binaryData]);

  useEffect(() => {
    const fetchrunLinearComplexityTestData = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/run_linear_complexity_test/?binary_data=${binaryData}`
        );
        setrunLinearComplexityTestResponse(response.data);
      } catch (error) {
        console.error("Error executing linear complexity test:", error);
      }
    };
    fetchrunLinearComplexityTestData();
  }, [binaryData]);
  useEffect(() => {
    const fetchrunNonOverlappingTestData = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/run_non_overlapping_test/?binary_data=${binaryData}`
        );
        setrunNonOverlappingTestResponse(response.data);
      } catch (error) {
        console.error("Error executing Non-overlapping test:", error);
      }
    };
    fetchrunNonOverlappingTestData();
  }, [binaryData]);

  useEffect(() => {
    const fetchrunOverlappingTestData = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/run_overlapping_test/?binary_data= ${binaryData}`
        );
        setrunOverlappingTestResponse(response.data);
      } catch (error) {
        console.error("Error executing Overlapping test:", error);
      }
    };
    fetchrunOverlappingTestData();
  }, [binaryData]);

  useEffect(() => {
    const fetchrunUniversalTestData = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/run_statistical_test/?binary_data=${binaryData}`
        );
        setrunUniversalTestResponse(response.data);
      } catch (error) {
        console.error("Error executing Universal test:", error);
      }
    };
    fetchrunUniversalTestData();
  }, [binaryData]);

  useEffect(() => {
    const fetchrunSerialTestData = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/run_serial_test/?binary_data=${binaryData}`
        );
        setrunSerialTestResponse(response.data);
      } catch (error) {
        console.error("Error executing Serial test:", error);
      }
    };
    fetchrunSerialTestData();
  }, [binaryData]);

  useEffect(() => {
    const fetchrunCumulativeSumsTestData = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/run_cumulative_sums_test/?binary_data=${binaryData}`
        );
        setrunCumulativeSumsTestResponse(response.data);
      } catch (error) {
        console.error("Error executing Cumulative Sums test:", error);
      }
    };
    fetchrunCumulativeSumsTestData();
  }, [binaryData]);

  useEffect(() => {
    const fetchrunBinaryMatrixRankTestData = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/run_binary_matrix_rank_text/?binary_data=${binaryData}`
        );
        setrunBinaryMatrixRankTestResponse(response.data);
      } catch (error) {
        console.error("Error executing Cumulative Sums test:", error);
      }
    };
    fetchrunBinaryMatrixRankTestData();
  }, [binaryData]);

  useEffect(() => {
    const fetchrunSpectralTestData = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/run_spectral_test/?binary_data= ${binaryData}`
        );
        setrunSpectralTestResponse(response.data);
      } catch (error) {
        console.error("Error executing Cumulative Sums test:", error);
      }
    };
    fetchrunSpectralTestData();
  }, [binaryData]);

  useEffect(() => {
    const fecthrunAutoCorrelationtData = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/run_autocorrelation_test/?binary_data= ${binaryData}`
        );
        setrunAutoCorrelationtResponse(response.data);
      } catch (error) {
        console.error("Error executing auto correlation test:", error);
      }
    };
    fecthrunAutoCorrelationtData();
  }, [binaryData]);
  
  useEffect(() => {
    const fetchrunSpectralTestData = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/run_spectral_test/?binary_data= ${binaryData}`
        );
        setrunSpectralTestResponse(response.data);
      } catch (error) {
        console.error("Error executing Cumulative Sums test:", error);
      }
    };
    fetchrunSpectralTestData();
  }, [binaryData]);

  useEffect(() => {
    const fetchrunAdaptiveStatisticalTestData = async () => {
      try {
        const response = await axios.get(
          `http://localhost:8000/run_adaptive_statistical_test/?binary_data= ${binaryData}`
        );
        setrunAdaptiveStatisticalTestResponse(response.data);
      } catch (error) {
        console.error("Error executing adaptive statistical test:", error);
      }
    };
    fetchrunAdaptiveStatisticalTestData();
  }, [binaryData]);

  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "20% 20% auto 20% 20%  auto", // 6 columns of equal width
        gridTemplateRows: "repeat(10, 1fr)", // 10 rows of equal height (added one extra row)
        width: "100%", // Set width to 100%
        height: "100vh",
      }}
    >
      {/* Row with "Randomness testing" */}
      <div
        style={{
          gridColumn: "1 / -1", // Span the entire grid width
          gridRow: "1", // First row
          background: "black",
          color: "white",
          height: "10vh",
          textAlign: "center",
          lineHeight: "60px", // Adjust as needed for vertical centering
        }}
      >
        Randomness testing
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
        Test type
      </div>
      <div
        style={{
          textAlign: "center",
          border: "1px solid black",
          color: "white",
          backgroundColor: "blue",
        }}
      >
        p-value
      </div>
      <div
        style={{
          textAlign: "center",
          border: "1px solid black",
          color: "white",
          backgroundColor: "blue",
        }}
      >
        Result
      </div>
      <div
        style={{
          textAlign: "center",
          border: "1px solid black",
          color: "white",
          backgroundColor: "blue",
        }}
      >
        Test type
      </div>
      <div
        style={{
          textAlign: "center",
          border: "1px solid black",
          color: "white",
          backgroundColor: "blue",
        }}
      >
        p-value
      </div>
      <div
        style={{
          textAlign: "center",
          border: "1px solid black",
          color: "white",
          backgroundColor: "blue",
        }}
      >
        Result
      </div>

      {/* Content for the remaining grid cells */}
      {Array.from({ length: 48 }).map((_, index) => {
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
                <span style={{}}>1. Frequency Test</span>
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
                3. Runs Test
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
                5. Binary Matrix Rank Test
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
                7. Non-overlapping Template match
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
                9. Maurer's Universal Statistical Test
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
                11. Serial Test
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
                12. Approximate Entropy Test
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
                13. Cumulative Sums Test
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
                14. Autocorrelation Test
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
                15. Adaptive Statistical Test
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
                2. Frequency Test within a Block
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
                4. Test for the longest Run of Ones
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
                6. Discrete Fourier Transform Test
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
                8. Overlapping Template Matching Test
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
                10. Linear Complexity Test
              </div>
            </div>
          );
        } else if (index === 33 || index === 39) {
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
                  {frequencyTestResponse.p_value}
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
                  {frequencyTestResponse.result}
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
                  {frequencyBlockTestResponse.p_value}
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
                  {frequencyBlockTestResponse.result}
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
                <span style={{ color: "red" }}>{runTestResponse.p_value}</span>
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
                style={{ width: "100%", height: "20px", textAlign: "center" }}
              >
                <span style={{ color: "red" }}>{runTestResponse.result}</span>
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
                  {runlongestOneBlockTestResponse.p_value}
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
                  {runlongestOneBlockTestResponse.result}
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
                  {runBinaryMatrixRankTestResponse.p_value}
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
                  {runBinaryMatrixRankTestResponse.result}
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
                  {runSpectralTestResponse.p_value}
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
                  {runSpectralTestResponse.result}
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
                  {runLinearComplexityTestResponse.p_value}
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
                  {runLinearComplexityTestResponse.result}
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
                  {ApproximateEntropyTestResponse.p_value}
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
                  {ApproximateEntropyTestResponse.result}
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
                  {runNonOverlappingTestResponse.p_value}
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
                  {runNonOverlappingTestResponse.result}
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
                  {runOverlappingTestResponse.p_value}
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
                  {runOverlappingTestResponse.result}
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
                  {runUniversalTestResponse.p_value}
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
                  {runUniversalTestResponse.result}
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
                  {runSerialTestResponse.p_value}
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
                  {runSerialTestResponse.result}
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
                  {runCumulativeSumsTestResponse.p_value}
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
                  {runCumulativeSumsTestResponse.result}
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
                  {runAutoCorrelationtResponse.p_value}
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
                  {runAutoCorrelationtResponse.result}
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
                  {runAdaptiveStatisticalTestResponse.p_value}
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
                  {runAdaptiveStatisticalTestResponse.result}
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
  );
};

export default GridContainer;
