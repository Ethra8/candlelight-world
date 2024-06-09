from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Room(models.Model):
    EXPERIENCE_CATEGORIES = (
        ('MED', 'Medieval Castle'),
        ('REN', 'Renaissance'),
        ('VIC', 'Victorian Mansion'),
        ('DRA', 'Dracula Castle'),
        ('FAF', 'Fairy Forest'),
    )
    
    category = models.CharField(max_length=3, choices=EXPERIENCE_CATEGORIES)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    id = models.UUIDField(primary_key=True, default=1, editable=False, unique=True)
    image = CloudinaryField('image')

    def __str__(self):
        return self.display_name