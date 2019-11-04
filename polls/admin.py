from django.contrib import admin
from polls.models import Question, Choice

class  ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,         {'fields': ['question_text']}),
        ('Date Information',   {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

# Register your models here.
