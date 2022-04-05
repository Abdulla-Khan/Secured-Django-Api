from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 10,null=True)
    image = models.CharField(max_length = 200,null=True)
    rent = models.CharField(max_length = 10,null=True)
     

    def __str___(self):
        return self.title