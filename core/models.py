from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    # Ejemplo: 'Ramos', 'Cajas de Rosas', 'Funerarios'
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre

class ArregloFloral(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='arreglos/')
    
    # Campos específicos para "Bajo Pedido"
    tiempo_preparacion = models.CharField(max_length=100, help_text="Ej: 24 horas de anticipación")
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    # Método para generar el link de WhatsApp automáticamente
    @property
    def whatsapp_link(self):
        telefono = "593999254571" # El número de tu mamá con código de país
        mensaje = f"Hola, me interesa el arreglo: {self.nombre}"
        return f"https://wa.me/{593999254571}?text={mensaje.replace(' ', '%20')}"