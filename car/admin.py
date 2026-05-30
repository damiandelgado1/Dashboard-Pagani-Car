from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["brand", "model", "photo", "preview", "description", "photo_interior", "tires", "max_speed", "tire", "external_color", "internal_color", "stock", "availability", "price"]
    list_filter = ["brand", "model", "stock", "price"]
    search_fields = ["model", "price"]