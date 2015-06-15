from django.contrib import admin

from django_markdown.admin import MarkdownField, AdminMarkdownWidget, MarkdownModelAdmin

from .models import ErrorPost, Answer


class AnswerAdmin(admin.StackedInline):
    model = Answer
    max_num = 1
    formfield_overrides = {MarkdownField: {'widget': AdminMarkdownWidget}}


class ErrorPostAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]


admin.site.register(Answer, MarkdownModelAdmin)
admin.site.register(ErrorPost, ErrorPostAdmin)
