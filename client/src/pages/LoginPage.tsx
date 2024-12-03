import React, { useRef } from "react";
import { LoginPageProps } from "../Interfaces";
import UserSubmissionForm from "../components/UserSubmissionForm";
import { useAuth } from "../hooks/useAuth";

const LoginPage = ({ isLoggedIn }: LoginPageProps) => {
  const usernameRef = useRef<HTMLInputElement>(null);
  const passwordRef = useRef<HTMLInputElement>(null);
  const auth = useAuth();
  console.log("page loaded");
  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    //need to get the email and password printed
    const username = usernameRef.current?.value || "";
    const password = passwordRef.current?.value || "";
    console.log("Form submitted:", { username, password });
    auth.loginAction({ username, password });
    console.log("ERROR:", auth.error);
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
      {auth.error && <p style={{ color: "red" }}>{auth.error.message}</p>}
    </div>
  );
};

export default LoginPage;
