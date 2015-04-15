from django.contrib import admin

from .models import Error, Answer


class AnswerAdmin(admin.StackedInline):
	model = Answer
	max_num = 1


class ErrorAdmin(admin.ModelAdmin):
	inlines = [AnswerAdmin]
	change_form_template = 'errors/admin/change_form.html'


admin.site.register(Answer)
admin.site.register(Error, ErrorAdmin)
