from django.contrib import admin
from .models import *

admin.site.register(ProjectFolder)
admin.site.register(TodoItem)
admin.site.register(CompletedTask)
