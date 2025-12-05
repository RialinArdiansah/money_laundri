from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.db.models import Q, Sum
from django.utils import timezone
from datetime import datetime, timedelta, date
from decimal import Decimal

from .models import Akun, Karyawan, Pelanggan, Layanan, Transaksi, LogHistory
from .forms import LoginForm, PelangganForm, KaryawanForm, TransaksiForm, UpdateStatusForm, CekStatusForm


def is_owner(user):
    return user.is_authenticated and user.peran == 'Owner'


def is_karyawan_or_owner(user):
    return user.is_authenticated and user.peran in ['Karyawan', 'Owner']


def halaman_utama(request):
    return render(request, 'core/halaman_utama.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        else:
            messages.error(request, 'Username atau password salah')
    else:
        form = LoginForm()
    
    return render(request, 'core/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('halaman_utama')


@login_required
def dashboard(request):
    import json
    from django.db.models import Count, Case, When, IntegerField
    from django.db.models.functions import TruncDate
    
    today = timezone.now().date()
    week_ago = today - timedelta(days=6)
    
    # Single query for all statistics using conditional aggregation
    stats = Transaksi.objects.aggregate(
        total_transaksi=Count('id'),
        total_pendapatan=Sum('total_biaya'),
        transaksi_hari_ini=Count(Case(When(tanggal_masuk__date=today, then=1), output_field=IntegerField())),
        pendapatan_hari_ini=Sum(Case(When(tanggal_masuk__date=today, then='total_biaya'))),
        transaksi_aktif=Count(Case(When(~Q(status='Diambil'), then=1), output_field=IntegerField())),
        belum_lunas=Sum(Case(When(status_pembayaran='Belum Lunas', then='total_biaya'))),
    )
    
    # Recent Activities - Latest 10 transactions
    recent_activities = Transaksi.objects.select_related(
        'id_pelanggan', 'jenis_layanan'
    ).order_by('-tanggal_masuk')[:10]
    
    # Chart Data - Single query with database-level grouping
    daily_data = Transaksi.objects.filter(
        tanggal_masuk__date__gte=week_ago
    ).annotate(
        day=TruncDate('tanggal_masuk')
    ).values('day').annotate(
        count=Count('id')
    ).order_by('day')
    
    # Build chart data with all 7 days (fill missing days with 0)
    daily_dict = {item['day']: item['count'] for item in daily_data}
    last_7_days = [today - timedelta(days=i) for i in range(6, -1, -1)]
    daily_transactions = [daily_dict.get(day, 0) for day in last_7_days]
    chart_labels = [day.strftime('%d %b') for day in last_7_days]
    
    context = {
        'user': request.user,
        'total_transaksi': stats['total_transaksi'] or 0,
        'total_pendapatan': stats['total_pendapatan'] or 0,
        'transaksi_hari_ini': stats['transaksi_hari_ini'] or 0,
        'pendapatan_hari_ini': stats['pendapatan_hari_ini'] or 0,
        'recent_activities': recent_activities,
        'transaksi_aktif': stats['transaksi_aktif'] or 0,
        'belum_lunas': stats['belum_lunas'] or 0,
        'chart_labels': json.dumps(chart_labels),
        'daily_transactions': json.dumps(daily_transactions),
    }
    return render(request, 'core/dashboard.html', context)


@login_required
@user_passes_test(is_karyawan_or_owner)
def order_laundry(request):
    if request.method == 'POST':
        form = TransaksiForm(request.POST)
        if form.is_valid():
            try:
                transaksi = form.save(commit=False)
                transaksi.id_pegawai = request.user
                
                layanan = transaksi.jenis_layanan
                berat = transaksi.berat_cucian
                transaksi.total_biaya = layanan.harga_per_kg * berat
                
                transaksi.save()
                
                messages.success(request, 'Order berhasil disimpan.')
                return redirect('cetak_nota', transaksi_id=transaksi.id)
            except Exception as e:
                messages.error(request, 'Gagal menyimpan data order. Silakan coba lagi.')
        else:
            if form.errors:
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, error)
            else:
                messages.warning(request, 'Harap lengkapi semua data pesanan sebelum menyimpan.')
    else:
        form = TransaksiForm()
    
    pelanggan_list = Pelanggan.objects.all()
    layanan_list = Layanan.objects.all()
    
    context = {
        'form': form,
        'pelanggan_list': pelanggan_list,
        'layanan_list': layanan_list,
    }
    return render(request, 'core/order_laundry.html', context)


@login_required
@user_passes_test(is_karyawan_or_owner)
def tambah_pelanggan_ajax(request):
    if request.method == 'POST':
        form = PelangganForm(request.POST)
        if form.is_valid():
            pelanggan = form.save()
            return JsonResponse({
                'success': True,
                'message': 'Pelanggan berhasil ditambahkan.',
                'pelanggan': {
                    'id': pelanggan.id,
                    'nama': pelanggan.nama_pelanggan,
                    'nomor_hp': pelanggan.nomor_handphone
                }
            })
        else:
            errors = []
            for field, error_list in form.errors.items():
                for error in error_list:
                    errors.append(str(error))
            return JsonResponse({
                'success': False,
                'errors': errors
            })
    return JsonResponse({'success': False, 'message': 'Invalid request'})


@login_required
@user_passes_test(is_karyawan_or_owner)
def search_pelanggan(request):
    query = request.GET.get('q', '')
    if query:
        pelanggan = Pelanggan.objects.filter(
            Q(nama_pelanggan__icontains=query) | Q(nomor_handphone__icontains=query)
        )[:10]
        results = [{'id': p.id, 'nama': p.nama_pelanggan, 'nomor_hp': p.nomor_handphone} for p in pelanggan]
        return JsonResponse({'results': results})
    return JsonResponse({'results': []})


@login_required
@user_passes_test(is_karyawan_or_owner)
def get_layanan_harga(request, layanan_id):
    try:
        layanan = Layanan.objects.get(id=layanan_id)
        return JsonResponse({
            'harga_per_kg': str(layanan.harga_per_kg),
            'estimasi_waktu': layanan.estimasi_waktu
        })
    except Layanan.DoesNotExist:
        return JsonResponse({'error': 'Layanan tidak ditemukan'}, status=404)


def cek_status_laundry(request):
    transaksi = None
    if request.method == 'POST':
        form = CekStatusForm(request.POST)
        if form.is_valid():
            nomor_order = form.cleaned_data['nomor_order']
            nomor_telepon = form.cleaned_data['nomor_telepon']
            
            try:
                transaksi = Transaksi.objects.get(
                    nomor_order=nomor_order,
                    id_pelanggan__nomor_handphone=nomor_telepon
                )
            except Transaksi.DoesNotExist:
                messages.error(request, 'Nomor order tidak ditemukan')
    else:
        form = CekStatusForm()
    
    context = {
        'form': form,
        'transaksi': transaksi,
    }
    return render(request, 'core/cek_status_laundry.html', context)


@login_required
@user_passes_test(is_karyawan_or_owner)
def kelola_pelanggan(request):
    pelanggan_list = Pelanggan.objects.all().order_by('-tanggal_registrasi')
    context = {
        'pelanggan_list': pelanggan_list,
    }
    return render(request, 'core/kelola_pelanggan.html', context)


@login_required
@user_passes_test(is_karyawan_or_owner)
def tambah_pelanggan(request):
    if request.method == 'POST':
        form = PelangganForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pelanggan berhasil ditambahkan.')
            return redirect('kelola_pelanggan')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = PelangganForm()
    
    context = {'form': form, 'mode': 'tambah'}
    return render(request, 'core/form_pelanggan.html', context)


@login_required
@user_passes_test(is_karyawan_or_owner)
def edit_pelanggan(request, pelanggan_id):
    pelanggan = get_object_or_404(Pelanggan, id=pelanggan_id)
    if request.method == 'POST':
        form = PelangganForm(request.POST, instance=pelanggan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data pelanggan berhasil disimpan')
            return redirect('kelola_pelanggan')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = PelangganForm(instance=pelanggan)
    
    context = {'form': form, 'mode': 'edit', 'pelanggan': pelanggan}
    return render(request, 'core/form_pelanggan.html', context)


@login_required
@user_passes_test(is_karyawan_or_owner)
def hapus_pelanggan(request, pelanggan_id):
    pelanggan = get_object_or_404(Pelanggan, id=pelanggan_id)
    if request.method == 'POST':
        pelanggan.delete()
        messages.success(request, 'Data pelanggan berhasil dihapus')
    return redirect('kelola_pelanggan')


@login_required
@user_passes_test(is_owner)
def kelola_karyawan(request):
    karyawan_list = Karyawan.objects.select_related('akun').all()
    context = {
        'karyawan_list': karyawan_list,
    }
    return render(request, 'core/kelola_karyawan.html', context)


@login_required
@user_passes_test(is_owner)
def tambah_karyawan(request):
    if request.method == 'POST':
        form = KaryawanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data pegawai berhasil disimpan.')
            return redirect('kelola_karyawan')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = KaryawanForm()
    
    context = {'form': form, 'mode': 'tambah'}
    return render(request, 'core/form_karyawan.html', context)


@login_required
@user_passes_test(is_owner)
def edit_karyawan(request, karyawan_id):
    karyawan = get_object_or_404(Karyawan, id=karyawan_id)
    if request.method == 'POST':
        form = KaryawanForm(request.POST, instance=karyawan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data karyawan berhasil diperbarui.')
            return redirect('kelola_karyawan')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = KaryawanForm(instance=karyawan)
    
    context = {'form': form, 'mode': 'edit', 'karyawan': karyawan}
    return render(request, 'core/form_karyawan.html', context)


@login_required
@user_passes_test(is_owner)
def hapus_karyawan(request, karyawan_id):
    karyawan = get_object_or_404(Karyawan, id=karyawan_id)
    if request.method == 'POST':
        if karyawan.akun:
            karyawan.akun.delete()
        karyawan.delete()
        messages.success(request, 'Data karyawan berhasil dihapus.')
    return redirect('kelola_karyawan')


@login_required
@user_passes_test(is_karyawan_or_owner)
def daftar_transaksi(request):
    from django.core.paginator import Paginator
    from django.db.models import Count, Case, When
    from django.db.models.functions import TruncDate, TruncMonth
    from datetime import datetime, timedelta
    import json
    
    transaksi_list = Transaksi.objects.all().select_related('id_pelanggan', 'jenis_layanan', 'id_pegawai')
    
    # Filters
    tanggal_dari = request.GET.get('tanggal_dari')
    status_filter = request.GET.get('status')
    pembayaran_filter = request.GET.get('pembayaran')
    layanan_filter = request.GET.get('layanan')
    
    if tanggal_dari:
        transaksi_list = transaksi_list.filter(tanggal_masuk__gte=tanggal_dari)
    if status_filter:
        transaksi_list = transaksi_list.filter(status=status_filter)
    if pembayaran_filter:
        transaksi_list = transaksi_list.filter(status_pembayaran=pembayaran_filter)
    if layanan_filter:
        transaksi_list = transaksi_list.filter(jenis_layanan_id=layanan_filter)
    
    # Statistics - Single query with conditional aggregation
    stats = transaksi_list.aggregate(
        total_transaksi=Count('id'),
        total_pendapatan=Sum('total_biaya'),
        total_lunas=Sum(Case(When(status_pembayaran='Lunas', then='total_biaya'))),
        total_belum_lunas=Sum(Case(When(status_pembayaran='Belum Lunas', then='total_biaya'))),
    )
    
    today = datetime.now().date()
    week_ago = today - timedelta(days=6)
    
    # Chart Data - Daily transactions (single query with grouping)
    daily_data = Transaksi.objects.filter(
        tanggal_masuk__date__gte=week_ago
    ).annotate(
        day=TruncDate('tanggal_masuk')
    ).values('day').annotate(
        count=Count('id')
    ).order_by('day')
    
    daily_dict = {item['day']: item['count'] for item in daily_data}
    last_7_days = [today - timedelta(days=i) for i in range(6, -1, -1)]
    daily_transactions = [daily_dict.get(day, 0) for day in last_7_days]
    chart_labels_daily = [day.strftime('%d %b') for day in last_7_days]
    
    # Chart Data - Monthly revenue (single query with grouping)
    six_months_ago = today.replace(day=1) - timedelta(days=150)
    monthly_data = Transaksi.objects.filter(
        tanggal_masuk__date__gte=six_months_ago
    ).annotate(
        month=TruncMonth('tanggal_masuk')
    ).values('month').annotate(
        revenue=Sum('total_biaya')
    ).order_by('month')
    
    monthly_dict = {item['month'].date() if item['month'] else None: float(item['revenue'] or 0) for item in monthly_data}
    
    # Build last 6 months labels
    chart_labels_monthly = []
    monthly_revenue = []
    for i in range(5, -1, -1):
        month_date = today - timedelta(days=30*i)
        month_start = month_date.replace(day=1)
        chart_labels_monthly.append(month_date.strftime('%B'))
        monthly_revenue.append(monthly_dict.get(month_start, 0))
    
    # Get all layanan for filter
    all_layanan = Layanan.objects.all()
    
    # Pagination
    paginator = Paginator(transaksi_list.order_by('-tanggal_masuk'), 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'total_transaksi': stats['total_transaksi'] or 0,
        'total_pendapatan': stats['total_pendapatan'] or 0,
        'total_lunas': stats['total_lunas'] or 0,
        'total_belum_lunas': stats['total_belum_lunas'] or 0,
        'tanggal_dari': tanggal_dari,
        'status_filter': status_filter,
        'pembayaran_filter': pembayaran_filter,
        'layanan_filter': layanan_filter,
        'all_layanan': all_layanan,
        'chart_labels_daily': json.dumps(chart_labels_daily),
        'daily_transactions': json.dumps(daily_transactions),
        'chart_labels_monthly': json.dumps(chart_labels_monthly),
        'monthly_revenue': json.dumps(monthly_revenue),
    }
    return render(request, 'core/daftar_transaksi.html', context)


@login_required
@user_passes_test(is_karyawan_or_owner)
def detail_transaksi(request, transaksi_id):
    transaksi = get_object_or_404(Transaksi, id=transaksi_id)
    log_history = LogHistory.objects.filter(id_transaksi=transaksi).order_by('-waktu_perubahan')

    context = {
        'transaksi': transaksi,
        'log_history': log_history,
    }
    return render(request, 'core/detail_transaksi.html', context)

@login_required
@user_passes_test(is_karyawan_or_owner)
def update_status(request, transaksi_id):
    transaksi = get_object_or_404(Transaksi, id=transaksi_id)
    
    if request.method == 'POST':
        status_baru = request.POST.get('status')
        
        if transaksi.status == 'Sudah Diambil':
            messages.error(request, 'Transaksi sudah selesai. Hubungi Owner untuk pembatalan.')
            return redirect('detail_transaksi', transaksi_id=transaksi.id)
        
        if status_baru == 'Sudah Diambil' and transaksi.status_pembayaran == 'Belum Lunas':
            messages.error(request, 'Barang tidak dapat diambil. Harap lunasi pembayaran terlebih dahulu.')
            return redirect('detail_transaksi', transaksi_id=transaksi.id)
        
        status_sebelum = transaksi.status
        transaksi.status = status_baru
        transaksi.save()
        
        LogHistory.objects.create(
            id_transaksi=transaksi,
            status_sebelum=status_sebelum,
            status_sesudah=status_baru,
            id_pegawai=request.user,
            keterangan=f'Status diubah dari {status_sebelum} ke {status_baru}'
        )
        
        messages.success(request, 'Status berhasil diperbarui.')
        return redirect('detail_transaksi', transaksi_id=transaksi.id)
    
    return redirect('detail_transaksi', transaksi_id=transaksi.id)


@login_required
@user_passes_test(is_karyawan_or_owner)
def koreksi_status(request, transaksi_id):
    transaksi = get_object_or_404(Transaksi, id=transaksi_id)
    
    if transaksi.status == 'Sudah Diambil':
        messages.error(request, 'Status terkunci, tidak dapat dikoreksi')
        return redirect('detail_transaksi', transaksi_id=transaksi.id)
    
    status_mapping = {
        'Proses': 'Diterima',
        'Selesai': 'Proses',
    }
    
    status_sebelum = transaksi.status
    if status_sebelum in status_mapping:
        status_baru = status_mapping[status_sebelum]
        transaksi.status = status_baru
        transaksi.save()
        
        LogHistory.objects.create(
            id_transaksi=transaksi,
            status_sebelum=status_sebelum,
            status_sesudah=status_baru,
            id_pegawai=request.user,
            keterangan=f'Koreksi status dari {status_sebelum} kembali ke {status_baru}'
        )
        
        messages.success(request, f'Status berhasil dikoreksi kembali ke {status_baru}')
    else:
        messages.warning(request, 'Status tidak dapat dikoreksi mundur')
    
    return redirect('detail_transaksi', transaksi_id=transaksi.id)


@login_required
@user_passes_test(is_karyawan_or_owner)
def update_pembayaran(request, transaksi_id):
    transaksi = get_object_or_404(Transaksi, id=transaksi_id)
    
    if request.method == 'POST':
        transaksi.status_pembayaran = 'Lunas'
        transaksi.save()
        messages.success(request, 'Status pembayaran berhasil diperbarui menjadi Lunas')
    
    return redirect('detail_transaksi', transaksi_id=transaksi.id)


@login_required
@user_passes_test(is_karyawan_or_owner)
def cetak_nota(request, transaksi_id):
    transaksi = get_object_or_404(Transaksi, id=transaksi_id)
    context = {
        'transaksi': transaksi,
        'tanggal_cetak': datetime.now(),
    }
    return render(request, 'core/cetak_nota.html', context)




