from django import forms
from django.core import validators

class FormTarea(forms.Form):
    title = forms.CharField(
        label = "Titulo",
        max_length=50,
        required=True,
        validators=[
            validators.MinLengthValidator(4, 'El titulo es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9ñ ]*$', 'El titulo esta mal formado', 'invalid_title')
        ]
    )

    description = forms.CharField(
        label = "Contenido",
        required=True,
        validators=[
            validators.MaxLengthValidator(50, 'Te has pasado, has puesto mucho texto')
        ]
    )
