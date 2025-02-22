"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls import handler404
from base.views import contacto, departamento,departamento_eliminar, error_404, inicioAdmin, municipio

from base.views import logout_user
from django.contrib.auth.views import LoginView as login

####### Importes para subir imágenes #######
from django.conf import settings
from django.conf.urls.static import static
############################################

handler404= error_404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login.as_view(),name='inicio'),
    path('adm/',inicioAdmin,name='inicio-admin'),
    path('usuarios/',include('usuarios.urls')),
    
    path('productos/',include('productos.urls')),
    path('facturas/',include('facturas.urls')),


    path('extras/municipio',municipio,name='municipio'),
    path('extras/departamento',departamento,name='departamento'),
    path('extras/departamento/eliminar/<int:pk>/',departamento_eliminar,name='departamento_eliminar'),

    path('contacto/',contacto,name="contacto"),

    # path('loggedin/',loggedIn,name="inicio-sesion"),
    path('logout/',logout_user,name="logout"),

    path("select2/", include("django_select2.urls")),

]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
