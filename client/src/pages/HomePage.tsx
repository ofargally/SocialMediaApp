import { useState } from "react";
import { useAuth } from "../hooks/useAuth";
import Header from "../components/Header";
import Footer from "../components/Footer";

/*
const Homepage = () => {
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

*/

interface Post {
  id: string;
  user: {
    name: string;
    avatar: string;
  };
  content: string;
  timestamp: string;
  likes: number;
}

const SidebarComponent = () => (
  <aside className="hidden md:flex flex-col w-64 p-4 space-y-4 bg-white rounded-lg shadow">
    <nav className="space-y-2">
      <a href="#" className="flex items-center p-2 hover:bg-gray-100 rounded">
        <span className="ml-2">Profile</span>
      </a>
      <a href="#" className="flex items-center p-2 hover:bg-gray-100 rounded">
        <span className="ml-2">Settings</span>
      </a>
    </nav>
  </aside>
);

const PostComponent = ({ post }: { post: Post }) => (
  <div className="w-full bg-white rounded-lg shadow p-4 mb-4">
    <div className="flex items-center mb-4">
      <img src={post.user.avatar} alt="" className="w-10 h-10 rounded-full" />
      <div className="ml-2">
        <h3 className="font-semibold">{post.user.name}</h3>
        <p className="text-sm text-gray-500">{post.timestamp}</p>
      </div>
    </div>
    <p className="mb-4">{post.content}</p>
    <div className="flex items-center space-x-4">
      <button className="flex items-center text-gray-600 hover:text-blue-500">
        <span>{post.likes} Likes</span>
      </button>
      <button className="flex items-center text-gray-600 hover:text-blue-500">
        <span>Comment</span>
      </button>
      <button className="flex items-center text-gray-600 hover:text-blue-500">
        <span>Share</span>
      </button>
    </div>
  </div>
);

const CreatePostComponent = () => (
  <div className="w-full bg-white rounded-lg shadow p-4 mb-4">
    <textarea
      className="w-full p-2 border rounded-lg resize-none"
      placeholder="What's on your mind?"
      rows={3}
    />
    <div className="flex justify-between mt-2">
      <button className="text-gray-600 hover:text-blue-500">Add Photo</button>
      <button className="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600">
        Post
      </button>
    </div>
  </div>
);

const Homepage = () => {
  const auth = useAuth();
  const [posts] = useState<Post[]>([
    {
      id: "1",
      user: {
        name: "John Doe",
        avatar: "https://via.placeholder.com/40",
      },
      content: "This is a sample post content.",
      timestamp: "2 hours ago",
      likes: 10,
    },
  ]);

  return (
    <div>
      <div className="min-h-screen bg-gray-100">
        <Header />
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-24">
          <div className="flex gap-6">
            <SidebarComponent />
            <main className="flex-1 space-y-4">
              <CreatePostComponent />
              {posts.map((post) => (
                <PostComponent key={post.id} post={post} />
              ))}
            </main>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default Homepage;
