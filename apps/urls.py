from django.urls import path
from apps import views

urlpatterns = [
    path('', views.home, name='home'),
    path('single-product/', views.single_product, name='single_product'),
    path('contact/', views.contact_us, name='contact_us'),

    path('products/', views.product_list, name='products'),

    path('product/<int:id>/', views.single_product, name='single_product'),
    path('order-submit/', views.order_submit, name='order_submit'),

    path('women-products/', views.women_products, name='women_products'),
    path('men-products/', views.men_products, name='men_products'),
    path('kids-products/', views.kids_products, name='kids_products'),
    path('accessories-products/', views.accessories_products, name='accessories_products'),

    path('about-us/', views.about_us, name='about'),

    path('beauty-salon/', views.beauty_salon, name='beauty_salon')

]
