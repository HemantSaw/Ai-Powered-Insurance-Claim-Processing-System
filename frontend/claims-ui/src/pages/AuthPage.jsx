import { useEffect, useState } from "react";
import LoginForm from "../components/LoginForm";
import RegisterForm from "../components/RegisterForm";
import "../styles/auth.css";
import { useAuth } from "../context/AuthContext";

function AuthPage() {
  const [activeTab, setActiveTab] = useState("login");
  // const {logout} = useAuth()
  // useEffect(()=>{
  //   logout();
  // },[])
  return (
    <div className="auth-container">
      <div className="auth-card">
        
        {/* Tabs */}
        <div className="auth-tabs">
          <button
            className={activeTab === "login" ? "active" : ""}
            onClick={() => setActiveTab("login")}
          >
            Login
          </button>

          <button
            className={activeTab === "register" ? "active" : ""}
            onClick={() => setActiveTab("register")}
          >
            Register
          </button>
        </div>

        {/* Forms */}
        <div className="auth-content">
          {activeTab === "login" && <LoginForm />}
          {activeTab === "register" && <RegisterForm />}
        </div>

      </div>
    </div>
  );
}

export default AuthPage;
