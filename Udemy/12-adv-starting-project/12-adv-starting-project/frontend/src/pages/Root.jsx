import { useState, useEffect } from 'react';

import { Outlet, useNavigation } from 'react-router-dom';

import MainNavigation from '../components/MainNavigation.js';

export default function Root() {
  const navigation = useNavigation();

  return (
    <>
      <MainNavigation />
      <main>
        {/* {navigation.state === 'loading' && <p>Loading...</p>} */}
        <Outlet />
      </main>
    </>
  );
}
