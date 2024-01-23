from django.db import models

# Create your models here.

class Ciudad(models.Model):

    nombre_ciudad = models.CharField(max_length=30)
    anio_fundacion = models.IntegerField(blank=True, null=True)
    num_parques = models.IntegerField(blank=True, null=True)
    num_monumentos = models.IntegerField(blank=True, null=True)
    presupuesto_anual = models.FloatField(null=True, blank=True)
    clima = models.CharField(max_length=30)

    def __str__(self):
        return "%s %d %d %d %f %s" % (self.nombre_ciudad,
            self.anio_fundacion,
            self.num_parques,
            self.num_monumentos,
            self.presupuesto_anual,
            self.clima)

class Parroquia(models.Model):
    nombre_parroquia = models.CharField(max_length=30)    
    distrito = models.CharField(max_length=30)
    anio_creacion = models.IntegerField(blank=True, null=True)
    num_barrios = models.IntegerField(blank=True, null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - Distrito: %s - Fundación: %d - %d barrios" % (self.nombre_parroquia,
            self.distrito,
            self.anio_creacion,
            self.num_barrios)
        

