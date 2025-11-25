# 🚀 Deployment Guide

This guide outlines the steps to deploy the **Carbon-Aware SQL Engine** to a production environment using **Render** (Backend) and **Streamlit Cloud** (Frontend).

---

## 🏗️ Backend Deployment (Render)

We will deploy the FastAPI backend, PostgreSQL database, and Redis scheduler on Render.

### 1. Database Setup (PostgreSQL)
1.  Log in to [Render Dashboard](https://dashboard.render.com/).
2.  Click **New +** -> **PostgreSQL**.
3.  **Name**: `energy-ml-db`
4.  **Region**: Choose a region close to your users (e.g., Oregon, Frankfurt).
5.  **Plan**: Free (for testing) or Starter.
6.  **Create Database**.
7.  **Copy the `Internal Database URL`** (for internal services) and `External Database URL` (for local access if needed).

### 2. Redis Setup
1.  Click **New +** -> **Redis**.
2.  **Name**: `energy-ml-redis`
3.  **Region**: Same as your database.
4.  **Plan**: Free.
5.  **Create Redis**.
6.  **Copy the `Internal Redis URL`**.

### 3. Web Service (FastAPI)
1.  Click **New +** -> **Web Service**.
2.  Connect your GitHub repository.
3.  **Name**: `energy-ml-api`
4.  **Runtime**: Python 3.
5.  **Build Command**: `pip install -r requirements.txt`
6.  **Start Command**: `uvicorn src.api:app --host 0.0.0.0 --port 10000`
7.  **Environment Variables**:
    *   `DATABASE_URL`: Paste the *Internal Database URL* from Step 1.
    *   `REDIS_URL`: Paste the *Internal Redis URL* from Step 2.
    *   `ELECTRICITYMAPS_API_TOKEN`: Your API token.
    *   `ENERGY_ML_API_KEY`: Generate a strong secret key.
    *   `ENVIRONMENT`: `production`
    *   `PYTHON_VERSION`: `3.9.13` (or your local version)

### 4. Scheduler Service (Background Worker)
1.  Click **New +** -> **Background Worker**.
2.  Connect the same repository.
3.  **Name**: `energy-ml-scheduler`
4.  **Runtime**: Python 3.
5.  **Build Command**: `pip install -r requirements.txt`
6.  **Start Command**: `python -m src.scheduler.worker`
7.  **Environment Variables**: Same as Web Service.

---

## 🎨 Frontend Deployment (Streamlit Cloud)

We will deploy the dashboard on Streamlit Cloud.

1.  Log in to [Streamlit Cloud](https://streamlit.io/cloud).
2.  Click **New app**.
3.  Select your repository, branch, and main file path: `decision_app.py`.
4.  **Advanced Settings** -> **Secrets**:
    ```toml
    API_URL = "https://your-render-api-url.onrender.com"
    ENERGY_ML_API_KEY = "your-secret-key-from-render"
    ```
    *Note: Replace the URL with your actual Render Web Service URL.*
5.  **Deploy!**

---

## ✅ Verification

1.  Open your Streamlit App URL.
2.  Verify the "API Status" in the footer shows "🟢 Connected".
3.  Run a test query to ensure the full pipeline (Frontend -> API -> DB) is working.
