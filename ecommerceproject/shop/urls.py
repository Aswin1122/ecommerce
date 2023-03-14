from django.contrib import admin
from django.urls import path, include
from . import views


app_name='shop'
urlpatterns = [
    path('',views.allproductcat,name='allproductcat'),
    path('<slug:c_slug>/',views.allproductcat,name='products_by_cat'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodetails,name='procatdetail')
]
