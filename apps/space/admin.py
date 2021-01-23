from django.contrib import admin

from .models import Folder, List, Space

admin.site.register(Space)
admin.site.register(Folder)
admin.site.register(List)
