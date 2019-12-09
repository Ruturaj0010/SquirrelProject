

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . models import Squirrels

def View(request):
    context = {
               "sightings":Squirrels.objects.all(),"field_names":Squirrels._meta.get_fields()
              }
    return render(request, 'squirrelapp/View.html',context)
