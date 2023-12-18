from django import forms
from AppFutbol.models import Equipo, Jugador, Entrenador

#-----------------------------------------
class EquipoForm(forms.ModelForm):
    puntaje = forms.IntegerField(
        min_value=0,
        max_value=10,
        widget=forms.NumberInput(attrs={'type': 'number', 'min': 0, 'max': 10})
    )

    class Meta:
        model = Equipo
        fields = ['nombre', 'puntaje', 'imagen']

    def __init__(self, *args, **kwargs):
        super(EquipoForm, self).__init__(*args, **kwargs)

#---------------------------------------------------------
class JugadorForm(forms.ModelForm):
    puntaje = forms.IntegerField(
        min_value=0,
        max_value=10,
        widget=forms.NumberInput(attrs={'type': 'number', 'min': 0, 'max': 10})
    )

    class Meta:
        model = Jugador
        fields = ['nombre', 'puntaje']

#----------------------------------------------------------
class EntrenadorForm(forms.ModelForm):

    puntaje = forms.IntegerField(
        min_value=0,
        max_value=10,
        widget=forms.NumberInput(attrs={'type': 'number', 'min': 0, 'max': 10})
    )

    class Meta:
        model = Entrenador
        fields = ['nombre', 'puntaje']


class BusquedaFormJugador(forms.Form):
    nombre = forms.CharField()

class BusquedaFormEquipo(forms.Form):
    nombre = forms.CharField()

class BusquedaFormEntrenador(forms.Form):
    nombre = forms.CharField()