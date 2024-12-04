import { useState } from "react";
import { Routes, Route } from "react-router-dom";

import AuthProvider from "./hooks/useAuth";
import LoginPage from "./pages/LoginPage";
import Homepage from "./pages/Homepage";
import SignupPage from "./pages/SignupPage";
import StartingPage from "./pages/StartingPage";
import PrivateRoute from "./pages/PrivateRoute";

function App() {
  const [isSignedUp, setIsSignedUp] = useState(false);

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <AuthProvider>
        <Routes>
          <Route path="/" element={<StartingPage />} />
          <Route path="LoginPage" element={<LoginPage />} />
          <Route
            path="SignupPage"
            element={
              <SignupPage
                onSignup={() => setIsSignedUp((prevState) => !prevState)}
                isSignedUp={isSignedUp}
              />
            }
          />
          <Route element={<PrivateRoute />}>
            <Route path="Homepage" element={<Homepage />} />
          </Route>
        </Routes>
      </AuthProvider>
    </div>
  );
}

export default App;
