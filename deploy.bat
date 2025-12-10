@echo off
echo ========================================
echo MonarchTime - Railway Deployment Helper
echo ========================================
echo.

echo Checking git status...
git status
echo.

echo Adding all files...
git add .
echo.

set /p commit_msg="Enter commit message (or press Enter for default): "
if "%commit_msg%"=="" set commit_msg=Update MonarchTime

echo Committing changes...
git commit -m "%commit_msg%"
echo.

echo Pushing to GitHub...
git push
echo.

echo ========================================
echo Deployment Complete!
echo ========================================
echo.
echo Your changes have been pushed to GitHub.
echo Railway will automatically deploy the updates.
echo.
echo Check your Railway dashboard for deployment status.
echo.
pause
