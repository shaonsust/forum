from django.contrib import admin
from boards.models import Board, Topic, Post


class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_filter = ('name',)
    list_per_page = 15
    fields = ('name', 'description')
    search_fields = ('id', 'name')


class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'board', 'views', 'starter', 'last_updated')
    list_per_page = 15
    search_fields = ('id', 'subject', 'board', 'starter')
    fields = ('subject', 'board',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'topic', 'created_at')
    list_per_page = 15
    fields = ('message', 'topic')
    search_fields = ('id', 'topic', 'message')


admin.site.register(Board, BoardAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
