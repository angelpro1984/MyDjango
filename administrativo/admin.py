from django.contrib import admin

# Register your models here.

from administrativo.models import Ciudad, Parroquia

# Para administrar desde
# la interfaz de adminisración
# Agregar la clase Ciudad
#admin.site.register(Ciudad)

# Agregar la clase Parroquia

# Clase que hereda de Model Admin
class CiudadAdmin(admin.ModelAdmin):
    list_display =('nombre_ciudad','anio_fundacion')
    search_fields = ('nombre_ciudad', 'clima')
admin.site.register(Ciudad, CiudadAdmin)


#admin.site.register(Parroquia)

class ParroquiaAdmin(admin.ModelAdmin):
    list_display=('nombre_parroquia','num_barrios')

    raw_id_fields =('ciudad',)

admin.site.register(Parroquia, ParroquiaAdmin)