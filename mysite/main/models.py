from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
from django.db import models

# Create your models here.
class Professor(models.Model):
    code = models.CharField(max_length = 3, unique = 'True')
    name = models.CharField(max_length = 30)
    rating = models.PositiveIntegerField(default = 2, validators = [MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return u'%s %s %i' % (self.code, self.name, self.rating)
    

class Module(models.Model):
    code = models.CharField(max_length = 3)
    name = models.CharField(max_length = 30)
    year = models.IntegerField()
    semester = models.IntegerField()
    professors = models.ManyToManyField(Professor)
    rating = models.PositiveIntegerField(default = 2, validators = [MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return u'%s %s %i %i %i' % (self.code, self.name, self.year, self.semester, self.rating)


class Rating(models.Model):
    module_code = models.CharField(max_length = 3) 
    value = models.PositiveIntegerField(default = 2, validators = [MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return u'%s %i' % (self.module_code, self.value)