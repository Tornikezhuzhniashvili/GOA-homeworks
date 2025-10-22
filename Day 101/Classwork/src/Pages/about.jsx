import React from 'react'
import { Outlet } from 'react-router'

export default function About() {
  return (
    <div>
      <b>About</b>
      <Outlet/>
    </div>
  )
}
