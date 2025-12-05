# Panduan Instalasi - Sistem Manajemen Laundry

Panduan ini menjelaskan cara menginstal aplikasi Sistem Manajemen Laundry di berbagai sistem operasi.

## Persyaratan Sistem

- **Python**: 3.10 atau lebih baru (direkomendasikan 3.12)
- **Database**: PostgreSQL (menggunakan Supabase)
- **RAM**: Minimal 2GB
- **Disk**: Minimal 500MB ruang kosong

---

## Daftar Isi

1. [Instalasi di Windows](#instalasi-di-windows)
2. [Instalasi di macOS](#instalasi-di-macos)
3. [Instalasi di Linux Ubuntu/Debian](#instalasi-di-linux-ubuntudebian)
4. [Instalasi di Linux Fedora/RHEL/CentOS](#instalasi-di-linux-fedorarhel)
5. [Instalasi di Arch Linux](#instalasi-di-arch-linux)
6. [Konfigurasi Database](#konfigurasi-database)
7. [Menjalankan Aplikasi](#menjalankan-aplikasi)
8. [Troubleshooting](#troubleshooting)

---

## Instalasi di Windows

### Langkah 1: Install Python

1. Download Python dari [python.org](https://www.python.org/downloads/)
2. Jalankan installer
3. **PENTING**: Centang "Add Python to PATH" saat instalasi
4. Klik "Install Now"

Verifikasi instalasi:
```cmd
python --version
pip --version
```

### Langkah 2: Download/Clone Project

```cmd
git clone <repository-url>
cd laundry_project
```

Atau download ZIP dan ekstrak ke folder pilihan Anda.

### Langkah 3: Buat Virtual Environment

```cmd
python -m venv venv
```

### Langkah 4: Aktifkan Virtual Environment

```cmd
venv\Scripts\activate
```

Anda akan melihat `(venv)` di awal command prompt.

### Langkah 5: Install Dependencies

```cmd
pip install -r requirements.txt
```

### Langkah 6: Konfigurasi Environment

Salin file `.env.example` menjadi `.env`:
```cmd
copy .env.example .env
```

Edit file `.env` dengan Notepad atau editor lain dan sesuaikan konfigurasi database.

### Langkah 7: Migrasi Database

```cmd
python manage.py migrate
```

### Langkah 8: Buat Superuser (Admin/Owner)

```cmd
python manage.py createsuperuser
```

### Langkah 9: Jalankan Server

```cmd
python manage.py runserver
```

Akses aplikasi di: `http://127.0.0.1:8000/`

### Script Otomatis (Windows)

Anda juga dapat menggunakan script `install.bat`:
```cmd
install.bat
```

---

## Instalasi di macOS

### Langkah 1: Install Homebrew (jika belum ada)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Langkah 2: Install Python

```bash
brew install python3
```

Verifikasi instalasi:
```bash
python3 --version
pip3 --version
```

### Langkah 3: Install Dependencies Sistem (untuk Pillow)

```bash
brew install libjpeg zlib libpng
```

### Langkah 4: Download/Clone Project

```bash
git clone <repository-url>
cd laundry_project
```

### Langkah 5: Buat Virtual Environment

```bash
python3 -m venv venv
```

### Langkah 6: Aktifkan Virtual Environment

```bash
source venv/bin/activate
```

### Langkah 7: Install Dependencies Python

```bash
pip install -r requirements.txt
```

### Langkah 8: Konfigurasi Environment

```bash
cp .env.example .env
nano .env  # atau gunakan editor pilihan Anda
```

### Langkah 9: Migrasi Database

```bash
python manage.py migrate
```

### Langkah 10: Buat Superuser

```bash
python manage.py createsuperuser
```

### Langkah 11: Jalankan Server

```bash
python manage.py runserver
```

### Script Otomatis (macOS)

```bash
chmod +x install.sh
./install.sh
```

---

## Instalasi di Linux Ubuntu/Debian

### Langkah 1: Update Sistem

```bash
sudo apt update && sudo apt upgrade -y
```

### Langkah 2: Install Python dan Dependencies

```bash
sudo apt install -y python3 python3-pip python3-venv
```

### Langkah 3: Install Dependencies untuk Pillow dan psycopg2

```bash
sudo apt install -y libjpeg-dev zlib1g-dev libpng-dev libpq-dev
```

### Langkah 4: Install Git (jika belum ada)

```bash
sudo apt install -y git
```

### Langkah 5: Download/Clone Project

```bash
git clone <repository-url>
cd laundry_project
```

### Langkah 6: Buat Virtual Environment

```bash
python3 -m venv venv
```

### Langkah 7: Aktifkan Virtual Environment

```bash
source venv/bin/activate
```

### Langkah 8: Install Dependencies Python

```bash
pip install -r requirements.txt
```

### Langkah 9: Konfigurasi Environment

```bash
cp .env.example .env
nano .env  # Edit konfigurasi database
```

### Langkah 10: Migrasi Database

```bash
python manage.py migrate
```

### Langkah 11: Buat Superuser

```bash
python manage.py createsuperuser
```

### Langkah 12: Jalankan Server

```bash
python manage.py runserver
```

### Script Otomatis (Ubuntu/Debian)

```bash
chmod +x install.sh
./install.sh
```

---

## Instalasi di Linux Fedora/RHEL

### Langkah 1: Update Sistem

```bash
sudo dnf update -y
```

### Langkah 2: Install Python dan Dependencies

```bash
sudo dnf install -y python3 python3-pip python3-devel
```

### Langkah 3: Install Dependencies untuk Pillow dan psycopg2

```bash
sudo dnf install -y libjpeg-devel zlib-devel libpng-devel postgresql-devel gcc
```

### Langkah 4: Install Git

```bash
sudo dnf install -y git
```

### Langkah 5: Download/Clone Project

```bash
git clone <repository-url>
cd laundry_project
```

### Langkah 6: Buat Virtual Environment

```bash
python3 -m venv venv
```

### Langkah 7: Aktifkan Virtual Environment

```bash
source venv/bin/activate
```

### Langkah 8: Install Dependencies Python

```bash
pip install -r requirements.txt
```

### Langkah 9: Konfigurasi Environment

```bash
cp .env.example .env
nano .env
```

### Langkah 10: Migrasi dan Jalankan

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## Instalasi di Arch Linux

### Langkah 1: Update Sistem

```bash
sudo pacman -Syu
```

### Langkah 2: Install Python dan Dependencies

```bash
sudo pacman -S python python-pip
```

### Langkah 3: Install Dependencies untuk Pillow dan psycopg2

```bash
sudo pacman -S libjpeg-turbo zlib libpng postgresql-libs base-devel
```

### Langkah 4: Install Git

```bash
sudo pacman -S git
```

### Langkah 5: Download/Clone Project

```bash
git clone <repository-url>
cd laundry_project
```

### Langkah 6: Buat Virtual Environment

```bash
python -m venv venv
```

### Langkah 7: Aktifkan Virtual Environment

```bash
source venv/bin/activate
```

### Langkah 8: Install Dependencies Python

```bash
pip install -r requirements.txt
```

### Langkah 9: Konfigurasi dan Jalankan

```bash
cp .env.example .env
nano .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## Konfigurasi Database

### Menggunakan Supabase (Rekomendasi)

1. Buat akun di [supabase.com](https://supabase.com)
2. Buat project baru
3. Dapatkan kredensial database dari Settings > Database
4. Edit file `.env`:

```env
SECRET_KEY=your-secret-key-generate-random-string
DEBUG=True

DB_NAME=postgres
DB_USER=postgres.xxxxx
DB_PASSWORD=your-password
DB_HOST=aws-0-ap-south-1.pooler.supabase.com
DB_PORT=5432
```

### Menggunakan PostgreSQL Lokal

1. Install PostgreSQL di sistem Anda
2. Buat database baru:
   ```sql
   CREATE DATABASE laundry_db;
   CREATE USER laundry_user WITH PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE laundry_db TO laundry_user;
   ```
3. Edit file `.env`:
   ```env
   DB_NAME=laundry_db
   DB_USER=laundry_user
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

---

## Menjalankan Aplikasi

### Mode Development

```bash
# Windows
python manage.py runserver

# Linux/macOS
python3 manage.py runserver
```

Akses: `http://127.0.0.1:8000/`

### Mode Production (dengan Gunicorn - Linux/macOS)

```bash
pip install gunicorn
gunicorn laundry_project.wsgi:application --bind 0.0.0.0:8000
```

### Collect Static Files (untuk Production)

```bash
python manage.py collectstatic --noinput
```

---

## Membuat Data Awal

### Membuat Layanan Laundry

Setelah migrasi, buat data layanan melalui Django shell:

```bash
python manage.py shell
```

```python
from core.models import Layanan

Layanan.objects.create(nama_layanan='Cuci Kering', harga_per_kg=5000, estimasi_waktu=1)
Layanan.objects.create(nama_layanan='Cuci Setrika', harga_per_kg=7000, estimasi_waktu=2)
Layanan.objects.create(nama_layanan='Setrika Saja', harga_per_kg=3000, estimasi_waktu=1)

print("Layanan berhasil dibuat!")
exit()
```

---

## Troubleshooting

### Error: "python not found" atau "python3 not found"

**Windows:**
- Pastikan Python sudah terinstall dan ditambahkan ke PATH
- Coba restart Command Prompt/Terminal

**Linux/macOS:**
- Install Python: `sudo apt install python3` atau `brew install python3`

### Error: "No module named 'psycopg2'"

```bash
pip install psycopg2-binary
```

Jika masih error di Linux:
```bash
# Ubuntu/Debian
sudo apt install libpq-dev python3-dev
pip install psycopg2-binary

# Fedora
sudo dnf install postgresql-devel python3-devel
pip install psycopg2-binary
```

### Error: "No module named 'PIL'" atau Error Pillow

**Linux Ubuntu/Debian:**
```bash
sudo apt install libjpeg-dev zlib1g-dev libpng-dev
pip install --force-reinstall Pillow
```

**Linux Fedora:**
```bash
sudo dnf install libjpeg-devel zlib-devel libpng-devel
pip install --force-reinstall Pillow
```

**macOS:**
```bash
brew install libjpeg zlib libpng
pip install --force-reinstall Pillow
```

### Error: "FATAL: password authentication failed"

- Periksa kredensial database di file `.env`
- Pastikan user dan password benar
- Untuk Supabase, gunakan password dari dashboard (bukan password akun)

### Error: "connection refused" ke database

- Pastikan host database benar
- Periksa koneksi internet (untuk Supabase)
- Untuk PostgreSQL lokal, pastikan service PostgreSQL berjalan:
  ```bash
  # Linux
  sudo systemctl start postgresql
  
  # macOS
  brew services start postgresql
  ```

### Error: "Permission denied" saat menjalankan script

**Linux/macOS:**
```bash
chmod +x install.sh
./install.sh
```

### Virtual Environment tidak aktif

**Windows:**
```cmd
venv\Scripts\activate
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

### Port 8000 sudah digunakan

Jalankan di port lain:
```bash
python manage.py runserver 8080
```

---

## Catatan Penting

1. **Jangan commit file `.env`** - File ini berisi kredensial sensitif
2. **Gunakan SECRET_KEY yang kuat** untuk production
3. **Set DEBUG=False** untuk production
4. **Backup database** secara berkala
5. **Update dependencies** secara berkala untuk keamanan

---

## Kontak & Support

Jika mengalami kendala, silakan:
1. Periksa bagian Troubleshooting di atas
2. Baca dokumentasi Django: [docs.djangoproject.com](https://docs.djangoproject.com)
3. Hubungi tim developer
