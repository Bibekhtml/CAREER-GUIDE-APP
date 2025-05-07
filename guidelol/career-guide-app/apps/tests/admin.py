# File: /career-guide-app/career-guide-app/apps/tests/admin.py

from django.contrib import admin
from .models import TestModel  # Replace with your actual model name

@admin.register(TestModel)  # Replace with your actual model name
class TestModelAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Replace with your actual fields
    search_fields = ('field1',)  # Replace with your actual fields
    list_filter = ('field2',)  # Replace with your actual fields