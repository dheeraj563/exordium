
from django.contrib.auth import authenticate, login, logout
from home.forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views import generic
from sign_up.models import *
from django.conf import settings
from django.conf.urls.static import static
from sign_up.models import Student
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def index(request):

    template = loader.get_template('home/index.html')

    return HttpResponse(template.render())

def finddata(request):
    context = {}
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password= password)
        if user:
            login(request,user)
            return HttpResponse('You successfully loged in')
        else:
            context["error"] = "provide valid cradential!!"
            return redirect('home/login.html')

def search(request):
    template = loader.get_template('home/search.html')
    return HttpResponse(template.render({}, request))

def serpro(request):
    rn = request.POST['sea']
    print(rn)
    if Student.objects.filter(roll_no=rn):
        template = loader.get_template('home/serpro.html')
        new = Student.objects.get(roll_no=rn)
        context = {'new':new}
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("Invalid roll no/ This roll no is registered")
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home/registration')
        else:
            return HttpResponse('you fill something wrong')

    else:
        form = RegistrationForm()
        return render(request, 'home/register.html',{'form': form})

def success(request):
    return HttpResponse('succeess')
