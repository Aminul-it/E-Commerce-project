from django.shortcuts import render,get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app_shop.models import Product
from app_order.models import Cart,Order

@login_required
def add_to_cart(request,pk):
    item = get_object_or_404(Product,pk=pk)
    order_item = Cart.objects.get_or_create(item=item,user=request.user,purchased=False)
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitem.filter(item=item).exists():
            order_item[0].quantity +=1
            order_item[0].save()
            messages.info(request,"Thos Item Quantity was Updated")
            return redirect('app_shop:Home')
        else:
            order.orderitem.add(order_item[0])
            messages.info(request,"This Item was Added Successfully ")
            return redirect('app_shop:Home')
    else:
        order = Order(user=request.user)
        order.save()
        order.orderitem.add(order_item[0])
        messages.info(request,"This Item Was Added Successfully")
        return redirect('app_shop:Home')
@login_required
def Cart_View(request):
    carts = Cart.objects.filter(user=request.user,purchased=False)
    orders = Order.objects.filter(user=request.user,ordered=False)
    if carts.exists() and orders.exists():
        order = orders[0]
        return render( request,'app_order/cart.html', context={'carts':carts,'order':order})

    else:
        messages.warning(request,"you donot have item in your  cart ")
        return redirect('app_shop:Home')

@login_required
def Remove_from_cart(request,pk):
    item = get_object_or_404(Product,pk=pk)
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitem.filter(item=item).exists():
            order_remove = Cart.objects.filter(item=item,user=request.user,purchased=False)
            order_remove = order_remove[0]
            order.orderitem.remove(order_remove)
            order_remove.delete()
            messages.warning(request,"Item Delete Successfully")
            return redirect('app_shop:Home')
        else:
            messages.warning(request,'This Item Was Not In your cart')
            return redirect('app_shop:Home')

    else:
        messages.info(request,"You don't have an active order")
        return redirect('app_shop:Home')

@login_required
def increase_item(request,pk):
    item = get_object_or_404(Product,pk=pk)
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitem.filter(item=item).exists():

            order_item = Cart.objects.filter(item=item,user=request.user,purchased=False)[0]

            if order_item.quantity >= 1:
                order_item.quantity += 1
                order_item.save()
                messages.info(request, f" {item.name} item was Updated")
                return redirect("app_order:cart")


        else:
            messages.warning(request,f"{item.name}Item is not in your cart!")
            return redirect('app_shop:Home')
    else:
        messages.info(request,"You don't have an active order")
        return redirect('app_shop:Home')
@login_required
def decrease_item(request,pk):
    item = get_object_or_404(Product,pk=pk)
    order_qs = Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitem.filter(item=item).exists():

            order_item = Cart.objects.filter(item=item,user=request.user,purchased=False)[0]

            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, f" {item.name} item was Updated")
                return redirect("app_order:cart")
            else:
                order.orderitem.remove(order_item)
                order_item.delete()

        else:
            messages.warning(request,f"{item.name}Item is not in your cart!")
            return redirect('app_shop:Home')
    else:
        messages.info(request,"You don't have an active order")
        return redirect('app_shop:Home')
