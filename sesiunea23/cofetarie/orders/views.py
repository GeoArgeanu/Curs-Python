from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from orders.models import Order, OrderItem
from products.models import Product
from django.views.generic import TemplateView


# Create your views here.

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order_item, created = OrderItem.objects.get_or_create(product=product, user=request.user, ordered=False)
    order = Order.get_current_order(request.user)
    if order:
        if order.items.filter(product__id=product_id).exists():
            order.item.quantity += 1
            order_idem.save()
        else:
            order.item.add(order_item)

    else:
        order = Order.objects.create(user=request.user)
        order.items.add(order_item)
    return redirect('products:products')


class CartView(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        current_order = Order.get_current_order(self.request.user)
        total_price = current_order.total_price()
        shipping = 15
        return {
            'orders': current_order,
            'total_price': total_price,
            'shipping_tax': shipping,
            'total_price_with_shipping': total_price + shipping
        }
