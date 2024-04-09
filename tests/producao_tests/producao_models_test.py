from django.test import TestCase

from producao.models import Producao

from producao.constantesProducao import AdvisoryCertificate, Genre

from datetime import date, timedelta


class ProducaoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.title = "Título teste"
        cls.advisory_certificate = AdvisoryCertificate.GENERAL_AUDIENCES
        cls.length = timedelta(minutes=120)
        cls.genre = Genre.ACTION
        cls.trendimeter = 10
        cls.reviews = 5.0
        cls.specs = "Especificações teste"
        cls.synopsis = "Sinopse teste"
        cls.release_date = date.today()

        Producao.objects.create(
            title=cls.title,
            advisory_certificate=cls.advisory_certificate,
            length=cls.length,
            genre=cls.genre,
            trendimeter=cls.trendimeter,
            reviews=cls.reviews,
            specs=cls.specs,
            synopsis=cls.synopsis,
            release_date=cls.release_date
        )

    def testa_label_de_atributos(self):
        producao = Producao.objects.get(id=1)
        label_de_atributos = {
            'title': 'title',
            'advisory_certificate': 'advisory certificate',
            'length': 'length',
            'genre': 'genre',
            'trendimeter': 'trendimeter',
            'reviews': 'reviews',
            'specs': 'specs',
            'synopsis': 'synopsis',
            'release_date': 'release date',
        }
        for field, expected_label in label_de_atributos.items():
            with self.subTest(field=field):
                field_label = producao._meta.get_field(field).verbose_name
                self.assertEqual(field_label, expected_label)

    def test_max_lengths(self):
        producao = Producao.objects.get(id=1)
        max_lengths = {
            'title': 100,
            'advisory_certificate': 20,
            'genre': 20,
            'specs': 50,
            'synopsis': 500,
        }
        for field, expected_max_length in max_lengths.items():
            with self.subTest(field=field):
                max_length = producao._meta.get_field(field).max_length
                self.assertEqual(max_length, expected_max_length)

    def test_default_values(self):
        producao = Producao.objects.get(id=1)
        self.assertEqual(producao.trendimeter, self.trendimeter)
        self.assertEqual(producao.reviews, self.reviews)

    def test_str_method(self):
        producao = Producao.objects.get(id=1)
        self.assertEqual(str(producao), self.title)

# Tests for abstract models
# def test_field_definitions(self):
    #     expected_lengths = {
    #         'title': {'max_length': 100, 'min_length': 1},
    #         'advisory_certificate': {'max_length': 20, 'min_length': 1},
    #         'genre': {'max_length': 20, 'min_length': 1},
    #         'specs': {'max_length': 50, 'min_length': 5},
    #         'synopsis': {'max_length': 500, 'min_length': 10},
    #     }
    #
    #     for field, expected_length in expected_lengths.items():
    #         with self.subTest(field=field):
    #             field = Producao._meta.get_field(field)
    #             self.assertEqual(field.max_length, expected_length['max_length'])
    #
    #             # Get the MinLengthValidator for this field
    #             min_length_validator = next((v for v in field.validators if isinstance(v, MinLengthValidator)), None)
    #             if min_length_validator is not None:
    #                 self.assertEqual(min_length_validator.limit_value, expected_length['min_length'])
    #
    # def test_default_values(self):
    #     # If there are fields with default values, you can test them here
    #     pass