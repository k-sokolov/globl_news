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
from django.urls import path, include
#from globlnews.views import HomePageView, InstructionView, \
#    SignUpView, ImprintView, YourContributionsView, ScienceStuffView, \
#     ProjectInformationView, LoginView, LogOutView, FAQView
from globlnews.views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('instructions', InstructionView.as_view(), name='instructions'),
#    path('submit', SubmitView.as_view(), name='submit'),
#    path('summary', SummaryView.as_view(), name='summary'),
    path('account/signup', SignUpView.as_view(), name='signup'),
    path('account/login', LoginView.as_view(), name='login'),
    path('account/logout', LogOutView.as_view(), name='logout'),
    path('imprint', ImprintView.as_view(), name='imprint'),
    path('faq', FAQView.as_view(), name='faq'),
    path('contributions', YourContributionsView.as_view(), name='contributions'),
    path('science', ScienceStuffView.as_view(), name='science'),
    path('projectinformation', ProjectInformationView.as_view(), name='projectinformation'),
    path('summaries/', include('summaries.urls')),
    path('admin', admin.site.urls),
]
