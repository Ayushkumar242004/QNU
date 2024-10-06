import axios from 'axios';


const runBinaryMatrixRankTest = (binaryData) => {
    return axios.get('http://localhost:8000/run_binary_matrix_rank_text/', {
        params: {
            binary_data: binaryData
        }
    });
};

export { runBinaryMatrixRankTest };