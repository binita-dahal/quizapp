from django.db import models

# Create your models here.
# models to store quiz questions and answerr
class Question(models.Model):
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=500)
    option2 = models.CharField(max_length=500)
    option3 = models.CharField(max_length=500)
    option4 = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    # integer field to store difficulty level of question
    difficulty = models.IntegerField(default=1)

    def __str__(self):
        return self.question