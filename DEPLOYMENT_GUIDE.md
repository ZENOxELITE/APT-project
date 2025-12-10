# 🚀 Railway Deployment Guide - MonarchTime

## Quick Start (5 Minutes)

### 1. Push to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - MonarchTime watch store"

# Set main branch
git branch -M main

# Add your GitHub repository
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git push -u origin main
```

### 2. Deploy on Railway

1. **Go to Railway**
   - Visit: https://railway.app
   - Click "Login" and sign in with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Authorize Railway to access your repositories
   - Select your MonarchTime repository

3. **Automatic Deployment**
   - Railway will automatically:
     - Detect it's a Django project
     - Install dependencies from `requirements.txt`
     - Run migrations
     - Collect static files
     - Start the server with Gunicorn

4. **Get Your URL**
   - Click on your project
   - Go to "Settings" → "Domains"
   - Click "Generate Domain"
   - Your site will be live at: `your-app-name.up.railway.app`

### 3. Create Admin User (Optional)

To access the admin panel:

1. In Railway dashboard, click on your project
2. Go to "Settings" → "Service"
3. Scroll down and click "Open Terminal"
4. Run:
```bash
python manage.py createsuperuser
```
5. Follow the prompts to create your admin account
6. Access admin at: `your-app-name.up.railway.app/admin`

## 📱 Using Your App

### From Mobile
- Visit your Railway URL on your phone
- Navigate to "Add Product"
- Fill in the form and upload images
- Products will be saved and visible immediately!

### From Desktop
- Same process - works on any device
- All changes sync in real-time

## 🔧 Configuration (Optional)

### Environment Variables

In Railway dashboard:
1. Click on your project
2. Go to "Variables" tab
3. Add these (optional):

```
DEBUG=False
SECRET_KEY=your-secret-key-here
```

### Custom Domain

1. In Railway dashboard, go to "Settings" → "Domains"
2. Click "Custom Domain"
3. Add your domain and follow DNS instructions

## ✅ What's Included

All these files are already configured:
- ✅ `railway.json` - Railway configuration
- ✅ `Procfile` - Start command
- ✅ `requirements.txt` - Python dependencies
- ✅ `runtime.txt` - Python version
- ✅ Settings updated for production

## 🎯 Features That Work

- ✅ Add/Edit/Delete products
- ✅ Upload images (persist across deployments)
- ✅ SQLite database (or upgrade to PostgreSQL)
- ✅ Mobile responsive
- ✅ Static files served via Whitenoise
- ✅ Admin panel
- ✅ All CRUD operations

## 💡 Tips

1. **First Deployment**: May take 2-3 minutes
2. **Subsequent Deploys**: Automatic on every git push
3. **Database**: Persists between deployments
4. **Images**: Stored in `/media` folder (persistent)
5. **Logs**: View in Railway dashboard under "Deployments"

## 🆘 Troubleshooting

### Site not loading?
- Check Railway logs in dashboard
- Ensure all files are committed and pushed
- Verify `requirements.txt` is present

### Images not uploading?
- Check file size (Railway has limits)
- Verify media folder permissions
- Check Railway logs for errors

### Database reset?
- Railway persists SQLite by default
- For production, consider PostgreSQL (Railway offers free tier)

## 🎉 You're Done!

Your MonarchTime watch store is now live and accessible from anywhere!

Share your Railway URL and start adding products! 🚀
