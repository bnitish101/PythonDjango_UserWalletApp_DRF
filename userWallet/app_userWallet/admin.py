from django.contrib import admin

from .models import User, UserTransactionHistory
# Register your models here.

admin.site.register(User)
admin.site.register(UserTransactionHistory)