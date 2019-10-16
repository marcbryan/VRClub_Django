from django.contrib import admin
from .models import Usuario, Reserva, Aula, Material, Reserva_Material

admin.site.register(Usuario)
admin.site.register(Reserva)
admin.site.register(Aula)
admin.site.register(Material)
admin.site.register(Reserva_Material)
