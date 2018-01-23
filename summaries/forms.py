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
    q = forms.CharField(required=False, label=('Search'),
                        widget=forms.TextInput(attrs={'type': 'search'}))

    def __init__(self, *args, **kwargs):
        self.searchqueryset = kwargs.pop('searchqueryset', None)
        self.load_all = kwargs.pop('load_all', False)

        if self.searchqueryset is None:
            self.searchqueryset = SearchQuerySet()

        super(SearchForm, self).__init__(*args, **kwargs)

    def no_query_found(self):
        """
        Determines the behavior when no query was found.

        By default, no results are returned (``EmptySearchQuerySet``).

        Should you want to show all results, override this method in your
        own ``SearchForm`` subclass and do ``return self.searchqueryset.all()``.
        """
        return EmptySearchQuerySet()

    def search(self):
        if not self.is_valid():
            return self.no_query_found()

        if not self.cleaned_data.get('q'):
            return self.no_query_found()

        sqs = self.searchqueryset.auto_query(self.cleaned_data['q'])

        if self.load_all:
            sqs = sqs.load_all()

        return sqs

    def get_suggestion(self):
        if not self.is_valid():
            return None

        return self.searchqueryset.spelling_suggestion(self.cleaned_data['q'])


