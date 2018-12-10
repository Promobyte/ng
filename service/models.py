from urllib.parse import quote
from django.utils.encoding import iri_to_uri
from django.db import models
from django.utils import timezone
from django.utils import text
from django.db.models import signals

class Service(models.Model):
    created = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='service', null=True, blank=True)
    slug = models.SlugField(max_length=50, null=True, blank=True, db_index=True, allow_unicode=True)

    @property
    def get_absolute_url(self):
        url = "/%s/" % self.slug
        return url

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = text.slugify(self.title, allow_unicode=True)
        super(Service, self).save(*args, **kwargs)

