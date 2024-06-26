from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.question_text

    @admin.display(boolean=True, ordering="pub_date", description="Published recently?")
    def was_published_recently(self) -> bool:
        return (
            datetime.timedelta(days=0)
            < timezone.now() - self.pub_date
            < datetime.timedelta(days=1)
        )


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.question}: {self.choice_text}"
