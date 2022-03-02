from django.db import models

# Create your models here.

class Danisma(models.Model):
    isim = models.CharField(max_length=24)
    mail = models.EmailField()
    metin = models.TextField(max_length=10000)

    def __str__(self):
        return self.mail