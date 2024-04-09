from exemplo.models.base import *
from django.core.validators import MinValueValidator


class Example(BaseModel):
    nome = models.CharField(
        max_length=200,
        help_text="Nome do exemplo",
    )

    torcedores = models.IntegerField(
        default=0,
        help_text="Número de torcedores",
        validators=[MinValueValidator(0)],
    )

    class Meta:
        abstract = False

    def __str__(self):
        return f"{self.id} - {self.nome}: {self.torcedores}"
