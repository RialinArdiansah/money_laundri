@echo off
chcp 65001 >nul
title Instalasi Sistem Manajemen Laundry

echo ============================================
echo   Instalasi Sistem Manajemen Laundry
echo   Platform: Windows
echo ============================================
echo.

:: Check Python
echo [1/7] Memeriksa Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python tidak ditemukan!
    echo Silakan install Python dari https://www.python.org/downloads/
    echo Pastikan centang "Add Python to PATH" saat instalasi.
    pause
    exit /b 1
)
python --version
echo [OK] Python ditemukan.
echo.

:: Create virtual environment
echo [2/7] Membuat Virtual Environment...
if exist venv (
    echo Virtual environment sudah ada, melewati...
) else (
    python -m venv venv
    if errorlevel 1 (
        echo [ERROR] Gagal membuat virtual environment!
        pause
        exit /b 1
    )
)
echo [OK] Virtual environment siap.
echo.

:: Activate virtual environment
echo [3/7] Mengaktifkan Virtual Environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Gagal mengaktifkan virtual environment!
    pause
    exit /b 1
)
echo [OK] Virtual environment aktif.
echo.

:: Upgrade pip
echo [4/7] Mengupgrade pip...
python -m pip install --upgrade pip >nul 2>&1
echo [OK] pip sudah diupgrade.
echo.

:: Install dependencies
echo [5/7] Menginstall dependencies Python...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Gagal menginstall dependencies!
    pause
    exit /b 1
)
echo [OK] Dependencies terinstall.
echo.

:: Check .env file
echo [6/7] Memeriksa file konfigurasi...
if not exist .env (
    if exist .env.example (
        copy .env.example .env >nul
        echo [INFO] File .env dibuat dari .env.example
        echo [PENTING] Edit file .env dan sesuaikan konfigurasi database!
    ) else (
        echo [WARNING] File .env.example tidak ditemukan!
    )
) else (
    echo [OK] File .env sudah ada.
)
echo.

:: Run migrations
echo [7/7] Menjalankan migrasi database...
python manage.py migrate
if errorlevel 1 (
    echo [WARNING] Migrasi gagal. Pastikan konfigurasi database benar di file .env
) else (
    echo [OK] Migrasi database selesai.
)
echo.

echo ============================================
echo   Instalasi Selesai!
echo ============================================
echo.
echo Langkah selanjutnya:
echo 1. Edit file .env dan sesuaikan konfigurasi database
echo 2. Jalankan: python manage.py createsuperuser
echo 3. Jalankan: python manage.py runserver
echo 4. Buka browser: http://127.0.0.1:8000/
echo.
echo Untuk mengaktifkan virtual environment di sesi baru:
echo    venv\Scripts\activate
echo.
pause
