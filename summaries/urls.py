from __future__ import absolute_import

from django.urls import path, include

from .views import SubmitView, SummaryList, SummaryView
from .views import SearchView

urlpatterns = (
    path('submit', SubmitView.as_view(), name='submit'),

	path('search/', SearchView(), name='search'),


    path('overview', SummaryList.as_view(), name='home'),
    path(r'^(?P<slug>[-\w]+)/$', SummaryView.as_view(), name='summary')
)

