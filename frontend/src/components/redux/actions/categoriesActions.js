import axios from 'axios';

export const fetchProducts = () => async (dispatch) => {
    try {
        const response = await axios.get('/api/products/');
        dispatch({
            type: 'SET_CATEGORIES',
            payload: response.data,
        });
    } catch (error){
        console.error('Error  fetching categories:', error);
    }
}