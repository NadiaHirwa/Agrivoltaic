# 🌱 Render Deployment Guide for Agrivoltaic Dashboard

## Step-by-Step Deployment Instructions

### **Step 1: Prepare Your Files**

Make sure you have these files in your `Dashboard` folder:
- ✅ `app.py` (your main dashboard file)
- ✅ `requirements.txt` (Python dependencies)
- ✅ `render.yaml` (deployment configuration)
- ✅ `merged.csv` (your data file in `../Data/Processed/`)

### **Step 2: Create a GitHub Repository**

1. **Go to GitHub.com** and sign in
2. **Click "New repository"** (green button)
3. **Name it**: `agrivoltaic-dashboard`
4. **Make it Public** (free Render requires public repos)
5. **Don't initialize** with README (we'll upload our files)

### **Step 3: Upload Your Files to GitHub**

**Option A: Using GitHub Web Interface**
1. Go to your new repository
2. Click "uploading an existing file"
3. Drag and drop your entire `Dashboard` folder contents
4. Add commit message: "Initial dashboard upload"
5. Click "Commit changes"

**Option B: Using Git Commands**
```bash
# Navigate to your Dashboard folder
cd Dashboard

# Initialize git repository
git init

# Add all files
git add .

# Commit files
git commit -m "Initial dashboard upload"

# Add GitHub as remote
git remote add origin https://github.com/YOUR_USERNAME/agrivoltaic-dashboard.git

# Push to GitHub
git push -u origin main
```

### **Step 4: Deploy to Render**

1. **Go to [Render.com](https://render.com)**
2. **Sign up/Login** with your GitHub account
3. **Click "New +"** → **"Web Service"**
4. **Connect your GitHub repository**:
   - Select your `agrivoltaic-dashboard` repository
   - Render will auto-detect it's a Python app

### **Step 5: Configure Your Service**

Fill in these settings:

**Basic Settings:**
- **Name**: `agrivoltaic-dashboard`
- **Environment**: `Python 3`
- **Region**: Choose closest to you
- **Branch**: `main`

**Build & Deploy Settings:**
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`

**Advanced Settings:**
- **Plan**: `Free` (for testing)
- **Auto-Deploy**: ✅ Enabled

### **Step 6: Deploy**

1. **Click "Create Web Service"**
2. **Wait for deployment** (usually 2-5 minutes)
3. **Watch the logs** for any errors

### **Step 7: Get Your Dashboard URL**

Once deployment is successful:
1. **Copy the URL** from your Render dashboard
2. **It will look like**: `https://agrivoltaic-dashboard.onrender.com`
3. **Share this URL** with others!

---

## 🚨 Troubleshooting Common Issues

### **Issue 1: "Module not found" errors**
**Solution**: Make sure all dependencies are in `requirements.txt`

### **Issue 2: "Data file not found"**
**Solution**: 
1. Make sure `merged.csv` is in the correct path
2. Update the path in `app.py` if needed

### **Issue 3: "Port already in use"**
**Solution**: Render handles this automatically, but make sure you're using:
```python
app.run(debug=False, host='0.0.0.0', port=8050)
```

### **Issue 4: "Build failed"**
**Solution**:
1. Check the build logs in Render
2. Make sure all files are uploaded to GitHub
3. Verify `requirements.txt` has correct versions

---

## 📁 File Structure

Your GitHub repository should look like this:
```
agrivoltaic-dashboard/
├── app.py                 # Main dashboard file
├── requirements.txt       # Python dependencies
├── render.yaml           # Render configuration
└── Data/
    └── Processed/
        └── merged.csv    # Your data file
```

---

## 🔗 Your Dashboard URL

Once deployed, your dashboard will be available at:
**`https://your-app-name.onrender.com`**

Replace `your-app-name` with whatever you named your service in Render.

---

## 📞 Need Help?

If you encounter any issues:
1. **Check the Render logs** for error messages
2. **Verify all files** are uploaded to GitHub
3. **Make sure** your data file path is correct
4. **Contact support** if needed

---

## 🎉 Success!

Once deployed successfully, you'll have:
- ✅ A live, shareable dashboard URL
- ✅ Automatic deployments when you update GitHub
- ✅ Free hosting (with some limitations)
- ✅ Professional web service

**Your dashboard is now live and ready to share!** 🌱 