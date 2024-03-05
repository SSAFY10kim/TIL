import { useState, useEffect } from 'react'
import MainNavi from '../components/MainNavi.jsx'

export default function Error() {

  return (
    <>
      <MainNavi />
      <main>
        <h1>An error cccurred</h1>
        <p>Could not find this page!</p>
      </main>
    </>
  )
}