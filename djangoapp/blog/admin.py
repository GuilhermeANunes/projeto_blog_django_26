from django.contrib import admin
from site_setup.models import MenuLinks, SiteSetup

# Register your models here.
# @admin.register(MenuLinks)
# class MenuLinksAdmin(admin.ModelAdmin):
#     list_display = 'id', 'text', 'url_or_path'
#     list_display_links = 'id', 'text', 'url_or_path'
#     search_fields = 'id', 'text', 'url_or_path'

class MenuLinkInline(admin.TabularInline):
    model = MenuLinks
    extra = 1

@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = 'title', 'description'
    inlines = MenuLinkInline,

    def has_add_permission(self, request):
        return not SiteSetup.objects.exists()