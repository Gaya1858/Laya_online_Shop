from django.urls import path
from . import views

app_name = 'shop'

urlpatterns =[

    path('', views.home_page, name='home_page'),
    path('list.html', views.product_list, name='product_list'),
    path('about.html', views.about_page, name='about'),
    path('contact.html', views.contact_page, name='contact'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]