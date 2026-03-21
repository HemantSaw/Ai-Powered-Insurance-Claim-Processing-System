import { useState } from "react";
import api from "../api/axios";

function RegisterForm() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const res = await api.post("/user/register", {
      username,
      password,
      email
    });

    console.log(res.data);

    setMessage("Registered successfully. Please login.");
  };

  return (
    <form onSubmit={handleSubmit}>
      {message && <p>{message}</p>}

      <input
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      {/* <select value={role} onChange={(e) => setRole(e.target.value)}>
        <option value="USER">User</option>
        <option value="HOSPITAL">Hospital</option>
      </select> */}

      <button type="submit">Register</button>
    </form>
  );
}

export default RegisterForm;
