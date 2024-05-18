from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', views.admin_view, name='admin_view'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('api/locales/', views.locales_api, name='locales_api'),
    path('api/locales/<int:id>/', views.local_detail_api, name='local_detail_api'),
]