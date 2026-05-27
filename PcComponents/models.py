from django.db import models


class Productos(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to="productos/", null=True, blank=True)

    def __str__(self):
        return self.name


class Contacto(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    productos = models.ForeignKey(
        Productos,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
        related_name="mensaje",
    )

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = "mensaje"
