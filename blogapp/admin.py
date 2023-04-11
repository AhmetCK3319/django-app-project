from django.contrib import admin
from .models import Blog,Category
from django.utils.safestring import mark_safe


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=[
        'title',
        'is_active',
        'is_home',
        'slug',
        'selected_categories',
    ]

    list_editable=[
        'is_active',
        'is_home',
    ]
    search_fields=[
        'title',
        'descriptions',
    ]
    readonly_fields=[
        'slug'
    ]    
    list_filter=[
        
        'is_active',
        'is_home',
        'categories',
    ]

    def selected_categories(self,obj):
        html='<ol>'
        for category in obj.categories.all():
            html += '<li>' + category.name + '</li>'
        html +='</ol>'
        return mark_safe(html)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=[
        'name',
        'is_active',
        'slug',
        
    ]
    list_editable=[
        'is_active',
       
    ]
    search_fields=[
        'name',
        
    ]
    readonly_fields=[
        'slug'
    ]   
