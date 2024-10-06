import axios from 'axios';

const runUniversalTest = (binaryData) => {
    return axios.get('http://localhost:8000/run_statistical_test/', {
        params: {
            binary_data: binaryData
        }
    });
};


export { runUniversalTest };