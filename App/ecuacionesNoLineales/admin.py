from django.contrib import admin

from .models import EcuacionesNoLineales

# Register your models here.


class AdminEcuaciones(admin.ModelAdmin):
    list_display = ["funcion", "valorInicial", "delta", "iter"]

    class Meta:
        model = EcuacionesNoLineales
        fields = ["funcion", "valorInicial", "delta", "iter"]


admin.site.register(EcuacionesNoLineales, AdminEcuaciones)
