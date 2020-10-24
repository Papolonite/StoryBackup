from django.http import request
from django.shortcuts import redirect, render
from .forms import MataKuliahForm
from .models import MataKuliah

# Create your views here.
def profile(request):
    return render(request, 'my_profile.html', {'page_title' : "Papolonite's Profile"})

def home(request):
    return render(request, 'home.html', {'page_title' : 'Home'})

def createMatkul(request):
    form = MataKuliahForm(request.POST or None)
    if (form.is_valid() and request.method == 'POST'):
        form.save()
        return redirect('view_matkul')
    context = {'page_title': "Create matkul", 'form':form}
    return render(request, 'create_matkul.html', context)

def viewMatkul(request):
    mata_kuliah = MataKuliah.objects.all()
    context = {'page_title' : 'View Matkul', 'mata_kuliah':mata_kuliah}
    return render(request, 'view_matkul.html', context)

def viewMatkulDetail(request,id):
    mata_kuliah = MataKuliah.objects.get(id=id)
    context = {'page_title' : mata_kuliah.nama, 'mata_kuliah':mata_kuliah}
    return render(request, 'view_matkul_detail.html', context)

def deleteView(request,id):
    mata_kuliah = MataKuliah.objects.get(id=id)
    mata_kuliah.delete()
    return redirect('view_matkul')
