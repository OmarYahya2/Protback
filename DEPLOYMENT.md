# Deployment Guide for backpro on Render

## Prerequisites
- GitHub account
- Render account (free tier available)

## Steps to Deploy

### 1. Push Code to GitHub
1. Initialize git repository in the `Protback` folder
2. Add all files to git
3. Push to GitHub repository

### 2. Deploy on Render
1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New" → "Web Service"
3. Connect your GitHub repository
4. Select the repository with your Django code
5. Configure the service:
   - **Name**: `backpro`
   - **Environment**: `Python`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn backendcm.wsgi:application`
   - **Branch**: `main` (or your default branch)

### 3. Environment Variables
Render will automatically set these from the `render.yaml` file:
- `SECRET_KEY` (auto-generated)
- `DEBUG=False`
- `ALLOWED_HOSTS=backpro.onrender.com,omaryahya.vercel.app`
- `EMAIL_HOST_USER=omar.yahya965@gmail.com`
- `EMAIL_HOST_PASSWORD=xpikicmlkyhgkvqo`
- `DATABASE_URL` (from PostgreSQL database)

### 4. Database Setup
Render will automatically create a PostgreSQL database and connect it to your app.

### 5. Your API Endpoints
Once deployed, your API will be available at:
- Base URL: `https://backpro.onrender.com`
- Contact endpoint: `https://backpro.onrender.com/api/contact/`
- Admin panel: `https://backpro.onrender.com/admin/`

### 6. Frontend Integration
Update your frontend at `https://omaryahya.vercel.app` to use:
```javascript
const API_URL = 'https://backpro.onrender.com/api';
```

## Important Notes
- First deployment may take 5-10 minutes
- Free tier services may sleep after 15 minutes of inactivity
- Database will persist data between deployments
- CORS is configured to allow requests from your Vercel app

## Troubleshooting
- Check Render logs for deployment issues
- Ensure all environment variables are set correctly
- Verify database connection in Render dashboard
