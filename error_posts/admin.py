import json

from django.contrib import admin
from django.utils.translation import ugettext as _

from django_markdown.admin import MarkdownField, AdminMarkdownWidget, MarkdownModelAdmin

from .models import ErrorPost, Answer


class AnswerAdmin(admin.StackedInline):
    model = Answer
    max_num = 1
    formfield_overrides = {MarkdownField: {'widget': AdminMarkdownWidget}}


def _has_answer(error_post):
    return error_post.answers.exists()


class HasAnswerListFilter(admin.SimpleListFilter):
    title = _('has answer')
    parameter_name = 'has_answer'

    def lookups(self, request, model_admin):
        return (
            ('yes', _('Yes')),
            ('no',  _('No')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'yes':
            # distinct necessary here, see: http://stackoverflow.com/a/14832060/145349
            return queryset.filter(answers__isnull=False).distinct()
        if self.value() == 'no':
            return queryset.filter(answers__isnull=True)


class ErrorPostAdmin(admin.ModelAdmin):
    list_display = ['exception_type', 'raised_by', 'django_version', 'slug',
                    _has_answer, 'is_published']
    list_filter = ['is_published', HasAnswerListFilter, 'django_version',
                   'exception_type']
    search_fields = ['traceback']

    inlines = [AnswerAdmin]
    fields = ['is_published', 'exception_type',
              'raised_by', 'raised_by_line', 'django_version',
              'error_message', 'how_to_reproduce',
              'traceback', 'sanitized_traceback_html', 'parsed_traceback_html',
              'slug']
    readonly_fields = ['raised_by', 'raised_by_line',
                       'sanitized_traceback_html', 'parsed_traceback_html',
                       'slug']

    def sanitized_traceback_html(self, instance):
        return '<br><br><pre>{}</pre>'.format(instance.sanitized_traceback)
    sanitized_traceback_html.allow_tags = True

    def parsed_traceback_html(self, instance):
        return '<br><br><pre>{}</pre>'.format(json.dumps(instance.parsed_traceback, indent=2))
    parsed_traceback_html.allow_tags = True


admin.site.register(Answer, MarkdownModelAdmin)
admin.site.register(ErrorPost, ErrorPostAdmin)
