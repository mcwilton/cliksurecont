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



class Department(models.Model):
    # define department name and description columns, the id column will be added automatically.
    dept_name = models.CharField(max_length=1000)
    dept_desc = models.CharField(max_length=1000)
    # this is a inner class which is used to define unique index columns. You can specify multiple columns in a list or tuple.
    
    def __str__(self):
        ret = self.dept_name + ',' + self.dept_desc
        return ret

    class Meta:
        unique_together = ['dept_name']
