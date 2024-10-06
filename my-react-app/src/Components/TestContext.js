import React, { createContext, useContext } from 'react';

const TestContext = React.createContext();

export const TestContextProvider = ({ children }) => {
  const [checkedTests, setCheckedTests] = React.useState([]);

  return (
    <TestContext.Provider value={{ checkedTests, setCheckedTests }}>
      {children}
    </TestContext.Provider>
  );
};

export const useTestContext = () => {
  const context = useContext(TestContext);
  if (!context) {
    throw new Error('useTestContext must be used within a TestContextProvider');
  }
  return context;
};