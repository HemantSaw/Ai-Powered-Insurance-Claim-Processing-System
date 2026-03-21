import { useLocation, useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import api from "../api/axios";

function ClaimDetails(){
    const [claim, setClaim] = useState(null);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(true);
    const {id} = useParams()
    const location = useLocation();

    useEffect(()=>{
        const loadClaim = async()=>{
            try{
                console.log("inside useEffect 123")
                const response =  await api.get(`/claim/get-claim-by-id/${id}`)
                const data = response.data;
                console.log(response);
                setClaim(data.claim);
            }
            catch(err){
                setError("failed to load claim")
            }
            finally{
                setLoading(false);
            }
        }
        if (id) loadClaim();
    }, [id])
    if(loading){
        return <p>Loading claim...</p>;
    }
    if (error) return <p style={{ color: "red" }}>{error}</p>;
    if(!claim){
        return <h2>No claim found</h2>
    }
    
    console.log(claim);
    return (
        <>
        <div>
            <h2>Claim Detail</h2>
            <p>Claim ID: {claim.claim_id}</p>
            <p>Diagnosis: {claim.form_data?.diagnosis}</p>
            <p>Claimed amount: ₹{claim.claimed_amount}</p>
            <p>Policy decision: {claim.policy_decision ? claim.policy_decision.coverage_decision : "NA"}</p>
            <p>Evaluation result: {claim.evaluation_result ? claim.evaluation_result.evaluation_result:  "NA"}</p>
            <p>Claim status : {claim.status}</p>
        </div>
    </>
    )
}

export default ClaimDetails