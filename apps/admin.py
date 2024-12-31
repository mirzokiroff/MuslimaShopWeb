from django.contrib import admin

from apps.forms import CategoryForm, SocialMediaForm, About_UsForm, BeautyCategoryForm, BeautySalonForm
from apps.models import Category, Product, Social_Media, About_Us, Size, BeautyCategory, \
    BeautySalon, ProductImage


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm


class SocialMediaAdmin(admin.ModelAdmin):
    form = SocialMediaForm


class AboutUsAdmin(admin.ModelAdmin):
    form = About_UsForm


# class PortfolioImageInline(admin.TabularInline):
#     model = PortfolioImage
#     fields = ['image']
#     extra = 3
#
#
# class PortfolioInfoAdmin(admin.ModelAdmin):
#     form = PortfolioDetailsForm
#     list_display = ('name', 'category', 'client', 'project_date', 'project_url')
#     inlines = [PortfolioImageInline]


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('name', 'id', 'category', 'formatted_price', 'date')
    filter_horizontal = ('sizes',)
    readonly_fields = ('number', 'date')


class SizeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BeautyCategoryAdmin(admin.ModelAdmin):
    form = BeautyCategoryForm


class BeautySalonAdmin(admin.ModelAdmin):
    form = BeautySalonForm


admin.site.register(Category, CategoryAdmin)
admin.site.register(Social_Media, SocialMediaAdmin)
admin.site.register(About_Us, AboutUsAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(BeautyCategory, BeautyCategoryAdmin)
admin.site.register(BeautySalon, BeautySalonAdmin)
