from __future__ import absolute_import

from django.urls import path, include

from .views import SubmitView, SummaryList, SummaryView

urlpatterns = (
    path('submit', SubmitView.as_view(), name='submit'),

	path('search/', include('haystack.urls')),


    path('overview', SummaryList.as_view(), name='overview'),
    path(r'^(?P<slug>[-\w]+)/$', SummaryView.as_view(), name='summary')
)

