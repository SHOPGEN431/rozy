# Vercel Deployment Guide

This guide will help you deploy your LLC Directory Flask application to Vercel.

## 🚀 Quick Deployment Steps

### 1. Prepare Your Repository

Ensure your project structure looks like this:
```
rozy/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel configuration
├── DEPLOYMENT.md         # This file
├── README.md             # Project documentation
├── LLC Data.csv          # Your data file
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── service.html
│   ├── service_state.html
│   ├── top10_llc_services.html
│   ├── about.html
│   ├── contact.html
│   ├── privacy_policy.html
│   └── terms_and_conditions.html
└── static/               # Static assets (if any)
```

### 2. Deploy to Vercel

#### Option A: Deploy via Vercel Dashboard

1. **Go to Vercel**: Visit [vercel.com](https://vercel.com)
2. **Sign up/Login**: Use your GitHub account
3. **New Project**: Click "New Project"
4. **Import Repository**: Select your GitHub repository
5. **Configure Project**:
   - Framework Preset: Other
   - Root Directory: `./` (leave as default)
   - Build Command: Leave empty (Vercel will auto-detect)
   - Output Directory: Leave empty
6. **Deploy**: Click "Deploy"

#### Option B: Deploy via Vercel CLI

1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel**:
   ```bash
   vercel login
   ```

3. **Deploy**:
   ```bash
   vercel
   ```

### 3. Environment Variables (Optional)

If your app needs environment variables:

1. Go to your Vercel project dashboard
2. Navigate to Settings → Environment Variables
3. Add any required variables

### 4. Custom Domain (Optional)

1. Go to your Vercel project dashboard
2. Navigate to Settings → Domains
3. Add your custom domain
4. Configure DNS settings as instructed

## 📁 Required Files

### vercel.json
This file tells Vercel how to build and serve your Flask app:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ],
  "env": {
    "PYTHONPATH": "."
  }
}
```

### requirements.txt
Ensure this file contains all your Python dependencies:
```
Flask==2.3.3
pandas==2.0.3
Werkzeug==2.3.7
```

## 🔧 Troubleshooting

### Common Issues

1. **Build Fails**: Check that all dependencies are in `requirements.txt`
2. **Import Errors**: Ensure `PYTHONPATH` is set correctly in `vercel.json`
3. **File Not Found**: Make sure all template files are in the `templates/` directory
4. **CSV Loading Issues**: Ensure the CSV file path is correct

### Debug Steps

1. Check Vercel build logs for errors
2. Verify all file paths are correct
3. Test locally before deploying
4. Check that all imports work correctly

## 📊 Post-Deployment

### Verify Deployment

1. Check that your site loads correctly
2. Test all major functionality
3. Verify that the CSV data loads properly
4. Test mobile responsiveness

### Monitor Performance

1. Use Vercel Analytics (if available)
2. Monitor build times
3. Check for any runtime errors

## 🔄 Updates

To update your deployed site:

1. Push changes to your GitHub repository
2. Vercel will automatically redeploy
3. Or manually trigger a redeploy from the Vercel dashboard

## 📞 Support

If you encounter issues:

1. Check Vercel documentation
2. Review build logs
3. Test locally first
4. Contact Vercel support if needed

---

**Your LLC Directory will be live at: `https://your-project-name.vercel.app`**
