from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class QuestionModel(models.Model):
    name = models.CharField(max_length=1000)
 
    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.name    


class AnswerModel(models.Model):
    name = models.CharField(max_length=1000)
    is_true = models.BooleanField()
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE, related_name="question_answers")
    
    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"

    def __str__(self):
        return self.question.name + "|" + self.name   


class PollModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_polls")
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE, related_name="question_polls")

    class Meta:
        verbose_name = "Poll"
        verbose_name_plural = "Polls"

    def __str__(self):
        return self.user.username + "|" + self.question.name