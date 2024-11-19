from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import movie1
from .models import mlist

# Create your views here.

def movie (request):
    name=mlist.objects.all()
    context={'film':name}
    return render(request,'index.html',context)

def details (request,movie_id):
    ab=mlist.objects.get(id=movie_id)
    return render (request,'details.html',{'movie':ab})

def add_movie(request):
    if request.method=="POST":
     name = request.POST.get('name',)
     desc = request.POST.get('desc',)
     year = request.POST.get('year')
     img = request.FILES['img']
     film=mlist(name=name,desc=desc,year=year,img=img)
     film.save()

    return render(request,'add.html')

def update(request,id):
    movie2=mlist.objects.get(id=id)
    form1=movie1(request.POST or None,request.FILES,instance=movie2)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request,'edit.html',{'movie3':movie2,'form2':form1})

def delete(request,id):
    if request.method=='POST':
        variname=mlist.objects.get(id=id)
        variname.delete()
        return redirect('/')
    return render(request,'delete.html')

