import React, { useRef } from "react";
import { LoginPageProps } from "../Interfaces";
import useLogin from "../hooks/useLogin";
import { useNavigate } from "react-router-dom";
import UserSubmissionForm from "../components/UserSubmissionForm";

const LoginPage = ({ onLogin, isLoggedIn }: LoginPageProps) => {
  const usernameRef = useRef<HTMLInputElement>(null);
  const passwordRef = useRef<HTMLInputElement>(null);
  const { mutate: login, error } = useLogin();
  const navigate = useNavigate();
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
          navigate("/Homepage");
          // Handle successful login (e.g., update state, redirect)
        },
        onError: (error) => {
          console.error("Login failed:", error);
          // Handle login error (e.g., display error message)
        },
      }
    );
  };
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      {isLoggedIn ? (
        <div className="text-green-500 text-xl font-semibold">Logged in</div>
      ) : (
        <>
          <h1 className="text-3xl font-bold mb-4">Login Page</h1>
          <UserSubmissionForm
            handleSubmit={handleSubmit}
            usernameRef={usernameRef}
            passwordRef={passwordRef}
          />
        </>
      )}
      {error && <p style={{ color: "red" }}>{error.message}</p>}
    </div>
  );
};

export default LoginPage;
