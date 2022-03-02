from enum import Flag
from django import views
from uygulama.forms import KayitFormu
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'uygulama/index.html', {})

def kayit(request):
    registered = False

    if request.method == 'POST':
        kayit_formu = KayitFormu(data=request.POST)

        if kayit_formu.is_valid():
            kullanici = kayit_formu.save()
            kullanici.set_password(kullanici.password)
            kullanici.save()

            registered = True

        else:
            print(kayit_formu.errors)
            return HttpResponse("bir hata oluştu")
    
    else:
        kayit_formu = KayitFormu()

    return render(request, 'uygulama/kayit.html', {'kayit_formu': kayit_formu, 'registered': registered})

def giris(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        kullanici = authenticate(username=username, password=password)

        if kullanici:
            if kullanici.is_active:
                login(request, kullanici)
                return HttpResponseRedirect(reverse('index'))

        else:
            print("bir hata oluştu")
            return HttpResponse('bir hata oluştu')

    else:
        return render(request, ('uygulama/giris.html'), {})

@login_required
def cikis(request):
    logout(request)
    return render(request, 'uygulama/index.html', {})
    
def hakkimizda(request):
    return render(request, 'uygulama/hakkimizda.html', {})