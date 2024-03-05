import { useState, useEffect } from 'react'

import { Link } from 'react-router-dom'

const PRODUCT = [
  { id: 'p1', title: 'Product 1' },
  { id: 'p2', title: 'Product 2' },
  { id: 'p3', title: 'Product 3' },
]

export default function Product() {

  return (
    <>
      <h1>박스 내부</h1>
      <ul>
        {PRODUCT.map(prod => {
          return <li key={prod.id}><Link to={prod.id}>{prod.title}</Link></li>
        })}
      </ul>
    </>
  )
}