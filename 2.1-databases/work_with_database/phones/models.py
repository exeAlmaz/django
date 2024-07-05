from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.URLField(max_length=512)
    release_date = models.CharField(max_length=100)
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)