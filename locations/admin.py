from django.contrib import admin
from .models import FoodTruck
from import_export.admin import ImportExportModelAdmin

@admin.register(FoodTruck)
class FoodTruckAdmin(ImportExportModelAdmin):
    pass
