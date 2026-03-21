import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios";

function CreateClaim(){
    const [patientName, setPatientName] = useState("");
    const [diagnosis, setDiagnosis] = useState("");
    const [policyId, setPolicyId] = useState();
    const [claimedAmount, setClaimedAmount] = useState();
    const [admissionDate, setAdmissionDate] = useState("");
    const [dischargeDate, setDischargeDate] = useState("");
    const [error, setError] = useState(null);

    const navigate = useNavigate();

    const handleSubmit = async(e) => {
        e.preventDefault(); //stop the browsers to refresh page

        try{
            const res = await api.post("/claim/create-claim",{"patient_name" :patientName, "policy_id" : policyId, "diagnosis": diagnosis, "claimed_amount" : claimedAmount, "admission_date" : admissionDate, "discharge_date" : dischargeDate} )

            console.log(res);
            navigate("/claims");
        }
        catch(err){
            setError("Failed to create claim");
        }
    }

    return (
        <>  
            <div>
                <h2>Create Claim</h2>

                {error && <p style={{ color: "red" }}>{error}</p>}

                <form onSubmit={handleSubmit}>
                    <input
                    placeholder="Patient name"
                    value={patientName}
                    onChange={(e) => setPatientName(e.target.value)}
                    />

                    <input
                    type="number"
                    placeholder="Policy Id"
                    value={policyId}
                    onChange={(e) => setPolicyId(e.target.value)}
                    />

                    <input
                    placeholder="Diagnosis"
                    value={diagnosis}
                    onChange={(e) => setDiagnosis(e.target.value)}
                    />

                    <input
                    type="number"
                    placeholder="Claimed Amount"
                    value={claimedAmount}
                    onChange={(e) => setClaimedAmount(e.target.value)}
                    />

                    <input
                    type="date"
                    value={admissionDate}
                    onChange={(e) => setAdmissionDate(e.target.value)}
                    />

                    <input
                    type="date"
                    value={dischargeDate}
                    onChange={(e) => setDischargeDate(e.target.value)}
                    />

                    <button type="submit">Submit Claim</button>
                </form>
            </div>

        </>
    )
    
}
export default CreateClaim;