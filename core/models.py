from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta


class Akun(AbstractUser):
    PERAN_CHOICES = [
        ('Karyawan', 'Karyawan'),
        ('Owner', 'Owner'),
    ]
    peran = models.CharField(max_length=20, choices=PERAN_CHOICES, default='Karyawan')
    email = None
    first_name = None
    last_name = None
    
    class Meta:
        db_table = 'tb_akun'
        verbose_name = 'Akun'
        verbose_name_plural = 'Akun'
    
    def __str__(self):
        return f"{self.username} ({self.peran})"


class Karyawan(models.Model):
    akun = models.OneToOneField(Akun, on_delete=models.CASCADE, related_name='karyawan', null=True, blank=True)
    nama = models.CharField(max_length=200)
    alamat = models.TextField(blank=True, null=True)
    nomor_hp = models.CharField(max_length=15)
    
    class Meta:
        db_table = 'tb_karyawan'
        verbose_name = 'Karyawan'
        verbose_name_plural = 'Karyawan'
    
    def __str__(self):
        return self.nama


class Pelanggan(models.Model):
    nama_pelanggan = models.CharField(max_length=200)
    nomor_handphone = models.CharField(max_length=15, unique=True)
    alamat = models.TextField(blank=True, null=True)
    tanggal_registrasi = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = 'tb_pelanggan'
        verbose_name = 'Pelanggan'
        verbose_name_plural = 'Pelanggan'
    
    def __str__(self):
        return self.nama_pelanggan


class Layanan(models.Model):
    nama_layanan = models.CharField(max_length=100)
    harga_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    estimasi_waktu = models.IntegerField(help_text='Estimasi waktu dalam hari')
    
    class Meta:
        db_table = 'tb_layanan'
        verbose_name = 'Layanan'
        verbose_name_plural = 'Layanan'
    
    def __str__(self):
        return self.nama_layanan


class Transaksi(models.Model):
    STATUS_CHOICES = [
        ('Diterima', 'Diterima'),
        ('Proses', 'Proses'),
        ('Selesai', 'Selesai'),
        ('Diambil', 'Diambil'),
    ]
    
    STATUS_PEMBAYARAN_CHOICES = [
        ('Belum Lunas', 'Belum Lunas'),
        ('Lunas', 'Lunas'),
    ]
    
    nomor_order = models.CharField(max_length=50, unique=True)
    id_pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE, related_name='transaksi')
    id_pegawai = models.ForeignKey(Akun, on_delete=models.SET_NULL, null=True, related_name='transaksi')
    jenis_layanan = models.ForeignKey(Layanan, on_delete=models.CASCADE, related_name='transaksi')
    berat_cucian = models.DecimalField(max_digits=6, decimal_places=2)
    total_biaya = models.DecimalField(max_digits=12, decimal_places=2)
    tanggal_masuk = models.DateTimeField(auto_now_add=True)
    tanggal_estimasi_selesai = models.DateField()
    catatan = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Diterima')
    status_pembayaran = models.CharField(max_length=20, choices=STATUS_PEMBAYARAN_CHOICES, default='Belum Lunas')
    batas_penyimpanan = models.DateField(blank=True, null=True)
    
    class Meta:
        db_table = 'tb_transaksi'
        verbose_name = 'Transaksi'
        verbose_name_plural = 'Transaksi'
        ordering = ['-tanggal_masuk']
    
    def __str__(self):
        return f"{self.nomor_order} - {self.id_pelanggan.nama_pelanggan}"
    
    def save(self, *args, **kwargs):
        if not self.nomor_order:
            from datetime import datetime
            tanggal = datetime.now().strftime('%Y%m%d')
            last_order = Transaksi.objects.filter(nomor_order__startswith=f'ORD-{tanggal}').order_by('-nomor_order').first()
            if last_order:
                last_number = int(last_order.nomor_order.split('-')[-1])
                new_number = last_number + 1
            else:
                new_number = 1
            self.nomor_order = f'ORD-{tanggal}-{new_number:04d}'
        
        if not self.batas_penyimpanan and self.tanggal_estimasi_selesai:
            self.batas_penyimpanan = self.tanggal_estimasi_selesai + timedelta(days=2)
        
        super().save(*args, **kwargs)


class LogHistory(models.Model):
    id_transaksi = models.ForeignKey(Transaksi, on_delete=models.CASCADE, related_name='log_history')
    status_sebelum = models.CharField(max_length=20)
    status_sesudah = models.CharField(max_length=20)
    waktu_perubahan = models.DateTimeField(auto_now_add=True)
    id_pegawai = models.ForeignKey(Akun, on_delete=models.SET_NULL, null=True, related_name='log_history')
    keterangan = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'tb_log_history'
        verbose_name = 'Log History'
        verbose_name_plural = 'Log History'
        ordering = ['-waktu_perubahan']
    
    def __str__(self):
        return f"{self.id_transaksi.nomor_order} - {self.status_sebelum} → {self.status_sesudah}"
