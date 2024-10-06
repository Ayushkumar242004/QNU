import axios from 'axios';


const runCumulativeSumsTest = (binaryData) => {
    return axios.get('http://localhost:8000/run_cumulative_sums_test/', {
        params: {
            binary_data: binaryData
        }
    });
};

export { runCumulativeSumsTest };