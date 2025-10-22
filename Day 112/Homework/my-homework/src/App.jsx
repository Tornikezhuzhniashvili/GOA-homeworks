import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'



function App() {
  const [text, setText] = useState("Hello React");

  function changeText() {
    if (text === "Hello React") {
      setText("Hello Tailwind");
    } else {
      setText("Hello React");
    }
  }

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gradient-to-br from-blue-100 to-purple-200">
      <h1 className="text-4xl font-bold text-gray-800 mb-6">{text}</h1>
      <button onClick={changeText}
      className="px-6 py-3 bg-blue-500 text-white text-lg rounded-lg shadow-md hover:bg-blue-600 transition"
      >Change Text</button>
    </div>
  );
}

export default App;
