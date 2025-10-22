import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function Counter() {
  const [count, setCount] = useState(0);

  const increment = () => {
    setCount(count + 1);
  };
  

  return (
    <div>
      <h1>Count: {count}</h1>
      <button onClick={increment}>increment</button>
    </div>
  )
}

export default Counter;
