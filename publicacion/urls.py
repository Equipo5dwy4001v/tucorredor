from django.urls import path
from . import views

urlpatterns = [
    path('propiedades/listar', views.listar_galeria, name='listar_galeria'),
    #path('/propietario/nuevo', views.PropiedadCrear, name='propietario_nuevo'),
    #path('/propiedades/nuevo', views.DireccionCrear, name='propiedades_nuevo'),
    path('propiedades/nuevo', views.direccion_nuevo, name='propiedades_nuevo'),
    path('propietario/nuevo', views.propietario_nuevo, name='propietario_nuevo'),
    path('propietario/<int:pk>/editar', views.propietario_editar, name='propietario_editar'),
    path('propietario/<int:pk>/eliminar', views.propietario_eliminar, name='propietario_eliminar'),
    path('propiedades/otros', views.InmuebleNuevo, name='inmueble_nuevo'),
    path('propiedades/<int:pk>/requisitos', views.Nuevo, name='requisito_nuevo'),
    path('propiedades/listado', views.listar_direcciones, name='direccion_list'),
    path('propietario/listado', views.listar_propietarios, name="propietario_list"),
    path('cliente/nuevo', views.cliente_nuevo, name='cliente_nuevo'),
]