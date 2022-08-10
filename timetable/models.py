from django.db import models
from django.utils.translation import gettext_lazy as __

# Create your models here.
class Position(models.Model):
    name = models.CharField(__("position of teacher"), max_length=80)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'api'

class Teacher(models.Model):
    first_name = models.CharField(__('first name'), max_length=40)
    last_name = models.CharField(__('last name'), max_length=40, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_DEFAULT, related_name='teachers', default=1)

    def __str__(self):
        return f"{self.position} {self.last_name}.{self.first_name[:1]}"

    class Meta:
        app_label = 'api'
    

class Timetable(models.Model):
    time_from = models.TimeField(__('from'))
    time_until = models.TimeField(__('until'))

    def __str__(self):
        return f"{self.time_from} - {self.time_until}"

    class Meta:
        app_label = "api"
    
class Branch(models.Model):
    name = models.CharField(__("name of the branch"), max_length=255)
    abbreviation = models.CharField(__("abbreviation"), max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "api"

class Group(models.Model):
    name = models.CharField(__('name of the group'), max_length=255)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='groups')
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'api'    

class Room(models.Model):
    room_number = models.CharField(__('number of the room'), max_length=20)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.room_number
    
    class Meta:
        app_label = 'api'

class LessonName(models.Model):
    name = models.CharField(__("name of the lesson"), max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'api'

class LessonType(models.Model):
    name = models.CharField(__('type of lessons'), max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'api'

class Lesson(models.Model):
    name = models.ForeignKey(LessonName, on_delete=models.CASCADE, related_name='lessons')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='lessons')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='lessons')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='lessons')
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE)
    lesson_type = models.ForeignKey(LessonType, on_delete=models.CASCADE, related_name='lessons', default=1)
    even_week = models.BooleanField(__('even / odd week'), null=False)
    DAYS = (
        (1, __('Monday')),
        (2, __('Tuesday')),
        (3, __('Wednesday')),
        (4, __('Thursday')),
        (5, __('Friday')),
        (6, __('Saturday')),
        (7, __('Sunday')),
    )
    day = models.IntegerField(
        __('day of the week'), choices=DAYS)

    def __str__(self):
        return f'{self.name}, {self.day}'

    class Meta:
        app_label = 'api'
        ordering = ['day', 'timetable']