# app/serializers.py
from rest_framework import serializers
from .models import FormData

class FormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormData
        fields = ['question', 'answer1', 'answer2', 'answer3', 'answer4', 'answer5']
