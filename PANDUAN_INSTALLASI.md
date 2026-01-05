# Panduan Instalasi Sistem Manajemen Laundry

## Persyaratan Sistem

### Software yang Dibutuhkan:
- **Python 3.10 atau lebih tinggi** (direkomendasikan Python 3.12)
- **Node.js 16.0 atau lebih tinggi** (untuk Tailwind CSS)
- **Git** (opsional, untuk clone repository)
- **PostgreSQL Client** (jika menggunakan database lokal)
- **VS Code** atau text editor lainnya (direkomendasikan)

### Spesifikasi Hardware Minimal:
- **RAM**: 4GB (direkomendasikan 8GB)
- **Storage**: 2GB free space
- **OS**: Windows 10/11 atau macOS 10.15+

---

## 🎯 PILIH SKENARIO INSTALASI

### **Skenario A: Menggunakan File .env (Database Supabase)**
✅ **Pilih ini jika**: Anda menggunakan file .env yang sudah disediakan
✅ **Database**: Supabase (cloud PostgreSQL)
✅ **Setup**: Cepat, tidak perlu install PostgreSQL lokal
✅ **Cocok untuk**: Demo, presentasi, online deployment

### **Skenario B: Menggunakan Database Backup (Local)**
✅ **Pilih ini jika**: Anda menggunakan file backup SQL (.sql)
✅ **Database**: PostgreSQL lokal
✅ **Setup**: Lebih kompleks, perlu install PostgreSQL
✅ **Cocok untuk**: Development offline, testing lokal

---

## 🪟 PANDUAN WINDOWS - SKENARIO A

### File .env yang Disediakan (Supabase)

#### Langkah 1: Download & Ekstrak Project
1. Download file ZIP project
2. Ekstrak ke folder tanpa spasi, contoh: `C:\laundry-project`
3. **Pastikan file .env ada di root folder** (sama dengan manage.py)

#### Langkah 2: Install Python
1. Buka browser → https://www.python.org/downloads/
2. Download **Python 3.12** (klik tombol hijau Download)
3. Jalankan installer:
   - ✅ **Centang** "Add Python to PATH"
   - ✅ Pilih "Install for all users" (opsional)
   - ✅ Klik "Install Now"
4. Test instalasi (buka Command Prompt):
```cmd
python --version
pip --version
```

#### Langkah 3: Install Node.js
1. Buka browser → https://nodejs.org/
2. Download **LTS version** (recommended for most users)
3. Jalankan installer Next → Next → Install
4. Test instalasi:
```cmd
node --version
npm --version
```

#### Langkah 4: Setup Virtual Environment
1. Buka Command Prompt (Search "cmd" di Start Menu)
2. Navigate ke project folder:
```cmd
cd C:\laundry-project
```
3. Buat virtual environment:
```cmd
python -m venv venv
```
4. Aktivasi virtual environment:
```cmd
venv\Scripts\activate
```
5. **Cek sukses**: Prompt berubah menjadi `(venv) C:\laundry-project>`

#### Langkah 5: Install Dependencies
```cmd
# Install Python packages
pip install -r requirements.txt

# Install Node.js packages
npm install

# Build Tailwind CSS
npm run build:css
```

#### Langkah 6: Verify .env Configuration
```cmd
# Pastikan file .env ada
dir .env

# Check isi .env (opsional)
type .env
```
File .env harus berisi:
```env
SECRET_KEY=...
DEBUG=True
DB_NAME=your_supabase_db
DB_USER=your_supabase_user
DB_PASSWORD=your_supabase_password
DB_HOST=your_host.supabase.co
DB_PORT=5432
```

#### Langkah 7: Database Migrations
```cmd
# Buat migrasi
python manage.py makemigrations

# Jalankan migrasi
python manage.py migrate
```

#### Langkah 8: Create Superuser
```cmd
python manage.py createsuperuser
```
Input data admin:
```
Username: admin
Email: admin@laundry.com
Password: admin123
Password (again): admin123
```

#### Langkah 9: Jalankan Server
```cmd
python manage.py runserver
```

#### Langkah 10: Test Aplikasi
1. Buka browser → http://127.0.0.1:8000/
2. Login dengan: `admin` / `admin123`

---

## 🪟 PANDUAN WINDOWS - SKENARIO B

### Database Backup Local (PostgreSQL)

#### Langkah 1: Download & Ekstrak Project
1. Sama seperti Skenario A (langkah 1-5)

#### Langkah 2: Install PostgreSQL
1. Download dari https://www.postgresql.org/download/windows/
2. Pilih versi **15.x** atau **16.x**
3. Jalankan installer:
   - Password PostgreSQL: **laundry123** (ingat password ini)
   - Port: **5432** (default)
   - ✅ Centang "Install Stack Builder"
4. Setelah selesai, Stack Builder akan muncul:
   - Pilih "PostgreSQL Server" → Next
   - Pilih "pgAdmin 4" → Next → Install
   - (pgAdmin untuk GUI database)

#### Langkah 3: Setup Database
1. Buka **pgAdmin 4** dari Start Menu
2. Connect ke PostgreSQL:
   - Password: `laundry123`
3. Klik kanan **Databases** → Create → Database
   - Name: `laundry_db`
   - Owner: `postgres`
   - Click Save
4. Restore backup:
   - Klik kanan database `laundry_db` → Restore
   - Browse ke file .sql backup Anda
   - Klik Restore

#### Langkap 4: Setup .env File
1. Create file `.env` di project root:
```cmd
copy .env.example .env
```
2. Edit `.env` dengan Notepad atau VS Code:
```env
SECRET_KEY=django-insecure-laundry-project-key
DEBUG=True

# Local PostgreSQL Configuration
DB_NAME=laundry_db
DB_USER=postgres
DB_PASSWORD=laundry123
DB_HOST=localhost
DB_PORT=5432
```
3. Save file

#### Langkah 5: Lanjut Setup
```cmd
# Aplikasi virtual environment ( jika sudah )
venv\Scripts\activate

# Install dependencies (jika belum)
pip install -r requirements.txt
npm install
npm run build:css

# Test koneksi database
python manage.py dbshell --command="SELECT version();"

# Jalankan migrasi (jika needed)
python manage.py migrate --run-syncdb

# Create superuser (jika belum ada)
python manage.py createsuperuser
```

#### Langkah 6: Jalankan Server
```cmd
python manage.py runserver
```

---

## 🍎 PANDUAN MACOS - SKENARIO A

### File .env yang Disediakan (Supabase)

#### Langkah 1: System Preparation
1. Update macOS ke versi terbaru
2. Install Xcode Command Line Tools:
```bash
xcode-select --install
```
3. Install Homebrew (Package Manager):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
4. Follow instructions untuk menambahkan Homebrew ke PATH:
```bash
# Untuk Mac dengan Apple Silicon (M1/M2/M3):
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
eval "$(/opt/homebrew/bin/brew shellenv)"

# Untuk Mac dengan Intel:
eval "$(/usr/local/bin/brew shellenv)"
```

#### Langkah 2: Install Python
```bash
# Install Python 3.12
brew install python@3.12

# Verify installation
python3 --version
pip3 --version

# Link python3 ke command 'python' (opsional)
echo 'alias python=python3' >> ~/.zshrc
echo 'alias pip=pip3' >> ~/.zshrc
source ~/.zshrc
```

#### Langkah 3: Install Node.js
```bash
# Install Node.js LTS
brew install node

# Verify installation
node --version
npm --version
```

#### Langkah 4: Setup Project Directory
```bash
# Buka Terminal baru setelah Homebrew setup
# Navigate ke Downloads atau folder tempat file ZIP
cd ~/Downloads

# Extract file ZIP (jika belum)
# Atau ekstrak manual di Finder, lalu navigate ke folder
cd ~/laundry-project

# Verify project structure
ls -la
# Harus melihat: manage.py, requirements.txt, .env, dll
```

#### Langkah 5: Setup Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Verify activation (prompt berubah menjadi (venv))
which python
# Should show: /path/to/project/venv/bin/python
```

#### Langkah 6: Install Dependencies
```bash
# Upgrade pip dalam virtual environment
pip install --upgrade pip

# Install Python packages
pip install -r requirements.txt

# Install Node.js packages
npm install

# Build Tailwind CSS
npm run build:css
```

#### Langkah 7: Setup Environment Variables
```bash
# Check if .env file exists
ls -la .env

# If .env tidak ada, copy dari .env.example
cp .env.example .env

# Verify .env content (opsional)
cat .env
```
Edit .env jika perlu:
```bash
# Buka dengan VS Code
code .env

# Atau dengan nano
nano .env
# Save: Ctrl+X, Y, Enter
```

#### Langkah 8: Database Setup
```bash
# Test database connection ke Supabase
python manage.py dbshell --command="SELECT version();"

# Run migrations
python manage.py makemigrations
python manage.py migrate
```

#### Langkah 9: Create Administrator
```bash
# Create superuser interactively
python manage.py createsuperuser
```
Input credentials:
```
Username: admin
Email address: admin@laundry.com
Password: admin123
Password (again): admin123
```

#### Langkah 10: Testing & Launch
```bash
# Test Django setup
python manage.py check

# Run development server
python manage.py runserver

# Open in browser
open http://127.0.0.1:8000/
```

---

## 🍎 PANDUAN MACOS - SKENARIO B

### Database Backup Local (PostgreSQL)

#### Langkah 1: Install PostgreSQL
```bash
# Install PostgreSQL via Homebrew
brew install postgresql@16

# Start PostgreSQL service
brew services start postgresql@16

# Verify PostgreSQL running
brew services list
# Should show postgresql@16 as "started"

# Set password untuk postgres user
psql postgres
# Ketik perintah ini di psql:
ALTER USER postgres PASSWORD 'laundry123';
\q
```

#### Langkap 2: Create Database and Restore
```bash
# Setup database
psql -U postgres -c "CREATE DATABASE laundry_db;"
psql -U postgres -c "CREATE USER laundry_user WITH PASSWORD 'laundry123';"
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE laundry_db TO laundry_user;"

# Restore backup (sesuaikan path file backup)
psql -h localhost -U postgres -d laundry_db < /path/to/your/backup.sql

# Verify restore
psql -h localhost -U postgres -d laundry_db -c "\dt"
```

#### Langkah 3: Setup .env untuk Local Database
```bash
# Create .env file
cp .env.example .env

# Edit dengan nano atau VS Code
nano .env
```
Edit konten menjadi:
```env
SECRET_KEY=django-insecure-laundry-project-key-for-local-dev
DEBUG=True

# Local PostgreSQL Configuration
DB_NAME=laundry_db
DB_USER=postgres
DB_PASSWORD=laundry123
DB_HOST=localhost
DB_PORT=5432
```
Save dan keluar: `Ctrl+X`, `Y`, `Enter`

#### Langkah 4: Complete Project Setup
```bash
# Navigate ke project (jika belum)
cd ~/laundry-project

# Activate virtual environment
source venv/bin/activate

# Install dependencies (jika belum)
pip install -r requirements.txt
npm install
npm run build:css

# Test database connection
python manage.py dbshell --command="SELECT version();"

# Sync database dengan models Django
python manage.py migrate --run-syncdb

# Create admin user (jika belum ada)
python manage.py createsuperuser
```

#### Langkah 5: Final Testing
```bash
# Django system check
python manage.py check

# Run server
python manage.py runserver

# Test di browser
open http://127.0.0.1:8000/
```

#### Langkah 6: Optional Tools (Recommended)
```bash
# Install pgAdmin untuk database GUI (opsional)
brew install --cask pgadmin4

# Install Postico untuk PostgreSQL GUI client (macOS friendly)
brew install --cask postico

# Install TablePlus untuk universal database tool
brew install --cask tableplus
```

---

## 🔧 TROUBLESHOOTING MACOS

### Common Issues & Solutions:

#### Virtual Environment Issues
```bash
# Error: python3: command not found
# Solution: Install via Homebrew
brew install python@3.12

# Virtual environment tidak aktif
# Deactivate dulu lalu activate lagi:
deactivate
source venv/bin/activate
```

#### Permission Issues
```bash
# Fix folder permissions
sudo chown -R $USER:staff ~/laundry-project

# Fix venv permissions
chmod -R 755 venv/
```

#### Node.js Issues
```bash
# Clear npm cache
npm cache clean --force

# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

#### PostgreSQL Connection Issues
```bash
# Stop and restart PostgreSQL
brew services stop postgresql@16
brew services start postgresql@16

# Check status
brew services list | grep postgres

# Manual connection test
psql -h localhost -U postgres -d laundry_db
```

#### Django Issues
```bash
# Clear cache
find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} +

# Recompile Python
python -c "import py_compile; py_compile.compile('manage.py')"
```

### macOS Terminal Troubleshooting:
```bash
# Reset Terminal permissions
sudo chmod +x /usr/local/bin/*

# Check PATH
echo $PATH

# Add to PATH (temporary)
export PATH="/opt/homebrew/bin:$PATH"
export PATH="/opt/homebrew/sbin:$PATH"
```

## 🔧 Troubleshooting Common Issues

### Error: "No module named 'psycopg2'"
```bash
# Windows
pip install psycopg2-binary

# macOS
pip3 install psycopg2-binary
```

### Error: "python command not found" (macOS)
```bash
# Gunakan python3 instead of python
python3 --version
```

### Error: Virtual Environment tidak aktif
```bash
# Windows
venv\Scripts\activate

# macOS
source venv/bin/activate
```

### Error: Database Connection Failed
1. Pastikan PostgreSQL service running:
   - Windows: Buka Services, cari "postgresql", Start
   - macOS: `brew services start postgresql`

2. Cek koneksi database:
```bash
# Windows
psql -U your_user -h localhost -d your_database

# macOS
psql -h localhost -U postgres -d laundry_db
```

### Error: Permission Denied (macOS)
```bash
# Fix permissions untuk virtual environment
sudo chown -R $USER:staff venv
```

### Error: Tailwind CSS tidak berkerja
```bash
# Build ulang CSS
npm run build:css

# Atau refresh browser dengan clear cache
# Ctrl+F5 (Windows) atau Cmd+Shift+R (macOS)
```

---

## 🚀 Menjalankan Aplikasi (Setelah Instalasi)

### Cara 1: Development Mode
```bash
# Windows (dengan virtual environment aktif)
python manage.py runserver

# macOS (dengan virtual environment aktif)
python manage.py runserver
```

### Cara 2: Production Mode (Opsional)
```bash
# Install Gunicorn (Linux/macOS)
pip install gunicorn

# Jalankan dengan Gunicorn
gunicorn --bind 0.0.0.0:8000 laundry_project.wsgi:application
```

---

## 📱 Akses Aplikasi

Setelah server berjalan, akses melalui browser:

### URL Utama:
- **Halaman Utama**: http://127.0.0.1:8000/
- **Login**: http://127.0.0.1:8000/login/
- **Dashboard**: http://127.0.0.1:8000/dashboard/

### Akun Default (jika menggunakan database backup):
- **Username**: `admin`
- **Password**: Coba password berikut, sesuai backup:
  - `admin123`
  - `password`
  - Atau hubungi penyedia project untuk password

Jika tidak berhasil, buat superuser baru:
```bash
python manage.py createsuperuser
```

---

## 🎯 Quick Start Checklist

### Sebelum Memulai:
- [ ] Python 3.10+ terinstall
- [ ] Node.js 16+ terinstall
- [ ] Project sudah diekstrak
- [ ] File `.env` ada di root folder

### Proses Instalasi:
- [ ] Buat dan aktivasi virtual environment
- [ ] Install Python dependencies (`pip install -r requirements.txt`)
- [ ] Install Node.js dependencies (`npm install`)
- [ ] Build Tailwind CSS (`npm run build:css`)
- [ ] Setup database (pakai .env atau backup)
- [ ] Jalankan migrasi
- [ ] Create superuser
- [ ] Jalankan server di port 8000

### Testing:
- [ ] Buka http://127.0.0.1:8000/ di browser
- [ ] Login dengan akun admin
- [ ] Test fitur dashboard
- [ ] Test tambah pelanggan
- [ ] Test buat order laundry

---

## 📞 Bantuan Tambahan

### Jika mengalami masalah:
1. Pastikan semua requirements terinstall
2. Cekkoneksi database
3. Restart virtual environment
4. Clear browser cache
5. Cek error logs di terminal

### Error Logs Common:
- **ModuleNotFoundError**: Install missing dependencies
- **OperationalError**: Database connection issue
- **TemplateDoesNotExist**: Folder structure issue
- **PermissionError**: File/directory permissions

### Contact Support:
- Email: support@laundry-system.com
- Documentation: https://docs.laundry-system.com
- GitHub Issues: https://github.com/project/issues

---

## 📝 Catatan untuk Dosen

### File Penting yang Perlu Diperiksa:
1. **`.env`** - Berisi konfigurasi database Supabase
2. **`requirements.txt`** - Python dependencies
3. **`manage.py`** - Django management script
4. **`settings.py`** - Konfigurasi utama aplikasi

### Database:
- menggunakan PostgreSQL dengan Supabase
- Schema lengkap tersedia di models.py
- Migration files ada di core/migrations/

### Login Default (setelah install dari backup):
- Username: `admin`
- Password: `admin123` (cek file .env atau backup)

### Fitur yang Bisa Dicoba:
1. Dashboard dan monitoring
2. Manajemen pelanggan
3. Order laundry dengan auto-calculation
4. Tracking status cucian
5. Laporan transaksi
6. Role-based access (Owner vs Pegawai)

---

**Selamat Menggunakan Sistem Manajemen Laundry!**
  
Project ini dikembangkan untuk memenuhi kebutuhan sistem informasi laundry yang komprehensif dengan fitur lengkap dan user interface yang modern.
