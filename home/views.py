from django.shortcuts import render,redirect
from .models import CarouselProducts, Product
from .forms import QuotationForm

# Create your views here.

def Home(request):
    product = CarouselProducts.objects.all()
    form = QuotationForm()
    if request.method == 'POST':
        form = QuotationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'product':product ,
        'form': form
    }
    return render(request, 'home/index.html', context)

def Products(request):
    products = Product.objects.all()
    return render(request, 'home/products.html', {'products':products})
