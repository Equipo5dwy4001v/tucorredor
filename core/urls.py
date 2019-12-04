"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from perfiles.views import SignUpView, BienvenidaView, SignInView, SignOutView, BuscarView
from . import views

from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('publicaciones/', include('publicacion.urls')),
    # urls para inicio de secion 
    url(r'^incia-sesion/$', SignInView.as_view(), name='sign_in'),
    url(r'^$', BienvenidaView.as_view(), name='bienvenida'),
    url(r'^registrate/$', SignUpView.as_view(), name='sign_up'),
    url(r'^cerrar-sesion/$', SignOutView.as_view(), name='sign_out'),
    #urls para barra de busqueda
    url(r'^busqueda/$', BuscarView.as_view(), name='resultadoBusqueda'),
    #urls para reseteo de clave
    url(r'^reseteo/reseteopassword$',PasswordResetView,{'template_name':'recuperacion/Form.html',
        'email_template_name':'recuperacion/mail.html'},name='password_reset'),
    url(r'^reseteo/reseteohecho$',PasswordResetDoneView,{'template_name':'recuperacion/hecho.html'},name='password_done'),
    url(r'^reseteo/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',PasswordResetConfirmView,{'template_name':'recuperacion/confirmacion.html'},name='password_confirm'),
    url(r'^reseteo/completo$',PasswordResetCompleteView,{'template_name':'recuperacion/completo.html'},name='password_complete'),
]
