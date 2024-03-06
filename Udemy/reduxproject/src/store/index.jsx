import { configureStore } from '@reduxjs/toolkit';

import counterReducer from './counter.jsx';
import authReducer from './auth.jsx';

const store = configureStore({
  reducer: {
    counter: counterReducer,
    auth: authReducer,
  },
});

export default store;
