from django.shortcuts import render

# Create your views here.

def checkList(request):
    return render(request, 'checklist.html')