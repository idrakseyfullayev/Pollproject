from django.contrib import admin
from poll.models import QuestionModel, AnswerModel, PollModel

# Register your models here.

admin.site.register(QuestionModel)
admin.site.register(PollModel)

# admin.site.register(AnswerModel)

@admin.register(AnswerModel)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'name', "is_true")