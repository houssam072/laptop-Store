from django.db import models

# Create your models here.


def image_upload(instance, filename):
    image_name, extension = filename.split('.')
    return '%s/%s/%s.%s'%('images',instance.__class__.__name__,image_name, extension)


class Category(models.Model):
    cat_name = models.CharField(max_length = 120, unique = True)
    cat_image = models.ImageField(upload_to=image_upload)

    
    def __str__(self): 
        return self.cat_name