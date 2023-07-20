from django.db import models
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class UserModel(models.Model):
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    phone_number = PhoneNumberField(blank = True)
    email = models.EmailField(max_length=100, blank= True)
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        db_table = 'person'