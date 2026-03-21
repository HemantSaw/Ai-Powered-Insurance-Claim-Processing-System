import { useState } from "react";
import { useParams } from "react-router-dom";
import api from "../api/axios";

function HospitalClaimDetails(){
    const { id } = useParams();
    const [file, setFile] = useState(null);
    const [message, setMessage] = useState(null);

    const handleFileUpload = async(e)=>{
        e.preventDefault();

        if (!file) return;

        // const res = api.post(..., {"file": file})
        const formData = new FormData();
        formData.append("file", file);
        console.log("moving to call the api or not")
        try {
            await api.post(`/document/claims/${id}/documents`, formData);
            setMessage("Document uploaded successfully");
        } catch (err) {
            setMessage("Upload failed", err);
        }
    }
    return (
    <div>
      <h2>Upload Documents for Claim ID {id}</h2>

      {message && <p>{message}</p>}

      <form onSubmit={handleFileUpload}>
        <input
          type="file"
          accept=".pdf,.png,.jpg,.jpeg"
          onChange={(e) => setFile(e.target.files[0])}
        />
        <button type="submit">Upload</button>
      </form>
    </div>
  );
}
export default HospitalClaimDetails;