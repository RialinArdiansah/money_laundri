from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Pengguna, Pelanggan, Transaksi, Layanan
from datetime import date, timedelta


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
            'placeholder': 'Masukkan username'
        })
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
            'placeholder': 'Masukkan password'
        })
    )


class PelangganForm(forms.ModelForm):
    class Meta:
        model = Pelanggan
        fields = ['nama_pelanggan', 'nomor_handphone', 'alamat']
        labels = {
            'nama_pelanggan': 'Nama Lengkap',
            'nomor_handphone': 'Nomor Handphone',
            'alamat': 'Alamat',
        }
        widgets = {
            'nama_pelanggan': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Masukkan nama lengkap'
            }),
            'nomor_handphone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Masukkan nomor handphone'
            }),
            'alamat': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Masukkan alamat (opsional)',
                'rows': 3
            }),
        }
    
    def clean_nama_pelanggan(self):
        nama = self.cleaned_data.get('nama_pelanggan')
        if not nama or len(nama.strip()) < 3:
            raise forms.ValidationError('Nama lengkap tidak boleh kosong')
        return nama
    
    def clean_nomor_handphone(self):
        nomor = self.cleaned_data.get('nomor_handphone')
        if not nomor.isdigit():
            raise forms.ValidationError('Nomor handphone hanya boleh angka')
        if len(nomor) < 10 or len(nomor) > 13:
            raise forms.ValidationError('Nomor handphone harus 10-13 digit')
        
        if self.instance.pk:
            if Pelanggan.objects.exclude(pk=self.instance.pk).filter(nomor_handphone=nomor).exists():
                pelanggan_lama = Pelanggan.objects.exclude(pk=self.instance.pk).filter(nomor_handphone=nomor).first()
                raise forms.ValidationError(f'Nomor handphone sudah digunakan oleh pelanggan {pelanggan_lama.nama_pelanggan}.')
        else:
            if Pelanggan.objects.filter(nomor_handphone=nomor).exists():
                pelanggan_lama = Pelanggan.objects.filter(nomor_handphone=nomor).first()
                raise forms.ValidationError(f'Nomor handphone sudah digunakan oleh pelanggan {pelanggan_lama.nama_pelanggan}.')
        
        return nomor


class KaryawanForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Masukkan password (minimal 6 karakter)'
        })
    )
    
    class Meta:
        model = Pengguna
        fields = ['nama', 'username', 'password', 'nomor_handphone', 'peran']
        labels = {
            'nama': 'Nama',
            'username': 'Username',
            'nomor_handphone': 'Nomor Handphone',
            'peran': 'Jabatan',
        }
        widgets = {
            'nama': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Masukkan nama'
            }),
            'username': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Masukkan username'
            }),
            'nomor_handphone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Masukkan nomor handphone'
            }),
            'peran': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500'
            }),
        }
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if self.instance.pk:
            if Pengguna.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
                raise forms.ValidationError('Username sudah digunakan')
        else:
            if Pengguna.objects.filter(username=username).exists():
                raise forms.ValidationError('Username sudah digunakan')
        return username
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not self.instance.pk and not password:
            raise forms.ValidationError('Password harus diisi untuk pegawai baru')
        if password and len(password) < 6:
            raise forms.ValidationError('Password minimal 6 karakter')
        return password
    
    def clean_nomor_handphone(self):
        nomor = self.cleaned_data.get('nomor_handphone')
        if not nomor.isdigit():
            raise forms.ValidationError('Nomor handphone hanya boleh angka')
        if len(nomor) < 10 or len(nomor) > 13:
            raise forms.ValidationError('Nomor handphone harus 10-13 digit')
        return nomor
    
    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user


class TransaksiForm(forms.ModelForm):
    pelanggan_search = forms.CharField(
        required=False,
        label='Pencarian Pelanggan',
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Cari nama atau nomor HP pelanggan',
            'id': 'pelanggan-search'
        })
    )
    
    class Meta:
        model = Transaksi
        fields = ['id_pelanggan', 'jenis_layanan', 'berat_cucian', 'tanggal_estimasi_selesai', 'catatan']
        labels = {
            'id_pelanggan': 'Pelanggan',
            'jenis_layanan': 'Jenis Layanan',
            'berat_cucian': 'Berat (Kg)',
            'tanggal_estimasi_selesai': 'Tanggal Estimasi Selesai',
            'catatan': 'Catatan Tambahan',
        }
        widgets = {
            'id_pelanggan': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500',
                'id': 'pelanggan-select'
            }),
            'jenis_layanan': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500'
            }),
            'berat_cucian': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Masukkan berat dalam kg',
                'step': '0.01',
                'min': '0.01'
            }),
            'tanggal_estimasi_selesai': forms.DateInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500',
                'type': 'date'
            }),
            'catatan': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Catatan tambahan (opsional)',
                'rows': 3
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            self.fields['tanggal_estimasi_selesai'].initial = date.today() + timedelta(days=2)
    
    def clean_berat_cucian(self):
        berat = self.cleaned_data.get('berat_cucian')
        if berat and berat < 1:
            raise forms.ValidationError('Berat cucian minimal 1 kg')
        return berat
    
    def clean_jenis_layanan(self):
        layanan = self.cleaned_data.get('jenis_layanan')
        if not layanan:
            raise forms.ValidationError('Pilih layanan dahulu')
        return layanan


class UpdateStatusForm(forms.Form):
    STATUS_CHOICES = [
        ('Diterima', 'Diterima'),
        ('Proses', 'Proses'),
        ('Selesai', 'Selesai'),
        ('Sudah Diambil', 'Sudah Diambil'),
    ]
    
    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        label='Status Pesanan',
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500'
        })
    )


class CekStatusForm(forms.Form):
    nomor_order = forms.CharField(
        label='Nomor Order',
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Masukkan nomor order'
        })
    )
    nomor_telepon = forms.CharField(
        label='Nomor Telepon',
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Masukkan nomor telepon'
        })
    )
