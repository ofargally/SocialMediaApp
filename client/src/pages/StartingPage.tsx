import { useNavigate } from "react-router-dom";

const StartingPage = () => {
  const navigate = useNavigate();
  return (
    <div className="min-h-screen flex flex-col">
      <header className="text-center text-2xl font-bold mt-4">
        SocialMediaApp
      </header>
      <div className="flex flex-col items-center text-center p-4 text-lg">
        <p>
          Hi, this is my Social media app, developed to experiment with the
          FastAPI + React stack. To get started, please click on the log in
          button or the sign up button below!
        </p>
      </div>
      <div className="flex flex-col items-center space-y-4 mt-4">
        <button
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
          onClick={() => navigate("/LoginPage")}
        >
          Log in
        </button>
        <button
          className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
          onClick={() => navigate("/SignupPage")}
        >
          Sign up
        </button>
      </div>
      <footer className="text-center mt-auto mb-4">ofargally</footer>
    </div>
  );
};

export default StartingPage;
