from django.db import models

# Create your models here.
class Feedback(models.Model):

    subjec = (
        ('SalesMarketing' , 'SalesMarketing'),
        ('Creative Design' , 'Creative Design'),
        ('UIUX' , 'UIUX')
    )

    name = models.CharField(max_length=255)
    email = models.EmailField()
    subjects = models.CharField(max_length=255, choices=subjec)
    message = models.TextField()

    def __str_(self):
        return self.name
