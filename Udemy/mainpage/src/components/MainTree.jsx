import { useState, useEffect } from 'react'

import maintree from '../assets/images/maintree.png'

export default function MainTree() {

  return (
    <>
      <img className="relative mb-16"
        src={maintree} alt="MainTree"
      />
    </>
  )
}