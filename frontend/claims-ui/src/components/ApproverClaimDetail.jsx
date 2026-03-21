import { useEffect, useState } from "react";
import { useLocation, useParams } from "react-router-dom";
import api from "../api/axios";

function ApproverClaimDetail(){
    const [claim, setClaim] = useState(null);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(true);
    const {id} = useParams()
    const location = useLocation();
    const [agentResult, setAgentResult] = useState(null);
    const [running, setRunning] = useState(false);

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

    const handleRunAgent = async () => {
        setRunning(true);

        try {
        const res = await api.post(`/approver/claim/${id}/agent-act`);
        setAgentResult(res.data);
        
        // reload claim after decision
        const updated = await api.get(`/claim/get-claim-by-id/${id}`);
        setClaim(updated.data.claim);

        } catch (err) {
        console.error(err);
        } finally {
        setRunning(false);
        }
    };

    if(loading){
        return <p>Loading claim...</p>;
    }
    if (error) return <p style={{ color: "red" }}>{error}</p>;
    if(!claim){
        return <h2>No claim found</h2>
    }

    return (
        <div>
      <h2>Claim {claim.claim_id}</h2>

      <p><strong>Status:</strong> {claim.status}</p>
      <p><strong>Claimed Amount:</strong> ₹{claim.claimed_amount}</p>

      <h3>Form Data</h3>
      <pre>{JSON.stringify(claim.form_data, null, 2)}</pre>

      <h3>Extracted Data</h3>
      <pre>{JSON.stringify(claim.extracted_data, null, 2)}</pre>

      <h3>Evaluation Result</h3>
      <pre>{JSON.stringify(claim.evaluation_result, null, 2)}</pre>

      <h3>Policy Decision</h3>
      <pre>{JSON.stringify(claim.policy_decision, null, 2)}</pre>

      <button onClick={handleRunAgent} disabled={running}>
        {running ? "Running Agent..." : "Run Agent"}
      </button>

      {agentResult && (
        <div style={{ marginTop: "20px", border: "1px solid #333", padding: "10px" }}>
          <h3>Final Agent Decision</h3>
          <pre>{JSON.stringify(agentResult, null, 2)}</pre>
        </div>
      )}
    </div>
    )
}
export default ApproverClaimDetail;