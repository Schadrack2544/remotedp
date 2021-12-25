
from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
import random

from django.template.loader import get_template

#from global_login_required import login_not_required

from Academic.models import Student, Marks
from Academic.utils import render_to_pdf


def personal_info(request):
    
    return render(request, 'personal_info.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("dashboard")
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


#@login_not_required
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        # to check whether the two pin match
        if password == cpassword:
            if User.objects.filter(email=email).exists():
                print('email already taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                print('username already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request, 'Password do not match')
            return redirect('register')

    return render(request, 'register.html')




def login_success(request):
    rand = random.randint(2180, 2189)
    return render(request, 'login_success.html',{'rand':rand})


def dashboard(request):
    return render(request, 'dashboard.html')


def home(request):
    return render(request, 'home.html')

def transcript(request,*args,**kwargs):
    template=get_template("transcript.html")
    context={
        "invoice_id":123,
        "customer_name":"Schadrack Godson",
        "amount":1399.99,
        "date":"today"
    }
    html=template.render(context)
    pdf=render_to_pdf('transcript.html',context)
    if pdf:
        response=HttpResponse(pdf,content_type="application/pdf")
        filename="Invoice_%s.pdf"%("1234456")
        content="inline;filename='%s'" %(filename)
        download=request.GET.get('download')
        if download:
            content="attachment;filename='%s'" %(filename)
        response['content-Disposition']=content
        return response
    return HttpResponse("Not Found")
    