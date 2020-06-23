from django.db import models

# Create your models here.

class Link(models.Model):
    # obliga a usar caracteres alfanumericos, guiones o barras y no permite caracteres especiales o espacios. ideal para clave a forma de registro
    key = models.SlugField(verbose_name="Nombnre clave",max_length=100, unique=True)
    name = models.CharField(max_length=200, verbose_name="Red social")
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "enlaces"
        verbose_name_plural = "enlaces"
        ordering = ['name']

    def __str__(self):
        return self.name
