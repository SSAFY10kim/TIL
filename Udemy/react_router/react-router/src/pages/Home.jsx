import { useState, useEffect } from 'react'
import { Link, useNavigate } from 'react-router-dom'

export default function Home() {
  const navigate = useNavigate();

  function navigateHandler() {
    navigate('/products')
  }

  return (
    <>
      <h1>박스 외부</h1>
      <p>Go To <Link to="/products">The list of Products</Link>.</p>
      <p>
        <button onClick={navigateHandler}>Navigate</button>
      </p>
    </>
  )
}