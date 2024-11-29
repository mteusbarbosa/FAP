from django.contrib import admin
from .models import Advogado, Assistente, Juiz, Promotor, Reu, Processo

admin.site.register(Advogado)
admin.site.register(Assistente)
admin.site.register(Juiz)
admin.site.register(Promotor)
admin.site.register(Reu)
admin.site.register(Processo)