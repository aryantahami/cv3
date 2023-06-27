from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description')
    fields = ('title', 'description', 'image', ('youtube_link', 'linkedin_link', 'github_link'))


admin.site.register(Article, ArticleAdmin)
