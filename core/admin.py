from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Akun, Karyawan, Pelanggan, Layanan, Transaksi, LogHistory


@admin.register(Akun)
class AkunAdmin(UserAdmin):
    list_display = ['username', 'peran', 'is_active', 'date_joined']
    list_filter = ['peran', 'is_active', 'date_joined']
    search_fields = ['username']
    ordering = ['-date_joined']
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Peran', {'fields': ('peran',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Tanggal Penting', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'peran', 'password1', 'password2'),
        }),
    )


@admin.register(Karyawan)
class KaryawanAdmin(admin.ModelAdmin):
    list_display = ['nama', 'nomor_hp', 'akun', 'alamat']
    search_fields = ['nama', 'nomor_hp']
    list_filter = ['akun__peran']


admin.site.register(Pelanggan)
admin.site.register(Layanan)
admin.site.register(Transaksi)
admin.site.register(LogHistory)
