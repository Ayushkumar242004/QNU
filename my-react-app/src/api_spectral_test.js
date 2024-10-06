import axios from 'axios';


const runSpectralTest = (binaryData) => {
    return axios.get('http://localhost:8000/run_spectral_test/', {
        params: {
            binary_data: binaryData
        }
    });
};

export { runSpectralTest };