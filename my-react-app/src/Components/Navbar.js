// import React, { useState } from 'react';

// const Navbar = () => {
//   const [isCollapsed, setIsCollapsed] = useState(true); // State to track the collapse status

//   const handleToggle = () => {
//     setIsCollapsed(!isCollapsed); // Toggle the collapse state
//   };

//   return (
//     <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
//       <div className="container">
//         <a className="navbar-brand" href="#">Test Suite</a>
//         <button 
//           className="navbar-toggler" 
//           type="button" 
//           onClick={handleToggle} // Handle toggle click
//           aria-controls="navbarNav" 
//           aria-expanded={!isCollapsed} 
//           aria-label="Toggle navigation"
//         >
//           <span className="navbar-toggler-icon"></span>
//         </button>
//         <div className={`collapse navbar-collapse ${isCollapsed ? '' : 'show'}`} id="navbarNav">
//           <ul className="navbar-nav ml-auto">
//             <li className="nav-item">
//               <a className="nav-link" href="/">NIST Statistical Tests</a>
//             </li>
//             <li className="nav-item">
//               <a className="nav-link" href="/dieharder_test">DieHarder Tests</a>
//             </li>
//             <li className="nav-item">
//               <a className="nav-link" href="/server_link">QRNG Server Link</a>
//             </li>
//           </ul>
//         </div>
//       </div>
//     </nav>
//   );
// }

// export default Navbar;
// import React, { useState } from 'react';

// const Navbar = () => {
//   const [isCollapsed, setIsCollapsed] = useState(true); // State to track the collapse status

//   const handleToggle = () => {
//     setIsCollapsed(!isCollapsed); // Toggle the collapse state
//   };

  

//   return (
//     <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
//       <div className="container">
//         <a className="navbar-brand" href="#">Test Suite</a>
//         <button 
//           className="navbar-toggler" 
//           type="button" 
//           onClick={handleToggle} // Handle toggle click
//           aria-controls="navbarNav" 
//           aria-expanded={!isCollapsed} 
//           aria-label="Toggle navigation"
//         >
//           <span className="navbar-toggler-icon"></span>
//         </button>
//         <div className={`collapse navbar-collapse ${isCollapsed ? '' : 'show'}`} id="navbarNav">
//           <ul className="navbar-nav ml-auto">
//             <li className="nav-item">
//               <a className="nav-link" href="/">NIST Statistical Tests</a>
//             </li>
//             <li className="nav-item">
//               <a className="nav-link" href="/dieharder_test">DieHarder Tests</a>
//             </li>
//             <li className="nav-item">
//               <a className="nav-link" href="/server_link">QRNG Server Link</a>
//             </li>
//           </ul>
//         </div>
//       </div>
//     </nav>
//   );
// }

// export default Navbar;

import React, { useState } from 'react';

const Navbar = () => {
  const [isCollapsed, setIsCollapsed] = useState(true); // State to track the collapse status

  const handleToggle = () => {
    setIsCollapsed(!isCollapsed); // Toggle the collapse state
  };

  const handleLogout = () => {
    // Logic for logout, e.g., clearing tokens
    localStorage.clear();
    window.location.href = "/login"; // Redirect to login after logout
  };

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <div className="container">
        <a className="navbar-brand" href="#">Test Suite</a>
        <button 
          className="navbar-toggler" 
          type="button" 
          onClick={handleToggle} // Handle toggle click
          aria-controls="navbarNav" 
          aria-expanded={!isCollapsed} 
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className={`collapse navbar-collapse ${isCollapsed ? '' : 'show'}`} id="navbarNav">
          {/* Left-aligned navbar items */}
          <ul className="navbar-nav">
            <li className="nav-item">
              <a className="nav-link" href="/">NIST Statistical Tests</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="/dieharder_test">DieHarder Tests</a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="/server_link">QRNG Server Link</a>
            </li>
          </ul>
          {/* Right-aligned logout button */}
          <div className="ml-auto">
            <button className="btn btn-danger logout-button" onClick={handleLogout}>
              Logout
            </button>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
