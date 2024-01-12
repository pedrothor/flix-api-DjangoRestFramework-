from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movies


class Review(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(validators=[
        MinValueValidator(0, 'Deve ser maior ou igual a 0 (zero)'),
        MaxValueValidator(5, 'Deve ser menor ou igual a 5 (cinco)')
    ])
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.movie


