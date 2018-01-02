from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=200)
    short_summary = models.CharField(max_length=1000)
    image = models.ImageField(upload_to = './pic_folder/', default = 'pic_folder/None/no-img.png')
    # TODO: in production it is required to set the MEDIA_ROOT to a valid directory to save the data


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=8000)
    tags = models.ManyToManyField('Tag', db_table='articletag')
    link_original_article = models.CharField(max_length=200)
    paper_original_article = models.CharField(max_length=200)
    name_author_original_article = models.CharField(max_length=200)
    publication_date_original_article = models.DateField()
    publication_country_original_article = models.CharField(max_length=200)
    image = models.ImageField(upload_to='./pic_folder/', default='pic_folder/None/no-img.png')
    topic = models.ForeignKey(
        'Topic',
        on_delete=models.CASCADE(),
    )
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE(),
    )


class Tag(models.Model):
    title = models.CharField(max_length=200)
    WHO = 'WHO'
    WHERE = 'WHERE'
    WHAT = 'WHAT'
    WHEN = 'WHEN'
    TAG_CHOICES = (
        (WHO, 'Who-tag'),
        (WHERE, 'Where-tag'),
        (WHAT, 'What-tag'),
        (WHEN, 'When-tag'),
    )
    tag = models.CharField(
        max_length=5,
        choices=TAG_CHOICES,
        default=WHAT,
    )


class Comments(models.Model):
    title = models.CharField(max_length=200)
    short_summary = models.CharField(max_length=1000)
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE(),
    )
    article = models.ForeignKey(
        'Article',
        on_delete=models.CASCADE(),
    )