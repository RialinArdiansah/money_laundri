from django.urls import path
from . import views

urlpatterns = [
    path('', views.halaman_utama, name='halaman_utama'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    path('order-laundry/', views.order_laundry, name='order_laundry'),
    path('search-pelanggan/', views.search_pelanggan, name='search_pelanggan'),
    path('tambah-pelanggan-ajax/', views.tambah_pelanggan_ajax, name='tambah_pelanggan_ajax'),
    path('get-layanan-harga/<int:layanan_id>/', views.get_layanan_harga, name='get_layanan_harga'),
    
    path('cek-status-laundry/', views.cek_status_laundry, name='cek_status_laundry'),
    
    path('kelola-pelanggan/', views.kelola_pelanggan, name='kelola_pelanggan'),
    path('tambah-pelanggan/', views.tambah_pelanggan, name='tambah_pelanggan'),
    path('edit-pelanggan/<int:pelanggan_id>/', views.edit_pelanggan, name='edit_pelanggan'),
    path('hapus-pelanggan/<int:pelanggan_id>/', views.hapus_pelanggan, name='hapus_pelanggan'),
    
    path('kelola-karyawan/', views.kelola_karyawan, name='kelola_karyawan'),
    path('tambah-karyawan/', views.tambah_karyawan, name='tambah_karyawan'),
    path('edit-karyawan/<int:karyawan_id>/', views.edit_karyawan, name='edit_karyawan'),
    path('hapus-karyawan/<int:karyawan_id>/', views.hapus_karyawan, name='hapus_karyawan'),
    
    path('daftar-transaksi/', views.daftar_transaksi, name='daftar_transaksi'),
    path('detail-transaksi/<int:transaksi_id>/', views.detail_transaksi, name='detail_transaksi'),
    path('update-status/<int:transaksi_id>/', views.update_status, name='update_status'),
    path('koreksi-status/<int:transaksi_id>/', views.koreksi_status, name='koreksi_status'),
    path('update-pembayaran/<int:transaksi_id>/', views.update_pembayaran, name='update_pembayaran'),
    
    path('cetak-nota/<int:transaksi_id>/', views.cetak_nota, name='cetak_nota'),
]
