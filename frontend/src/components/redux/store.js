import {legacy_createStore, applyMiddleware, combineReducers } from 'redux';
import { thunk } from 'redux-thunk';
import productsReducer from '../reducers/productsReducers' ;
import categoriesReducer from '../reducers/categoriesReducers';



const rootReducer = combineReducers({
    categories: categoriesReducer,
    products: productsReducer
});

const store = legacy_createStore(rootReducer, applyMiddleware(thunk));

export default store;

