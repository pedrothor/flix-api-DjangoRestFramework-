from django.db import models


POSITION_CHOICES = [
    ('Director', 'Director'),
    ('Sound designer', 'Sound designer'),
    ('Assistant Director', 'Assistant Director'),
    ('Producer', 'Producer'),
    ('Production Assistant', 'Production Assistant'),
    ('Makeup artist', 'Makeup artist'),
    ('Camera operator', 'Camera operator'),
    ('Script supervisor', 'Script supervisor'),
]


class Employee(models.Model):
    name = models.CharField(max_length=200)
    birth = models.DateField()
    position = models.CharField(max_length=200, choices=POSITION_CHOICES)
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
