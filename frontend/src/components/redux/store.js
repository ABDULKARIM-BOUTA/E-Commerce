import {legacy_createStore, applyMiddleware, combineReducers } from 'redux';
import { thunk } from 'redux-thunk';
import productsReducers from '../reducers/productsReducers' ;
import categoriesReducers from '../reducers/categoriesReducers';



const rootReducer = combineReducers({
    categories: categoriesReducers,
    products: productsReducers
});

const store = legacy_createStore(rootReducer, applyMiddleware(thunk));

export default store;

