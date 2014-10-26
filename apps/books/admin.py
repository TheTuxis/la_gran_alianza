from django.contrib import admin
from apps.books.models import Pregunta, Respuesta, Libro, Capitulo, Pagina


admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Libro)
admin.site.register(Capitulo)
admin.site.register(Pagina)
