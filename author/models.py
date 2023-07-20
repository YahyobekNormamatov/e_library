from django.db import models

# Create your models here.


class AuthorModel(models.Model):
    image = models.ImageField(upload_to ='upload/author/')
    name = models.CharField(max_length=65, default='Nomalum')
    last_name = models.CharField(max_length=65, default='Nomalum')
    info = models.TextField()
    date_birth = models.DateField(default='01-01-2023')
    date_dead = models.DateField(default='01-01-2023')
    contury = models.CharField(max_length=50, default='')



    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'Author'
