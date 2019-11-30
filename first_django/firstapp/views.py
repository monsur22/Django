from django.shortcuts import render
from .models import Firstapp
from django.shortcuts import redirect
from django.http import JsonResponse
from firstapp.forms import FirstappForm  
from . import forms  
# Create your views here.
def home(request):
   datas = Firstapp.objects.all()
   return render(request,'view.html',{'datas':datas})

def add(request):
  
   return render(request,'add.html')

def add_post(request):
    print(request.POST)

    first_name = request.GET['first_name']
    last_name = request.GET['last_name']
    desc = request.GET['desc']
    # data = Firstapp(first_name=first_name, last_name=last_name, desc=desc)
    # data.save()
    Firstapp.objects.create(
            first_name = first_name,
            last_name = last_name,
            desc = desc,
            )
    return redirect('/firstapp/list')


def lists(request):
   datas = Firstapp.objects.all()
   return render(request,'list.html',{'datas':datas})

def delete(request, id):
    data = Firstapp.objects.get(pk=id)
    data.delete()
    return redirect('/firstapp/list')

def edit(request, id):
    data = Firstapp.objects.get(pk=id)
    context = {
        'data': data
    }
    return render(request, 'edit.html', context)


def update(request, id):
    data = Firstapp.objects.filter(pk=id).update(
        first_name = request.GET['first_name'],
        last_name = request.GET['last_name'],
        desc = request.GET['desc']
    )
    # first_name = request.GET['first_name']
    # last_name = request.GET['last_name']
    # desc = request.GET['desc']
    # data.save()
   #  return JsonResponse(data)
    return redirect('/firstapp/list')
# ///test
def test(request):
   # form=FirstappForm(request.POST or None)

   # if form.is_valid():
   #     post = form.save(commit=False)
     
   #     post.save()
   # context={
   #    "form":form
   # }
   # return render(request,'test.html',context)  
    if request.method == "POST":  
        form = FirstappForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/firstap')  
            except:  
                pass  
    else:  
        form = FirstappForm()  
    return render(request,'test.html',{'form':form}) 

