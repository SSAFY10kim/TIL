import { useState, useEffect } from 'react'
import { Outlet } from 'react-router-dom'

import MainNavi from './components/MainNavi'
import classes from './Root.module.css'

export default function RootLayout() {

  return (
    <>
      <MainNavi />
      <main className={classes.content}>
        <Outlet />
      </main>
    </>
  )
}