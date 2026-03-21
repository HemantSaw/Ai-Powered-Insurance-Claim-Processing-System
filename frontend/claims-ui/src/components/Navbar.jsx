import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import "../styles/navbar.css";

function Navbar() {
  const { userRole, logout } = useAuth();

  return (
    <nav className="navbar">
      <h3>Insurance Claimer</h3>

      {userRole && (
        <div>
          <span className="user">{userRole}</span>
          <button className="logout" onClick={logout}>Logout</button>
        </div>
      )}
    </nav>
  );
}

export default Navbar;
