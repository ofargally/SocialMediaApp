import React, { useRef } from "react";
import LoginPageProps from "../Interfaces";
import useLogin from "../hooks/useLogin";

const LoginPage = ({ onLogin, isLoggedIn }: LoginPageProps) => {
  const usernameRef = useRef<HTMLInputElement>(null);
  const passwordRef = useRef<HTMLInputElement>(null);
  const { mutate: login, error } = useLogin();

  console.log("page loaded");
  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    //need to get the email and password printed
    const username = usernameRef.current?.value || "";
    const password = passwordRef.current?.value || "";
    console.log("Form submitted:", { username, password });
    login(
      { username, password }, // Variables passed to the mutation function
      {
        onSuccess: (data) => {
          console.log("Login successful:", data);
          onLogin();
          // Handle successful login (e.g., update state, redirect)
        },
        onError: (error) => {
          console.error("Login failed:", error);
          // Handle login error (e.g., display error message)
        },
      }
    );
  };

  const LoginForm = () => {
    return (
      <form
        onSubmit={handleSubmit}
        className="w-full max-w-md bg-white p-8 rounded-lg shadow-md"
      >
        <div className="mb-4">
          <label
            htmlFor="email"
            className="block text-gray-700 text-sm font-bold mb-2"
          >
            Email:
          </label>
          <input
            type="email"
            id="email"
            ref={usernameRef}
            required
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          />
        </div>
        <div className="mb-6">
          <label
            htmlFor="password"
            className="block text-gray-700 text-sm font-bold mb-2"
          >
            Password:
          </label>
          <input
            type="password"
            id="password"
            ref={passwordRef}
            required
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
          />
        </div>
        <button
          type="submit"
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
        >
          Log In
        </button>
      </form>
    );
  };
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      {isLoggedIn ? (
        <div className="text-green-500 text-xl font-semibold">Logged in</div>
      ) : (
        <>
          <h1 className="text-3xl font-bold mb-4">Login Page</h1>
          <LoginForm />
        </>
      )}
      {error && <p style={{ color: "red" }}>{error.message}</p>}
    </div>
  );
};

export default LoginPage;
