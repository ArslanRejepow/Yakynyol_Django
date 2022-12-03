from django.shortcuts import render, redirect
from users.models import User
from .models import Category, Favourite, Product, Market, Service
from .forms import FavouriteForm, ProductForm

# Create your views here.


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    # print(request.user)
    if request.user.id:
        favourites = Favourite.objects.filter(user=request.user)
        context['favourites'] = favourites

    return render(request, 'shopping/home.html', context=context)


def services(request):
    services = Service.objects.all()
    categories = Category.objects.all()
    context = {
        'services': services,
        'categories': categories,
    }
    # print(request.user)
    if request.user.id:
        favourites = Favourite.objects.filter(user=request.user)
        context['favourites'] = favourites

    return render(request, 'shopping/services.html', context=context)


def profile(request):
    return render(request, 'shopping/profile.html')


##### ADD Views #####

def add_product(request):
    tempdict = request.POST.copy()
    user_ = User.objects.get(pk=request.user.pk)

    market_ = Market.objects.get(user=user_)
    print(market_)
    tempdict['market'] = market_
    request.POST = tempdict  # this is the added line

    form = ProductForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('shopping')

    return render(request, "shopping/add_product.html")


def add_to_favourites(request):
    id = request.GET.get('id')
    obj = {'user': request.user, "product": Product.objects.get(pk=id)}
    model = FavouriteForm(obj)
    model.save()
    return redirect('shopping')

##### UPDATE PRODUCT VIEWS #####


def update_product_view(request, pk):
    product = Product.objects.get(pk=pk)

    context = {
        'product': product,
    }

    return render(request, 'shopping/update_product.html', context=context)


def update_product(request):
    product = Product.objects.get(pk=request.POST.get('pk'))
    if 'name' in request.POST:
        product.name = request.POST.get('name')
    if 'price' in request.POST:
        product.price = request.POST.get('price')
    if 'about' in request.POST:
        product.about = request.POST.get('about')
    print(product.image_2)
    if 'image_1' in request.FILES:
        product.image_1 = request.FILES.get('image_1')
    if 'image_2' in request.FILES:
        product.image_2 = request.FILES.get('image_2')
    if 'image_3' in request.FILES:
        product.image_3 = request.FILES.get('image_3')

    product.save()
    print(product.image_2)
    return redirect('profile_market')


##### DELETE VIEWS #####

def delete_product(request, pk):
    instance = Product.objects.get(pk=pk)
    instance.delete()

    return redirect('profile_market')
