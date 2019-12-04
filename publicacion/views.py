from django.shortcuts import render, redirect, get_object_or_404
from .models import Galeria, Propietario, Region, Direccion, Comuna, Provincia, Sector, Inmueble, TipoInmueble                   
from .forms import PersonaForm, DireccionForm, TipoInmuebleForm, GaleriaForm, InmuebleForm, RequisitoForm, ClienteForm
from django.views.generic import CreateView, ListView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.
def listar_direcciones(request):
    direccion = Direccion.objects.all()
    return render(request, 'publicacion/direcciones_list.html', {'direccion': direccion})

def listar_propietarios(request):
    propietario = Propietario.objects.all()
    return render(request, 'publicacion/propietarios_list.html', {'propietario': propietario})

def listar_galeria(request):
    galerias = Galeria.objects.all()
    return render(request, 'publicacion/listar_galeria.html', {'galerias': galerias})

def propietario_nuevo(request):
    form = PersonaForm() 
    if request.method == "POST":
        form = PersonaForm(request.POST)  
        if form.is_valid():
            persona = form.save(commit=False)
            persona.save()
            return redirect('propiedades_nuevo')
        else:
            form = PersonaForm()    
    return render(request, 'publicacion/propietario_nuevo.html', {'form':form})

def propietario_editar(request, pk):
    propietario = get_object_or_404(Propietario, pk=pk)
    if request.method == "POST":
        form = PersonaForm(request.POST, instance=propietario)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.save()
            return redirect('publicacion/listar_galeria.html')
    else:
        form = PersonaForm(instance=propietario)
    return render(request, 'publicacion/propietario_editar.html', {'form':form})

def propietario_eliminar(request, pk):
    propietario = get_object_or_404(Propietario, pk=pk)
    propietario.delete()

def direccion_nuevo(request):
    form_dir = DireccionForm()
    #form2 = TipoInmuebleForm()
    region = Region.objects.all()
    provincia = Provincia.objects.all()
    comuna = Comuna.objects.all()
    sector = Sector.objects.all()    
    if request.method == "POST":
        form_dir = DireccionForm(request.POST)
        #form2 = TipoInmuebleForm(request.POST)
        if form_dir.is_valid():
            direccion = form_dir.save(commit=False)
            direccion.save()
            #tipode = form2.save(commit=False)
            #tipode.save()
            #return redirect('publicacion/listar_galeria.html')
            return redirect('inmueble_nuevo')
        else:
            form_dir = DireccionForm()
            #form2 = TipoInmuebleForm()
    return render(request, 'publicacion/propiedades_nuevo.html', 
                  {'form':form_dir,'region':region, 'provincia':provincia,
                   'comuna': comuna, 'sector': sector})

def InmuebleNuevo(request):
    propietario = Propietario.objects.all()
    tipo = TipoInmueble.objects.all()
    form = InmuebleForm()
    if request.method == "POST":
        form = InmuebleForm(request.POST)  
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.save()
            return redirect('requisito_nuevo', pk=inmueble.pk)
        else:
            form = InmuebleForm() 
    return render(request, 'publicacion/propietario_nuevo.html', {'form':form, 'propietario': propietario, 'tipo_inmueble':tipo})

def Nuevo(request,pk):
    inmueble = get_object_or_404(Inmueble, pk=pk)
    form = RequisitoForm() 
    if request.method == "POST":
        form = RequisitoForm(request.POST, instance=inmueble)  
        if form.is_valid():
            nuevo = form.save(commit=False)
            nuevo.save()
            return redirect('direccion_list')
        else:
            form = RequisitoForm()  
    return render(request, 'publicacion/requisitos.html', {'form':form})

def cliente_nuevo(request):
    form = ClienteForm() 
    direccion = Direccion.objects.all()
    tipo = TipoInmueble.objects.all()
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=tipo)  
        if form.is_valid():
           #direccion = request.direccion.get 
           cliente = form.save(commit=False)
           cliente.save()
           return redirect('bienvenida')
        else:
            form = ClienteForm()  
    return render(request, 'publicacion/cliente.html', {'form':form, 'tipo':tipo,'direccion':direccion})



