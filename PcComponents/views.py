from django.shortcuts import render, redirect, get_object_or_404
from .models import Productos, Contacto
from .forms import ContactoForm, ProductForm


# Create your views here.
def index(request):
    return render(request, "PcComponents/index.html")


def productos(request):
    productos = Productos.objects.all().order_by("-id")
    return render(request, "PcComponents/productos.html", {"productos": productos})


def about(request):
    return render(request, "PcComponents/about.html")


def crear_contacto(request, producto_id):
    producto = get_object_or_404(Productos, id=producto_id)

    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            reseña = form.save(commit=False)
            reseña.productos = producto
            reseña.save()
            return redirect("productos")
    else:
        form = ContactoForm()

    return render(
        request,
        "PcComponents/crear_contacto.html",
        {"form": form, "producto": producto},
    )


def editar_contacto(request, id):

    contacto = get_object_or_404(Contacto, id=id)

    if request.method == "POST":
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect("productos")
    else:

        form = ContactoForm(instance=contacto)
    return render(request, "PcComponents/editar_contacto.html", {"form": form})


def eliminar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)

    if request.method == "POST":
        contacto.delete()
        return redirect("productos")
    return render(
        request, "PcComponents/eliminar_contacto.html", {"contacto": contacto}
    )


def crear_producto(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("productos")
    else:
        form = ProductForm()
    return render(request, "PcComponents/crear_producto.html", {"form": form})
