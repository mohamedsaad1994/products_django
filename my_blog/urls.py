from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('product/<int:pk>/',views.product_details,name='product_details'),
    path('product/<pk>/delete',views.ProductDelete.as_view(),name='product_delete'),

]
