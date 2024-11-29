import LoginPage from "./components/LoginPage";
import HomePage from "./components/HomePage";
import { useState } from "react";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      {isLoggedIn ? (
        <HomePage />
      ) : (
        <LoginPage
          onLogin={() => setIsLoggedIn(true)}
          isLoggedIn={isLoggedIn}
        />
      )}
    </div>
  );
}

export default App;
