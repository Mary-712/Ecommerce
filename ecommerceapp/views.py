from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from ecommerceapp.models import Category,Product,Customer,Shopcart
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
import os

# Create your views here.
def home(request):
    
    return render(request,'home.html')

def adminhome(request):
    return render(request,'adminhome.html')

def userhome(request):
    b=Category.objects.all()
    return render(request,'userhome.html',{'b':b})

def loginn(request):
    
    return render(request,'login.html')
def fil(request,pk):
    c=Product.objects.filter(category=pk)
    b=Category.objects.all()
    return render(request,'fil.html',{'c':c,'b':b})

def login1(request):
    b=Category.objects.all()
    if request.method == 'POST':
        uname = request.POST['username']
        pas = request.POST['password']
        usr = auth.authenticate(username=uname,password=pas) 
        if usr is not None:
            if usr.is_superuser:
                login(request,usr)
                messages.info(request,f'Welcome Admin : {uname}')
                return redirect('adminhome')
            else:
                login(request,usr)
                messages.info(request,f'Welcome  {uname}')
                return render(request,'userhome.html',{'b':b})


def logoutt(request):
    logout(request)
    return redirect('home') 

def signup(request):
    return render(request,'signup.html')

def signupaction(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        pas = request.POST['pass']
        cpas = request.POST['cpass']
        email = request.POST['email']
        addrss = request.POST['address']
        contact = request.POST['contact']
        photo = request.FILES['image'] 

        if pas == cpas :
            if User.objects.filter(username = uname).exists():
                messages.info(request,'username exists')
                return redirect('signup')
            else:
                usr = User.objects.create_user(first_name = fname, last_name = lname, password = pas,email=email,username=uname)
                usr.save()
                b = Customer(address = addrss,contactnumber=contact,image=photo,user=usr)
                b.save()
                return redirect('home')
        else:
            messages.info(request,'password doesnt match')
            return redirect('signup')
        
def add_category(request):
    return render(request,'add_category.html')

def add_product(request):
    b=Category.objects.all()
    return render(request,'add_product.html',{'b':b}) 

def show_product(request):
    return render(request,'show_product.html')

def show_user(request):
    return render(request,'show_user.html')
def  category(request):
        if request.method == 'POST':
            category = request.POST['cata']
            b = Category(category=category)
            b.save()
            return render(request,'add_category.html' )
def addprod(request):
    if request.method=='POST':
        prod = request.POST['pname']
        des = request.POST['des']
        cat = request.POST['category']
        price = request.POST['price'] 
        photo = request.FILES['photo']
        p = Product(productname=prod,description=des,price=price,image=photo,category_id=cat)
        p.save()
        messages.info(request,'successfully added')
        return redirect('add_product')
def show_product(request):
    t = Product.objects.all()
    return render(request,'show_product.html',{'shw':t})

def show_user(request):
    s=Customer.objects.all()
    return render(request,'show_user.html',{'s':s})
def cart(request):
    user=request.user.id
    print(user)
    b=Category.objects.all()
    v=Customer.objects.get(user=user)
    cid=v.id
    a=Shopcart.objects.filter(customer=cid)
    return render(request,'cart.html',{'a':a,'b':b})
def addtocart(request,pk):
    cus = Customer.objects.get(user=request.user)
    n = cus.id
    p = Product.objects.get(id=pk)
    q = p.id
    m = Shopcart(product_id=q,customer_id=n)
    m.save()
    return redirect('cart')
def deletepage(request,pk):
    emp=Product.objects.get(id=pk)
    emp.delete()
    return redirect('show_product')
def deletepage1(request,pk):
    emp=Customer.objects.get(id=pk)
    emp.delete()
    return redirect('show_user')
def deletepage2(request,pk):
    emp=Shopcart.objects.get(id=pk)
    emp.delete()
    return redirect('cart')