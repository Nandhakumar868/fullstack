from django.contrib import admin

# Register your models here.
from .models import Registration_form



class RegistrationAdmin(admin.ModelAdmin):
    list_display = ["name","email","address","phone_no"]

admin.site.register(Registration_form,RegistrationAdmin)