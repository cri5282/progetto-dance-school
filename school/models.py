from django.db import models
from schoolmanagement.models import School


class DayOfTheWeek(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.number} - {self.name}"


class Classroom(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.name} (cap. {self.capacity})"


class Course(models.Model):
    subject = models.CharField(max_length=100)
    starting_hour = models.IntegerField()
    day_of_the_week = models.ForeignKey(
        DayOfTheWeek, on_delete=models.CASCADE, related_name="courses"
    )
    classroom = models.ForeignKey(
        Classroom, on_delete=models.CASCADE, related_name="courses"
    )
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="courses"
    )

    def __str__(self):
        return self.subject
