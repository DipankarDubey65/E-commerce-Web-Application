from django.shortcuts import render,redirect,HttpResponse
from app.models import Category,Sub_Category,Product,Items,RecommedItems,Slider,Contact,Order,Brand
from django.contrib.auth import authenticate,login
from app.models import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from cart.cart import Cart



def Index(request):
    category = Category.objects.all()
    brand = Brand.objects.all()
    brandID = request.GET.get('brand')
    categoryID = request.GET.get('category')

    items = Items.objects.all().order_by('-id')[:4]
    recommeditems = RecommedItems.objects.all().order_by('-id')[:3]
    slider = Slider.objects.all()
    if categoryID:
        product = Product.objects.filter(sub_category = categoryID).order_by('-id')[:6]
    elif brandID:
        product = Product.objects.filter(brand = brandID).order_by('-id')


    else:
        product = Product.objects.all().order_by('-id')[:6]
    context = {
        'category':category,
        'product':product,
        'items' : items,
        'recommeditems':recommeditems,
        'slider':slider,
        'brand':brand,

    }

    return render(request,"index.html",context)

def ContactUs(request):
    if request.method == "POST":
        contact = Contact(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message'),
        )
        contact.save()
    return render(request,"contact-us.html")

def Checkout(request):
    if request.method == "POST":
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        pincode = request.POST.get('pincode')
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk = uid)


        for i in cart:
            a = (int(cart[i]['price']))
            b = cart[i]['quantity']
            total = a*b
            order = Order(
                user = user,
                product = cart[i]['name'],
                price = cart[i]['price'],
                quantity = cart[i]['quantity'],
                image = cart[i]['image'],
                address = address,
                phone = phone,
                pincode = pincode,
                total = total,
            )
            order.save()
        request.session['cart'] = {}
        return redirect('index')


    return HttpResponse('this is checkout page')



def Blog(request):
    return render(request,"blog.html")

def SingleBlog(request):
    return render(request,"blog-single.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
            )
            login(request,new_user)
            return redirect('index')
    else:
        form = UserCreateForm()

    data ={
            'form':form
        }
    return render(request,'registration/signup.html',data)




@login_required(login_url="/account/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")

@login_required(login_url="/account/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")

@login_required(login_url="/account/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")

@login_required(login_url="/account/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")

@login_required(login_url="/account/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")

@login_required(login_url="/account/login/")
def cart_detail(request):

    return render( request,"cart/cart_detail.html")

def Your_order(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(pk=uid)
    order = Order.objects.filter(user = user)

    data ={
        'order':order,

    }
    return render(request,"Order.html",data)


def Product_page(request):
    category = Category.objects.all()
    brand = Brand.objects.all()
    brandID = request.GET.get('brand')
    categoryID = request.GET.get('category')

    items = Items.objects.all().order_by('-id')[:4]
    recommeditems = RecommedItems.objects.all().order_by('-id')[:3]
    slider = Slider.objects.all()
    if categoryID:
        product = Product.objects.filter(sub_category=categoryID).order_by('-id')[:6]
    elif brandID:
        product = Product.objects.filter(brand=brandID).order_by('-id')


    else:
        product = Product.objects.all().order_by('-id')[:6]
    data={
       'category': category,
        'brand' : brand,
        'product':product,
    }
    return render(request,"Product_page.html",data)



def ProductDetails(request,id):
    product = Product.objects.filter(id = id).first()
    data = {
        'product':product
    }
    return render(request,"product-details.html",data)

def Search(request):
    Query = request.GET['query']
    product = Product.objects.filter(name__icontains = Query)
    recommeditems = RecommedItems.objects.filter(name__icontains = Query)


    data = {
        'product':product,
        'recommeditems':recommeditems,
    }
    return render(request,"Search.html",data)

