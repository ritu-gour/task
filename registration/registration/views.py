from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from django.template import loader
from django.urls import reverse
import random
@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        # username=request.POST.get('username')
        username = random.randrange(999, 999999)
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("your password n confirm  pass same")
        else:

            my_user=User.objects.create_user(username,email,pass1)
            my_user.save()
            email = EmailMessage(
            'Test Email', #subjecr
            f'Thak your for. the mas: \n \n Your Mail verification otp {username}!  ', #mess
            settings.EMAIL_HOST_USER, #sender
            [email] #resiver
        )

            email.fail_silently =True
            email.send()
            n='please check the email verification Otp'
            return redirect('otps')
         
    return render(request,'signup.html')
       



         
    # return render(request,'signup.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        passs1=request.POST.get('pass')
        try:
            user=authenticate(request,username=User.objects.get(email=username),password=passs1)
        except:    
            user=authenticate(request,username=username,password=passs1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("user name n apss incorrect")  


    return render(request,'login.html')


# def otps(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
        
#         try:
#             user=authenticate(request,username=User.objects.get(email=username))
#         except:    
#             user=authenticate(request,username=username,password=passs1)
#         if user is not None:
#             login(request,user)
#             return redirect('home')
#         else:
#             return HttpResponse("user name n apss incorrect")  


#     return render(request,'otps.html')


def otps(request):
    if request.method=='POST':
        username=request.POST.get('username')
        user=authenticate(request,username=username)
        if user is not None:
            otps(request,user)
            return redirect('home')
        else:
            return render(request,'home.html')  


    return render(request,'otps.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')





# Create your views here.
