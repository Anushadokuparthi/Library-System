from datetime import datetime
from random import random
from secrets import choice
from sys import prefix
from unicodedata import category
from django import forms
from numpy import require
from lmsApp import models
import datetime

class SaveCategory(forms.ModelForm):
    name = forms.CharField(max_length=250)
    description = forms.Textarea()
    status = forms.CharField(max_length=2)

    class Meta:
        model = models.Category
        fields = ('name', 'description', 'status', )

    def clean_name(self):
        id = self.data['id'] if (self.data['id']).isnumeric() else 0
        name = self.cleaned_data['name']
        try:
            if id > 0:
                category = models.Category.objects.exclude(id = id).get(name = name, delete_flag = 0)
            else:
                category = models.Category.objects.get(name = name, delete_flag = 0)
        except:
            return name
        raise forms.ValidationError("Category Name already exists.")

class SaveSubCategory(forms.ModelForm):
    category = forms.CharField(max_length=250)
    name = forms.CharField(max_length=250)
    description = forms.Textarea()
    status = forms.CharField(max_length=2)

    class Meta:
        model = models.SubCategory
        fields = ('category', 'name', 'description', 'status', )

    def clean_category(self):
        cid = int(self.data['category']) if (self.data['category']).isnumeric() else 0
        try:
            category = models.Category.objects.get(id = cid)
            return category
        except:
            raise forms.ValidationError("Invalid Category.")

    def clean_name(self):
        id = int(self.data['id']) if (self.data['id']).isnumeric() else 0
        cid = int(self.data['category']) if (self.data['category']).isnumeric() else 0
        name = self.cleaned_data['name']
        try:
            category = models.Category.objects.get(id = cid)
            if id > 0:
                sub_category = models.SubCategory.objects.exclude(id = id).get(name = name, delete_flag = 0, category = category)
            else:
                sub_category = models.SubCategory.objects.get(name = name, delete_flag = 0, category = category)
        except:
            return name
        raise forms.ValidationError("Sub-Category Name already exists on the selected Category.")
     
class SaveBook(forms.ModelForm):
    sub_category = forms.CharField(max_length=250)
    isbn = forms.CharField(max_length=250)
    title = forms.CharField(max_length=250)
    description = forms.Textarea()
    author = forms.Textarea()
    publisher = forms.Textarea()
    date_published = forms.DateField()
    status = forms.CharField(max_length=2)

    class Meta:
        model = models.Books
        fields = ('isbn', 'sub_category', 'title', 'description', 'author', 'publisher', 'date_published', 'status', )

    def clean_sub_category(self):
        scid = int(self.data['sub_category']) if (self.data['sub_category']).isnumeric() else 0
        try:
            sub_category = models.SubCategory.objects.get(id = scid)
            return sub_category
        except:
            raise forms.ValidationError("Invalid Sub Category.")

    def clean_isbn(self):
        id = int(self.data['id']) if (self.data['id']).isnumeric() else 0
        isbn = self.cleaned_data['isbn']
        try:
            if id > 0:
                book = models.Books.objects.exclude(id = id).get(isbn = isbn, delete_flag = 0)
            else:
                book = models.Books.objects.get(isbn = isbn, delete_flag = 0)
        except:
            return isbn
        raise forms.ValidationError("ISBN already exists on the Database.")
  
