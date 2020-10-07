from django.db import models

# Create your models here.
class FeaturedArt(models.Model):
    image = models.ImageField(upload_to = 'images/FeaturedArt', blank = True, null = False)

    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.created_at)
