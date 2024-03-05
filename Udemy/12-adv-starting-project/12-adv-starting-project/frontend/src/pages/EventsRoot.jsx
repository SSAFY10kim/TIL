import { useState, useEffect } from 'react';
import { Outlet } from 'react-router-dom';

import EventNavigation from '../components/EventsNavigation.js';

export default function EventsRoot() {
  return (
    <>
      <EventNavigation />
      <Outlet />
    </>
  );
}
