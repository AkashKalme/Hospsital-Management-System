from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import auth, User
from patient import views
# Create your views here.

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            user = auth.authenticate(username=user.username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect(views.home)
            else:
                messages.error(request,"Invalid Credentials")
        else:
            messages.error(request,"User does not exist.")
    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        admintoken = request.POST['admintoken']
        email = request.POST['email']
        password = request.POST['password']
        if int(admintoken) == 9087:
            user = User.objects.create_user(username=fname+" "+lname, password=password, email=email, first_name=fname,last_name=lname)
            user.save()
            messages.success(request, 'Sign-up successful. You can login now')
        else:
            messages.error(request,"You are not authorised to this page")
    return redirect(login)

def logout(request):
    auth.logout(request)
    return redirect('/')