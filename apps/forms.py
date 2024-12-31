from django.forms import ModelForm

from apps.models import *


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class SizeForm(ModelForm):
    class Meta:
        model = Size
        fields = '__all__'


class SocialMediaForm(ModelForm):
    class Meta:
        model = Social_Media
        fields = '__all__'


class About_UsForm(ModelForm):
    class Meta:
        model = About_Us
        fields = '__all__'


class BeautyCategoryForm(ModelForm):
    class Meta:
        model = BeautyCategory
        fields = '__all__'


class BeautySalonForm(ModelForm):
    class Meta:
        model = BeautySalon
        fields = '__all__'
