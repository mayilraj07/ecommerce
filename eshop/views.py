from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from django.http import JsonResponse
from django.db.models import Q
import random

def home(request):
    total_cart = 0
    total_wishList = 0
    if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
        total_wishList = len(Favourite.objects.filter(user = request.user))
    category = Category.objects.filter(status = 1)
    products = Product.objects.filter(trending = 1,status=1)
    search = Product.objects.filter(status=1)
    return render(request,'main/index.html',locals())

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            uname = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request, username = uname, password = pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in successfully")
                return redirect('Home')
            else:
                messages.error(request,'Invalid User Name or Password')
                return redirect('Login')   
        return render(request,'main/login.html',{'login_page':'login'})
    
@login_required
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Logged out successfully')
    return redirect('/')

def register(request):
    form = CreateUserForm()
    searchItems = Product.objects.filter(status=1)
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registered Successfully')
            return redirect('Login')
        else:
            messages.error(request,'Register Failed')
            return redirect('Register')
    return render(request,'main/register.html',locals())

def search(request):
    searchText = request.GET.get('search')
    search= Product.objects.filter(status=1)
    if searchText == '':
        return redirect('/')
    else:
        productSearch = Product.objects.filter(Q(product_name__icontains = searchText,status = 1))
        if productSearch:
            return render(request,'main/productview.html',locals())
        else:
            messages.error(request,'No Items Found')
            return redirect('/')

def collections(request):
    total_cart = 0
    total_wishList = 0
    if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
        total_wishList = len(Favourite.objects.filter(user=request.user))
    category = Category.objects.filter(status = 1)
    searchItems = Product.objects.filter(status=1)
    return render(request,'main/collections.html',locals())

def productView(request,name):
    total_cart = 0
    total_wishList = 0
    categoryName = name
    if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
        total_wishList = len(Favourite.objects.filter(user = request.user))
    if(Category.objects.filter(status = 1, category_name=name )):
        products = Product.objects.filter(category__category_name = name, status = 1)
        searchItems = Product.objects.filter(status=1)
        return render(request,'main/productview.html',locals())
    else:
        messages.warning(request,"Category Not Found")
        return redirect('Collections')
    
def product_details(request,cname,pname):
    total_cart = 0
    total_wishList = 0
    if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
        total_wishList = len(Favourite.objects.filter(user=request.user))
        wishlist = Favourite.objects.filter(user=request.user,product__product_name = pname)
    if Category.objects.filter(category_name = cname, status = 1):
        if Product.objects.filter(product_name = pname, status = 1):
            products = Product.objects.filter(product_name = pname, status = 1).first()
            return render(request,'main/productdetails.html',locals())
        else:
            messages.error(request,'Product not found')
            return redirect('Collections')
    else:
        messages.error(request,"category not found")
        return redirect('Collections')

def addCart(request):
    if request.user.is_authenticated:
        productId = request.GET.get('product_id')
        productStatus = Product.objects.get(id = productId)
        category = Category.objects.get(product=productId)
        if Cart.objects.filter(user = request.user.id, product_id = productId):
            messages.error(request,'Already Added to Cart')
            return redirect('Product_details',cname=category.category_name,pname=productStatus.product_name)
        else:
            Cart.objects.create(user = request.user, product_id = productId)
            messages.success(request,'Added to cart')
            return redirect('Product_details',cname=category.category_name,pname=productStatus.product_name)
    else:
        return redirect('Login')
    
def viewCart(request):
    total_wishList = 0
    if request.user.is_authenticated:
        total_wishList = len(Favourite.objects.filter(user = request.user))
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        min_amount = 500
        for p in cart:
            value = p.product_qty * p.product.selling_price
            amount +=value
        if amount >= min_amount:
                totalAmount = amount
        else:
            totalAmount = amount + 40           
        return render(request, 'main/addtocart.html',locals())
    else:
        return redirect('Login')

def plusCart(request):
    if request.method == 'GET':
        product_id = request.GET['product_id']
        c = Cart.objects.get(Q(product=product_id)& Q(user = request.user))
        c.product_qty += 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        min_amount = 500
        for p in cart:
            value = p.product_qty * p.product.selling_price
            amount +=value
        if amount >= min_amount:
                totalAmount = amount
        else:
            totalAmount = amount + 40
        data = {
            'quantity':c.product_qty,
            'amount':amount,
            'totalamount':totalAmount,
            'min_amount':min_amount
        }
        return JsonResponse(data)
    
def minusCart(request):
    if request.method == 'GET':
        product_id = request.GET['product_id']
        c = Cart.objects.get(Q(product=product_id)& Q(user = request.user))
        c.product_qty -= 1
        if c.product_qty < 1:
            c.product_qty = 1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        min_amount = 500
        for p in cart:
            value = p.product_qty * p.product.selling_price
            amount +=value
        if amount >= min_amount:
                totalAmount = amount
        else:
            totalAmount = amount + 40
        data = {
            'quantity':c.product_qty,
            'amount':amount,
            'totalamount':totalAmount,
            'min_amount':min_amount
        }
        return JsonResponse(data)
    
def removeCart(request,pid):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user,product_id=pid)
        cart.delete()
        return redirect('Cart')
    else:
        return redirect('/')
    
def addWishlist(request,pid):
    if request.user.is_authenticated:
        product = Product.objects.get(id = pid)
        category = Category.objects.get(product=pid)
        if Favourite.objects.filter(user = request.user.id, product_id = pid):
            messages.error(request,'Already Added to Wishlist')
            return redirect('Product_details',cname=category.category_name,pname=product.product_name)
        else:
            Favourite.objects.create(user = request.user, product_id = pid)
            messages.success(request,'Added to Wishlist')
            return redirect('Product_details',cname=category.category_name,pname=product.product_name)
    else:
        return redirect('Login')

def view_wishlist(request):
    total_cart = 0
    if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
        user = request.user
        wishlist = Favourite.objects.filter(user=user)
        amount = 0
        min_amount = 500
        for p in wishlist:
            value = p.product_qty * p.product.selling_price
            amount +=value
        if amount >= min_amount:
                totalAmount = amount
        else:
            totalAmount = amount + 40           
        return render(request, 'main/wishlist.html',locals())
    else:
        return redirect('Login')
    
def addCount(request):
    if request.method == 'GET':
        product_id = request.GET['product_id']
        c = Favourite.objects.get(Q(product=product_id)& Q(user = request.user))
        c.product_qty += 1
        c.save()
        user = request.user
        wishlist = Favourite.objects.filter(user=user)
        amount = 0
        min_amount = 500
        for p in wishlist:
            value = p.product_qty * p.product.selling_price
            amount +=value
        if amount >= min_amount:
            totalAmount = amount
        else:
            totalAmount = amount + 40
        data = {
            'quantity':c.product_qty,
            'amount':amount,
            'totalamount':totalAmount,
            'min_amount':min_amount
        }
        return JsonResponse(data)
    
def minusCount(request):
    if request.method == 'GET':
        product_id = request.GET['product_id']
        c = Favourite.objects.get(Q(product=product_id)& Q(user = request.user))
        c.product_qty -= 1
        if c.product_qty < 1:
            c.product_qty = 1
        c.save()
        user = request.user
        cart = Favourite.objects.filter(user=user)
        amount = 0
        min_amount = 500
        for p in cart:
            value = p.product_qty * p.product.selling_price
            amount +=value
        if amount >= min_amount:
                totalAmount = amount
        else:
            totalAmount = amount + 40
        data = {
            'quantity':c.product_qty,
            'amount':amount,
            'totalamount':totalAmount,
            'min_amount':min_amount
        }
        return JsonResponse(data)
    
def remove_wishlist(request,pid):
    if request.user.is_authenticated:
        wishlist = Favourite.objects.get(user=request.user,product_id=pid)
        wishlist.delete()
        return redirect('wishlist')
    else:
        return redirect('/')

def buyProduct(request,pid):
    total_cart = 0
    total_wishList = 0
    if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
        total_wishList = len(Favourite.objects.filter(user = request.user))
        product = Product.objects.get(id = pid)
        if product:
            buyproduct = BuyProduct.objects.all()
            buyproduct.delete() 
            BuyProduct.objects.create(user = request.user, product_id = pid)
            buyItem = BuyProduct.objects.filter(user=request.user)
            print(type(buyItem))
            amount = 0
            min_amount = 500
            for p in buyItem:
                value = p.product_qty * p.product.selling_price
                amount +=value
            if amount >= min_amount:
                totalAmount = amount
            else:
                totalAmount = amount + 40 
            return render(request,'main/buyproduct.html',locals())
        else:
            return redirect('/')
    else:
        return redirect('Login')

def addQty(request):
    if request.method == 'GET':
        product_id = request.GET['product_id']
        c = BuyProduct.objects.get(Q(product=product_id)& Q(user = request.user))
        c.product_qty += 1
        c.save()
        user = request.user
        product = BuyProduct.objects.filter(user=user)
        amount = 0
        min_amount = 500
        for p in product:
            value = p.product_qty * p.product.selling_price
            amount +=value
        if amount >= min_amount:
                totalAmount = amount
        else:
            totalAmount = amount + 40
        data = {
            'quantity':c.product_qty,
            'amount':amount,
            'totalamount':totalAmount,
            'min_amount':min_amount
        }
        return JsonResponse(data)
    
def minQty(request):
    if request.method == 'GET':
        product_id = request.GET['product_id']
        c = BuyProduct.objects.get(Q(product=product_id)& Q(user = request.user))
        c.product_qty -= 1
        if c.product_qty < 1:
            c.product_qty = 1
        c.save()
        user = request.user
        buy = BuyProduct.objects.filter(user=user)
        amount = 0
        min_amount = 500
        for p in buy:
            value = p.product_qty * p.product.selling_price
            amount +=value
        if amount >= min_amount:
                totalAmount = amount
        else:
            totalAmount = amount + 40    
        data = {
            'quantity':c.product_qty,
            'amount':amount,
            'totalamount':totalAmount,
            'min_amount' : min_amount

        }
        return JsonResponse(data)
    
def removeProduct(request,product_id):
    buy_product = BuyProduct.objects.get(user = request.user,product=product_id)
    buy_product.delete()
    return redirect('/')

@login_required
def viewProfile(request):
    total_cart = 0
    total_wishList = 0
    if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
        total_wishList = len(Favourite.objects.filter(user = request.user))
        user_info = User.objects.get(id=request.user.id)
        if request.method == 'POST':
            user_data = User.objects.get(id=request.user.id)
            user_data.first_name = request.POST.get('first_name')
            user_data.last_name = request.POST.get('last_name')
            user_data.username = request.POST.get('username')
            user_data.email = request.POST.get('email')
            user_data.save()
            messages.success(request,'Updated Successfully')
            return redirect('profile')
    return render(request,'main/profile.html',locals())

@login_required
def address(request):
    total_cart = 0
    total_wishList = 0
    if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
        total_wishList = len(Favourite.objects.filter(user = request.user))
    add = Customer.objects.filter(user=request.user)
    return render(request,'main/address.html',locals())

@login_required
def newAddress(request):
    form = CustomerAddressForm()
    total_cart = 0
    total_wishList = 0
    if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
        total_wishList = len(Favourite.objects.filter(user = request.user))
    if request.method == 'POST':
        form = CustomerAddressForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            address = form.cleaned_data['address']
            landmark = form.cleaned_data['landmark']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            pincode = form.cleaned_data['zipcode']
            address_type = form.cleaned_data['address_type']
            add = Customer(user=user,name=name,locality=locality,address=address,landmark=landmark,city=city,mobile=mobile,state=state,zipcode=pincode,address_type=address_type)
            add.save()
            messages.success(request,'Success')
            return redirect('address')
    return render(request,'main/new-address.html',locals())

@login_required
def updateAddress(request,id):
    total_cart = 0
    total_wishList = 0
    if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
        total_wishList = len(Favourite.objects.filter(user = request.user))
        add = Customer.objects.get(id=id)
        forms = CustomerAddressForm(instance=add)
        if request.method == 'POST':
            form = CustomerAddressForm(request.POST)
            if form.is_valid():
                add = Customer.objects.get(id=id)
                add.user = request.user
                add.name = form.cleaned_data['name']
                add.locality = form.cleaned_data['locality']
                add.address = form.cleaned_data['address']
                add.city = form.cleaned_data['city']
                add.mobile = form.cleaned_data['mobile']
                add.state = form.cleaned_data['state']
                add.landmark = form.cleaned_data['landmark']
                add.zipcode = form.cleaned_data['zipcode']
                add.address_type = form.cleaned_data['address_type']
                add.save()
                messages.success(request,'Registered Successfully')
                return redirect('address')
            else:
                messages.success(request,'Invalid')
                return redirect('address')
        return render(request,'main/updateAddress.html',locals())
    
@login_required
def deleteAddress(request,delete_id):
    addr = Customer.objects.get(id = delete_id)
    addr.delete()
    return redirect('address')

@login_required        
def shippingAddress(request,product):
    total_cart = 0
    total_wishList = 0
    if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
        total_wishList = len(Favourite.objects.filter(user=request.user))
        user = request.user
        add = Customer.objects.filter(user=user)
        form = CustomerAddressForm()
        if product == 'cart':
            item = Cart.objects.filter(user=user)
        if product == 'wishlist':
            item = Favourite.objects.filter(user=user)
        if product == 'buy':
            item = BuyProduct.objects.filter(user=user)
        famount = 0
        min_amount = 500
        for p in item:
            value = p.product_qty * p.product.selling_price
            famount +=value
        if famount >= min_amount:
                totalAmount = famount
        else:
            totalAmount = famount + 40
    return render(request,'main/shipping-address.html',locals())

@login_required
def checkOut(request,item):
    total_cart = 0
    total_wishList = 0
    if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
        total_wishList = len(Favourite.objects.filter(user=request.user))
        user = request.user
        add = Customer.objects.filter(user=user)
        if item == 'cart':
            total_items = Cart.objects.filter(user=user)
        if item == 'wishlist':
            total_items = Favourite.objects.filter(user=user)
        if item == 'buy':
            total_items = BuyProduct.objects.filter(user=user)
        famount = 0
        min_amount = 500
        for p in total_items:
            value = p.product_qty * p.product.selling_price
            famount +=value
        if famount >= min_amount:
                totalAmount = famount
        else:
            totalAmount = famount + 40
        if request.method == 'POST':
            cust_add = request.POST.get('custid')
            del_add = Customer.objects.get(id=cust_add)
        return render(request,'main/checkout.html',locals())
    else:
        return redirect('Login')

@login_required
def payment(request,custid,product_item):
    total_cart = 0
    total_wishList = 0
    if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
        total_wishList = len(Favourite.objects.filter(user=request.user))
        user = request.user
        add = Customer.objects.get(id=custid)
        if product_item == 'cart':
            total_items = Cart.objects.filter(user=user)
        if product_item == 'wishlist':
            total_items = Favourite.objects.filter(user=user)
        if product_item == 'buy':
            total_items = BuyProduct.objects.filter(user=user)
        famount = 0
        min_amount = 500
        for p in total_items:
            value = p.product_qty * p.product.selling_price
            famount +=value
        if famount >= min_amount:
                totalAmount = famount
        else:
            totalAmount = famount + 40
        if request.method == 'POST':
            payMode = request.POST.get('payment_mode')
            orderId = paymentOrderId()
            payment_data = Payment(user=request.user,amount=totalAmount,payment_mode=payMode,paid=False,order_id=orderId).save()
            payment = Payment.objects.get(order_id=orderId)
            for c in total_items:
                OrderPlaced(user=user,customer=add,product=c.product,quantity=c.product_qty,payment=payment).save()
                c.delete()
            return redirect('orderinfo') 
    return render(request,'main/payment.html',locals())

def randNum(num):
  randnum = random.randrange(0, 16)
  return num[randnum]

def paymentOrderId():
  rand_num = ''
  hex = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
  for i in range(12):
    rand_num += str(randNum(hex))
  return rand_num

@login_required
def orderInfo(request):
    return render(request,'main/orderinfo.html')

@login_required
def orders(request):
    total_cart = 0
    total_wishList = 0
    total_cart = len(Cart.objects.filter(user=request.user))
    total_wishList = len(Favourite.objects.filter(user=request.user))
    order_placed = OrderPlaced.objects.filter(user=request.user)
    return render(request,'main/orders.html',locals()) 

@login_required
def viewOrders(request,orderid):
    total_cart = 0
    total_wishList = 0
    total_cart = len(Cart.objects.filter(user=request.user))
    total_wishList = len(Favourite.objects.filter(user=request.user))
    order_placed = OrderPlaced.objects.filter(user=request.user,id=orderid)
    return render(request,'main/vieworders.html',locals()) 

@login_required
def cancelOrder(request,orderid):
    if request.user.is_authenticated:
        total_cart = len(Cart.objects.filter(user=request.user))
        total_wishList = len(Favourite.objects.filter(user=request.user))
        order = OrderPlaced.objects.get(user=request.user,id=orderid)
        order.status = 'Cancel'
        order.save()
    return redirect('viewOrders',orderid)

@login_required
def returnOrder(request,orderid):
    if request.user.is_authenticated:
        order = OrderPlaced.objects.get(user=request.user,id=orderid)
        order.status = 'Return'
        order.save()
    return redirect('orders')