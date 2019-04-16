from django.db import models
from django.core.validators import MinLengthValidator

class Constellation(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Constellation must be greater than 1 character")]
    )

    def __str__(self):
        return self.name

class Star(models.Model):
    nickname = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")]
    )
    number = models.PositiveIntegerField()
    location = models.CharField(max_length=300)
    constellation = models.ForeignKey('Constellation', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname
