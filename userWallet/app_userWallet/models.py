from django.db import models

# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # pass
    username = models.CharField(max_length=30, unique=False)
    email = models.EmailField(unique=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class UserTransactionHistory(models.Model):
    userWallet = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updateAmount = models.DecimalField(max_digits=5, decimal_places=2)
    added_by = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __decimal__(self):
        return self.updateAmount