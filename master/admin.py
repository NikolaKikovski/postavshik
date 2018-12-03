from django.contrib import admin
from .models import Company, Item


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "master")


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "company")
