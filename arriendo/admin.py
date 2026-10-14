from django.contrib import admin

# Register your models here.

from .models import Equipo, Arriendo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo')
    search_fields = ('tipo',)
    list_filter = ('nombre',)


@admin.register(Arriendo)
class ArriendoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'formato')
    search_fields = ('formato',)
    list_filter = ('descripcion',)

    @admin.display(description = "Precio", ordering = "precio")
    def formato(self, obj):
        return f"${obj.precio:,}".replace("," , ".")