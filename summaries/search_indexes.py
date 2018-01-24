from haystack import indexes
import datetime
from summaries.models import Summary


class SummaryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=False)
    body = indexes.CharField(model_attr='text')
    title = indexes.CharField(model_attr='title')
    user = indexes.CharField(model_attr='user')
    submission_date_summary = indexes.DateField(model_attr='submission_date_summary')
    publisher_original_article = indexes.CharField(model_attr='publisher_original_article')
    publication_country_original_article = indexes.CharField(model_attr='publication_country_original_article')
    publication_date_original_article = indexes.DateField(model_attr='publication_date_original_article')
    
    def get_model(self):
        return Summary

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(submission_date_summary__lte=datetime.datetime.now())
        
    