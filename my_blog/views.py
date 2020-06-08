from django.shortcuts import render ,get_object_or_404
from .models import Product
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request,'my_blog/index.html',{"products":products})

def product_details(request,pk):
    Product.objects.get(pk=pk)

class ProductDelete(DeleteView):
    model=Product
    success_url="/" 