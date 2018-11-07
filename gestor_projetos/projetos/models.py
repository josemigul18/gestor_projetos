from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=30)
    username_manager = models.CharField(max_length=30)
    budget = models.IntegerField()



    def __init__(self, *args, **kwargs):
        models.Model.__init__(self, *args, **kwargs)


    def __str__(self):
        return self.name

class Assignment(models.Model):
    name = models.CharField(max_length=30)
    project_id = models.IntegerField()
    programer_id = models.IntegerField()
    finished = models.BooleanField(default=False)
    date = models.DateField()
    description = models.CharField(max_length=200)

    def __init__(self, *args, **kwargs):
        models.Model.__init__(self, *args, **kwargs)


    def __str__(self):
        return self.name