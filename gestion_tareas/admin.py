from django.contrib import admin
from .models import Tarea

# Configuracion extra en el panel
class TareaAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

# Register your models here.
admin.site.register(Tarea, TareaAdmin)

# Configuracion del panel
title = "App Django"
subtitle = "Panel de gestión"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
