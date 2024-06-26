from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.models import User
# from .models import Receipt, Category


# class ReceiptForm(forms.ModelForm):
#     class Meta:
#         model = Receipt
#         fields = ['name', 'category', 'description', 'steps', 'time', 'photo']
#
#
#
# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = ['name', 'description', 'photo']
#
#     def clean_name(self):
#         name = self.cleaned_data.get('name')
#         name_lower = name.lower()
#         if Category.objects.filter(name__iexact=name_lower).exists():
#             raise forms.ValidationError("This category name already exists.")
#         return name
#
#
# class RecipeSearchForm(forms.Form):
#     search_query = forms.CharField(label='Search', max_length=100)