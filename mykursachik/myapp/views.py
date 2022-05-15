from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
from .models import Ad
from .models import Director
from .forms import AdForm
from .forms import DirectorForm
from .forms import RegisterForm
from .forms import LoginForm
# Create your views here.

def index(request):
    # context = {
    #     'name': 'Niita',
    # }
    features = Feature.objects.all()
    return render(request, 'index.html', {'features':features})


def counter(request):
    words = request.GET['words']
    return render(request, 'counter.html')

#Register/Login


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                 messages.info(request, 'Username Already Exists')
                 return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password,)
                user.save()
                return redirect('login')
    
        else: 
            messages.info(request, 'Password Not The Same')
            return redirect('register')
    else:

        return render(request, 'register.html')

def login(request):
     if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']

         user = auth.authenticate(username=username, password=password)

         if user is not None:
             auth.login(request, user)
             return redirect('/')
         else:
            messages.info(request, 'Credentials Invalid')
            return redirect ('login')
     else: 
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


# TV

def tv(request):
    ads = Ad.objects.order_by()
    data = {"ads": ads}
    return render(request, 'tv.html', context=data)

def tv_filtrated(request):
    ads = Ad.objects.filter(price__lte = 100)
    data = {"ads": ads}
    return render(request, 'tv_filtrated.html', context=data)

def create_tv(request):
    if request.method == 'POST':
        name = request.POST['name']
        details = request.POST['details']
        price = request.POST['price']
        director = request.POST['director']
        user = request.POST['user']

        if Ad.objects.filter(name=name).exists():
            messages.info(request, 'Ad Already Exists')
            return redirect('create_tv')
        else:
            ad = Ad.objects.create(name=name, details=details, price=price, director_id=director, user_id=user)
            ad.save()
            return redirect('tv')
    else:
        adform = AdForm()
        return render(request, 'tv_create.html', {"form": adform})



# Director

def director(request):
     directors = Director.objects.order_by()
     data = {"directors": directors}
     return render(request, 'director.html', context=data)






def post(request, pk):
    return render(request, 'post.html', {'pk' : pk})
