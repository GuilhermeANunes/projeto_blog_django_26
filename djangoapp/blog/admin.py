from django.contrib import admin
from site_setup.models import MenuLinks, SiteSetup
from blog.models import Tag, Category, Page, Post

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

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug',
    list_display_links = 'name',
    search_fields = 'id', 'name', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        'slug': ('name',),
    }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug',
    list_display_links = 'name',
    search_fields = 'id', 'name', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        'slug': ('name',),
    }

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'slug', 'is_published',
    list_display_links = 'title',
    search_fields = 'id', 'title', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        'slug': ('title',),
    }

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'slug', 'is_published', 'created_by',
    list_display_links = 'title',
    search_fields = 'id', 'title', 'slug', 'excerpt', 'content',
    list_filter = 'category', 'is_published',
    list_per_page = 50
    list_editable = 'is_published',
    ordering = '-id',
    readonly_fields = 'created_at', 'created_by', 'updated_at',  'updated_by',
    prepopulated_fields = {
        'slug': ('title',),
    }

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        obj.save()