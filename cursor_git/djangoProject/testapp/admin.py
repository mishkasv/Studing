from django.contrib import admin

from .models import City,Food,Country,Restaurant,Personal,Menu

class Menu_admin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('foods',)
    search_fields = ('titls',)
    pass

class Restaurant_admin(admin.ModelAdmin):
    list_display = ('name','county','city',)
    autocomplete_fields = ('menu',)

admin.site.register(City)
admin.site.register(Food)
admin.site.register(Country)
admin.site.register(Restaurant,Restaurant_admin)
admin.site.register(Personal)
admin.site.register(Menu, Menu_admin)
# Register your models here.

