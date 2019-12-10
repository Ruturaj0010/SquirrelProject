

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . models import Squirrels
from .forms import SquirrelForm

def home(request):
    return render(request,'squirrelapp/home.html')

def View(request):
    context = {
           "sightings":Squirrels.objects.all(),"field_names":Squirrels._meta.get_fields()
         }
    return render(request, 'squirrelapp/View.html',context)

def coordinates(request):
    quirrels  = Squirrels.objects.all()[:100]
    context = {
            "squirrels": squirrels,
        }
    return render(request, 'squirrelapp/map.html', context)

def edit_squirrel(request, Unique_Squirrel_ID):
    squirrel = Squirrels.objects.get(Squirrel_ID=Unique_Squirrel_ID)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/squirrelapp/')
    else:
        form = SquirrelForm(instance=squirrel)
    context = {
            'form':form,
        }
    return render(request, 'squirrelapp/edit.html', context)

def add_squirrel(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/squirrelapp/')
    else:
        form = SquirrelForm()
    context = {
            'form':form,
        }
    return render(request, 'squirrelapp/add.html', context)

def stats(request):
    black_count = 0
    cinnamon_count = 0
    gray_count = 0
    eating_count = 0
    juvenile_count = 0
    adult_count = 0
    running_count=0
    climbing_count = 0
    chasing_count = 0
    foraging_count = 0
    kuks_count = 0
    quaas_count = 0
    moans_count = 0
    tail_flags_count=0
    for s in Squirrels.objects.all():
        if s.Running == True:
            running_count +=1
        else:
            pass
        if s.Climbing == True:
            climbing_count +=1
        else:
            pass
        if s.Chasing == True:
            chasing_count +=1
        else:
            pass
        if s.Fur_Colour == 'Black':
            black_count +=1
        elif s.Fur_Colour == 'Cinnamon':
            cinnamon_count +=1
        elif s.Fur_Colour == 'Gray':
            gray_count +=1
        else:
            pass
        if s.Foraging == True:
            foraging_count +=1
        else:
            pass
        if s.Eating == True:
            eating_count +=1
        else:
            pass
        if s.Age == 'Juvenile':
            juvenile_count +=1
        elif s.Age == 'Adult':
            adult_count +=1
        else:
            pass
        if s.Kuks == True:
            kuks_count +=1
        else:
            pass
        if s.Quaas == True:
            quaas_count +=1
        else:
            pass
        if s.Moans == True:
            moans_count +=1
        else:
            pass
        if s.Tail_flags == True:
            tail_flags_count +=1
        else:
            pass
     details = {'Squirrels found eating': eating_count,
                 'Squirrels found running':running_count,
                 'Sqquirrels found climbing':climbing_count,
                 'Squirrels found chasing':chasing_count,
                 'Squirrels found with black fur':black_count,
                 'Squirrels found with cinnamon fur':cinnamon_count,
                 'Squirrels found with gray fur':gray_count,
                 'Squirrels found foraging':foraging_count,
                 'Squirrels found flagging tails':tail_flags_count,
                 'Squirrels found as a juvenile':juvenile_count,
                 'Squirrels found as a adult': adult_count,
                 'Squirrels found making kuk sounds':kuks_count,
                 'Squirrels found making quaas sounds':quaas_count,
                 'Squirrels found making moan sounds': moans_count,
               }
     context = {"stats":details}
     return render(request, 'squirrelapp/stats.html', context)


        








