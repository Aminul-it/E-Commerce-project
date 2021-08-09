from django.shortcuts import render
from app_order.models import Order
from app_payment.models import Billingaddress
from app_payment.forms import BillingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def checkout(request):
    saved_address = Billingaddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    form = BillingForm(instance=saved_address)
    if request.method == 'POST':
        form = BillingForm(request.POST,instance=saved_address)
        if form.is_valid():
            form.save()
            form = BillingForm(instance=saved_address)
            messages.success(request,f"Shipping Address Saved!")
    order_qs = Order.objects.filter(user=request.user,ordered=False)

    order_items = order_qs[0].orderitem.all()
    order_total = order_qs[0].get_totals()
    return render(request,'app_payment/checkout.html',context={'form':form, 'order_items':order_items,"order_total":order_total,'saved_address':saved_address})
