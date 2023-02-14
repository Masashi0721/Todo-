from django.db import models

# Create your models here.

Categorychoices = [
    ("job", "仕事"),
    ("hobby", "趣味"),
    ("university", "大学"),
    ("others", "その他")
]

class Event(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    event_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=Categorychoices, null=True)
