from django.db import models

# Noticias
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='noticias/', null=True, blank=True)

    def __str__(self):
        return self.titulo


# Jugadoras
class Jugadora(models.Model):
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='jugadoras/', null=True, blank=True)

    def __str__(self):
        return self.nombre



# Entrenadores
class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='entrenadores/', null=True, blank=True)

    def __str__(self):
        return self.nombre


# Directiva
class Directivo(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='directiva/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.cargo}"


# Torneos
class Torneo(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField(null=True, blank=True)
    fechaend = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to='torneos/', null=True, blank=True)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    pos1 = models.CharField(max_length=100, blank=True, null=True)
    pos2 = models.CharField(max_length=100, blank=True, null=True)
    pos3 = models.CharField(max_length=100, blank=True, null=True)
    ultimocampeon = models.CharField(max_length=100, blank=True, null=True)
    formato = models.TextField(blank=True, null=True)
    equipos = models.TextField(blank=True, null=True)
    sedes = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.titulo


# Galería
class Galeria(models.Model):
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='galeria/')
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo


# Eventos del Calendario
class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.DateField()
    lugar = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.titulo} ({self.fecha})"


# Enlaces
class Enlace(models.Model):
    titulo = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.titulo


# Historia editable
class Historia(models.Model):
    contenido = models.TextField()

    def __str__(self):
        return "Sección de Historia"

class Productos(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        return self.nombre