from django.test import TestCase

from exemplo.models import Example
from django.core.exceptions import ValidationError

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'projeto_dev_I.settings'


class ExampleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Example.objects.create(nome="Maria")

    def test_example_atributo_nome(self):
        example = Example.objects.get(id=1)
        expected_nome = "Maria"
        self.assertEqual(expected_nome, example.nome, "Maria")

    def test_example_atributo_torcedores(self):
        example = Example.objects.get(id=1)
        expected_torcedores = 0
        self.assertEqual(expected_torcedores, example.torcedores)

    def test_example_metodo_str(self):
        example = Example.objects.get(id=1)
        expected_object_name = example.__str__()
        self.assertEqual(expected_object_name, str(example))

    def text_example_atributo_nome_max_length(self):
        nome_max_length = Example._meta.get_field('nome').max_length
        nome_longo = "a" * (nome_max_length + 1)
        example = Example(nome=nome_longo)

        with self.assertRaises(ValidationError):
            example.full_clean()
