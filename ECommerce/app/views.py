from django.shortcuts import render
from django.views import View
from .form import CustomerRegistrationForm ,LoginForm
from .models import Customer , Product , Cart, OrderPlaced
from django.contrib.auth import authenticate,login as auth_login , logout as auth_logout 
from django.contrib.auth.decorators import login_required


class ProductView(View):
    def get(self,request):
        topwear = Product.objects.filter(category = 'TW')
        bottomwear = Product.objects.filter(category = 'BW')
        mobile = Product.objects.filter(category = 'M')
        laptop = Product.objects.filter(category = 'L')

        return render(request,'app/home.html',{'topwears':topwear,'bottomwears':bottomwear,
                                               'mobiles':mobile,'laptops':laptop})

class ProductDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request , 'app/productdetail.html' , {'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')



def mobile(request,data = None):
    if data==None:
        mobiles = Product.objects.filter(category = 'M')
    
    elif data=='Redmi' or data == 'Sumsung':
        mobiles = Product.objects.filter(category = 'M').filter(brand = data)    
    
    elif  data == 'below':
        mobiles = Product.objects.filter(category ='M').filter(discount_price=10000)
        
    elif data == 'above':
        mobiles = Product.objects.filter(category = 'M').filter(discount_price= 10000)
    
    return render(request, 'app/mobile.html', {'mobiles':mobiles})


def login(request):
    form = LoginForm()
    return render(request, 'app/login.html',{'form':form})



class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',{'form':form})
    
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'app/customerregistration.html',{'form':form})


def checkout(request):
 return render(request, 'app/checkout.html')

def logout(request):
    if request.method=='POST':
        logout(request)
    return render(request,'app/logout.html')