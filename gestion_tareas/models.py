from django.db import models
from mainapp.models import Usuario

# Create your models here.
class Tarea(models.Model):
    title = models.CharField(max_length=50, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    delivery_at = models.DateTimeField(verbose_name="Entregado el")
    usuario = models.ForeignKey(Usuario, editable=False, verbose_name="Usuario", null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"

    def __str__(self):
        return self.title
