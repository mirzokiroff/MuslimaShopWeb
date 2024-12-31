from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from apps.models import Category, Product, Social_Media, About_Us, Order, BeautySalon


def base(request):
    about_us = About_Us.objects.all()

    return render(request, 'base.html', {'about': about_us})


def home(request):
    categories = Category.objects.all()
    men_category = Category.objects.get(name="Erkaklar")
    women_category = Category.objects.get(name="Ayollar")
    kids_category = Category.objects.get(name="Bolalar")

    men_products = Product.objects.filter(category=men_category)
    women_products = Product.objects.filter(category=women_category)
    kids_products = Product.objects.filter(category=kids_category)

    social_media = Social_Media.objects.all()
    about_us = About_Us.objects.all()

    return render(request, 'index.html', {
        'men_products': men_products,
        'women_products': women_products,
        'kids_products': kids_products,
        'categories': categories,
        'social_media': social_media,
        'about_us': about_us,
    })


def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products.html', {'page_obj': page_obj, 'products': products})


def women_products(request):
    women_category = Category.objects.get(name="Ayollar")
    women_products = Product.objects.filter(category=women_category)
    paginator = Paginator(women_products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'women-product.html', {'women_products': women_products, 'page_obj': page_obj})


def men_products(request):
    men_category = Category.objects.get(name="Erkaklar")
    men_products = Product.objects.filter(category=men_category)
    paginator = Paginator(men_products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'men-product.html', {'men_products': men_products, 'page_obj': page_obj})


def kids_products(request):
    kids_category = Category.objects.get(name="Bolalar")
    kids_products = Product.objects.filter(category=kids_category)
    paginator = Paginator(kids_products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'kids-product.html', {'kids_products': kids_products, 'page_obj': page_obj})


def accessories_products(request):
    accessories_category = Category.objects.get(name="Aksessuarlar")
    accessories_products = Product.objects.filter(category=accessories_category)
    paginator = Paginator(accessories_products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'accessories-product.html',
                  {'accessories_products': accessories_products, 'page_obj': page_obj})


def single_product(request, id):
    product = Product.objects.get(id=id)
    images = product.images.all()  # Bog'langan barcha rasmlarni olish
    return render(request, 'single-product.html', {'product': product, 'images': images})


def contact_us(request):
    about_us_info = About_Us.objects.all()
    social_media = Social_Media.objects.all()
    return render(request, 'contact.html', {'social_media': social_media, "about_us": about_us_info})


def about_us(request):
    about_us_info = About_Us.objects.all()
    social_media = Social_Media.objects.all()
    return render(request, 'about.html', {'about_us': about_us_info, 'social_media': social_media})


def order_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        quantity = request.POST.get('quantity')
        product_id = request.POST.get('product_id')
        selected_size = request.POST.get('selected_size', '').strip()
        selected_image = request.POST.get('selected_image', None)  # Agar qiymat bo'lmasa, None qaytadi
        print(selected_image)

        if not selected_size:  # Agar hajm tanlanmasa, foydalanuvchiga xato ko'rsatish
            messages.error(request, 'Mahsulot hajmini tanlang!')
            return HttpResponseRedirect(reverse('single_product', args=[product_id]))

        product = Product.objects.get(id=product_id)
        product_price = product.price
        total_price = int(quantity) * float(product_price)

        if not selected_image:
            selected_image = product.image.url if product.image else 'media/products/bkiyim.jpg'

        print(selected_image)


        if  selected_image:
            selected_image = selected_image.replace(f'{selected_image}', f'http://muslimashop.uz{selected_image}')
            print("aaa")
            print(selected_image)

        # Order modeliga buyurtmani saqlash
        order = Order.objects.create(
            name=name,
            phone=phone,
            product=product,
            quantity=quantity,
            size=selected_size
        )

        # Admin emailiga xabar yuborish
        html_content = f"""
            <h2>Zakaz ma'lumotlari</h2>
            <p><strong>Buyurtmachi:</strong> {name}</p>
            <p><strong>Telefon:</strong> {phone}</p>
            <p><strong>Mahsulot Nomi:</strong> {product.name}</p>
            <p><strong>Mahsulot ID:</strong> {product_id}</p>
            <p><strong>Soni:</strong> {quantity} ta</p>
            <p><strong>Tanlangan Hajm:</strong> {selected_size}</p>
            <p><strong>Mahsulot Narxi:</strong> {product.price} {product.price_type}</p>
            <p><strong>Jami Narx:</strong> {total_price} {product.price_type}</p>
            <p><strong>Tanlangan Rasm:</strong></p>
            <img src="{selected_image}" alt="Selected Product Image" style="max-width: 100%;">
            <br>
            <button><strong><a href="{selected_image}">ustiga bosing</a></strong></button>
        """
        print(selected_image)

        # Emailni yuborish
        email = EmailMessage(
            subject=f'ZAKAZ: {product.name}',
            body=html_content,
            from_email='mirsidiq3421@gmail.com',
            to=['mirsiddiqmirzokirov@gmail.com'],
        )
        email.content_subtype = "html"  # HTML formatni belgilash
        email.send(fail_silently=False)
        # Muvaffaqiyatli xabarni foydalanuvchiga ko'rsatish
        messages.success(request, 'Buyurtma muvaffaqiyatli yuborildi!')
        return HttpResponseRedirect(reverse('single_product', args=[product.id]))
    else:
        return redirect('home')


def beauty_salon(request):
    beauty_salon = BeautySalon.objects.all()
    about_us = About_Us.objects.all()
    social_media = Social_Media.objects.all()
    return render(request, 'beauty-salon.html', {'about': about_us, 'social_media': social_media,
                                                 'beauty_salon': beauty_salon})
