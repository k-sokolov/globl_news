from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

#class Topic(models.Model):
#    title = models.CharField(max_length=200)
#    short_summary = models.CharField(max_length=1000)
#    image = models.ImageField(upload_to = './pic_folder/', default = 'pic_folder/None/no-img.png')
    # TODO: in production it is required to set the MEDIA_ROOT to a valid directory to save the data


class Summary(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=8000)
    tags = models.ManyToManyField('Tag', db_table='articletag')
    link_original_article = models.CharField(max_length=255)
    publisher_original_article = models.CharField(max_length=255)
    name_author_original_article = models.CharField(max_length=255)
    publication_date_original_article = models.DateField()
    publication_country_original_article = models.CharField(max_length=255)
    #image = models.ImageField(upload_to='../pic_folder/', default='pic_folder/None/no-img.png')
    submission_date_summary = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, blank=True)
#    topic = models.ForeignKey(
 #       'Topic',
#        on_delete=models.CASCADE(),
#    )

    #Slug
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        ordering = ('submission_date_summary',)
        unique_together = ('user', 'title')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.id)
        super(Summary, self).save(*args, **kwargs)


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
        User,
        on_delete=models.CASCADE,
    )
    article = models.ForeignKey(
        'Summary',
        on_delete=models.CASCADE,
    )