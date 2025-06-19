from django.forms import ModelForm
# añadir pais
from administrativo.models import Estudiante, Pais

class EstudianteForm(ModelForm): 
    class Meta:
        model = Estudiante 
        fields = ['nombre', 'apellido', 'cedula'] 

# Crear un formulario para el modelo Pais
class PaisForm(ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre', 'capital', 'numero_provincias', 'numero_habitantes']


