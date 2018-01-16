from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from braces import views
from . import forms
from . import models

#class SubmitView(
#    views.LoginRequiredMixin,
#    generic.CreateView):
#
#    form_class = forms.SummaryForm
#
#    template_name = 'submit.html'

class SubmitView(views.LoginRequiredMixin,
                 views.FormValidMessageMixin,
                 generic.CreateView):
    success_url = reverse_lazy('home')
    form_class = forms.SummaryForm
    form_valid_message = 'Thanks for Submitting a Summary'
    model = models.Summary
    template_name = 'submit.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(SubmitView, self).form_valid(form)


class SummaryView(generic.DetailView):

    model = models.Summary
    template_name = 'summary.html'
