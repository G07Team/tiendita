import requests

URL_API = 'http://localhost/sigepe/public/api'
URI_PRODUCTOS = '/productos'
URI_PRODUCTO_BY_ID = '/producto_details'
URI_PEDIDOS = '/pedidos'

def get_products():
    url = URL_API + URI_PRODUCTOS
    r = requests.get(url)
    productos = r.json()
    return productos


def get_product_by_id(id):
    url = URL_API + URI_PRODUCTO_BY_ID + '/'+ id
    r = requests.get(url)
    producto = r.json()
    producto_details = producto['producto']
    return producto_details

def save_pedido(data_to_save):

    url = URL_API + URI_PEDIDOS
    headers = {'Accept': "application/json"}

    x = requests.post(url, json=data_to_save, headers=headers)
    x.cookies.clear()
    return x
