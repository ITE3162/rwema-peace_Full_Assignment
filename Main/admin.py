from django.contrib import admin
from Main.models import About, Service, Contact

# Register your models here.

admin.site.register(About)


@admin.register(Service)
class serviceAdmin(admin.ModelAdmin):
    list_display = ['Title', 'Subtext']


@admin.register(Contact)
class contactAdmin(admin.ModelAdmin):
    list_display = ['Email', 'Subject']
