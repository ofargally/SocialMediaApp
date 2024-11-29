import React from "react";
import LoginPageProps from "../Interfaces";

const LoginPage = ({ onLogin, isLoggedIn }: LoginPageProps) => {
  const Button = () => {
    return (
      <button
        onClick={onLogin}
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      >
        Log in
      </button>
    );
  };
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      {isLoggedIn ? (
        <div className="text-green-500 text-xl font-semibold">Logged in</div>
      ) : (
        <>
          <h1 className="text-3xl font-bold mb-4">Login Page</h1>
          <Button />
        </>
      )}
    </div>
  );
};

export default LoginPage;
