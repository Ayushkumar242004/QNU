import axios from 'axios';

const runLinearComplexityTest = (binaryData) => {
    return axios.get('http://localhost:8000/run_linear_complexity_test/', {
        params: {
            binary_data: binaryData
        }
    });
};


export { runLinearComplexityTest };