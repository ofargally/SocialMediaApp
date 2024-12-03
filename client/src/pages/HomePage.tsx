import { useAuth } from "../hooks/useAuth";

const HomePage = () => {
  const auth = useAuth();
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <header className="w-full bg-blue-500 text-white py-4">
        <h1 className="text-center text-3xl font-bold">
          Welcome to the HomePage
        </h1>
      </header>
      <main className="flex-grow flex flex-col items-center justify-center">
        <p className="text-lg text-gray-700">
          This is the main content of the HomePage.
        </p>
        <button
          onClick={() => auth.logOut()}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mt-4"
        >
          Log out
        </button>
      </main>
      <footer className="w-full bg-blue-500 text-white py-2">
        <p className="text-center">© 2023 Your Company</p>
      </footer>
    </div>
  );
};

export default HomePage;
