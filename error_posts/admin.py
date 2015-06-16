import json

from django.contrib import admin

from django_markdown.admin import MarkdownField, AdminMarkdownWidget, MarkdownModelAdmin

from .models import ErrorPost, Answer


class AnswerAdmin(admin.StackedInline):
    model = Answer
    max_num = 1
    formfield_overrides = {MarkdownField: {'widget': AdminMarkdownWidget}}


class ErrorPostAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]
    fields = ['exception_type', 'error_message', 'django_version',
              'traceback', 'sanitized_traceback_html', 'parsed_traceback_html']
    readonly_fields = ['sanitized_traceback_html', 'parsed_traceback_html']

    def sanitized_traceback_html(self, instance):
        return instance.sanitized_traceback
    sanitized_traceback_html.allow_tags = False

    def parsed_traceback_html(self, instance):
        return '<br><br><pre>{}</pre>'.format(json.dumps(instance.parsed_traceback, indent=2))
    parsed_traceback_html.allow_tags = True


admin.site.register(Answer, MarkdownModelAdmin)
admin.site.register(ErrorPost, ErrorPostAdmin)
