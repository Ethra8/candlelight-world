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
        ('MEDIEVAL CASTLE', 'MEDIEVAL CASTLE'),
        ('RENAISSANCE VILLA', 'RENAISSANCE VILLA'),
        ('VICTORIAN MANSION', 'VICTORIAN MANSION'),
        ('DRACULA CASTLE', 'DRACULA CASTLE'),
        ('FAIRY FOREST', 'FAIRY FOREST'),
    )
    
    display_name = models.CharField(max_length=100, choices=EXPERIENCE_DISPLAY)
    category = models.CharField(max_length=3, choices=EXPERIENCE_CATEGORIES)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    image = CloudinaryField('image')
    image_dinning = CloudinaryField('image')
    image_extra = CloudinaryField('image')
    
    
    def __str__(self):
        return self.display_name