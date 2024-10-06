import axios from 'axios';

const runRandomExcursionsTest = (binaryData) => {
    return axios.get('http://localhost:8000/random_excursions_test/', {
        params: {
            binary_data: binaryData
        }
    });
};

const runRandomExcursionsVariantTest = (binaryData) => {
    return axios.get('http://localhost:8000/random_excursions_variant_test/', {
        params: {
            binary_data: binaryData
        }
    });
};


export { runRandomExcursionsTest };
export { runRandomExcursionsVariantTest };