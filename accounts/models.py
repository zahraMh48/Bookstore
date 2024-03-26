from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser): # baraye charfield null ro True nazar chon string khali dare ""
    age = models.PositiveIntegerField(null=True, blank=True)  # null hichi tosh nist va mal database, but blank baraye form ejaze mide khali bashe (validation)
