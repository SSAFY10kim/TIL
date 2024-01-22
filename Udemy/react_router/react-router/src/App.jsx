import { useState, useEffect } from 'react'

import { createBrowserRouter, RouterProvider } from 'react-router-dom'

import Home from './pages/Home.jsx'
import Product from './pages/Product.jsx'
import RootLayout from './Root.jsx'
import ErrorPage from './pages/Error.jsx'


const router = createBrowserRouter([
  {
    path: '/',
    element: <RootLayout />,
    errorElement: <ErrorPage />,
    children: [
      { path: '/', element: <Home /> },
      { path: '/products', element: <Product /> },
    ],
  },


])

export default function App() {

  return (
    <RouterProvider router={router} />
  )
}