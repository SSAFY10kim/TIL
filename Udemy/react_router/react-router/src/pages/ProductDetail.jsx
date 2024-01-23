import { useState, useEffect } from 'react'

import { useParams, Link } from 'react-router-dom'

export default function ProductDetail() {
  const params = useParams()

  return (
    <>
      <h1>Product Detail Page</h1>
      <p>{params.id}</p>
      <p><Link to=".." relative='path'>Back</Link></p>
    </>
  )
}