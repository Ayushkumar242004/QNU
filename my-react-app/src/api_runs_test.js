import axios from 'axios';


const runTest = (binaryData) => {
    return axios.get('http://localhost:8000/run_runs_test/', {
        params: {
            binary_data: binaryData
        }
    });
};


export { runTest };
