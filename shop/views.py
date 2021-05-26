from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, Shop, Stock
from .forms import ItemForm, ShopForm, StockForm

def index(request):
    if (request.method == 'POST'):
        obj = Item()
        form = ItemForm(request.POST, instance=obj)
        form.save()
    params = {
            'index':'index',
            'list':'list',
            'edit':'edit',
        }
    return render(request, 'shop/index.html', params)


def create_item(request):
    if (request.method == 'POST'):
        obj = Item()
        form = ItemForm(request.POST, instance=obj)
        form.save()
        return redirect(to='list_item')
    params = {
            'form':ItemForm(),
        }
    return render(request, 'shop/create_item.html', params)


def create_shop(request):
    if (request.method == 'POST'):
        obj = Shop()
        form = ShopForm(request.POST, instance=obj)
        form.save()
        return redirect(to='list_shop')
    params = {
            'form':ShopForm(),
        }
    return render(request, 'shop/create_shop.html', params)


def create_stock(request):
    if (request.method == 'POST'):
        obj = Stock()
        form = StockForm(request.POST, instance=obj)
        form.save()
        return redirect(to='list_stock')
    params = {
            'form':StockForm(),
        }
    return render(request, 'shop/create_stock.html', params)


def list_item(request):
    itemdata = Item.objects.all()
    params = {
            'itemdata': itemdata,
        }
    return render(request, 'shop/list_item.html', params)


def list_shop(request):
    shopdata = Shop.objects.all()
    params = {
            'shopdata': shopdata,
        }
    return render(request, 'shop/list_shop.html', params)


def list_stock(request):
    stockdata = Stock.objects.all()
    params = {
            'stockdata': stockdata,
        }
    return render(request, 'shop/list_stock.html', params)


def delete_item(request, id_):
    item = Item.objects.get(id = id_)
    if (request.method == 'POST'):
        item.delete()
        return redirect(to='list_item')
    params = {
            'item':item,
        }
    return render(request, 'shop/delete_item.html', params)


def delete_shop(request, id_):
    item = Shop.objects.get(id = id_)
    if (request.method == 'POST'):
        item.delete()
        return redirect(to='list_shop')
    params = {
            'item':item,
        }
    return render(request, 'shop/delete_shop.html', params)


def delete_stock(request, id_):
    item = Stock.objects.get(id = id_)
    if (request.method == 'POST'):
        item.delete()
        return redirect(to='list_stock')
    params = {
            'item':item,
        }
    return render(request, 'shop/delete_stock.html', params)


def edit_item(request, id_):
    obj = Item.objects.get(id = id_)
    if (request.method == 'POST'):
        form = ItemForm(request.POST, instance=obj)
        form.save()
        return redirect(to='list_item')
    params = {
            'form':ItemForm(instance=obj),
            'id':id_
        }
    return render(request, 'shop/edit_item.html', params)


def edit_shop(request, id_):
    obj = Shop.objects.get(id = id_)
    if (request.method == 'POST'):
        form = ItemForm(request.POST, instance=obj)
        form.save()
        return redirect(to='list_shop')
    params = {
            'form':ShopForm(instance=obj),
            'id':id_,
        }
    return render(request, 'shop/edit_shop.html', params)


def edit_stock(request, id_):
    obj = Stock.objects.get(id = id_)
    if (request.method == 'POST'):
        form = StockForm(request.POST, instance=obj)
        form.save()
        return redirect(to='list_stock')
    params = {
            'form':StockForm(instance=obj),
            'id':id_
        }
    return render(request, 'shop/edit_stock.html', params)