# app/urls.py
from django.urls import path
from .views import FormView, QuestionerView, AnswersView, ClearDataView

urlpatterns = [
    path('form/', FormView.as_view(), name='form_data_view'),
    path('questioner/', QuestionerView.as_view(), name='questioner_view'),
    path('answers/', AnswersView.as_view(), name='answers_view'),
    path('clear-data/', ClearDataView.as_view(), name='clear_data_view'),  # Add this line
]
