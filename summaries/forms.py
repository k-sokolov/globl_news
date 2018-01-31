from django import forms

import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

from haystack.query import EmptySearchQuerySet, SearchQuerySet

from . import models

class SummaryForm(forms.ModelForm):
    class Meta:
        fields = ('title', 'text', 'link_original_article', 'publisher_original_article',
                  'name_author_original_article', 'title_original_article',
                   'publication_date_original_article',
                  'publication_country_original_article')
        model = models.Summary

    def __init__(self, *args, **kwargs):
        super(SummaryForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            #'tags',
            'text',
            'link_original_article',
            'publisher_original_article',
            'name_author_original_article',
            'title_original_article',
            'publication_date_original_article',
            'publication_country_original_article',
            ButtonHolder(Submit('add', 'Add', css_class='btn-primary'))
        )

    #def clean_publication_date_original_article(self):
    #    publication_date = self.cleaned_data.get('publication_date_original_article')
    #    current_date = datetime.datetime.now()


        
class SearchForm(forms.Form):
    text_contains = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        self.searchqueryset = kwargs.pop('searchqueryset', None)
        self.load_all = kwargs.pop('load_all', False)

        if self.searchqueryset is None:
            self.searchqueryset = SearchQuerySet()#.models(models.Summary)

        super(SearchForm, self).__init__(*args, **kwargs)

    def no_query_found(self):
        """
        Determines the behavior when no query was found.

        By default, no results are returned (``EmptySearchQuerySet``).

        Should you want to show all results, override this method in your
        own ``SearchForm`` subclass and do ``return self.searchqueryset.all()``.
        """
        print(1)
        return self.searchqueryset.all()

    def search(self):
        if not self.is_valid():
            return self.no_query_found()

        if not self.cleaned_data.get('text_contains'):
            return self.no_query_found()

        sqs = self.searchqueryset.auto_query(self.cleaned_data['text_contains'])

        if self.load_all:
            sqs = sqs.load_all()

        return sqs

    def get_suggestion(self):
        if not self.is_valid():
            return None

        return self.searchqueryset.spelling_suggestion(self.cleaned_data['text_contains'])

class AdvancedSearchForm(SearchForm):


    title_contains = forms.CharField(max_length=255, required=False)
    submission_date_summary = forms.DateField(required=False,\
                                widget=forms.TextInput(attrs={'placeholder': 'mm/dd/yyyy'}))
                                
    publication_date_original_article = forms.DateField(required=False,\
                                widget=forms.TextInput(attrs={'placeholder': 'mm/dd/yyyy'}))
                                
    publisher_original_article = forms.CharField(max_length=255, required=False)
    publication_country_original_article = forms.CharField(max_length=255, required=False)
    tags = forms.CharField(max_length=255, required=False)
    

    
    def no_query_found(self):
        
        return self.searchqueryset.all().filter()

    def search(self):
        if not self.is_valid():
            return self.no_query_found()       


       # First, store the SearchQuerySet received from other processing.
        sqs = super(AdvancedSearchForm, self).search()


        # Check to see if a start_date was chosen.
        if self.cleaned_data['title_contains']:
            sqs = sqs.filter(title=self.cleaned_data['title_contains'])

        # Check to see if an end_date was chosen.
        if self.cleaned_data['submission_date_summary']:
            sqs = sqs.filter(submission_date_summary=self.cleaned_data['submission_date_summary'])
            
        if self.cleaned_data['publication_date_original_article']:
            sqs = sqs.filter(publication_date_original_article=self.cleaned_data['publication_date_original_article'])
            
        if self.cleaned_data['publisher_original_article']:
            sqs = sqs.filter(publisher_original_article=self.cleaned_data['publisher_original_article'])
            
        if self.cleaned_data['publication_country_original_article']:
            sqs = sqs.filter(publication_country_original_article=self.cleaned_data['publication_country_original_article'])
            
        if self.cleaned_data['tags']:
            sqs = sqs.autocomplete(tags=self.cleaned_data['tags'])

        return sqs
