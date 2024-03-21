from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # La primera variable indica el titulo con el que aparecera,
    # la segunda indica los campos que tendra
    fieldsets = [
        (None,
            {"fields": ["question_text"]}
        ),
        ("Date information",
            {"fields": ["pub_date"],
            "classes":["collapse"],}
        ),
    ]

    inlines = [ChoiceInline]

    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]

    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)
""" Para poner dos campos debajo de un titulo
    fieldsets = [
        ("Date information and Qtext", {"fields": ["question_text","pub_date"]}),
    ]
    para ordenar los campos
    fields = ["pub_date", "question_text"]
"""