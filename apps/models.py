from django.db import models
from django.db.models import CharField, ImageField, PositiveIntegerField, DateTimeField, TextField, Model, ForeignKey, \
    CASCADE, BooleanField, URLField, ManyToManyField


class Category(Model):
    name = CharField(verbose_name='Kategoriya Nomi', max_length=128)
    image = ImageField(verbose_name='Kategoriya Rasmi', upload_to='category/')
    description = TextField(verbose_name='Kategoriya Haqida qisqacha', blank=True, null=True)
    date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Size(Model):
    name = CharField(max_length=10, verbose_name='Mahsulot (Kiyim) Hajmi', null=True, blank=True)
    size_shoes = PositiveIntegerField(verbose_name='Mahsulot (Oyoq Kiyim) Hajmi', null=True, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        elif self.size_shoes:
            return str(self.size_shoes)
        return "Noma'lum hajm"


class Product(Model):
    PRICE_TYPES = (
        ("uzs", "UZS"),
        ('$', '$'),
    )

    category = ForeignKey(Category, verbose_name='Mahsulot Kategoriyasi', on_delete=CASCADE)
    name = CharField(verbose_name='Mahsulot Nomi', max_length=128)
    price = PositiveIntegerField(verbose_name='Mahsulot Narxi', default=0)
    price_type = CharField(verbose_name='Mahsulot Narxi Turi', choices=PRICE_TYPES, max_length=4)
    image = ImageField(verbose_name='Mahsulot Rasmi', upload_to='products/', blank=True, null=True)
    date = DateTimeField(auto_now_add=True)
    number = PositiveIntegerField(default=0)
    sizes = ManyToManyField(Size, verbose_name='Mahsulot Hajmlari', blank=True)

    def __str__(self):
        return f"{self.id} {self.category} bo'limida --> {self.name}"

    def formatted_price(self):
        return f"{self.price} {self.get_price_type_display()}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='Mahsulot Rasmi')
    image = models.ImageField(upload_to='products/', verbose_name='Mahsulot Qo\'shimcha Rasmi')

    def __str__(self):
        return f"Image for {self.product.name} {self.product.id} {self.product.category}"



class Social_Media(Model):
    image = ImageField(verbose_name='Ijtimoiy Tarmoq rasmi', upload_to='social_media/', blank=True, null=True)
    name = CharField(verbose_name='Ijtimoiy Tarmoq nomi', max_length=128, blank=True, null=True)
    url = URLField(verbose_name='Ijtimoiy Tarmoq url', blank=True, null=True)
    date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class About_Us(Model):
    shop_address = CharField(verbose_name="Do'kon Manzili", max_length=222, blank=True, null=True)
    work_time = CharField(verbose_name="Do'kon Ishlash Vaqti", max_length=128, blank=True, null=True)
    phone = CharField(verbose_name="Do'kon Raqami", max_length=128, blank=True, null=True)
    email = CharField(verbose_name="Do'kon Pochtsi", max_length=128, blank=True, null=True)
    office_address = CharField(verbose_name="Offis Manzili", max_length=222, blank=True, null=True)
    date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shop_address


class Order(Model):
    name = CharField(max_length=100)
    phone = CharField(max_length=20)
    product = ForeignKey(Product, on_delete=CASCADE)
    quantity = PositiveIntegerField()
    created_at = DateTimeField(auto_now_add=True)
    size = CharField(max_length=10)

    def __str__(self):
        return f"Buyurtma: {self.name} - {self.product.name}"


class BeautyCategory(models.Model):
    name = models.CharField(verbose_name='Salon Kategoriya Nomi', max_length=128)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BeautySalon(models.Model):
    PRICE_TYPES = (
        ('uzs', 'UZS'),
        ('usd', 'USD'),
    )
    name = models.CharField(max_length=222, blank=True, null=True, verbose_name='Xizmat Nomi, Agar kerak bo\'lsa')
    category = models.ForeignKey(BeautyCategory, verbose_name='Xizmat Kategoriyasi, Majburiy', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0, blank=True, null=True,
                                        verbose_name='Xizmat Narxi, Agar kerak bo\'lsa')
    price_type = models.CharField(verbose_name='Xizmat Narxi Turi', choices=PRICE_TYPES, max_length=3, blank=True,
                                  null=True)
    image = models.ImageField(verbose_name='Xizmat Rasmi', upload_to='beauty_salon/', blank=True, null=True)
    video = models.FileField(verbose_name='Xizmat Videosi', upload_to='beauty_salon/videos/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
