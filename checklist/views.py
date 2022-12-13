from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormCheckList
from .models import check_list

# Create your views here.

def checkList(request):

    if request.method == 'POST':
        form = FormCheckList(request.POST or None)
        if form.is_valid():

            form.save()
            form = FormCheckList()

    id_itineario = request.session["id_itinerario"]

    return render(request, 'checklist.html',{'idItinerario':id_itineario})