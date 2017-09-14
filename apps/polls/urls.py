# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
router.register(r'questions/(?P<question_id>.+)/choices', views.ChoiceViewSet, base_name='choices')


urlpatterns = [
    url(r'^api/', include(router.urls)),
]
