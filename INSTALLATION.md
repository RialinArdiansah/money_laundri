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

## Konfigurasi Environment (.env)

### Langkah 1: Salin File Environment

```bash
# Windows
copy .env.example .env

# Linux/macOS
cp .env.example .env
```

### Langkah 2: Penjelasan Variabel Environment

Buka file `.env` dengan text editor (Notepad, VS Code, nano, dll):

```env
SECRET_KEY=your-secret-key-here
DEBUG=True

# PostgreSQL Configuration
DB_NAME=your_database_name
DB_USER=your_supabase_user
DB_PASSWORD=your_supabase_password
DB_HOST=your_supabase_host.supabase.co
DB_PORT=5432
```

| Variabel | Deskripsi | Contoh |
|----------|-----------|--------|
| `SECRET_KEY` | Kunci rahasia Django untuk keamanan (enkripsi session, CSRF, dll). **Wajib unik dan rahasia!** | `django-insecure-abc123xyz...` |
| `DEBUG` | Mode debug. Set `True` untuk development, `False` untuk production | `True` atau `False` |
| `DB_NAME` | Nama database PostgreSQL | `postgres` |
| `DB_USER` | Username database | `postgres.abcd1234` |
| `DB_PASSWORD` | Password database | `MySecurePassword123` |
| `DB_HOST` | Alamat host database | `aws-0-ap-south-1.pooler.supabase.com` |
| `DB_PORT` | Port database PostgreSQL | `5432` |

### Langkah 3: Generate SECRET_KEY

**Opsi 1 - Menggunakan Python:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**Opsi 2 - Menggunakan Python (tanpa Django):**
```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

**Opsi 3 - Online Generator:**
Kunjungi [djecrety.ir](https://djecrety.ir/) untuk generate SECRET_KEY

Salin hasil generate dan paste ke file `.env`:
```env
SECRET_KEY=hasil-generate-secret-key-anda-disini
```

---

## Konfigurasi Database

### Opsi A: Menggunakan Supabase (Rekomendasi untuk Pemula)

Supabase menyediakan PostgreSQL gratis di cloud, tidak perlu install database lokal.

#### Langkah 1: Buat Akun Supabase

1. Kunjungi [supabase.com](https://supabase.com)
2. Klik **"Start your project"** atau **"Sign Up"**
3. Daftar menggunakan GitHub, Google, atau Email

#### Langkah 2: Buat Project Baru

1. Setelah login, klik **"New Project"**
2. Isi informasi project:
   - **Name**: `laundry-app` (atau nama lain)
   - **Database Password**: Buat password yang kuat (simpan password ini!)
   - **Region**: Pilih region terdekat (contoh: `Southeast Asia (Singapore)`)
3. Klik **"Create new project"**
4. Tunggu beberapa menit sampai project selesai dibuat

#### Langkah 3: Dapatkan Kredensial Database

1. Di dashboard project, klik menu **"Project Settings"** (ikon gear di sidebar kiri bawah)
2. Pilih tab **"Database"**
3. Scroll ke bagian **"Connection string"**
4. Pilih mode **"URI"** dan lihat connection string
5. Atau lihat bagian **"Connection parameters"** untuk detail:

| Parameter | Lokasi di Supabase | Contoh Nilai |
|-----------|-------------------|--------------|
| `DB_HOST` | Host | `aws-0-ap-southeast-1.pooler.supabase.com` |
| `DB_NAME` | Database name | `postgres` |
| `DB_USER` | User | `postgres.abcdefgh12345` |
| `DB_PASSWORD` | Password yang Anda buat saat membuat project | `YourPassword123` |
| `DB_PORT` | Port | `5432` (gunakan `6543` untuk Transaction pooler) |

#### Langkah 4: Isi File .env

```env
SECRET_KEY=your-generated-secret-key
DEBUG=True

DB_NAME=postgres
DB_USER=postgres.abcdefgh12345
DB_PASSWORD=YourPassword123
DB_HOST=aws-0-ap-southeast-1.pooler.supabase.com
DB_PORT=5432
```

> **Catatan Penting:**
> - Gunakan password yang Anda buat saat membuat project, bukan password akun Supabase
> - Jika koneksi timeout, coba gunakan port `6543` (Transaction pooler) daripada `5432`

---

### Opsi B: Menggunakan PostgreSQL Lokal

#### Windows

1. Download PostgreSQL dari [postgresql.org/download/windows](https://www.postgresql.org/download/windows/)
2. Jalankan installer dan ikuti wizard:
   - Catat password untuk user `postgres`
   - Port default: `5432`
3. Buka **pgAdmin** atau **SQL Shell (psql)**
4. Buat database:
   ```sql
   CREATE DATABASE laundry_db;
   ```
5. Isi file `.env`:
   ```env
   SECRET_KEY=your-generated-secret-key
   DEBUG=True
   
   DB_NAME=laundry_db
   DB_USER=postgres
   DB_PASSWORD=password-postgres-anda
   DB_HOST=localhost
   DB_PORT=5432
   ```

#### Linux (Ubuntu/Debian)

```bash
# Install PostgreSQL
sudo apt install postgresql postgresql-contrib

# Masuk ke PostgreSQL
sudo -u postgres psql

# Buat database dan user
CREATE DATABASE laundry_db;
CREATE USER laundry_user WITH PASSWORD 'your_secure_password';
ALTER ROLE laundry_user SET client_encoding TO 'utf8';
ALTER ROLE laundry_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE laundry_user SET timezone TO 'Asia/Jakarta';
GRANT ALL PRIVILEGES ON DATABASE laundry_db TO laundry_user;
\q
```

Isi file `.env`:
```env
SECRET_KEY=your-generated-secret-key
DEBUG=True

DB_NAME=laundry_db
DB_USER=laundry_user
DB_PASSWORD=your_secure_password
DB_HOST=localhost
DB_PORT=5432
```

#### macOS

```bash
# Install PostgreSQL via Homebrew
brew install postgresql@15
brew services start postgresql@15

# Buat database
createdb laundry_db

# Atau masuk ke psql dan buat manual
psql postgres
CREATE DATABASE laundry_db;
\q
```

Isi file `.env`:
```env
SECRET_KEY=your-generated-secret-key
DEBUG=True

DB_NAME=laundry_db
DB_USER=your_mac_username
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=5432
```

---

### Verifikasi Koneksi Database

Setelah konfigurasi `.env`, verifikasi koneksi:

```bash
# Aktifkan virtual environment terlebih dahulu
# Windows: venv\Scripts\activate
# Linux/macOS: source venv/bin/activate

python manage.py check --database default
```

Jika berhasil, akan muncul:
```
System check identified no issues (0 silenced).
```

Jika ada error koneksi, periksa:
1. Kredensial database di `.env` sudah benar
2. Database server sudah berjalan
3. Koneksi internet (untuk Supabase)
4. Firewall tidak memblokir port 5432

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
