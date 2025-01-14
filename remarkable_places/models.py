from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class RemarkablePlace(models.Model):

    name = models.CharField(max_length=255) 
    location = models.PointField()
    rating = models.PositiveIntegerField( 
        default=3,
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )

    def __str__(self):
        return self.name