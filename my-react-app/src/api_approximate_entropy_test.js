import axios from 'axios';


const runApproximateEntropyTest = (binaryData) => {
    return axios.get('http://localhost:8000/run_approximate_entropy_test/', {
        params: {
            binary_data: binaryData
        }
    });
};

export { runApproximateEntropyTest };