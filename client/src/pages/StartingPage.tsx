import { useNavigate } from "react-router-dom";

const StartingPage = () => {
  const navigate = useNavigate();
  navigate("/login");
  return <div>StartingPage</div>;
};

export default StartingPage;
