from django.contrib import admin
from poll.models import QuestionModel, ChoiceModel, PollModel

# Register your models here.

admin.site.register(QuestionModel)
admin.site.register(PollModel)


# admin.site.register(AnswerModel)

@admin.register(ChoiceModel)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'name', "is_true")

