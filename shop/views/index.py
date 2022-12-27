from django.views import View
from django.shortcuts import render
from shop.models import Category, Customer, Product, Cart

def index(request):
    current_user = request.user
    products = Product.objects.all()
    petfood = Product.objects.filter(category_id=1)
    petvacc = Product.objects.filter(category_id=2)
    pets = Product.objects.filter(category_id=3)
    petaccessories = Product.objects.filter(category_id=4)
    petgroom = Product.objects.filter(category_id=5)
    petshelter = Product.objects.filter(category_id=6)
    categories = Category.objects.all()
    carts = Cart.objects.filter(user_id=current_user.id)

    customer = []
    try:
        customer = Customer.objects.get(user_id=current_user.id)
    except:
        pass
    
    qty = 0
    total = 0
    for cart in carts:
        total = total + cart.amount
        qty = qty + cart.qty
    
    params = {
        'customer':customer,
        'products': products,
        'petfood': petfood,
        'petvacc': petvacc ,
        'pets': pets ,
        'petaccessories': petaccessories,
        'petgroom': petgroom,
        'petshelter': petshelter,
        'categories':categories,
        'qty':qty,
        'total':total,
        'carts':carts,
    }

    return render(request, 'index.html', params)