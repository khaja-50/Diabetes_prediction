from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class patient(models.Model):
    date=models.DateField(default= timezone.now)
    name = models.CharField(max_length=255, null=False)
    so = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    Pregnancies = models.IntegerField(default=0)
    Glucose = models.IntegerField(default=0)
    BloodPressure = models.IntegerField(default=0)
    SkinThickness = models.IntegerField(default=0)
    Insulin = models.IntegerField(default=0)
    BMI = models.DecimalField(max_digits=10, decimal_places=5, default=0.0)
    DiabetesPedigreeFunction = models.DecimalField(max_digits=10, decimal_places=5, default=0.0)
    Age = models.IntegerField(default=0)
    Outcome = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.name} - {self.address}"




