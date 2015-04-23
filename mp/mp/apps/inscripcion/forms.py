# -*- coding: utf-8 -*-
from django import forms
from django.forms import Select
from models import *

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad