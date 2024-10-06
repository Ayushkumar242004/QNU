import axios from 'axios';

const runNonOverlappingTest = (binaryData) => {
    return axios.get('http://localhost:8000/run_non_overlapping_test/', {
        params: {
            binary_data: binaryData
        }
    });
};

const runOverlappingTest = (binaryData) => {
    return axios.get('http://localhost:8000/run_overlapping_test/', {
        params: {
            binary_data: binaryData
        }
    });
};


export { runNonOverlappingTest };
export { runOverlappingTest };