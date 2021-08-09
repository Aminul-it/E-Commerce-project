from django.urls import path
from app_order import views
app_name = "app_order"

urlpatterns = [
   path('add/<pk>/',views.add_to_cart, name="add"),
   path('cart/', views.Cart_View,name="cart"),
   path('remove/<pk>/',views.Remove_from_cart,name="remove"),
   path('increase/<pk>/', views.increase_item,name="increase"),
   path('decrease/<pk>/',views.decrease_item,name="decrease")


]
