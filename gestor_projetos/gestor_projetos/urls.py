"""gestor_projetos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from pessoas import urls as urls_pessoas
from home import urls as urls_home
from projetos import urls as urls_proj

urlpatterns = [
    path('', include(urls_home)),
    path('admin/', admin.site.urls),
    path('login/', auth_views.login, name='login'),
    path('pessoas/', include(urls_pessoas)),
    path('proj/', include(urls_proj), name='proj'),

]
