import { useState } from "react";
import { Routes, Route } from "react-router-dom";

import LoginPage from "./pages/LoginPage";
import HomePage from "./pages/HomePage";
import SignupPage from "./pages/SignupPage";
import StartingPage from "./pages/StartingPage";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [isSignedUp, setIsSignedUp] = useState(false);
  //use useLogin hook to check if user is logged in
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <Routes>
        <Route path="/" element={<StartingPage />} />
        <Route path="Homepage" element={<HomePage />} />
        <Route
          path="LoginPage"
          element={
            <LoginPage
              onLogin={() => setIsLoggedIn(true)}
              isLoggedIn={isLoggedIn}
            />
          }
        />
        <Route
          path="SignupPage"
          element={
            <SignupPage
              onSignup={() => setIsSignedUp(true)}
              isSignedUp={false}
            />
          }
        />
      </Routes>
    </div>
  );
}

export default App;

/* //For non-router layout
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      {isLoggedIn ? (
        <HomePage />
      ) : (
        <LoginPage
          isLoggedIn={isLoggedIn}
          onLogin={() => setIsLoggedIn(true)}
        />
      )}
    </div>
  );

*/
