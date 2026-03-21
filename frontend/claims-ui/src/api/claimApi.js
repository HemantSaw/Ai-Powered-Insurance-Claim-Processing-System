import api from "./axios"

// fetch all claims
export const fetchClaims = async () => {
  const response = await api.get("/claim/get-claims")
  return response.data
}

// fetch single claim
export const fetchClaimById = async (id) => {
  const response = await api.get(`/claims/${id}`)
  return response.data
}
