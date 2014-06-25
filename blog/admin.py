from django.contrib import admin
from blog.models import Blog, Event, FileManager

admin.site.register(Blog)
admin.site.register(Event)
admin.site.register(FileManager)