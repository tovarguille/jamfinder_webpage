from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('local/<int:id>/', views.local_detail, name='local_detail'),
    path('myadmin/', views.admin_view, name='admin_view'),  # Cambia la URL a 'myadmin'
    path('myadmin/add/', views.add_local, name='add_local'),  # Cambia la URL a 'myadmin/add/'
    path('myadmin/delete/<int:id>/', views.delete_local, name='delete_local'),  # Cambia la URL a 'myadmin/delete/<int:id>/'
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.index, name='index'),
]