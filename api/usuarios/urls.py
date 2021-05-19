from django.urls import path
from usuarios import views


urlpatterns = [
    path('bienvenida/', views.welcome, name='bienvenida'),
    path('registrarse/', views.register, name='register'),
    path('iniciar-sesion/', views.login, name='login'),
    path('cerrar-sesion/', views.logout, name='logout'),
]    
