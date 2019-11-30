from django.shortcuts import render
from .models import Category,Product
# from .models import Product
from django.shortcuts import redirect
from django.http import JsonResponse
from django.conf import settings
# from firstapp.forms import FirstappForm  
# from . import forms  
from django.core.files.storage import FileSystemStorage
# Create your views here.

# Category Start form here
def add(request):
    print(request.POST)

    if request.method == "POST": 
        c_name = request.POST['c_name']
        data = Category(c_name=c_name)
        data.save()
    
        return redirect('/product/category/list')
    else:
        return render(request,'category/add.html')  


def lists(request):
   datas = Category.objects.all()
   return render(request,'category/list.html',{'datas':datas})

def delete(request, id):
    data = Category.objects.get(pk=id)
    data.delete()
    return redirect('/product/category/list')

def edit(request, id):
    data = Category.objects.get(pk=id)
    context = {
        'data': data
    }
    return render(request, 'category/edit.html', context)


def update(request, id):
    data = Category.objects.filter(pk=id).update(
        c_name = request.GET['c_name'],
       
    )

    return redirect('/product/productlist')

# Product Start form here
def product_add(request):
    print(request.POST)
    cats = Category.objects.all()
    if request.method == 'POST' and request.FILES['image']:
        
        p_name = request.POST['p_name']
        p_desc = request.POST['p_desc']
        p_price = request.POST['p_price']
        p_c_name = request.POST['p_c_name']
        status = 0

        category = Category.objects.get(id=p_c_name)

        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        data = Product(p_name=p_name,image=filename,p_desc=p_desc,p_price=p_price,p_c_name=category,status=status)
        data.save()
   

        return redirect('/product/product-list',{
            'uploaded_file_url': uploaded_file_url
        })
    else:
        return render(request,'product/add.html',{'cats':cats})  


def product_lists(request):
   datas = Product.objects.all()
   return render(request,'product/list.html',{'datas':datas})

def product_delete(request, id):
    data = Product.objects.get(pk=id)
    # image.delete(save=True)
    if data:
        data.image.delete(save=True)
        data.delete()
    return redirect('/product/product-list')
    
def product_edit(request, id):
    data = Product.objects.get(pk=id)
    cats = Category.objects.all()
    context = {
        'data': data,
        'cats': cats
    }
    return render(request, 'product/edit.html', context)


def product_update(request):

    if request.FILES["img"]:
        myfile = request.FILES["img"]
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
    else:
        print ("error") 


    
        # uploaded_file_url = fs.url(filename)

    data = Product.objects.filter(id= request.POST['id'] ).update(
    p_name = request.POST['p_name'],
    p_desc = request.POST['p_desc'],
    p_price = request.POST['p_price'],
    p_c_name = request.POST['p_c_name'],
    image = filename,
    status = 0,)
    
    return redirect('/product/product-list')