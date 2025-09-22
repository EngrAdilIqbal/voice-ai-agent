
##AI Voice Agent Tool

An end-to-end **AI Voice Agent** application that enables automated calling, call monitoring, and transcript summarization.
This project is built with a **React frontend**, a **FastAPI backend**, and uses **Supabase** for database storage.

⚠️ **Note**: For security reasons, API keys (OpenAI, Retell) have been removed from this repository. Please configure your own `.env` file before running.

---

## 🏗️ Project Structure

```
ai-voice-agent-tool/
│── backend/         # FastAPI backend (AI logic, DB, API integrations)
│── frontend/        # React frontend (Dashboard UI)
│── database/        # Supabase setup & schema
│── README.md        # Project documentation
```

---

## ⚙️ Tech Stack

* **Backend**: FastAPI, Python, Uvicorn
* **Frontend**: React (Vite), TailwindCSS, shadcn/ui
* **Database**: Supabase (Postgres + Auth + Storage)
* **AI**: OpenAI GPT models (summarization, agent logic)
* **Telephony**: Retell API (voice call handling)

---

## 🔑 Environment Variables

Create a `.env` file inside the `backend/` folder:

```ini
# OpenAI
OPENAI_API_KEY=your_openai_api_key_here

# Retell API
RETELL_API_KEY=your_retell_api_key_here

# Supabase
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_service_role_key
```

⚠️ Do **not** commit this file to GitHub.

---

## 🖥️ Setup & Installation

### 1️⃣ Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate    # (Linux/Mac)
venv\Scripts\activate       # (Windows)

pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

Backend will run on: **[http://localhost:8000](http://localhost:8000)**

---

### 2️⃣ Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend will run on: **[http://localhost:5173](http://localhost:5173)**

---

### 3️⃣ Database (Supabase)

* Create a project at [Supabase](https://supabase.com).
* Configure tables for **Drivers**, **Calls**, and **Configs**.
* Update `.env` with your **Supabase URL** and **Service Role Key**.

---

## Features

✅ **Driver & Load Management** – Store driver details and load numbers in Supabase
✅ **Call Initiation** – Start AI-driven calls directly from the dashboard
✅ **Live Call Monitoring** – Track call sessions via Retell API
✅ **Transcript Summarization** – Auto-generate call summaries using OpenAI GPT
✅ **Professional Dashboard** – Modern UI with TailwindCSS & shadcn/ui

---

## Security Notes

* API keys are **not included** in this repo.
* Use `.env` file to manage credentials.
* Do not expose API keys in frontend code.
* Rotate keys if compromised.

---

## 🚀 Deployment

* **Backend**: Deploy on Render, Railway, or AWS/GCP/Azure
* **Frontend**: Deploy on Vercel or Netlify
* **Database**: Supabase (managed PostgreSQL)
