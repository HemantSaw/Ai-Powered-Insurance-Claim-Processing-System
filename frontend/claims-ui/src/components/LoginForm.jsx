import { useState } from "react"
import { useNavigate } from "react-router-dom"
import { useAuth } from "../context/AuthContext"
import api from "../api/axios" 

function LoginForm(){
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [error, setError] = useState(null)

    const navigate = useNavigate()

    const {login} = useAuth();

    const handleSubmit = async(e)=>{
        e.preventDefault() //stop the browsers page refresh
        try{      
            const response = await api.post("/user/login", {
                username, password
            })
            console.log("in line 18 of login page. ",response);
            const token = response.data.token;
            const userRole = response.data.role;

            // localStorage.setItem("token", token);
            // localStorage.setItem('userRole', userRole)
            login(token, userRole);

            if (userRole === "USER") navigate("/claims")
            else if (userRole === "HOSPITAL") navigate("/hospital/claims")
            else if (userRole === "APPROVER") navigate("/approver/dashboard")
        }
        catch(err){
            setError("Invalid credentials")
        }
    }

    return (
        <>
            
            {error && <p style={{ color: "red" }}>{error}</p>}
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Username</label><br />
                    <input
                        type="text"
                        placeholder="Enter your username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                </div>
                <div>
                    <label>Password</label><br />
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
                </div>
                <button type="submit">Login</button>
            </form>
        </>
    )
}

export default LoginForm