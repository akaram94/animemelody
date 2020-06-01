from django.contrib import admin

from .models import Show, Theme

# Register your models here.
class ShowAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'season')
    search_fields = ['name']

class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'show', 'theme_type')
    search_fields = ['name', 'show__name']

admin.site.register(Show, ShowAdmin)
admin.site.register(Theme, ThemeAdmin)

