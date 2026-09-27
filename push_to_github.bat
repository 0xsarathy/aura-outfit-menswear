@echo off
echo ========================================================
echo   AURA OUTFIT - Push to GitHub
echo ========================================================
echo.
echo Make sure you have created the repository 'aura-outfit-menswear' on https://github.com/new
echo.
pause

git remote remove origin 2>nul
git remote add origin https://github.com/0xsarathy/aura-outfit-menswear.git
git branch -M main
git push -u origin main

echo.
echo ========================================================
echo   Successfully pushed to GitHub!
echo   Now go to https://vercel.com/new to import and deploy.
echo ========================================================
pause
