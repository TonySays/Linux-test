from socket import TIPC_IMPORTANCE
from django.db import models
from datetime import datetime

# Create your models here.
class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("date published", default= datetime.now)

def _str_(self):
    return self.tutorial_title 


