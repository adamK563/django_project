# app/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, FormData

class FormDataAdmin(admin.ModelAdmin):
    list_display = ('question_and_answer', 'user_name')  # Add 'user_name' to the displayed fields

    actions = ['clear_questions']

    def clear_questions(self, request, queryset):
        queryset.delete()

    clear_questions.short_description = "Clear selected questions"

    def user_name(self, obj):
        return obj.user.name if obj.user else ''  

    user_name.short_description = "User Name"

    def question_and_answer(self, obj):
        question = obj.question
        answer = obj.selected_answer or 'none'
        return f"{question}: {answer}"

    question_and_answer.short_description = "Question and Answer"

admin.site.register(FormData, FormDataAdmin)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'name')  

admin.site.register(CustomUser, CustomUserAdmin)
