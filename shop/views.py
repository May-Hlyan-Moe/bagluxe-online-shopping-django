from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Product, Brand, Category, Cart, CartItem, Order, OrderItem
from accounts.models import User


def home(request):
    featured = Product.objects.filter(is_featured=True, is_active=True)[:6]
    brands = Brand.objects.all()
    new_arrivals = Product.objects.filter(is_active=True).order_by('-created_at')[:8]
    return render(request, 'shop/home.html', {
        'featured': featured,
        'brands': brands,
        'new_arrivals': new_arrivals,
    })


def product_list(request):
    products = Product.objects.filter(is_active=True)
    brands = Brand.objects.all()
    categories = Category.objects.all()

    brand_slug = request.GET.get('brand')
    category_slug = request.GET.get('category')
    query = request.GET.get('q')
    sort = request.GET.get('sort', 'newest')

    if brand_slug:
        products = products.filter(brand__slug=brand_slug)
    if category_slug:
        products = products.filter(category__slug=category_slug)
    if query:
        products = products.filter(Q(name__icontains=query) | Q(brand__name__icontains=query))

    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    else:
        products = products.order_by('-created_at')

    return render(request, 'shop/product_list.html', {
        'products': products,
        'brands': brands,
        'categories': categories,
        'selected_brand': brand_slug,
        'selected_category': category_slug,
        'query': query,
        'sort': sort,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related = Product.objects.filter(brand=product.brand, is_active=True).exclude(id=product.id)[:4]
    return render(request, 'shop/product_detail.html', {'product': product, 'related': related})


def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'shop/brand_list.html', {'brands': brands})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_active=True)
    if not product.is_in_stock():
        messages.error(request, 'Sorry, this item is out of stock.')
        return redirect('shop:product_detail', slug=product.slug)

    cart, _ = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        if item.quantity < product.stock:
            item.quantity += 1
            item.save()
            messages.success(request, f'Updated quantity for {product.name}.')
        else:
            messages.warning(request, 'No more stock available.')
    else:
        messages.success(request, f'{product.name} added to your cart.')
    return redirect('shop:cart')


@login_required
def cart_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    return render(request, 'shop/cart.html', {'cart': cart})


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    item.delete()
    messages.success(request, 'Item removed from cart.')
    return redirect('shop:cart')


@login_required
def update_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    qty = int(request.POST.get('quantity', 1))
    if qty < 1:
        item.delete()
    elif qty <= item.product.stock:
        item.quantity = qty
        item.save()
    return redirect('shop:cart')


@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    if not cart.items.exists():
        messages.warning(request, 'Your cart is empty.')
        return redirect('shop:cart')

    if request.method == 'POST':
        address = request.POST.get('address')
        if not address:
            messages.error(request, 'Please provide a shipping address.')
            return render(request, 'shop/checkout.html', {'cart': cart})

        order = Order.objects.create(
            user=request.user,
            shipping_address=address,
            total_price=cart.get_total(),
        )
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                product_name=item.product.name,
                price=item.product.price,
                quantity=item.quantity,
            )
            item.product.stock -= item.quantity
            item.product.save()
        cart.items.all().delete()
        messages.success(request, f'Order #{order.id} placed successfully!')
        return redirect('shop:order_detail', order_id=order.id)

    return render(request, 'shop/checkout.html', {'cart': cart})


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'shop/order_list.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'shop/order_detail.html', {'order': order})


@login_required
def seller_dashboard(request):
    if not request.user.is_seller() and not request.user.is_staff:
        messages.error(request, 'Access denied.')
        return redirect('shop:home')
    products = Product.objects.all().order_by('-created_at')
    orders = Order.objects.all().order_by('-created_at')[:10]
    buyers = User.objects.filter(role='buyer').count()
    return render(request, 'shop/seller_dashboard.html', {
        'products': products,
        'orders': orders,
        'buyers': buyers,
    })
