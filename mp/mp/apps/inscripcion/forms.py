# -*- coding: utf-8 -*-

from django import forms
from django.forms.models import ModelForm


__author__ = 'gzacur'


class InscripcionActividadForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    apellido = forms.CharField(max_length=100, required=True)
    fecha_nacimiento = forms.DateField(label="Fecha de nacimiento", required=True)
    telefono = forms.CharField(max_length=50, label="Teléfono", required=True)
    cedula = forms.IntegerField(min_value=0, required=True, label="Cédula")
    email = forms.EmailField(widget=forms.EmailInput, label="E-mail", required=True)
    email_repetir = forms.EmailField(widget=forms.EmailInput, label="E-mail (repetir)",
                                     help_text="Repita el mail escrito anteriormente...", required=True)

    def clean_email_repetir(self):
        email = self.cleaned_data['email']
        email_repetir = self.cleaned_data['email_repetir']

        if email != email_repetir:
            raise forms.ValidationError("Los e-mails no son iguales")

        return email






