import { useState, useEffect } from 'react'
import { NavLink } from 'react-router-dom'

import classes from './MainNavi.module.css'

export default function MainNavi() {

  return (
    <header className={classes.header}>
      <nav>
        <ul className={classes.list}>
          <li>
            <NavLink
              to="/"
              className={({ isActive }) =>
                isActive ? classes.active : undefined}
              end
            >
              Home
            </NavLink>
          </li>
          <li>
            <NavLink
              to="/products" className={({ isActive }) =>
                isActive ? classes.active : undefined}>
              Product
            </NavLink>
          </li>
        </ul>
      </nav >
    </header >
  )
}