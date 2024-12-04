import { useAuth } from "../hooks/useAuth";
const Header = () => {
  const auth = useAuth();
  return (
    <header className="bg-white shadow fixed top-0 left-0 right-0 z-10">
      <div className="container mx-auto px-4 py-4">
        <div className="flex justify-between items-center">
          <h1 className="text-2xl font-bold text-gray-900">AI SOCIAL</h1>
          <div className="flex items-center gap-4">
            <input
              type="search"
              placeholder="Search..."
              className="w-64 px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <button
              onClick={() => auth.logOut()}
              className="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600"
            >
              Log out
            </button>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
