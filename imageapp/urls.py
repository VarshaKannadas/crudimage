from django.urls import path
from .import views
urlpatterns=[
    path('',views.index,name='index'),
    path('add_product',views.add_product,name='add_product'),
    path('show_product',views.show_product,name='show_product'),
    
   path('editpage/<int:pk>/', views.editpage, name='editpage'),
   path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
   path('delete/<int:pk>/', views.delete, name='delete'),


]