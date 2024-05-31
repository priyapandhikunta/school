from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *
from django.http import HttpResponse


def Student(request):
    ESO=StudentForm()
    d={'ESO':ESO}

    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            print(SFDO.cleaned_data)
            print(SFDO.cleaned_data['Sname'])
            return HttpResponse('Data Submitted')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'School.html',d)


