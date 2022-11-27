from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name = "store"),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name="product-detail"),
    path('cart/', views.cart, name = "cart"),
    path('checkout/', views.checkout, name = "checkout"),
    path('update_item/', views.updateItem, name = "update_item"), 
    path('process_order/', views.processOrder, name = "process_order"),
    path('payment_success/', views.payment_success, name = "payment_success"),

]
