from datetime import datetime
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Patient,History
from django.utils import timezone

# Create your views here.

def texttolist(arr):
    if arr != None:
        l = arr.split(',')
        for j in l:
            if j == "":
                l.remove("")
        return l
    else:
        return list()


def listtotext(arr):
    l = ""
    for i in arr:
        l = l + str(i) + ","
    return l

def home(request):
    allpatients = Patient.objects.filter(notvisited=True)
    allhistorys = History.objects.all()
    params = {'allpatients':allpatients,'allhistorys':allhistorys}
    return render(request,'dashboard.html',params)

def addpatient(request):
    return render(request,"addpatient.html")

def about(request):
    return render(request,"aboutus.html")

def contact(request):
    return render(request,"contactus.html")

def allpatients(request):
    allpatients = Patient.objects.all()
    allhistorys = History.objects.all()
    params = {'allpatients':allpatients,'allhistorys':allhistorys}
    return render(request,"allpatients.html",params)

def print(request):
    if request.method == "POST":
        name = request.POST['name']
        patient = Patient.objects.get(name=name)
        j = History.objects.get(patient=patient)
        return render(request,"print.html",{'patient':patient,'j':j})
    else:
        messages.error(request,"Unknown error occured. ")
        return redirect(home)

def savepatient(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        address = request.POST['address']
        gender = request.POST['gender']
        email = request.POST['email']
        dob = request.POST['dob']
        height = request.POST['height']
        weight = request.POST['weight']
        reason = request.POST['reason']
        if not(Patient.objects.filter(name=fname + " " + lname).exists()):
            p = Patient.objects.create(name=fname + " " + lname,gender=gender,date_of_Birth=dob,address=address,email=email,height=height,weight=weight,reason=reason,dateofvisit=timezone.now())
            p.save()
            request.session['patientname'] = p.name
            messages.success(request,"Details of patient added successfully ! Now add history")
            return redirect(addhistory)
        else:
            messages.error(request,"Patient Info already exist in database")
            return redirect(addpatient)
    else:
        messages.error(request,"Unknown error occured. Error : You tried to save a patient info")
        return redirect(addpatient)

def addhistory(request):
        patientname = request.session['patientname']
        p = Patient.objects.get(name=patientname)
        return render(request,"history.html",{'patient':p})

def visited(request):
    if request.method == "POST":
        name = request.POST['name']
        patient = Patient.objects.get(name=name)
        patient.notvisited = False
        patient.save()
        messages.success(request,"Patient marked as visited")
    else:
        messages.error(request,"Unknown error occured. ")
    return redirect(home)

def savehistory(request):
    if request.method == "POST":
        dieases = list()
        for i in request.POST:
            if request.POST[i] == str(1):
                dieases.append(i)
        n = request.POST['patient']
        patient = Patient.objects.get(name=n)
        allergy = request.POST['allergy']
        other = request.POST['other']
        operations = request.POST['operations']
        currentmedications = request.POST['currentmedications']
        Exercise = request.POST['Exercise']
        Eating = request.POST['Eating']
        Alcohol = request.POST['Alcohol']
        smoke = request.POST['smoke']
        Caffeine = request.POST['Caffeine']
        obj = History.objects.create(patient=patient,allergy=allergy,other=other,operations=operations,currentmedications=currentmedications,Exercise=Exercise,Eating=Eating,Alcohol=Alcohol,smoke=smoke,Caffeine=Caffeine,dieases=listtotext(dieases))
        obj.save()
        messages.success(request,"Patient history added successfully")
    else:
        messages.error(request,"Unknown error occured. ")
    return redirect(home)