from django.contrib import admin
from .models import Question, Alternative

class QuestionAdmin(admin.ModelAdmin):
    ...

class AlternativeAdmin(admin.ModelAdmin):
    ...

admin.site.register(Question, QuestionAdmin)
admin.site.register(Alternative, AlternativeAdmin)