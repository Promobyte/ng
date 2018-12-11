from django.db import models
from django.utils import timezone
from django.utils import text
from service.models import Service


class Article(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    headline = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='article')
    slug = models.SlugField(max_length=50, null=True, blank=True, db_index=True, allow_unicode=True, unique=True),


    @property
    def get_absolute_url(self):
        url = "/{0}/{1}/".format(self.service.slug, self.slug)
        return url

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = text.slugify(self.title, allow_unicode=True)
        super(Article, self).save(*args, **kwargs)
