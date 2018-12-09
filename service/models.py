
from django.conf import settings
from django.db import models
from django.utils import timezone
from slugify import slugify
from django.utils import text
from unidecode import unidecode
from django.template import defaultfilters
from django.utils.encoding import iri_to_uri



class Service(models.Model):
    created = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='service', null=True, blank=True)
    slug = models.SlugField(max_length=50, null=True, blank=True, db_index=True, allow_unicode=True)

    def get_absolute_url(self):
        return "/%s/" % self.slug

    def __str__(self):
        return self.title

    def __init__(self, *args, **kwargs):
        super(Service, self).__init__(*args, **kwargs)
        self.slug = text.slugify(self.title, allow_unicode=True)

