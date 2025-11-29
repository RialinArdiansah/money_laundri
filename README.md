# Sistem Manajemen Laundry Berbasis Web

Sistem manajemen laundry lengkap dengan Django backend, Tailwind CSS frontend, dan PostgreSQL Supabase sebagai database.

## Fitur Utama

### Untuk Pegawai/Owner:
- **Login** - Autentikasi pengguna dengan role-based access (Pegawai/Owner)
- **Order Laundry** - Membuat pesanan laundry baru dengan pencarian pelanggan dan kalkulasi otomatis
- **Kelola Data Pelanggan** - CRUD data pelanggan dengan validasi nomor HP unik
- **Kelola Data Karyawan** - CRUD data karyawan (khusus Owner)
- **Daftar Transaksi** - Melihat semua transaksi laundry
- **Update Status Pesanan** - Mengubah status cucian (Diterima → Proses → Selesai → Sudah Diambil)
- **Koreksi Status** - Mengembalikan status ke tahap sebelumnya
- **Cetak Nota** - Mencetak nota transaksi
- **Laporan Transaksi** - Laporan dengan filter tanggal dan status
- **Status Cucian** - Monitoring status laundry

### Untuk Pelanggan (Public):
- **Cek Status Laundry** - Cek status pesanan menggunakan nomor order dan nomor telepon

## Struktur Proyek

```
laundry_project/
├── laundry_project/
│   ├── __init__.py
│   ├── settings.py          # Konfigurasi Django + PostgreSQL Supabase
│   ├── urls.py               # URL routing utama
│   ├── asgi.py
│   └── wsgi.py
├── core/
│   ├── migrations/
│   ├── templates/core/       # Semua template HTML
│   │   ├── base.html
│   │   ├── halaman_utama.html
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   ├── order_laundry.html
│   │   ├── cek_status_laundry.html
│   │   ├── kelola_pelanggan.html
│   │   ├── form_pelanggan.html
│   │   ├── kelola_karyawan.html
│   │   ├── form_karyawan.html
│   │   ├── daftar_transaksi.html
│   │   ├── detail_transaksi.html
│   │   ├── cetak_nota.html
│   │   ├── laporan_transaksi.html
│   │   └── status_cucian.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py             # Model: Pengguna, Pelanggan, Layanan, Transaksi, LogHistory
│   ├── views.py              # Semua logika CRUD sesuai use case
│   ├── forms.py              # Form handling dengan validasi
│   └── urls.py               # URL routing core app
├── static/
│   └── css/
│       └── input.css         # Tailwind CSS input
├── manage.py
├── requirements.txt
├── package.json              # Node.js dependencies untuk Tailwind
├── tailwind.config.js        # Konfigurasi Tailwind CSS
├── .env.example              # Template environment variables
└── README.md
```

## Database Schema

### Tabel: tb_pengguna (Custom User Model)
- id (PK)
- username (Unique)
- password
- peran (Pegawai/Owner)
- nama_lengkap
- email
- nomor_handphone
- tanggal_bergabung

### Tabel: tb_pelanggan
- id (PK)
- nama_pelanggan
- nomor_handphone (Unique)
- alamat
- tanggal_registrasi

### Tabel: tb_layanan
- id (PK)
- nama_layanan
- harga_per_kg
- estimasi_waktu (dalam hari)

### Tabel: tb_transaksi
- id (PK)
- nomor_order (Unique, auto-generated: ORD-YYYYMMDD-XXXX)
- id_pelanggan (FK → tb_pelanggan)
- id_pegawai (FK → tb_pengguna)
- jenis_layanan (FK → tb_layanan)
- berat_cucian
- total_biaya (auto-calculated)
- tanggal_masuk
- tanggal_estimasi_selesai
- catatan
- status (Diterima, Proses, Selesai, Sudah Diambil)
- status_pembayaran (Belum Lunas, Lunas)
- batas_penyimpanan (auto-calculated: estimasi + 2 hari)

### Tabel: tb_log_history
- id (PK)
- id_transaksi (FK → tb_transaksi)
- status_sebelum
- status_sesudah
- waktu_perubahan
- id_pegawai (FK → tb_pengguna)
- keterangan

## Instalasi

### 1. Clone/Download Project
```bash
cd D:/RPLBO/laundry_project
```

### 2. Buat Virtual Environment
```bash
python -m venv venv
```

### 3. Aktivasi Virtual Environment
Windows:
```bash
venv\Scripts\activate
```

### 4. Install Dependencies Python
```bash
pip install -r requirements.txt
```

### 5. Setup Environment Variables
Salin file `.env.example` menjadi `.env` dan sesuaikan konfigurasi database Supabase:
```
DB_NAME=your_database_name
DB_USER=your_supabase_user
DB_PASSWORD=your_supabase_password
DB_HOST=your_supabase_host.supabase.co
DB_PORT=5432
```

Atau edit langsung di `laundry_project/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_supabase_user',
        'PASSWORD': 'your_supabase_password',
        'HOST': 'your_supabase_host.supabase.co',
        'PORT': '5432',
    }
}
```

### 6. Install Node.js Dependencies (untuk Tailwind CSS)
```bash
npm install
```

### 7. Build Tailwind CSS
```bash
npm run build:css
```

Untuk development dengan auto-rebuild:
```bash
npm run watch:css
```

### 8. Migrasi Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 9. Buat Superuser (Owner)
```bash
python manage.py createsuperuser
```
Ikuti instruksi untuk membuat akun Owner pertama.

### 10. (Opsional) Buat Data Layanan
Masuk ke Django Admin atau gunakan shell:
```bash
python manage.py shell
```
```python
from core.models import Layanan

Layanan.objects.create(
    nama_layanan='Cuci Kering',
    harga_per_kg=5000,
    estimasi_waktu=1
)

Layanan.objects.create(
    nama_layanan='Cuci Setrika',
    harga_per_kg=7000,
    estimasi_waktu=2
)

Layanan.objects.create(
    nama_layanan='Setrika Saja',
    harga_per_kg=3000,
    estimasi_waktu=1
)
```

### 11. Jalankan Server
```bash
python manage.py runserver
```

Akses aplikasi di: `http://127.0.0.1:8000/`

## Akses Halaman

### Public (Tidak perlu login):
- Halaman Utama: `/`
- Login: `/login/`
- Cek Status Laundry: `/cek-status-laundry/`

### Pegawai/Owner (Perlu login):
- Dashboard: `/dashboard/`
- Order Laundry: `/order-laundry/`
- Data Pelanggan: `/kelola-pelanggan/`
- Daftar Transaksi: `/daftar-transaksi/`
- Status Cucian: `/status-cucian/`
- Laporan Transaksi: `/laporan-transaksi/`

### Owner Only:
- Data Karyawan: `/kelola-karyawan/`

## Use Case Implementation

### 1. Login
- **Actor**: Pegawai, Owner
- **Flow**: Input username & password → Validasi → Redirect ke dashboard sesuai role
- **Exception**: Username/password salah → Error message

### 2. Membuat Pesanan Laundry
- **Actor**: Pegawai, Owner
- **Flow**: 
  - Pilih pelanggan (atau tambah baru)
  - Pilih layanan
  - Input berat cucian
  - Sistem kalkulasi total biaya otomatis
  - Set tanggal estimasi
  - Simpan → Generate nomor order → Cetak nota
- **Alternative**: Tambah pelanggan baru via modal popup
- **Exception**: Validasi berat minimal 1 kg, layanan harus dipilih

### 3. Cek Status Laundry
- **Actor**: Pelanggan (Public)
- **Flow**: Input nomor order + nomor telepon → Tampilkan status
- **Exception**: Nomor order tidak ditemukan

### 4. Kelola Data Pelanggan
- **Actor**: Pegawai, Owner
- **Flow**: CRUD pelanggan
- **Validation**: 
  - Nama minimal 3 karakter
  - Nomor HP harus unik, hanya angka, 10-13 digit
- **Exception**: Nomor HP sudah terdaftar

### 5. Kelola Data Karyawan
- **Actor**: Owner
- **Flow**: CRUD karyawan
- **Validation**:
  - Username harus unik
  - Password minimal 6 karakter
  - Nomor HP valid
- **Exception**: Username sudah digunakan

### 6. Update Status Pesanan
- **Actor**: Pegawai, Owner
- **Flow**: 
  - Update status: Diterima → Proses → Selesai → Sudah Diambil
  - Catat di log history
- **Alternative**: Koreksi status (rollback ke status sebelumnya)
- **Exception**:
  - Blokir pengambilan jika belum lunas
  - Status "Sudah Diambil" terkunci

## Validasi & Business Rules

### Pelanggan:
- Nama tidak boleh kosong (minimal 3 karakter)
- Nomor HP harus unik
- Nomor HP hanya angka (10-13 digit)

### Karyawan:
- Username harus unik
- Password minimal 6 karakter
- Nomor HP harus valid (10-13 digit)

### Transaksi:
- Berat cucian minimal 1 kg
- Jenis layanan wajib dipilih
- Total biaya = harga_per_kg × berat_cucian
- Nomor order auto-generate: ORD-YYYYMMDD-XXXX
- Batas penyimpanan = estimasi selesai + 2 hari
- Status pembayaran default: Belum Lunas
- Status final "Sudah Diambil" terkunci, tidak bisa diubah

### Status Workflow:
```
Diterima → Proses → Selesai → Sudah Diambil
    ↑         ↑        ↑
    └─────────┴────────┘ (Koreksi Status diizinkan)
```

### Pembayaran:
- Barang tidak dapat diambil (status → Sudah Diambil) jika status_pembayaran = "Belum Lunas"

## Teknologi

- **Backend**: Django 4.2.7
- **Database**: PostgreSQL (Supabase)
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Authentication**: Django Auth dengan Custom User Model
- **ORM**: Django ORM

## Pesan Error & Notifikasi

Semua pesan sesuai spesifikasi dokumen:
- ✅ "Username atau password salah"
- ✅ "Order berhasil disimpan."
- ✅ "Pelanggan berhasil ditambahkan."
- ✅ "Nomor handphone hanya boleh angka"
- ✅ "Nomor handphone sudah digunakan oleh pelanggan [nama]."
- ✅ "Berat cucian minimal 1 kg"
- ✅ "Pilih layanan dahulu"
- ✅ "Data pegawai berhasil disimpan."
- ✅ "Data pegawai berhasil diperbarui."
- ✅ "Data pegawai berhasil dihapus."
- ✅ "Nomor order tidak ditemukan"
- ✅ "Barang tidak dapat diambil. Harap lunasi pembayaran terlebih dahulu."
- ✅ "Transaksi sudah selesai. Hubungi Owner untuk pembatalan."
- ✅ "Status berhasil diperbarui."
- ✅ "Harap lengkapi semua data pesanan sebelum menyimpan."

## Catatan Penting

1. Pastikan PostgreSQL Supabase sudah dikonfigurasi dengan benar
2. Tailwind CSS menggunakan CDN untuk kemudahan (sudah included di base.html)
3. Semua terminologi, penamaan field, dan flow sesuai 100% dengan dokumen spesifikasi
4. Format nomor order: ORD-YYYYMMDD-XXXX (auto-generated)
5. Custom User Model menggunakan AbstractUser dengan field tambahan
6. Role-based access control: Owner memiliki akses penuh, Pegawai tidak bisa kelola karyawan

## Troubleshooting

### Error: "No module named 'psycopg2'"
```bash
pip install psycopg2-binary
```

### Error: Tailwind CSS tidak berfungsi
Pastikan CDN Tailwind sudah ada di base.html atau jalankan:
```bash
npm run build:css
```

### Error: Database connection
Periksa konfigurasi database di settings.py dan pastikan kredensial Supabase benar.

## Lisensi

Project ini dibuat untuk keperluan pembelajaran dan pengembangan sistem manajemen laundry.

## Kontak

Untuk pertanyaan atau bantuan, silakan hubungi tim developer.
