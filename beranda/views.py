from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    isi = 'Hello There !'
    return render(request, 'home.html', {'judul' : 'SMK Islam Al-Fikri','isi':isi})
