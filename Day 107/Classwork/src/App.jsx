// import React from 'react'

// export default function App() {
//   return (
//     <div className='flex justify-center items-center h-screen bg-gray-500'>
//       <div className='w-[500px]'>
//         {/* red */}
//         <div className='w-full h-[60px] bg-red-500' /> 
//         {/* white */}
//         <div className='w-full h-[20px] bg-white'/> 
//         {/* black */}
//         <div className='w-full h-[300px] bg-black'/> 
//       </div>
//     </div>
//   )
// }

import React from 'react'

export default function App() {
  return (
    <div className='flex justify-center items-center h-screen'>
      <div className='w-[300px] grid gap-5 '>
        {/* red */}
        <div className='w-full h-[100px] bg-red-500 border-[5px]'/>
        {/* red */}
        <div className='w-full h-[100px] bg-red-500 border-[5px]'/>
        {/* red */}
        <div className='w-full h-[100px] bg-red-500 border-[5px]'/>
        {/* green */}
        <div className='w-full h-[100px] bg-green-500 border-[5px]'/>
      </div>
    </div>
  )
}


