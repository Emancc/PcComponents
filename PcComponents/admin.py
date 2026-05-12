from django.contrib import admin
from .models import Contacto, Productos


# Register your models here.
@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "stock",
    )

    list_filter = ("name", "stock")
    search_fields = ("name",)


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "mensaje", "productos")
