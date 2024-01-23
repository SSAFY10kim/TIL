import { useState, useEffect } from 'react'

import { createBrowserRouter, RouterProvider } from 'react-router-dom'

import Home from './pages/Home.jsx'
import Product from './pages/Product.jsx'
import RootLayout from './Root.jsx'
import ErrorPage from './pages/Error.jsx'
import ProductDetail from './pages/ProductDetail.jsx'


const router = createBrowserRouter([
  {
    path: '/root',
    element: <RootLayout />,
    errorElement: <ErrorPage />,
    children: [
      { index: true, element: <Home /> },
      { path: 'products', element: <Product /> },
      { path: 'products/:id', element: <ProductDetail /> }
    ],
  },


])

export default function App() {

  return (
    <RouterProvider router={router} />
  )
}