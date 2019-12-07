

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . models import Squirrels
from .forms import SquirrelForm

def View(request):
        context = {
                     "sightings":Squirrels.objects.all(),"field_names":Squirrels._meta.get_fields()
                                    }
 return render(request, 'Squirrel_Sightings/view_all.html',context)
