from django.contrib import admin

from .models import ErrorPost, Answer


class AnswerAdmin(admin.StackedInline):
    model = Answer
    max_num = 1


class ErrorPostAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]
    change_form_template = 'error_posts/admin/change_form.html'


admin.site.register(Answer)
admin.site.register(ErrorPost, ErrorPostAdmin)
