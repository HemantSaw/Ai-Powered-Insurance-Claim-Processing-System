import { useEffect, useState } from "react";
import api from "../api/axios";
import { Link } from "react-router-dom";

function ApproverClaimList(){
    const [claims, setClaims] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null)

    useEffect(()=>{
        const loadClaims = async()=>{
            try{
                const response = await api.get("/claim/get-all-claims")
                const data = response.data;
                console.log("get all claims in approver", data);
                setClaims(data.claim_list);
            }
            catch(err){
                setError("Failed to load claims");
            }
            finally{
                setLoading(false)
            }
        }
        loadClaims();
    }, [])

    if(!claims){
        return <p>No claims to review</p>
    }
    return (
        <div>
            <h2>Approver Dashboard</h2>

            {claims.map((claim) => (
                <div key={claim.id} style={{ border: "1px solid #ccc", padding: "10px", marginBottom: "10px" }}>
                <p><strong>Claim ID:</strong> {claim.claim_id}</p>
                <p><strong>Status:</strong> {claim.status}</p>

                <Link to={`/approver/claims/${claim.claim_id}`}>
                    Review Claim
                </Link>
                </div>
            ))}
        </div>
    )
}

export default ApproverClaimList;