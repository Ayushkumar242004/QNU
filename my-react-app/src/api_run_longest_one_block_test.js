import axios from 'axios';

const runlongestOneBlockTest = (binaryData) => {
    return axios.get('http://localhost:8000/run_longest_one_block_test/', {
        params: {
            binary_data: binaryData
        }
    });
};
export { runlongestOneBlockTest };