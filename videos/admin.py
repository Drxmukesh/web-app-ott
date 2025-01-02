from django.contrib import admin
from .models import Video, Title, Description

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title',)

class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)

class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('video', 'text', 'created_at')
    search_fields = ('video__title',)

admin.site.register(Video, VideoAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Description, DescriptionAdmin)