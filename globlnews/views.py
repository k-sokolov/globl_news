from django.views import generic
import os
import globlnews.settings as settings

#TODO: The view-type (generic.) needs to be adapted based on the purpose of the page

class HomePageView(generic.TemplateView):
    template_name = 'home.html'


class InstructionView(generic.TemplateView):
    template_name = 'instructions.html'


class SubmitView(generic.CreateView):
    #TODO: Add corresponding model and additional stuff here
    template_name = 'submit.html'


class SummaryView(generic.TemplateView):
    template_name = 'summary.html'


class SignUpView(generic.CreateView):
    #TODO: Add corresponding model and additional stuff here
    template_name = 'signup.html'


class ImprintView(generic.TemplateView):
    template_name = 'imprint.html'


class YourContributionsView(generic.TemplateView):
    template_name = 'contributions.html'


class ScienceStuffView(generic.TemplateView):
    template_name = 'sciencestuff.html'


class ProjectInformationView(generic.TemplateView):
    template_name = 'projectinformation.html'