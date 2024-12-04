import React, { useRef } from "react";
import { SignupPageProps } from "../Interfaces";
import UserSubmissionForm from "../components/UserSubmissionForm";
import useCreateUser from "../hooks/useCreateUser";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../hooks/useAuth";

const SignupPage = ({ isSignedUp, onSignup }: SignupPageProps) => {
  const usernameRef = useRef<HTMLInputElement>(null);
  const passwordRef = useRef<HTMLInputElement>(null);
  const { mutate: createUser, error } = useCreateUser();
  const navigate = useNavigate();
  const auth = useAuth();

  console.log("page loaded");
  console.log("isSignedUp", isSignedUp);
  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    //need to get the email and password printed
    const username = usernameRef.current?.value || "";
    const password = passwordRef.current?.value || "";
    console.log("Form submitted:", { username, password });
    createUser(
      { username, password }, // Variables passed to the mutation function
      {
        onSuccess: (data) => {
          console.log("Login successful:", data);
          onSignup();
          auth.logOut();
          navigate("/LoginPage");
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
      {isSignedUp ? (
        <>
          <div className="text-green-500 text-xl font-semibold">Signed up</div>
          <div className="flex space-x-4 mb-4">
            <button
              onClick={() => navigate("/")}
              className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
            >
              Home
            </button>
            <button
              onClick={() => {
                onSignup();
              }}
              className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
            >
              Create New Account
            </button>
            <button
              onClick={() => navigate("/LoginPage")}
              className="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600 transition-colors"
            >
              Login
            </button>
          </div>
        </>
      ) : (
        <>
          <div className="flex space-x-4 mb-4"></div>
          <h1 className="text-3xl font-bold mb-4">Signup Page</h1>
          <UserSubmissionForm
            handleSubmit={handleSubmit}
            usernameRef={usernameRef}
            passwordRef={passwordRef}
          />
          {error && <p style={{ color: "red" }}>{error.message}</p>}
        </>
      )}
    </div>
  );
};

export default SignupPage;
