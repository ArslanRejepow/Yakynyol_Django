from django.shortcuts import render, redirect
from users.models import User
from .models import Product, Market
from .forms import ProductForm

# Create your views here.
def home(request):

    return render(request, 'shopping/home.html')


def add_product(request):
    tempdict = request.POST.copy()
    user_ = User.objects.get(pk = request.user.pk)
    
    market_ = Market.objects.get(user = user_)
    print(market_)
    tempdict['market'] = market_
    request.POST = tempdict  # this is the added line
    
    form = ProductForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('shopping')

    return render(request, "shopping/add_product.html")

def profile(request):
    
    return render(request, 'shopping/profile.html')

def update_product_view(request, pk):
    product = Product.objects.get(pk = pk)

    context = {
        'product': product,
    }

    return render(request, 'shopping/update_product.html', context = context)
    
def update_product(request):
    product = Product.objects.get(pk = request.POST.get('pk'))
    if 'name' in request.POST: product.name = request.POST.get('name')
    if 'price' in request.POST: product.price = request.POST.get('price')
    if 'about' in request.POST: product.about = request.POST.get('about')
    print(product.image_2)
    if 'image_1' in request.FILES: product.image_1 = request.FILES.get('image_1')
    if 'image_2' in request.FILES: product.image_2 = request.FILES.get('image_2')
    if 'image_3' in request.FILES: product.image_3 = request.FILES.get('image_3')

    product.save()
    print(product.image_2)
    return redirect('profile_market')

def delete_product(request, pk):
    instance = Product.objects.get(pk=pk)
    instance.delete()
    
    return redirect('profile_market')