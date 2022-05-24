from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Ad
from .models import Director
from .models import Method
from .forms import AdForm
from .forms import DirectorForm
from .forms import RegisterForm
from .forms import LoginForm
from .forms import Search
# Create your views here.

def index(request):
    return render(request, 'index.html')


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
    ads = Ad.objects.order_by('-mark')
    data = {"ads": ads}
    return render(request, 'tv.html', context=data)

def tv_filtrated(request):
    ads = Ad.objects.filter(price__lte = 100)
    data = {"ads": ads}
    return render(request, 'tv.html', context=data)

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

def tv_search(request):
    if request.method == 'POST':
        search = request.POST['search']
        ads = Ad.objects.filter(name=search)
        data = {"ads": ads}
        return render(request, 'tv.html', context=data)
    else:
        form = Search()
        return render(request, 'tv_create.html', {"form": form})



# Director

def director(request):
     directors = Director.objects.order_by()
     data = {"directors": directors}
     return render(request, 'director.html', context=data)

def director_search(request):
    if request.method == 'POST':
        search = request.POST['search']
        directors = Director.objects.filter(name=search)
        data = {"directors": directors}
        return render(request, 'director.html', context=data)
    else:
        form = Search()
        return render(request, 'tv_create.html', {"form": form})


def director_filtrated(request):
     directors = Director.objects.filter(age__lte = 100)
     data = {"directors": directors}
     return render(request, 'director.html', context=data)



# Method

def method(request):
    method = Method.objects.all()

    if not method:
        ads = Ad.objects.order_by('-mark')
        v1_order = 0
        v2_order = 1
        v3_order = 2
        v1_mark = ads[v1_order].mark
        v2_mark = ads[v2_order].mark
        v3_mark = ads[v3_order].mark
        v1_name = ads[v1_order].name
        v2_name = ads[v2_order].name
        v3_name = ads[v3_order].name
        if request.method == 'POST':
            method = Method.objects.create(v1_order=v1_order, v2_order=v2_order, v3_order=v3_order, v1_mark=v1_mark, v2_mark=v2_mark, v3_mark=v3_mark)
            method.save()
            choice = request.POST['choice']
            kekplus = int(request.POST['kekplus'])
            if choice == "left" and v1_mark < v2_mark + v3_mark:
                v1_mark += kekplus
            elif choice == "right" and v1_mark > v2_mark + v3_mark:
                v1_mark -= kekplus
            Ad.objects.filter(id = (v1_order+1)).update(mark = v1_mark)
            return redirect('method')
        data = {"v1_name": v1_name, "v2_name": v2_name, "v3_name": v3_name, "v1_mark": v1_mark, "v2_mark": v2_mark, "v3_mark": v3_mark}
        return render(request, 'method.html', context=data)
    else:
        ads = Ad.objects.order_by('-mark')
        method = Method.objects.latest('v1_order')
        adsAmount = int(Ad.objects.all().count())
        v1_order = int(method.v2_order)
        v2_order = int(v1_order + 1)
        v3_order = int(v2_order + 1)
        if v3_order == adsAmount:
            return redirect('tv')
        v1_mark = ads[v1_order].mark
        v2_mark = ads[v2_order].mark
        v3_mark = ads[v3_order].mark
        v1_name = ads[v1_order].name
        v2_name = ads[v2_order].name
        v3_name = ads[v3_order].name
        data = {"v1_name": v1_name, "v2_name": v2_name, "v3_name": v3_name, "v1_mark": v1_mark, "v2_mark": v2_mark, "v3_mark": v3_mark}
        if request.method == 'POST':
            method = Method.objects.create(v1_order=v1_order, v2_order=v2_order, v3_order=v3_order, v1_mark=v1_mark, v2_mark=v2_mark, v3_mark=v3_mark)
            method.save()
            choice = request.POST['choice']
            kekplus = int(request.POST['kekplus'])
            if choice == "left" and v1_mark < v2_mark + v3_mark:
                v1_mark += kekplus
            elif choice == "right" and v1_mark > v2_mark + v3_mark:
                v1_mark -= kekplus
            Ad.objects.filter(id = (v1_order+1)).update(mark = v1_mark)
            return redirect('method')
        return render(request, 'method.html', context=data)
    
        

