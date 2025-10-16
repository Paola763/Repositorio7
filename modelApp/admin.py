from django.contrib import admin
from .models import Empleado

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
 list_display = ("id", "nombre", "email", "telefono")
 search_fields = ("nombre", "email")