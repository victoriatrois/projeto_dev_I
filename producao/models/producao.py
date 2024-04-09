from producao.models.base import BaseModel
from producao.constantesProducao import AdvisoryCertificate, Genre

from django.core.validators import MinLengthValidator
from django.db import models


class Producao(BaseModel):
    title = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(1)]
    )
    advisory_certificate = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(1)],
        choices=AdvisoryCertificate.choices,
        default=AdvisoryCertificate.PARENTS_STRONGLY_CAUTIONED
    )
    length = models.DurationField()
    genre = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(1)],
        choices=Genre.choices,
        default=Genre.ACTION

    )
    trendimeter = models.IntegerField()
    reviews = models.FloatField()
    specs = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(5)]
    )
    synopsis = models.TextField(
        max_length=500,
        validators=[MinLengthValidator(10)]
    )
    release_date = models.DateField()

    class Meta:
        abstract = False

    def __str__(self):
        return self.title
