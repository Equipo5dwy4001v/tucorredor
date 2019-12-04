from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.views.generic import CreateView, TemplateView, ListView
from django.contrib.auth.views import LoginView, LogoutView

class SignOutView(LogoutView):
    pass

from .models import Perfil
from .forms import SignUpForm


class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

class BienvenidaView(TemplateView):
   template_name = 'perfiles/bienvenida.html'

class SignInView(LoginView):
    template_name = 'perfiles/iniciar_sesion.html'

class SignOutView(LogoutView):
    template_name = 'perfiles/bienvenida.html'

class BuscarView(TemplateView):
    template_name = 'busqueda/resultadoBusqueda.html'

    def post(self, request,*args, **kwargs):
        buscar = request.POST['b']
        print (buscar)
        return render(request,'busqueda/resultadoBusqueda.html')

