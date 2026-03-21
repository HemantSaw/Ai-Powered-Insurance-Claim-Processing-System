import { useEffect, useState } from "react";
import api from "../api/axios";
import ClaimCard from "./ClaimCard"
import { useNavigate } from "react-router-dom";

function ClaimList(){
    const [claims, setClaims] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    const navigate = useNavigate()

    useEffect(()=>{
        const loadClaims = async()=>{
            try{
                const response = await api.get("/claim/get-claims")
                const data = response.data;
                setClaims(data.claims_list);
            }
            catch (err) {
                setError("Failed to load claims");
            } finally {
                setLoading(false);
            }
        }

        loadClaims();
    }, []);

    const goToCreateClaim = ()=>{
        navigate("/create/claim")
    }
    return (
        <>
            <div className="claim_container">
                <h2>My Claims</h2>
                <button className="create_claim" onClick={goToCreateClaim}>Create claim</button>
                {claims.map((claim) => (
                    <ClaimCard
                    key={claim.claim_id}
                    claim_id={claim.claim_id}
                    amount={claim.form_data.claimed_amount}
                    status={claim.status}
                    />
                ))}
            </div>
        </>
    )
}

export default ClaimList;