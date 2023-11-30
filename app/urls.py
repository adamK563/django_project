# app/urls.py
from django.urls import path
from .views import FormDataView

urlpatterns = [
    path('formdata/', FormDataView.as_view(), name='form_data_view'),
]
