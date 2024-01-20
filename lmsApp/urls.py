from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="home-page"),
    path('home',views.home,name='home-page'),
    path('category',views.category,name='category-page'),
    path('manage_category',views.manage_category,name='manage-category'),
    path('manage_category/<int:pk>',views.manage_category,name='manage-category-pk'),
    path('view_category/<int:pk>',views.view_category,name='view-category-pk'),
    path('save_category',views.save_category,name='save-category'),
    path('delete_category/<int:pk>',views.delete_category,name='delete-category'),
    path('sub_category',views.sub_category,name='sub_category-page'),
    path('manage_sub_category',views.manage_sub_category,name='manage-sub_category'),
    path('manage_sub_category/<int:pk>',views.manage_sub_category,name='manage-sub_category-pk'),
    path('view_sub_category/<int:pk>',views.view_sub_category,name='view-sub_category-pk'),
    path('save_sub_category',views.save_sub_category,name='save-sub_category'),
    path('delete_sub_category/<int:pk>',views.delete_sub_category,name='delete-sub_category'),
    path('books',views.books,name='book-page'),
    path('manage_book',views.manage_book,name='manage-book'),
    path('manage_book/<int:pk>',views.manage_book,name='manage-book-pk'),
    path('view_book/<int:pk>',views.view_book,name='view-book-pk'),
    path('save_book',views.save_book,name='save-book'),
    path('delete_book/<int:pk>',views.delete_book,name='delete-book'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
