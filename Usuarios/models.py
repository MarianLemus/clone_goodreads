from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.postgres.fields import JSONField


class User(AbstractBaseUser, PermissionsMixin, models.Model):

    # unique, no se van a repetir
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=40)
    apaterno = models.CharField(max_length=25)
    amaterno = models.CharField(max_length=25)
    email = models.EmailField(unique=True, max_length=50)
    sexo = models.CharField(choices=(('M','Mujer'),('H','Hombre')), max_length=16,blank=True)
    biblioteca = models.CharField(max_length=25)
    # intermediario entre trans de cada modelo, object managaer de cada modelo
    objects = UserManager()

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
