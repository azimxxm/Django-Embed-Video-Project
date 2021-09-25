from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin

@admin.register(Video)
class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    list_display = ['id', 'title', 'added']
    search_fields = ['title',]
