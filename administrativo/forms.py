from django.forms import ModelForm
from administrativo.models import Parroquia


class ParroquiaForm(ModelForm): 
    class Meta:
        model = Parroquia 
        fields = ['nombre_parroquia', 'distrito',
                  'anio_creacion',
                   'num_barrios',
                   'ciudad'] 

 
