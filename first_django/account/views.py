from django.http import HttpResponse
from django.shortcuts import render
from .models import Account
from .models import Verifyaccount
from django.shortcuts import redirect  
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password,check_password #password check
from django.core.mail import send_mail #Email
from django.core import mail#Email
from django.template.loader import render_to_string#Email
from django.utils.html import strip_tags#Email
from django.conf import settings
from django.utils.crypto import get_random_string #Random code
# import bcrypt
# Create your views here.
def add(request):
    print(request.POST)  
    if request.method == "POST":
         
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        
        password = request.POST['password']
        unique_id = get_random_string(length=32)
        subject = 'Subject'
        html_message = render_to_string('mail_template.html', {'pk': unique_id,'email': email})
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        to = email
        mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

        data = Verifyaccount(fname=fname,lname=lname,email=email,token=unique_id,password=make_password(password))
        data.save()

        return redirect('/account/list')
    else:
        return render(request,'uadd.html')
def verify(request, email , token):
    # print(request.POST)
    data = Verifyaccount.objects.filter(email=email).get() 
    if  data.email == email and data.token == token:
         
        fname = data.fname
        lname = data.lname
        email = data.email
        
        password = data.password
      
      
        data = Account(fname=fname,lname=lname,email=email,password=password)
        data.save()
        verify = Verifyaccount.objects.filter(email=email).get()
        verify.delete()
        return redirect('/account/list')
    else:
        return render(request,'uadd.html')  


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password=request.POST['password']


        user = Account.objects.get(email=email)
    
        if check_password(password, user.password):
            request.session['email'] = user.email
            return HttpResponse('Login ')
        else:
            return HttpResponse('P not correct ',{"email" : email})
         

    else:
        return render(request,'login.html')  
def forget(request):
    if request.method == "POST":
        email = request.POST['email']
        
        verify = Verifyaccount.objects.filter(email=email).get()
        verify.delete()

        unique_id = get_random_string(length=32)
        subject = 'Subject'
        html_message = render_to_string('forget_email.html', {'pk': unique_id,'email': email})
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        to = email
        mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)

        data = Verifyaccount(email=email,token=unique_id)
        data.save()

        return redirect('/account/list')
         

    else:
        return render(request,'forget.html')
  

def update(request, email , token):
    # request.session['email'] = user.email
    # request.session['token'] = user.token
    data = Verifyaccount.objects.filter(email=email,token=token).get() 
    if  data:
         
        return render(request,'update_pasword.html',{'data':data}) 
        
    else:
        return render(request,'uadd.html')  


def update_pasword(request):   
    data = Verifyaccount.objects.filter(email=request.POST['email'],token=request.POST['token']).get()
    if  data:
        update = Account.objects.filter(email = request.POST['email']).update(
            password=make_password(request.POST['password']),
        )
        # update = Account.objects.filter(email = request.POST['email'])
        # data = Account(password=make_password(request.POST['password'])
        # data.save()
        
        verify = Verifyaccount.objects.filter(email=request.POST['email'],token=request.POST['token']).get()
        verify.delete()
        return HttpResponse(' Upadate')
    else:
        return HttpResponse('Not Upadate')



def logout(request):
    try:
        del request.session['email']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")


def lists(request):
   datas = Account.objects.all()
   return render(request,'ulist.html',{'datas':datas})



def email(request):
    unique_id = get_random_string(length=32)
    # subject = 'Thank you for registering to our site'
    # message = ''
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = ['monsurahmedshafiq@gmail.com']
    # send_mail( subject, message, email_from, recipient_list )
    subject = 'Subject'
    html_message = render_to_string('mail_template.html', {'pk': unique_id})
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    to = 'monsurahmedshafiq@gmail.com'

    mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    # return redirect('redirect to a new page')
    return HttpResponse("Email Send")
