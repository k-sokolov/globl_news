"""globlnews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from globlnews.views import HomePageView
from globlnews.views import InstructionView
from globlnews.views import SubmitView
from globlnews.views import SummaryView
from globlnews.views import SignUpView
from globlnews.views import ImprintView
from globlnews.views import YourContributionsView
from globlnews.views import ScienceStuffView
from globlnews.views import ProjectInformationView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('instructions', InstructionView.as_view(), name='instructions'),
    path('submit', SubmitView.as_view(), name='submit'),
    path('summary', SummaryView.as_view(), name='summary'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('imprint', ImprintView.as_view(), name='imprint'),
    path('contributions', YourContributionsView.as_view(), name='contributions'),
    path('science', ScienceStuffView.as_view(), name='science'),
    path('projectinformation', ProjectInformationView.as_view(), name='projectinformation'),
    path('admin', admin.site.urls),
]
