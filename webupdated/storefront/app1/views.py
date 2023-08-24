from django.shortcuts import render , HttpResponse,redirect
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate,login as django_login, logout
from app1 import views
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        existing_user = User.objects.filter(username=username).first()

        if password1 != password2:
            return HttpResponse("Passwords do not match!")

        if existing_user:
            return HttpResponse("username is taken! Come up with new one")
        else:
            myuser = User.objects.create_user(username, email, password1)
            myuser.save()
            return redirect('login')

    return render(request, 'signup.html')

def home(request):
    return render(request, 'home.html')
def login(request): 
    if request.user.is_authenticated:
        return redirect ('home' )
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1= request.POST.get('pass')
        user = authenticate(username=username,password=pass1) 
        if user is not None:
            django_login(request,user)
            response = redirect('home') 
            response.set_cookie('username', username)
            return response
        else :
           return HttpResponse("invalid credentials")

    return render(request,'login.html')
def LogoutPage(request):
    logout(request)
    return redirect('login') 

def newarrival(request): 
        products = Product.objects.all()
        context = {'products': products } 
        return render(request,'newarrival.html',context=context)

def categories(request):
    if request.method == "GET":
        return render(request,"categories.html") 
def cart(request):
    if request.user.is_authenticated:
         items = orderItem.objects.all()
         context = {'items': items}
         return render(request,"cart.html",context=context) 
    else:
        return redirect('login')
def apparel(request): 
        category_id = 1
        products = Product.objects.filter(category_id=category_id)
        context={'products': products }
        return render (request ,"apparel.html" ,context=context )

def kicks(request):
        products = Product.objects.all().filter(category_id=2)
        context={'products': products }
        return render (request ,"kicks.html" ,context=context )

def checkout(request):
            if request.method == "GET": 
                name=request.GET.get('name')
                address=request.GET.get('address')
                city= request.GET.get('city')
                state= request.GET.get('state')
                zipcode= request.GET.get('zipcode')
                shipping_instance = shipping(name=name ,address=address, city=city, state=state, zipcode=zipcode)
                shipping_instance.save()
                HttpResponse("saved!")
                if request.user.is_authenticated:
                    items = orderItem.objects.all()
                    context={'items': items }
                    return render (request ,"checkout.html" , context=context )
                else:
                     return redirect ('login')
            
def product_detail(request,id):
      product = Product.objects.filter(id=id).first()
      return render(request, 'product_detail.html', {'product': product})

@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        cart_data = request_data
        user = request.user  
        for item in cart_data:
            product_id = item['id']
            quantity = item['quantity']
            product = Product.objects.get(pk=product_id)
            order_item = orderItem(product=product, quantity=quantity)
            order_item.save()
        return JsonResponse({'message': 'Items added to cart.'})
@csrf_exempt
def remove_from_cart(request):
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)
            product_id = request_data['id']
            try:
                order_item = orderItem.objects.get(product_id=product_id)
                order_item.delete()
                return JsonResponse({'message': 'Item removed from cart.'})
            except orderItem.DoesNotExist:
                return JsonResponse({'message': 'Item not found in cart.'}, status=400)
        except Exception:
            return JsonResponse({'message': 'Error processing the request.'}, status=500)
