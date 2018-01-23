from django import forms

import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

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
