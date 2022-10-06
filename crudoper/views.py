from django.shortcuts import render,redirect
from .forms import *
from .models import *


##########################################
#               Employee                 #  
##########################################


def bird_create(request):
    if request.method == "POST":
        form = BirdForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/bird_list')
            except:
                pass
    else:
        form = BirdForm()
        return render(request,'bird_create.html',{'form':form})

def bird_list(request):
    birds = Bird.objects.all()
    return render(request,"bird_list.html",{'birds':birds})

def bird_edit(request, id):
    bird = Bird.objects.get(id=id)
    form = BirdForm(instance = bird)

    if request.method == 'POST':
        form = BirdForm(request.POST, instance = bird)
        if form.is_valid():
            form.save()
            return redirect("/bird_list")
    return render(request,'bird_edit.html', {'bird':bird,'form':form})

def destroy(request, id):
    bird = Bird.objects.get(id=id)
    bird.delete()
    return redirect("/bird_list")


##########################################
#              Department                #  
##########################################



def bird_family_create(request):
    if request.method == "POST":
        form = BirdFamilyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/bird_family_list')
            except:
                pass
    else:
        form = BirdFamilyForm()
        return render(request,'bird_family_create.html',{'form':form})

def bird_family_list(request):
    bird_family = BirdFamily.objects.all()
    return render(request,"bird_family_list.html",{'bird_family':bird_family})

def bird_family_edit(request, id):
    bird_family = BirdFamily.objects.get(id=id)
    form = BirdFamilyForm(instance = bird_family)

    if request.method == 'POST':
        form = BirdFamilyForm(request.POST, instance = bird_family)
        if form.is_valid():
            form.save()
            return redirect("/bird_family_list")
    return render(request,'bird_family_edit.html', {'bird_family':bird_family,'form':form})

def bird_family_destroy(request, id):
    bird_family = BirdFamily.objects.get(id=id)
    bird_family.delete()
    return redirect("/dep_list")

