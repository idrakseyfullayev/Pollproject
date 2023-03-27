from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    photo = models.ImageField(upload_to="accountphotos", blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    cor_uns_number = models.IntegerField(default=0)
    uncur_uns_number = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return self.user.username    