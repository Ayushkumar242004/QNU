import axios from 'axios';

const runSerialTest = (binaryData) => {
    return axios.get('http://localhost:8000/run_serial_test/', {
        params: {
            binary_data: binaryData
        }
    });
};


export { runSerialTest };