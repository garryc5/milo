from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
EXERCISES = (
    ('R', 'Running'),
    ('A', 'Arms'),
    ('L', 'Legs'),
    ('C', 'Core'),
)

class Profile(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField('date of birth')
    picture = models.CharField(max_length=100)
    sport_bio = models.TextField(max_length=250)
    goal = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    # return reverse('detail', kwargs={'cat_id': self.id})


class Activity(models.Model):
    activity = models.CharField(
        max_length=1,
        choices=EXERCISES,
        default=EXERCISES[0][0]
    )
    weight = models.IntegerField()
    reps = models.IntegerField()
    # running for reps will be miles ran
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Calories(models.Model):
    calories_in = models.IntegerField()
    calories_out = models.IntegerField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
class Photo(models.Model):
    url = models.CharField(max_length=200)
    image = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for image_id {self.image_id} @{self.url}"