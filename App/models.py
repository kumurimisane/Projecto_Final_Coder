from django.db import models

# Create your models here.

class Cartas (models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    elegir_nivel =  (
        ('0', 'Ninguna'),
        ('1', '✪'),
        ('2', '✪✪'),
        ('3', '✪✪✪'),
        ('4', '✪✪✪✪'),
        ('5', '✪✪✪✪✪'),
        ('6', '✪✪✪✪✪✪'),
        ('7', '✪✪✪✪✪✪✪'),
        ('8', '✪✪✪✪✪✪✪✪'),
        ('9', '✪✪✪✪✪✪✪✪✪'),
        ('10', '✪✪✪✪✪✪✪✪✪✪'),
        ('11', '✪✪✪✪✪✪✪✪✪✪✪'),
        ('12', '✪✪✪✪✪✪✪✪✪✪✪✪'),
    )
    nivel = models.CharField(max_length=50, choices= elegir_nivel)
    ataque = models.CharField(max_length=5)
    defensa = models.CharField(max_length=5)
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='cartas/', null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} - {self.tipo} - {self.nivel} - {self.ataque} -{self.defensa} - {self.descripcion}'
    

class Mazo (models.Model):
    
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    carta_principal = models.CharField(max_length=50)
    cantidad_de_cartas = models.IntegerField()
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='mazo/', null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} - {self.tipo} - {self.carta_principal} - {self.cantidad_de_cartas} - {self.descripcion}'

class Torneo (models.Model):
    nombre_torneo = models.CharField(max_length=50)
    cantidad_participantes = models.IntegerField()
    lugar_del_torneo = models.CharField(max_length=50)
    premio = models.CharField(max_length=50)
    codigo_de_torneo = models.IntegerField()
    imagen = models.ImageField(upload_to='torneo/', null=True, blank=True)

    def __str__(self):
        return f'{self.nombre_torneo} - {self.cantidad_participantes} - {self.lugar_del_torneo} - {self.premio} - {self.codigo_de_torneo}'

class Contacto (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    mensaje = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} - {self.apellido} - {self.email} - {self.mensaje}'