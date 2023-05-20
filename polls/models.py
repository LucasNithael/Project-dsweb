from django.db import models
from user.models import User

class Question(models.Model):
    text = models.CharField(max_length=150)
    pub_date = models.DateField()
    author = models.ForeignKey(
        User, related_name='author',
        on_delete = models.CASCADE, null=True
    )
    def __str__(self):
        return f"{self.id} - {self.text}"

class Alternative(models.Model):
    text = models.CharField(max_length=80)
    vote = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    def __str__(self):
        return f"{self.id} - {self.text}"