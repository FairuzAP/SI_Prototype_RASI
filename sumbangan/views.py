from django.shortcuts import render, redirect
from .models import TransaksiSumbangan
from django.db.models import Sum
from .forms import PemberianForm, PermohonanForm

# Create your views here.
def index(request):
    total_pemberian = TransaksiSumbangan.objects.filter(jenis='Pemberian').aggregate(Sum('jumlah')).get('jumlah__sum', 0.00)
    total_permintaan = TransaksiSumbangan.objects.filter(jenis='Permintaan').aggregate(Sum('jumlah')).get('jumlah__sum', 0.00)
    return render(request, 'index.html', {
        'total_pemberian' : total_pemberian,
        'total_permintaan' : total_permintaan
    })

def beri(request):
    total_pemberian = TransaksiSumbangan.objects.filter(jenis='Pemberian').aggregate(Sum('jumlah')).get('jumlah__sum',0.00)
    total_permintaan = TransaksiSumbangan.objects.filter(jenis='Permintaan').aggregate(Sum('jumlah')).get('jumlah__sum',0.00)
    if request.method == 'POST':
        form = PemberianForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sumbangan:index')
        else:
            print(form.errors)
    else:
        form = PemberianForm()

    return render(request, 'index.html', {
        'beri_error': form.errors,
        'total_pemberian': total_pemberian,
        'total_permintaan': -total_permintaan
    })

def minta(request):
    total_pemberian = TransaksiSumbangan.objects.filter(jenis='Pemberian').aggregate(Sum('jumlah')).get('jumlah__sum',0.00)
    total_permintaan = TransaksiSumbangan.objects.filter(jenis='Permintaan').aggregate(Sum('jumlah')).get('jumlah__sum',0.00)
    if request.method == 'POST':
        form = PermohonanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sumbangan:index')
    else:
        form = PermohonanForm()
    return render(request, 'index.html', {
        'minta_error': form.errors,
        'total_pemberian': total_pemberian,
        'total_permintaan': -total_permintaan
    })