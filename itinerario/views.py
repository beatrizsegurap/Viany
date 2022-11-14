from django.shortcuts import render

# Create your views here.


def dash(request):
    return render(request, 'itinerario/dash.html')


def dash2(request):
    return "CHAO\n"
