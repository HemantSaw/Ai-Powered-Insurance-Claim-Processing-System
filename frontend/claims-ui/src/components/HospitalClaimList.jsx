import { useEffect, useState } from "react";
import api from "../api/axios";
import { Link, useParams } from "react-router-dom";

function HospitalClaimList(){
    const [claims, setClaims] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null)
    const param = useParams()
    useEffect(()=>{
        const loadClaims = async()=>{
            try{
                const response = await api.get("/claim/get-all-claims")
                const data = response.data;
                console.log("get all claims", data);
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
        <>
            <div>
                <h2>Hospital Claims</h2>
                <span>{loading ? "..fetching" : ""}</span>
                {claims.map((claim) => (
                    <div 
                    style={{
                        border: "1px solid #ccc",
                        padding: "10px",
                        marginBottom: "10px",
                        cursor: "pointer"
                        }}
                    >
                    <p>Claim id {claim.claim_id}</p>
                    <p>Claimed Amount: {claim.claimed_amount}</p>
                    {claim.status == "CREATED" ? <Link to={`/hospital/claims/${claim.claim_id}`}>
                        View & Upload Documents
                    </Link> : <p>claim status : {claim.status}</p>}
                    </div>
                ))}
            </div>
        </>
    )
}

export default HospitalClaimList;