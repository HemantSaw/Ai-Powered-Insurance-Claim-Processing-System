import { createContext, useContext, useState } from "react";
import { useNavigate } from "react-router-dom";

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [token, setToken] = useState(localStorage.getItem("token"));
  const [userRole, setUserRole] = useState(localStorage.getItem("userRole"));

  const navigate = useNavigate()

  const login = (token, userRole) => {
    localStorage.setItem("token", token);
    localStorage.setItem("userRole", userRole);
    setToken(token);
    setUserRole(userRole);
  };

  const logout = () => {
    localStorage.clear();
    setToken(null);
    setUserRole(null);
    navigate("/login");
    console.log("logged out")
  };

  return (
    <AuthContext.Provider value={{ token, userRole, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);
