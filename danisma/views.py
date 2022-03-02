from django.http import HttpResponse
from django.shortcuts import render
from danisma.forms import DanismaFormu

# Create your views here.

def danisma(request):
    if request.method == 'POST':
        danisma_formu = DanismaFormu(data=request.POST)

        if danisma_formu.is_valid():
            danisma_formu.save()

            return HttpResponse("<h1>En kısa zamanda mail adresinize dönüş yapılacaktır</h1>")

        else:
            print("yine olmadı amk")
            print(danisma_formu.errors)
            return HttpResponse("bir hata oluştu")

    else:
        danisma_formu = DanismaFormu()

    return render(request, 'uygulama/danisma.html', {'danisma_formu': danisma_formu})