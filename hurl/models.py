from django.db import models

# Create your models here.
class Url(models.Model):
  urlname = models.URLField(primary_key=True)
  #alias1 = models.URLField()
  #alias2 = models.URLField()


