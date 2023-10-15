from django.contrib import admin
from .models import Exhibition, ExhibitionType

admin.site.register(ExhibitionType)

@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'type', 'tickets_quantity')