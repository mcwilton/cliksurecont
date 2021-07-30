from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    phone_number = models.IntegerField(blank=False, default='')
    created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        ret = self.name
        return ret

    class Meta:
        unique_together = ['name']


