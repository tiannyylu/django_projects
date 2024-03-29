from django.db import models
from django.core.validators import MinLengthValidator

class Kind(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Kind must be greater than 1 character")]
    )

    def __str__(self):
        return self.name

class Pet(models.Model):
    nickname = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")]
    )
    weight = models.PositiveIntegerField()
    foods = models.CharField(max_length=300)
    kind = models.ForeignKey('Kind', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname
