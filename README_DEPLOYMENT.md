# backpro - Django Backend Deployment

## 📋 Overview
Your Django backend is now ready for deployment on Render with the service name **backpro**. All necessary configuration files have been created and your frontend at `https://omaryahya.vercel.app` is configured to work with the deployed backend.

## 🎯 What's Been Configured

### ✅ Files Created/Modified:
1. **`requirements.txt`** - All Python dependencies including production packages
2. **`render.yaml`** - Render deployment configuration with service name "backpro"
3. **`build.sh`** - Build script for Render deployment
4. **`settings.py`** - Updated for production with environment variables
5. **`runtime.txt`** - Python version specification
6. **`.gitignore`** - Git ignore patterns
7. **`deploy.py`** - Deployment helper script
8. **`.env.example`** - Environment variables template

### ⚙️ Production Settings:
- **Database**: PostgreSQL (automatically provisioned by Render)
- **Static Files**: WhiteNoise for serving static files
- **CORS**: Configured to allow your Vercel frontend
- **Security**: Production-ready settings with environment variables
- **Email**: Gmail SMTP configuration preserved

### 🌐 API Endpoints:
Once deployed, your API will be available at:
- **Base URL**: `https://backpro.onrender.com`
- **Contact Form**: `https://backpro.onrender.com/api/contact/`
- **User Accounts**: `https://backpro.onrender.com/api/accounts/`
- **Admin Panel**: `https://backpro.onrender.com/admin/`

## 🚀 Deployment Steps

### 1. Push to GitHub
```bash
# Initialize git repository
git init
git add .
git commit -m "Initial commit - Django backend for deployment"

# Add your GitHub repository
git remote add origin https://github.com/yourusername/your-repo.git
git push -u origin main
```

### 2. Deploy on Render
1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **"New"** → **"Web Service"**
3. Connect your GitHub repository
4. The `render.yaml` file will automatically configure:
   - Service name: **backpro**
   - Environment: Python
   - Build command: `./build.sh`
   - Start command: `gunicorn backendcm.wsgi:application`
   - Database: PostgreSQL (free tier)

### 3. Environment Variables (Auto-configured)
These are set automatically from `render.yaml`:
- `SECRET_KEY`: Auto-generated secure key
- `DEBUG`: False (production mode)
- `ALLOWED_HOSTS`: backpro.onrender.com,omaryahya.vercel.app
- `DATABASE_URL`: Auto-configured PostgreSQL connection
- `EMAIL_HOST_USER`: omar.yahya965@gmail.com
- `EMAIL_HOST_PASSWORD`: Your Gmail app password

## 🔗 Frontend Integration

Update your frontend code at `https://omaryahya.vercel.app` to use the new backend:

```javascript
// Replace any localhost URLs with:
const API_BASE_URL = 'https://backpro.onrender.com/api';

// Example: Contact form submission
const submitContactForm = async (formData) => {
  const response = await fetch(`${API_BASE_URL}/contact/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(formData)
  });
  return response.json();
};
```

## 📝 Important Notes

### 🕐 First Deployment
- Initial deployment may take 5-10 minutes
- Database migrations will run automatically
- Static files will be collected automatically

### 💰 Free Tier Limitations
- Service may sleep after 15 minutes of inactivity
- Database has storage limits on free tier
- Cold start may take 30-60 seconds after sleep

### 🔒 Security
- DEBUG is disabled in production
- Secret key is auto-generated
- CORS is restricted to your frontend domain
- Database credentials are managed by Render

## 🛠️ Maintenance

### Database Migrations
New migrations will run automatically on each deployment via `build.sh`

### Environment Variables
Update them in the Render dashboard under your service settings

### Logs
Access logs through the Render dashboard for debugging

## 🎉 You're Ready!

Your Django backend is fully configured for production deployment on Render. Once deployed, your frontend at `https://omaryahya.vercel.app` will be able to communicate with your backend at `https://backpro.onrender.com`.

The contact form and any other API endpoints will work seamlessly between your Vercel frontend and Render backend!
