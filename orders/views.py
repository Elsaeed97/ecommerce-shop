from django.shortcuts import render
from .forms import OrderCreateForm 
from .models import OrderItem
from cart.cart import Cart 
# Create your views here.

# def checkout(request):
#     context = {}
#     return render(request, 'orders/checkout.html', context)



def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],price=item['price'],
                                        quantity=item['quantity']) 
            cart.clear()
            return render(request, 'orders/created.html',{'order':order})

    else:
        form = OrderCreateForm()
        return render(request,'orders/create.html', {'cart':cart, 'form':form}) 