from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import ForgotPassword, CapturePassword
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

# This view is for login page
def user_login(request):
    if request.method=="POST":
        form_data=request.POST
        fm=AuthenticationForm(request=request,data=request.POST)
        return HttpResponse('tahnkyou for logging in')
        """
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            #Below section can e used only when DB tables are ready
            #user=authenticate(username=uname, password=passwd)
            if user is not None:
                print('user id and password is correct')
                #login(request,user)
                #name={'name':uname,}
                return render(request,'woodshophome/login.html',name)
        """
        return HttpResponse('logged in')
        """
        #this must be decommented when abovr section are decommented
        else:
            return render(request,'woodshophome/login.html')
        """
    else:
        fm=AuthenticationForm(request=request,data=request.POST)
        form={'form':fm}
        return render(request,'woodshophome/login1.html',form)

#this is for for validating user id and mobile number for resetting password
def forgot_password(request):
    if request.method=="POST":
        print('getting data from form for validation')
        data=request.POST
        print('data is: ',data)
        username=data['username']
        mobile_number=data['mobile_number']
        print('user name is: ',username)
        print('modile number  is: ',mobile_number)
        d={'username':username,'mobile_number':mobile_number}
        request.session['session_data']=d
        #Now try to check if user idd mobile umber exists, if yes then render template for capturing password
        fm=CapturePassword()                  #this wil be deleted when #Now try .. id decommented
        form={'form':fm}                     #this wil be deleted when #Now try .. id decommented
        return render(request,'woodshophome/capture_password.html',form) #this wil be deleted when #Now try .. id decommented
        """
        queryset = MyAccount.objects.filter(username=user_name,mobile_number=mobile_number).values('email', 'mobile_number','username')
        if not queryset.exists():
            messages.warning(request, 'Please enter valid email id and mobile number')
            fm=ForgotPassword()
            form={'form':fm}
            return render(request,'woodshophome/forgot_uid_pass.html',form)
        else:
            print('data in queryset')
            print('user name is: ',queryset[0]['username'])
            name=user_name
            mobile_number=mobile_number
            d={'name':name,'mobile_number':mobile_number}
            request.session['session_data']=d
            print('user name is: ',name)
            return redirect('capture-password')
        """
    else:
        #need to rende form
        print('rendering forget password html page')
        fm=ForgotPassword()
        form={'form':fm}
        return render(request,'woodshophome/forget_password.html',form)

#this view is for capturing new password if user id and mobile number are validated successfully
def capture_password(request):
    session_data=request.session.get('session_data',default="Guest")
    if request.method=="POST":
        data=request.POST
        password1=data['password1']
        password2=data['password2']
        if password2==password2:
            #both password matched now update password in DB
            return HttpResponse('password changed successfully')
            """
            queryset=MyAccount.objects.get(username=user_name,mobile_number=mobile_number)
            queryset.set_password('Comedy@125')
            queryset.save()
            del request.session['session_data']
            return redirect('login')
            """
        else:
            messages.warning(request,"password didn't matched, password file is case sensitive")
            fm=CapturePassword()
            form={'form':fm}
            render(request,'woodshophome/capture_password.html',form)
        
    else:
        fm=CapturePassword()
        form={'form':fm}
        render(request,'woodshophome/capture_password.html',form)

#this view is for user registration
def signup(request):
    return HttpResponse('this is signup form')
