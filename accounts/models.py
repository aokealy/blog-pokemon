from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import FileExtensionValidator


# Create your models here.
class AccountModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='account', validators=[FileExtensionValidator(['jpg', 'png'])])

    def __str__(self):
        return self.user.username