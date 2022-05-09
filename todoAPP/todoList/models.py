from django.db import models

# Create your models here.
class Daily(models.Model):
    date = models.DateTimeField()
    title = models.TextField(max_length=30)
    content = models.TextField()

    def __str__(self):
        return self.title

class daily_thing(models.Model):
    thing = models.ForeignKey(Daily, on_delete=models.CASCADE)
    create_date = models.DateTimeField()
