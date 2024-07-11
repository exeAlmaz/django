from django.shortcuts import render, redirect

# from phones.models import Phone
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_map = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }
    phones = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort:
        phones = phones.order_by(sort_map[sort])
    context = {
        'phones': phones
    }

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.filter(slug=slug)
    for phone in phones:
        context = {'phone': phone}
    return render(request, template, context)

