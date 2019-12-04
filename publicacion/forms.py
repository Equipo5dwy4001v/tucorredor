from django import forms
from .models import Galeria, Cliente, Inmueble, Propietario, Region, Direccion, TipoInmueble, Requisito, BitacoraContactos

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ('nombre', 'apellidos', 'rut', 'dv', 'movil', 'fijo')

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion 
        fields = ('calle', 'numero', 'detalle', 'codigo_postal', 'region','provincia','comuna','sector' )

class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ('propietario','tipo_inmueble')

class TipoInmuebleForm(forms.ModelForm):
    tipo = forms.ModelChoiceField(queryset=TipoInmueble.objects.all())

    class Meta:
      model = TipoInmueble
      fields = ('tipo',)

class RequisitoForm(forms.ModelForm):
    class Meta:
        model = Requisito
        fields = ('descripcion', 'cantidad', 'obligatorio','inmueble')

class GaleriaForm(forms.ModelForm):
    class Meta:
        model = Galeria 
        fields = ('inmueble', 'tipo_contenido', 'contenido')

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente        
        fields = ('nombre', 'apellidos', 'email','movil','fijo')
        second_model = TipoInmueble
        second_fields = ('descripcion',)

#class BitacoraContactosForm(forms.ModelForm):
#    class Meta:
#        model = BitacoraContactos
 #       fields = ('inmueble', 'cliente', 'consulta'
