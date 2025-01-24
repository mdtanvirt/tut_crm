
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('client/<int:pk>', views.client, name='client'),
    path('client_delete/<int:pk>', views.client_delete, name='client_delete'),
    path('add_client/', views.add_client, name='add_client'),
    path('client_update/<int:pk>', views.client_update, name='client_update'),
    path('client/orders/<int:client_pk>/', views.orders, name='orders'),
    path('client/new_order/<int:client_pk>/', views.new_order, name='new_order'),
    path('client/service/<int:client_pk>/', views.service, name='service'),
    path('client/new_service/<int:client_pk>/', views.new_service, name='new_service'),
    path('client/product/<int:client_pk>/', views.product, name='product'),
    path('client/new_product/<int:client_pk>/', views.new_product, name='new_product'),
    path('export_csv/', views.export_csv, name='export_csv'),
    path('export_pdf/', views.export_pdf, name='export_pdf'),
]
