import LoginPage from "./components/LoginPage";
import HomePage from "./components/HomePage";
import { useState } from "react";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  //use useLogin hook to check if user is logged in
  return (
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
}

export default App;
