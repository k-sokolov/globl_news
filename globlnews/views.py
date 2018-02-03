from __future__ import absolute_import

from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from braces import views

from .forms import RegistrationForm, LoginForm

#TODO: The view-type (generic.) needs to be adapted based on the purpose of the page

class HomePageView(generic.TemplateView):
    template_name = 'home.html'


class InstructionView(generic.TemplateView):
    template_name = 'instructions.html'

class FAQView(generic.TemplateView):
    template_name = 'faq.html'


class SignUpView(views.AnonymousRequiredMixin,
                 views.FormValidMessageMixin,
                 generic.CreateView):
    #TODO: Add corresponding model and additional stuff here
    success_url = reverse_lazy('home')
    form_class = RegistrationForm
    form_valid_message = 'Thanks for signing up'
    model = User
    template_name = 'account/signup.html'


class LoginView(views.AnonymousRequiredMixin,
                views.FormValidMessageMixin,
                generic.FormView):
    form_class = LoginForm
    form_valid_message = 'You are logged in now'
    success_url = reverse_lazy('home')
    template_name = 'account/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogOutView(views.LoginRequiredMixin,
                 generic.RedirectView):

    url = reverse_lazy('home')
    form_valid_message = 'You are logged out now'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)


class ImprintView(generic.TemplateView):
    template_name = 'imprint.html'


class YourContributionsView(generic.TemplateView):
    template_name = 'contributions.html'


class ScienceStuffView(generic.TemplateView):
    template_name = 'sciencestuff.html'


class ProjectInformationView(generic.TemplateView):
    template_name = 'projectinformation.html'

class TermsView(generic.TemplateView):
        template_name = 'terms.html'
