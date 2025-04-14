


from django.contrib import admin
from .models import District, Tahsil, Village, Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'village', 'latitude', 'longitude')
    search_fields = ('name',)
    readonly_fields = []
    fieldsets = (
        (None, {
            'fields': ('name', 'village', 'latitude', 'longitude', 'polygon_data')
        }),
    )

admin.site.register(District)
admin.site.register(Tahsil)
admin.site.register(Village)
