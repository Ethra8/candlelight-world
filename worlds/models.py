from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Room(models.Model):
    EXPERIENCE_CATEGORIES = (
        ('MED', 'Medieval'),
        ('REN', 'Renaissance'),
        ('VIC', 'Victorian'),
        ('DRA', 'Dracula'),
        ('FAF', 'Fairy Forest'),
    )

    EXPERIENCE_DISPLAY = (
        ('MEDCAS', 'MEDIEVAL CASTLE'),
        ('RENVIL', 'RENAISSANCE VILLA'),
        ('VICMAN', 'VICTORIAN MANSION'),
        ('DRACAS', 'DRACULA CASTLE'),
        ('FAIFOR', 'FAIRY FOREST'),
    )
    
    display_name = models.CharField(max_length=100, choices=EXPERIENCE_DISPLAY)
    category = models.CharField(max_length=3, choices=EXPERIENCE_CATEGORIES)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    image = CloudinaryField('image')
    
    
    def __str__(self):
        return self.display_name