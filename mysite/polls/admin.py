from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)




# from django.contrib import admin

# from .models import Question, Choice

# class ChoiceInLine(admin.StackedInLine):
# 	model = Choice
# 	extra = 3


# class QuestionAdmin(admin.ModelAdmin):
# 	fieldsets = [
# 	('Question Area',                     {'fields':['question_text']}),
# 	('Date Information',        {'fields':['pub_date'], 'classes':['collapse']}),

# 	]
# 	inlines = [ChoiceInLine]

# admin.site.register(Question, QuestionAdmin)
