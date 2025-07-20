@echo off
setlocal enabledelayedexpansion

:: === KONFIGURASI ===
set "GIT_PATH=F:\WEBUI_jarvis1507\Git\bin\git.exe"
set "REPO_PATH=F:\WEBUI_jarvis1507"
set "REMOTE_URL=https://github.com/vandjee/webui-jarvis1507.git"

:: === MULAI ===
echo [🔁] Masuk ke folder proyek...
cd /d "%REPO_PATH%"

:: === Inisialisasi git jika belum ada ===
if not exist ".git" (
    echo [🧱] Inisialisasi Git...
    "%GIT_PATH%" init
)

:: === Tambah dan commit ===
echo [➕] Menambahkan file...
"%GIT_PATH%" add .

echo [📝] Commit...
"%GIT_PATH%" commit -m "Update by JARVIS1507"

:: === Set remote jika belum diset ===
"%GIT_PATH%" remote get-url origin >nul 2>&1
if errorlevel 1 (
    echo [🌐] Menambahkan remote origin...
    "%GIT_PATH%" remote add origin "%REMOTE_URL%"
)

:: === Push ===
echo [🚀] Push ke GitHub...
"%GIT_PATH%" push -u origin main

echo.
echo [✅] Push selesai! Project sudah masuk ke GitHub.
pause
