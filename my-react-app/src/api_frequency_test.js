// src/api.js

import axios from 'axios';

const runFrequencyTest = (binaryData) => {
    return axios.get('http://localhost:8000/run_frequency_test/', {
        params: {
            binary_data: binaryData
        }
    });
};
const runFrequencyBlockTest = (binaryData) => {
    return axios.get('http://localhost:8000/run_frequency_block_test/', {
        params: {
            binary_data: binaryData
        }
    });
};

export { runFrequencyTest };
export { runFrequencyBlockTest };

