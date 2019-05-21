from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('publish')
    content = models.TextField()

    def __str__(self):
        return self.content[:20]
    
    def summary(self):
        return self.content[:10]
