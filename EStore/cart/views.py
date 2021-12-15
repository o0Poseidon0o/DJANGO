from django.shortcuts import render, get_object_or_404, redirect
from cart.cart import Cart
from store.models import Product


# Create your views here.
def cart_detail(request):
    return render(request, 'store/cart.html')


def buy_now(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    if request.POST.get('quantity'):
        cart.add(product=product, quantity=int(request.POST.get('quantity')))
    return redirect('cart:cart_detail')
