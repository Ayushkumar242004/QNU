import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Heading from './Components/Heading'; 
import Navbar from './Components/Navbar'; 
import Up from './Components/up';
import End from './Components/End';
import DieharderTest from './Components/DieharderTest';
import ServerLink from './Components/Server_link'
function App() {
  return (
    <Router>
      <div className="App">
        <Heading />
        <Navbar />
        <Routes>
          {/* Home route */}
          <Route path="/" element={<><Up /></>} />
          {/* DieHarder Test route */}
          <Route path="/dieharder_test" element={<><DieharderTest /></>} />
          
          <Route path="/server_link" element={<><ServerLink /></>} />
          
        </Routes>
      </div>
    </Router>
  );
}

export default App;
