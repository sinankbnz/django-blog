from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('make/',views.make,name='make'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('read/<int:id>/', views.read, name='read'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('register/',views.register,name='register'),
    
]