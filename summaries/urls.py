from __future__ import absolute_import

from django.urls import path, include

from .views import SubmitView

urlpatterns = (
    path('submit', SubmitView.as_view(), name='submit'),
	path('search/', include('haystack.urls'))
)