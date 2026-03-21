import './App.css'
import { Routes, Route } from "react-router-dom"

import ClaimList from './components/ClaimList'
import ClaimDetails from "./components/ClaimDetails"
import ProtectedRoute from "./components/ProtectedRoute"
import Navbar from "./components/Navbar"
import AuthPage from "./pages/AuthPage"
import CreateClaim from "./components/CreateClaim"
import HospitalClaimList from './components/HospitalClaimList'
import HospitalClaimDetails from './components/HospitalClaimDetails'
import ApproverClaimList from './components/ApproverClaimList'
import ApproverClaimDetail from './components/ApproverClaimDetail'

function App() {
  return (
    <> 
      <Navbar/>
      <Routes>

        <Route path="/login" element={<AuthPage/>} />

        {/* ---------- USER ROUTES START HERE ------------ */}

        <Route path="/claims" element={
          <ProtectedRoute allowedRoles={["USER"]}>
            <ClaimList />
          </ProtectedRoute>
          } />
        <Route path="/claim/:id" element={
          // <ProtectedRoute allowedRoles={["USER"]}>   
            <ClaimDetails />
          // </ProtectedRoute>
          }/>
        <Route path="/create/claim" element={
          <ProtectedRoute allowedRoles={["USER"]}>
            <CreateClaim />
          </ProtectedRoute>
        }/>

        {/* ---------- HOSPITAL ROUTES START HERE ----------- */}
        <Route path='/hospital/claims' element={
          <ProtectedRoute allowedRoles={["HOSPITAL", "USER"]}>
            <HospitalClaimList /> 
          </ProtectedRoute>
        }/>
        <Route
          path="/hospital/claims/:id"
          element={
            <ProtectedRoute allowedRoles={["HOSPITAL"]}>
              <HospitalClaimDetails />
            </ProtectedRoute>
          }
        />


        {/* ---------- APPROVER ROUTES START HERE ------------- */}
          <Route
            path='/approver/dashboard'
            element={
              <ProtectedRoute allowedRoles={["APPROVER"]}>
                <ApproverClaimList />
              </ProtectedRoute>
             } />

          <Route
            path="/approver/claims/:id"
            element={
              <ProtectedRoute allowedRoles={["APPROVER"]}>
                <ApproverClaimDetail />
              </ProtectedRoute>
            }
          />
      </Routes>
    </>
  )
}

export default App
