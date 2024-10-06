import React, { useState } from 'react';
import Heading from './Components/Heading'; // Adjusted import path
import Navbar from './Components/Navbar'; // Adjusted import path
import Up from './Components/up';
import Down from './Components/down';
import End from './Components/End';
import RandomTest from './Components/RandomTest';
import RandomVariantTest from './Components/RandomVariantTest';


function App() {
  return (
    <div className="App">
      <Heading />
      <Navbar />
      <Up />
      
       <End  />
    </div>
  );
}

export default App;
