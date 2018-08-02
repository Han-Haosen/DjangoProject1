from django.shortcuts import render

from django.http import HttpResponse
from django.http import Http404

from .models import Pet

def home(request):
    pets = Pet.objects.all()
    return render(request,'home.html',{'pets':pets})

def pet_detail(request,id):
    pet1 = Pet.objects.get(id=id)
    return render(request,'pet_detail.html',{'pet1':pet1})
