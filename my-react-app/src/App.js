// import React from 'react';
// import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
// import Heading from './Components/Heading'; 
// import Navbar from './Components/Navbar'; 
// import Up from './Components/up';
// import End from './Components/End';
// import DieharderTest from './Components/DieharderTest';
// import ServerLink from './Components/Server_link'
// function App() {
//   return (
//     <Router>
//       <div className="App">
//         <Heading />
//         <Navbar />
//         <Routes>
//           {/* Home route */}
//           <Route path="/" element={<><Up /></>} />
//           {/* DieHarder Test route */}
//           <Route path="/dieharder_test" element={<><DieharderTest /></>} />
          
//           <Route path="/server_link" element={<><ServerLink /></>} />
          
//         </Routes>
//       </div>
//     </Router>
//   );
// }

// export default App;


// import React from 'react';
// import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
// import Heading from './Components/Heading'; 
// import Navbar from './Components/Navbar'; 
// import Up from './Components/up';
// import End from './Components/End';
// import DieharderTest from './Components/DieharderTest';
// import ServerLink from './Components/Server_link'


// function App() {
//   return (
//     <Router>
//       <div className="App">
//         <Heading />
//         <Navbar />
//         <Routes>
//           {/* Home route */}
//           <Route path="/" element={<><Up /></>} />
//           {/* DieHarder Test route */}
//           <Route path="/dieharder_test" element={<><DieharderTest /></>} />
          
//           <Route path="/server_link" element={<><ServerLink /></>} />
          
//           {/* <Route path='/layout' element={<Layout/>}/>
//           <Route index element={<Home/>}/>
//           <Route path="login" element={<Login/>}/>
//           <Route path="register" element={<Register/>}/> */}

//         </Routes>
//       </div>
//     </Router>
//   );
// }

// export default App;
import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import axios from 'axios';
import Heading from './Components/Heading';
import Navbar from './Components/Navbar';
import Up from './Components/up';
import DieharderTest from './Components/DieharderTest';
import ServerLink from './Components/Server_link';
import Login from './pages/Login';
import Register from './pages/Register';

const App = () => {
  const [isLoggedIn, setLoggedIn] = useState(() => {
    // Initialize isLoggedIn state based on whether accessToken exists in localStorage
    const token = localStorage.getItem("accessToken");
    return !!token;
  });
  const [username, setUsername] = useState("");

  useEffect(() => {
    if (isLoggedIn) {
      const checkLoggedInUser = async () => {
        try {
          const token = localStorage.getItem("accessToken");
          if (token) {
            const config = {
              headers: {
                "Authorization": `Bearer ${token}`,
              },
            };
            const response = await axios.get("http://127.0.0.1:8000/api/user/", config);
            setUsername(response.data.username);
          } else {
            setLoggedIn(false);
            setUsername("");
          }
        } catch (error) {
          setLoggedIn(false);
          setUsername("");
        }
      };
      checkLoggedInUser();
    }
  }, [isLoggedIn]);

  // Private Route component to protect pages
  const PrivateRoute = ({ element }) => {
    return isLoggedIn ? element : <Navigate to="/login" />;
  };

  // Redirects to the protected routes if the user is already logged in
  const ProtectedRouteRedirect = ({ element }) => {
    return isLoggedIn ? <Navigate to="/" /> : element;
  };

  return (
    <Router>
      <div className="App">
        {/* Authentication Pages */}
        <Routes>
          <Route path="/login" element={<ProtectedRouteRedirect element={<Login setLoggedIn={setLoggedIn} />} />} />
          <Route path="/register" element={<ProtectedRouteRedirect element={<Register />} />} />
          
          {/* Protected Routes */}
          <Route 
            path="/" 
            element={
              <PrivateRoute element={
                <>                 
                  <Navbar />
                  <Up />
                </>
              }/>
            } 
          />
          <Route 
            path="/dieharder_test" 
            element={
              <PrivateRoute element={
                <>
                  <Navbar />
                  <DieharderTest />
                </>
              }/>
            } 
          />
          <Route 
            path="/server_link" 
            element={
              <PrivateRoute element={
                <>
                  <Navbar />
                  <ServerLink />
                </>
              }/>
            } 
          />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
