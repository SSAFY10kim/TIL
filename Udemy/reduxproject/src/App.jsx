import { Fragment } from 'react';
import { useSelector } from 'react-redux';

import Counter from './components/Counter.jsx';
import Header from './components/Header.jsx';
import Auth from './components/Auth.jsx';
import UserProfile from './components/UserProfile.jsx';

function App() {
  const isAuth = useSelector((state) => state.auth.isAuthenticated);

  return (
    <Fragment>
      <Header />
      {isAuth && <UserProfile />}
      {!isAuth && <Auth />}
      <Counter />
    </Fragment>
  );
}

export default App;
