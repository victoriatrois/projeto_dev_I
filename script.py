from exemplo.models.example import Example
from django.contrib.auth import get_user_model
from random import randint

User = get_user_model()
User.objects.create_superuser("test_superuser", "test_superuser@user.com", "test_superuser_password")

gremio = Example(nome="Grêmio")
gremio.save()

# 996520732 Cassio