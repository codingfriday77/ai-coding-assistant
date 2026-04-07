# Deployment Guide for Render

## Overview
This project is configured to deploy on Render.com with:
- **Backend**: FastAPI server running on port 8000
- **Frontend**: Streamlit app running on port 8501
- **Both services deployed separately** for scalability

---

## Prerequisites
1. GitHub account with this repository pushed
2. Render.com account (free tier available)
3. OpenAI API key

---

## Deployment Steps

### 1. Connect Your Repository to Render

1. Go to [render.com](https://render.com)
2. Click **"New +"** → **"Web Service"**
3. Choose **"Deploy existing code from a repository"**
4. Search for and connect your GitHub repository

### 2. Deploy Backend Service

1. **Create First Web Service**
   - Name: `ai-coding-backend`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn backend.app:app --host 0.0.0.0 --port 8000`
   - Instance Type: Free

2. **Add Environment Variable**
   - Key: `OPENAI_API_KEY`
   - Value: `sk-proj-your-actual-key-here`
   - Click **Add**

3. Click **Create Web Service**
4. Wait for deployment to complete (2-5 minutes)
5. Copy the backend URL (e.g., `https://ai-coding-backend.onrender.com`)

### 3. Deploy Frontend Service

1. **Create Second Web Service** (same repo, different service)
   - Name: `ai-coding-frontend`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `streamlit run frontend/main.py --server.port=8501 --server.address=0.0.0.0`
   - Instance Type: Free

2. **Add Environment Variables**
   - Key: `BACKEND_URL`
   - Value: `https://ai-coding-backend.onrender.com` (from step 2)
   - Click **Add**

3. Click **Create Web Service**
4. Wait for deployment to complete

---

## Configuration Files

### `render.yaml`
- Defines both backend and frontend services
- Specifies build and start commands
- Environment variables configuration

### `.streamlit/config.toml`
- Streamlit configuration for production
- Runs headless mode (no browser needed on server)
- Listens on all interfaces (0.0.0.0)

### `start.sh`
- Optional script to run both services locally
- Used for development/testing

### `frontend/main.py`
- Updated to use `BACKEND_URL` environment variable
- Falls back to `localhost:8000` if not set

---

## After Deployment

1. Visit your frontend URL: `https://ai-coding-frontend.onrender.com`
2. Enter a code prompt and select a language
3. Click **"Generate Code"**
4. The frontend will call the backend API to generate code

---

## Troubleshooting

### Frontend can't connect to backend
- Check that `BACKEND_URL` is set correctly in frontend service environment variables
- Ensure backend service is fully deployed and running

### OpenAI API errors
- Verify `OPENAI_API_KEY` is correct in backend environment variables
- Check that your API key has credits available

### Streamlit connection refused
- Free tier on Render may need ~15 seconds to start
- Refresh the page if you get connection errors on first load

### View logs
- On Render dashboard, click service name → **Logs** tab
- Scroll to see deployment and runtime errors

---

## Cost Considerations

- **Free tier**: Includes background services with ~750 hours/month
- **Limitations**: Auto-spins down after 15 mins of inactivity
- **Recommendation**: Use paid tier for production apps ($7/month minimum)

---

## Local Testing

To test locally before deployment:

```bash
# Terminal 1: Start backend
uvicorn backend.app:app --reload

# Terminal 2: Start frontend
streamlit run frontend/main.py
```

Then visit `http://localhost:8501`

---

## Redeploy Changes

All changes pushed to GitHub automatically trigger redeployment on Render.
