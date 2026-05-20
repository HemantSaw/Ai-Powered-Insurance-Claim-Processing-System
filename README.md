# Agentic AI Insurance Claim Processing System

An end-to-end AI-powered insurance claim automation platform that combines LLM-based agent orchestration, OCR-powered document intelligence, and human-in-the-loop claim approval workflows.

The system simulates a real-world insurance ecosystem with separate personas for Users, Hospitals, and Approvers, enabling secure claim creation, medical document processing, automated evaluation, and intelligent decision-making.

---

# 🚀 Features

## 🔐 Authentication & Authorization
- JWT-based secure authentication
- Role-based access control (RBAC)
- Separate personas:
  - User
  - Hospital
  - Approver
- Protected frontend and backend routes

---

## 👤 User Portal
- Register/Login
- Create insurance claims
- View personal claims
- Track claim status lifecycle
- View claim details and AI evaluation results

---

## 🏥 Hospital Portal
- View assigned claims
- Upload medical documents (PDF/Image)
- OCR-ready document pipeline
- Trigger AI extraction workflows

---

## 🤖 Agentic AI Claim Evaluation Engine

Implemented a ReAct-style LLM orchestration system capable of autonomously:

- Extracting structured medical information from OCR text
- Comparing extracted data with submitted form data
- Detecting inconsistencies and mismatches
- Validating insurance policy balance and eligibility
- Generating structured claim decisions
- Escalating ambiguous claims for human review

### Decision Types
- APPROVE
- REJECT
- NEEDS_HUMAN_REVIEW

---

## 🧠 Human-in-the-Loop Workflow

The system follows a conservative decision architecture:

- High-confidence claims → automated recommendation
- Ambiguous or risky claims → escalated to Approver
- Final decisions remain auditable and explainable

---

# 🏗️ System Architecture

```text
User Creates Claim
        ↓
Hospital Uploads Documents
        ↓
OCR + Medical Data Extraction
        ↓
LLM Agent Evaluation
        ↓
Policy Balance Validation
        ↓
Decision Engine
   ↙          ↘
APPROVE   NEEDS_REVIEW
                ↓
         Human Approver
```

---

# ⚙️ Tech Stack

## Frontend
- React (Vite)
- React Router
- Axios
- Context API

## Backend
- Flask
- SQLAlchemy
- JWT Authentication
- Flask Blueprints

## AI / Agentic Layer
- Azure OpenAI / GPT-4
- ReAct Agent Architecture
- Tool Calling Workflow
- OCR Pipeline (EasyOCR)

## Database
- SQLite (development)
- Easily extensible to PostgreSQL/MySQL

---

# 🧩 Core AI Tools

The ReAct agent uses tool-based reasoning with the following tools:

- get_claim_context
- extract_medical_data
- evaluate_claim_data
- check_policy_balance
- move_to_review
- send_to_human

---

# 📌 Claim Lifecycle

```text
CREATED
   ↓
DOCUMENTS_UPLOADED
   ↓
EXTRACTED
   ↓
EVALUATED
   ↓
AUTO_APPROVED_CANDIDATE
        OR
NEEDS_HUMAN_REVIEW
        OR
REJECTED
```

---

# 🔒 Security Highlights

- JWT-secured APIs
- Role-based route protection
- Backend-driven identity validation
- Secure multipart file uploads
- Persona-restricted workflows

---

# 📂 Project Structure

```text
frontend/
 ├── src/
 │    ├── pages/
 │    ├── components/
 │    ├── context/
 │    ├── api/
 │    └── styles/

backend/
 ├── models/
 ├── routes/
 ├── services/
 ├── agents/
 ├── tools/
 ├── utils/
 └── app.py
```

---

# ▶️ Running the Project

## Backend Setup

```bash
cd backend

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python app.py
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

# 🔮 Future Improvements

- LangGraph-based agent orchestration
- Fraud detection engine
- Multi-agent collaboration
- Real-time notifications
- Vector database for medical semantic search
- Cloud deployment (Docker + Kubernetes)
- Async workflow execution with Celery/Redis

---

# 📖 Key Learnings

This project focuses on combining:
- Deterministic backend business logic
- Probabilistic LLM reasoning
- Human-in-the-loop AI systems
- Real-world workflow orchestration
- Secure full-stack architecture

---

# 👨‍💻 Author

Hemant Saw  
Software Developer | AI Enthusiast | Building Agentic AI Systems
