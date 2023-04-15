from django.contrib import admin

from .models import community_event_manager, Location, Group, Contributor

# Register your models here.

class community_event_managerAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'location', 'date')
    list_filter = ('location', 'group_name', 'date')
    prepopulated_fields = {'slug': ('title', )}



admin.site.register(community_event_manager, community_event_managerAdmin)
admin.site.register(Location)
admin.site.register(Group)
admin.site.register(Contributor)
