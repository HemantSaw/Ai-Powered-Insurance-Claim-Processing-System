import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
function ClaimCard(props){
    const navigate = useNavigate();
    return (
    <>
        <div 
            onClick={() => navigate(`/claim/${props.claim_id}`)} 
            style={{
            border: "1px solid #ccc",
            padding: "10px",
            marginBottom: "10px",
            cursor: "pointer"
            }}
        >
            <p><strong>Claim ID:</strong> {props.claim_id}</p>
            <p><strong>Amount:</strong> ₹{props.amount}</p>
            <p><strong>Status:</strong> {props.status}</p>
        </div>
    </>
    )
}

export default ClaimCard