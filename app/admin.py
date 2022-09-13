from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subjects', 'message')

admin.site.register(Feedback, FeedbackAdmin)
