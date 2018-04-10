from django.db import models

# Create your models here.
class Comment(models.Model):
    postId = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return self.name
