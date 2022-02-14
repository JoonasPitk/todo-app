from dataclasses import fields
from django.contrib import admin

from .models import Tehtava, Kategoria

@admin.register(Tehtava)
class TehtavaAdmin (admin.ModelAdmin):
    list_display = ['id', 'otsikko']

@admin.register(Kategoria)
class KategoriaAdmin (admin.ModelAdmin):
    pass
