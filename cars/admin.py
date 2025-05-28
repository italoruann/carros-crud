from django.contrib import admin

from .models import Brand, Car


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value') # é o cabeçalho da tabela no admin do Django
    search_fields = ('model', 'brand') # é o campo de busca do cabeçalho da tabela no admin do Django

# Para aparecer no admin do Django, é necessário registrar o modelo e o modelo admin
admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)