from django.db import models


class userPreference(models.Model):
    name = models.CharField(max_length=100, unique=True, error_messages={'unique':"This name has already been registered."})
    favourite_colour = models.CharField(max_length = 100,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    #dateCompleted = models.DateTimeField(null=True,blank=True)
    #cat = models.BooleanField(default=False)
    #dog = models.BooleanField(default=False)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    CAT_DOG = ((0,'Cat'), (1, 'Dog'))
    cat_or_dog = models.PositiveSmallIntegerField(choices=CAT_DOG, default=0, verbose_name='Cat/Dog')

    def __str__(self):
        return self.name