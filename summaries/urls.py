from __future__ import absolute_import

from django.urls import path

from .views import SubmitView

urlpatterns = (
    path('submit', SubmitView.as_view(), name='submit'),
)