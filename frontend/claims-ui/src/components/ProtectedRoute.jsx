import { Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

function ProtectedRoute({ allowedRoles, children }){
    const {token, userRole} = useAuth();
    if (!token) {
        return <Navigate to="/login" />;
    }
    if (!allowedRoles.includes(userRole)) {
        return <Navigate to="/login" />;
    }
    return children;
}

export default ProtectedRoute;