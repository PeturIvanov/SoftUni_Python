from django.contrib import admin

from main_app.models import Veterinarian


@admin.register(Veterinarian)
class VeterinarianAdmin(admin.ModelAdmin):
    pass
