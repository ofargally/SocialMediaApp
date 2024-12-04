import React, { useRef } from "react";
import UserSubmissionForm from "../components/UserSubmissionForm";
import { useAuth } from "../hooks/useAuth";
import { useNavigate } from "react-router-dom";
const LoginPage = () => {
  const usernameRef = useRef<HTMLInputElement>(null);
  const passwordRef = useRef<HTMLInputElement>(null);
  const auth = useAuth();
  const navigate = useNavigate();
  console.log(auth.token);
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
      {auth.token ? (
        <>
          <div className="text-green-500 text-xl font-semibold">Logged in</div>
          <button
            onClick={() => navigate("/Homepage")}
            className="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
          >
            Go to Homepage
          </button>
        </>
      ) : (
        <>
          <h1 className="text-3xl font-bold mb-4">Login Page</h1>
          <UserSubmissionForm
            handleSubmit={handleSubmit}
            usernameRef={usernameRef}
            passwordRef={passwordRef}
          />
          {auth.error && <p style={{ color: "red" }}>{auth.error.message}</p>}
        </>
      )}
    </div>
  );
};

export default LoginPage;
