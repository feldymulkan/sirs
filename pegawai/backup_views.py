from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Pegawai
from .forms import PegawaiForm

#create
def create_pegawai(request):
    if request.method == 'POST':
        form = PegawaiForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pegawai berhasil ditambahkan")
            return redirect('list_pegawai')
    else:
        form = PegawaiForm()
    return render(request, 'pegawai/create_pegawai.html', {'form': form})

#read
def list_pegawai(request):
    query = request.GET.get('q', '')
    if query != '':
        pegawai_list = Pegawai.objects.filter(nama__icontains=query)
    else:
        pegawai_list = Pegawai.objects.all()
    return render(request, 'pegawai/list_pegawai.html', {'pegawai_list':pegawai_list, 'query':query})

#delete
def delete_pegawai(request, pk):
    pegawai = get_object_or_404(Pegawai, pk=pk)
    
    if request.method == 'POST':
        pegawai.delete()
        messages.success(request, "Pegawai {pegawai.nama} berhasil dihapus")
        return redirect('list_pegawai')
    return render(request, 'pegawai/delete_pegawai.html', {'pegawai':pegawai})

#edit
def edit_pegawai(request, pk):
    pegawai = get_object_or_404(Pegawai, pk=pk)
    if request.method == 'POST':
        form = PegawaiForm(request.POST, instance=pegawai)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil diperbaharui!')
            return redirect('list_pegawai')
    else:
        form = PegawaiForm(instance=pegawai)
    return render(request, 'pegawai/edit_pegawai.html', {'form':form, 'pegawai':pegawai})
        
#search pegawai
# def search_pegawai(request):
#     query = request.GET.get('q', '')
#     pegawai_list = Pegawai.objects.filter(nama__icontains=query) if query else Pegawai.objects.all()
#     return render(request, 'pegawai/search_pegawai.html', {'pegawai_list':pegawai_list, 'query':query})

def toggle_status(request, pk):
    pegawai = get_object_or_404(Pegawai,pk=pk)
    pegawai.is_active = not pegawai.is_active
    pegawai.save()
    status = "diaktifkan" if pegawai.is_active else "dinonaktifkan"
    messages.success(request, f"{pegawai.nama} berhasil {status}")
    return redirect('list_pegawai')
    
    