from django.db import models
from datetime import datetime
# Create your models here.

# migration need to be done when you add models

class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length = 200) #when you have to set a max limit
    tutorial_content = models.TextField()               #no limit - more like an article body
    tutorial_published = models.DateTimeField("date published", default=datetime.now())

    def __str__(self):
        return self.tutorial_title

