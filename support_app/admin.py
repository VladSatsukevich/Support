from django.contrib import admin
from .models import Room, Message


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'date', 'value', 'answered', 'closed', 'freeze')
    list_display_links = ('room',)


admin.site.register(Room)
admin.site.register(Message, CategoryAdmin)
