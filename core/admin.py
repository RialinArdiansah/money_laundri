from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Pengguna, Pelanggan, Layanan, Transaksi, LogHistory


@admin.register(Pengguna)
class PenggunaAdmin(UserAdmin):
    list_display = ['username', 'nama', 'peran', 'is_active', 'date_joined']
    list_filter = ['peran', 'is_active', 'date_joined']
    search_fields = ['username', 'nama']
    ordering = ['-date_joined']
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informasi Personal', {'fields': ('nama',)}),
        ('Peran', {'fields': ('peran',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Tanggal Penting', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'nama', 'peran', 'password1', 'password2'),
        }),
    )


admin.site.register(Pelanggan)
admin.site.register(Layanan)
admin.site.register(Transaksi)
admin.site.register(LogHistory)
