from django.contrib import admin
from .models import Topic, Entry

class AdminTopic(admin.ModelAdmin):
  list_display = ("title", "description")

admin.site.register(Topic, AdminTopic)
admin.site.register(Entry)
