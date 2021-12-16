from django.contrib import admin

from main.models import Project, UserProjectCompleted


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level', 'programming_language', 'check',
                    'date_created', 'is_active', 'description')
    list_display_links = ('name',)
    ordering = ('id',)


@admin.register(UserProjectCompleted)
class UserProjectCompletedAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'project')
    list_display_links = ('user',)
    ordering = ('id',)
