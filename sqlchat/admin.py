from django.contrib import admin
from .models import user
from .models import chat_history
# Register your models here.
admin.site.register(user)
admin.site.register(chat_history)
