from django.db import models

CONSERVATION_CHOICES = (
    ('Extinct', 'EX'),
    ('Etinct in the wild', 'EW'),
    ('Crtically Endangered', 'CR'),
    ('Endangered', 'EN'),
    ('Vulnerable', 'VU'),
    ('Near threatened', 'NT'),
    ('Least concern', 'LC'),
    ('Not evaluated', 'NE')
)

# Create your models here.
class Bird(models.Model):
    watson_id = models.IntegerField(default=0)
    common_name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    wingspan = models.CharField(max_length=100)
    mass = models.IntegerField(default=0)
    lifespan = models.IntegerField(default=0)
    conservation_status = models.CharField(max_length=100, choices=CONSERVATION_CHOICES, default='Not evaluated')
    speed = models.IntegerField(default=0)
    fact = models.CharField(max_length=100)
    
    def __str__(self):
        pass

class ModelWithFileField(models.Model):
    user_photo = models.ImageField(upload_to='results/')