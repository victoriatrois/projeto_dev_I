# Arquivo que armazenará as configurações e partes administrativas do aplicativo
from django.contrib import admin
from exemplo.models import Example

# Register your models here.
admin.site.register(Example)