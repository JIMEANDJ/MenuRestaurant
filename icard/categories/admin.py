from django.contrib import admin
from categories.models import categories

@admin.register(categories)
class CategoriesAdmin(admin.ModelAdmin):
    pass