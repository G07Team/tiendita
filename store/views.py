from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
import json
from datetime import date
from .models import *
from .utils import cookieCart, cartData, guestOrder
from .service import get_products, save_pedido
import random
import requests

def store(request):
    print(request)
    data = cartData(request)
    print('data')
    print(data)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    products = get_products()
    list_products = products['productos']

    context = {'products': list_products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)


def cart(request):
    data = cartData(request)
    print("data")
    print(data)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    subtotal = order['get_cart_total']
    igv = subtotal * 0.18
    total = subtotal + igv
    num_random = str(random.random())
    context = {'items': items, 'order': order, 'cartItems': cartItems,
               'subtotal': subtotal, 'igv': igv, 'total': total, 'num_random': num_random}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    print("data")
    print(data)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    # transaction_id = datetime.datetime.now().timestamp()
    # data = json.loads(request.body)
    print('request in processOrder')
    today = date.today()
    # YY-mm-dd
    today_date = today.strftime("%Y-%m-%d")

    cart = json.loads(request.COOKIES['cart'])
    list_products = []
    list_qtys = []
    for i in cart:
    # We use try block to prevent items in cart that may have been removed from causing error
        list_products.append(i)
        list_qtys.append(cart[i]['quantity'])

    pedido = {'cod_pedido': request.POST['cod_pedido'],
              'fecha': today_date,
              'nombre_cli': request.POST['nombre_cli'],
              'ruc_cli': request.POST['ruc_cli'],
              'direccion_cli': request.POST['direccion_cli'],
              'telefono_cli': request.POST['telefono_cli'],
              'product': list_products,
              'qty': list_qtys,
              'monto_bruto': request.POST['monto_bruto'],
              'descuento': request.POST['descuento'],
              'monto_neto': request.POST['monto_neto']}
    print(pedido)
    result = save_pedido(pedido)
    print(result.content)
    cartItems = 0
    products = get_products()
    list_products = products['productos']
    context = {'products': list_products, 'cartItems': cartItems, "alert": True}
    response = render(request, 'store/store.html', context)
    response.delete_cookie('cart')
    return response