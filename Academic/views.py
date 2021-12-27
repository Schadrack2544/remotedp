
from django.contrib import messages
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
import random

from django.template.loader import get_template
import requests
import json
import uuid

#from global_login_required import login_not_required

from Academic.models import Module, Payment, Student,Transcript
from Academic.utils import render_to_pdf
from adminpanel.models import Themarks

def personal_info(request):
    
    return render(request, 'personal_info.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f'email: {username} and  password: {password}')
        user = authenticate(username=username,password=password)
        #user = User.objects.filter(email=email,password=password).exists()
        print (f'user is {user}')
        if user is not None:
            print("User exists")
            auth.login(request,user)
            return redirect("dashboard")
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


#@login_not_required
def register(request):
    if  request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        # to check whether the two pin match
        if password == cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('home')
        else:
            messages.info(request, 'Password do not match')
            return redirect('home')

    return render(request, 'register.html')



def login_success(request):
    rand = random.randint(2180, 2189)
    return render(request, 'login_success.html',{'rand':rand})


def dashboard(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        student=Student.objects.filter(email=email)
        return render(request, 'dashboard.html',{'student':student})
    else:
        return redirect('login')

def home(request):
    return render(request, 'home.html')
def pay(request):
    url = "https://opay-api.oltranz.com/opay/paymentrequest"
    txn_id=uuid.uuid4()
    payload = json.dumps({
        "amount": 100,
        "telephoneNumber": "250783544533",
        "organizationId": "bef0fc9b-6adb-4494-b01e-f5009874f3ba",
        "description": "Payment for Testing",
        "callbackUrl": "http://myonlineprints.com/payments/callback",
        "transactionId": str(txn_id)
})
    headers = {
      'Content-Type': 'application/json'
     }

    is_paid = requests.request("POST", url, headers=headers, data=payload)

    print(response)
    if is_paid:
        return redirect('transcript')
    else:
        return render(request, 'pay.html')
def is_student_paid(reg_number,level):
      payment=Payment.objects.filter(student_reg=reg_number,level=level)
      if payment.is_paid:
        return True
      else:
          return False
def transcript(request):
     template=get_template("transcript.html")
     transcript=['report','form']
     context={
    'transcript':transcript,
    }
     html=template.render(context)
     pdf=render_to_pdf('transcript.html',context)
     if pdf:
        response=HttpResponse(pdf,content_type="application/pdf")
        filename="Transcript_%s.pdf"%('218000597')
        content="inline;filename=%s" %(filename)
        download=request.GET.get('download')
        if download:
            content="attachment;filename=%s" %(filename)
        response['content-Disposition']=content
        return response
     return HttpResponse("Not Found")
             
def transcripter(request,*args,**kwargs):
    if request.method == 'POST':
        reg_number = request.POST.get('reg_number')
        level=request.POST.get('level')
        print(f'reg number is {reg_number} and level is {level}')
        template=get_template("transcript.html")
        if is_student_paid(reg_number,level):
                student=Student.objects.filter(student_reg=reg_number)
                marks1=Themarks.objects.filter(student_reg=reg_number,module_semester="1")
                marks2=Themarks.objects.filter(student_reg=reg_number,module_semester="2")
                marks=[marks1,marks2]
                transcript=[student,marks]
                context={
                'transcript':transcript,
                }
                html=template.render(context)
                pdf=render_to_pdf('transcript.html',context)
                if pdf:
                    response=HttpResponse(pdf,content_type="application/pdf")
                    filename="Transcript_%s.pdf"%("1234456")
                    content="inline;filename='%s'" %(filename)
                    download=request.GET.get('download')
                    if download:
                        content="attachment;filename='%s'" %(filename)
                    response['content-Disposition']=content
                    return response
                return HttpResponse("Not Found")
            
        else:
            messages.info(request,"You have to get the amount due to get the transcript")
            return redirect('pay',{'messages':messages})
    else:
        return redirect('dashboard')