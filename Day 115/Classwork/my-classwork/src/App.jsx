import React, { useEffect, useState } from 'react'


export default function App() {
  const [posts, setPosts] = useState([])
  useEffect(() => {
    const apiFetch = async () => {
    
      fetch('https://jsonplaceholder.typicode.com/posts')
      .then(response => response.json())
      .then(json => setPosts(json))
      .catch(err => console.log(err))
     }
     apiFetch()
  },[])
  return (
    <div>
      {posts.map(post => <div>{post.title}</div>)}
    </div>
  )
}
