from django.contrib import admin
from .models import Usuario, Reserva, Aula, Material, Reserva_Material


class ReservaInline(admin.StackedInline):
    model = Reserva
    extra = 2


class UsuarioAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Información del usuario', {'fields' : ['nombre', 'apellidos', 'edad', 'estudios']}),
    ]
    inlines = [ReservaInline]

#TODO: MaterialInline y AulaAdmin

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Reserva)
admin.site.register(Aula)
admin.site.register(Material)
admin.site.register(Reserva_Material)
