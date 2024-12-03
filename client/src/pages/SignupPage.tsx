import React, { useRef } from "react";
import { SignupPageProps } from "../Interfaces";
import UserSubmissionForm from "../components/UserSubmissionForm";
import useCreateUser from "../hooks/useCreateUser";
import { useNavigate } from "react-router-dom";

const SignupPage = ({ onSignup }: SignupPageProps) => {
  const usernameRef = useRef<HTMLInputElement>(null);
  const passwordRef = useRef<HTMLInputElement>(null);
  const { mutate: createUser, error } = useCreateUser();
  const navigate = useNavigate();

  console.log("page loaded");
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
          navigate("/login");
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
      <>
        <h1 className="text-3xl font-bold mb-4">Signup Page</h1>
        <UserSubmissionForm
          handleSubmit={handleSubmit}
          usernameRef={usernameRef}
          passwordRef={passwordRef}
        />
      </>
      {error && <p style={{ color: "red" }}>{error.message}</p>}
    </div>
  );
};

export default SignupPage;
