# MANUAL SETUP - TESTING WEBSITE

## 🎯 YANG DIBUTUHKAN:

**Hardware/Msoftware:**
- Python 3.10+ (wajib)
- Koneksi internet (untuk database cloud)

**Files dari project:**
- Folder project (extract dari ZIP)
- File `.env` (sudah disediakan)

---

## 📋 LANGKAH-LANGKAH

### **1. Extract Project**
- Extract ZIP ke folder tanpa spasi
- Contoh: `C:\laundry-project` (Windows) atau `~/laundry-project` (macOS)

### **2. Setup Python Environment**

**Windows:**
```cmd
cd C:\laundry-project
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**macOS:**
```bash
cd ~/laundry-project
python3 -m venv venv  
source venv/bin/activate
pip install -r requirements.txt
```

### **3. Start Website**
```cmd
# Windows
python manage.py runserver

# macOS  
python3 manage.py runserver
```

### **4. Test di Browser**
- Buka: http://127.0.0.1:8000/
- Login: http://127.0.0.1:8000/login/
- Username: `admin`
- Password: `admin123`

---

## ✅ CEK FUNCTIONALITY

### Basic Tests:
- [ ] Homepage opens
- [ ] Login successful  
- [ ] Dashboard loads
- [ ] Can view customer list
- [ ] Can create new order
- [ ] Can view transactions

### URL Testing:
- Dashboard: http://127.0.0.1:8000/dashboard/
- Order: http://127.0.0.1:8000/order-laundry/
- Pelanggan: http://127.0.0.1:8000/kelola-pelanggan/
- Transaksi: http://127.0.0.1:8000/daftar-transaksi/

---

## 🆘 ERROR FIX

| Error | Cara Fix |
|-------|----------|
| `'python' not found` | Install Python dari python.org (centang "Add to PATH") |
| `No module named 'psycopg2'` | Jalankan: `pip install psycopg2-binary` |
| Database connection failed | Pastikan file `.env` ada di folder utama |
| Port 8000 already in use | Ganti port: `python manage.py runserver 8080` |

---

## 📏 SUCCESS CRITERIA

**✅ WEBSITE BERHASIL JALAN JIKA:**
1. Bisa buka http://127.0.0.1:8000/ tanpa error
2. Login dengan admin/admin123 berhasil
3. Dashboard tampil dengan menu navigasi
4. Buka navigate ke fitur utama
5. Tidak ada database error

**🎯 READY FOR GRADING!**

---

## ⏱ ESTIMASI WAKTU

- **Install Python**: 10 menit (jika belum ada)
- **Setup Project**: 5 menit  
- **Testing**: 5 menit
- **Total**: **15-20 menit**

---

**Manual Setup Only - No Scripts Needed!** ✅
