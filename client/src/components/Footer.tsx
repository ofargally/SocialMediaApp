const Footer = () => {
  return (
    <footer className="bg-gray-800 text-white py-8 w-full">
      <div className="w-full px-4">
        <div className="flex flex-wrap justify-between">
          <div className="w-full md:w-1/3 mb-4 md:mb-0">
            <h3 className="text-xl font-bold mb-2">Ofargally</h3>
            <p className="text-gray-400">Building amazing web experiences</p>
          </div>
          <div className="w-full md:w-1/3 mb-4 md:mb-0">
            <h3 className="text-xl font-bold mb-2">Contact</h3>
            <p className="text-gray-400">Email: contact@ofargally.com</p>
          </div>
          <div className="w-full md:w-1/3">
            <h3 className="text-xl font-bold mb-2">Follow Us</h3>
            <div className="flex space-x-4">
              <a href="#" className="text-gray-400 hover:text-white">
                Twitter
              </a>
              <a href="#" className="text-gray-400 hover:text-white">
                LinkedIn
              </a>
              <a href="#" className="text-gray-400 hover:text-white">
                GitHub
              </a>
            </div>
          </div>
        </div>
        <div className="text-center mt-8 text-gray-400">
          <p>
            &copy; {new Date().getFullYear()} Ofargally. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
