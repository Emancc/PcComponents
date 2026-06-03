from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("productos/", views.productos, name="productos"),
    path("about/", views.about, name="about"),
    path(
        "crear_contacto/<int:producto_id>/", views.crear_contacto, name="crear_contacto"
    ),
    path("editar_contacto/<int:id>/", views.editar_contacto, name="editar_contacto"),
    path(
        "eliminar_contacto/<int:id>/", views.eliminar_contacto, name="eliminar_contacto"
    ),
    path("crear_producto/", views.crear_producto, name="crear_producto"),
]
