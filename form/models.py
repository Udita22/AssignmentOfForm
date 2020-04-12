from django.db import models

# Create your models here.
class createForm(models.Model):
    name = models.CharField(max_length=100, unique=True)
    favourite_colour = models.CharField(max_length = 100,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    #dateCompleted = models.DateTimeField(null=True,blank=True)
    cat = models.BooleanField(default=False)
    dog = models.BooleanField(default=False)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name