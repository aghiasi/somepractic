from django.db import models

# Create your models here.

class Articles(models.Model):
  title = models.CharField(max_length=15)
  slug = models.TextField(max_length=10)
  body = models.TextField(max_length=200)
  date = models.DateTimeField(auto_now_add=True)
  # thumbnail
  image =models.ImageField(default='default.jpg')
  # author
  def __str__(self):
   return self.title
  def snipet(self):
    return self.body[:50] +' ...'