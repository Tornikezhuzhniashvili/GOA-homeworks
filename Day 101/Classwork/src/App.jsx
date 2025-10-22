import React from "react";
import { Route, Routes } from "react-router";
import About from "./Pages/about";
import Home from "./Pages/home";

export default function App() {
  return (
    <div>
      <Routes>
        <Route path="/home">
          <Route path="" element={<Home />} />
        </Route>
        <Route path="/about">
          <Route path="" element={<About />} />
        </Route>
      </Routes>
    </div>
  );
}
