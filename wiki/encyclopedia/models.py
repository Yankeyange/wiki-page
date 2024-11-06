from django.db import models

# créons nos modèles ici

class Topic(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()

  def __str__(self):
    return self.title

class Entry(models.Model):
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
  text = models.TextField()

  class Meta:
    verbose_name_plural = "entries"

  def __str__(self):
    return f"{self.text[:50]}.."