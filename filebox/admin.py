from django.contrib import admin

from .models import Box, Filebox


class BoxAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_date')
    filter_horizontal = ('members',)


class FileBoxAdmin(admin.ModelAdmin):
    list_display = ('name', 'box', 'upload_by')
    list_filter = ('box__name',)


admin.site.register(Box, BoxAdmin)
admin.site.register(Filebox, FileBoxAdmin)
