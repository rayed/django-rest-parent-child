# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = ChoiceSerializer

    def get_queryset(self):
        question_id = self.kwargs['question_id']
        return Choice.objects.filter(question=question_id)
