# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from .models import Question, Choice

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('__all__')

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('__all__')
