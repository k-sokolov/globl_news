from __future__ import absolute_import

from django.urls import path

from .views import SubmitView, SummaryList

urlpatterns = (
    path('submit', SubmitView.as_view(), name='submit'),
    path('overview', SummaryList.as_view(), name='overview'),
)