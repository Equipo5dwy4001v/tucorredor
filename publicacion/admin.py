from django.contrib import admin
from .models import Region, Provincia, Comuna, Sector, TipoInmueble, Propietario, Inmueble, Direccion, TipoContenido, Galeria, Anuncio, Requisito, Cliente, BitacoraContactos

# Register your models here.
admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)
admin.site.register(TipoInmueble)
admin.site.register(Sector)

@admin.register(Propietario)
class PropietarioAdmin(admin.ModelAdmin):
    list_display = ( 'nombre', 'apellidos', 'rut', 'dv', 'movil', 'fijo')

@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('tipo_inmueble' , 'propietario')


@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ( 'calle', 'numero', 'detalle', 'codigo_postal', 'region', 'provincia', 'comuna', 'sector')


admin.site.register(TipoContenido)
admin.site.register(Galeria)
admin.site.register(Anuncio)
admin.site.register(Requisito)
admin.site.register(Cliente)
admin.site.register(BitacoraContactos)