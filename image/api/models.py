from django.db import models
import os

# def get_image_size(image):
#     """Calculate the image size in mega bytes."""
#     # Get the size of the image in bytes
    
#     return  / (1024 * 1024)
    

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    # compressed_image = models.ImageField(upload_to='images/', blank=True)
    name = models.CharField(max_length=100, blank=True)
    size = models.FloatField(editable=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ": " + str(self.image.size/ (1024*1024)) + " MB"
    
    def save(self, *args, **kwargs):
        # Calculate the size before saving
        if not self.pk:  # Only calculate size when creating a new instance
            self.size = self.image.size / (1024 * 1024)
        
        if not self.name:
            self.name = self.image.name
        
        super(Image, self).save(*args, **kwargs)

    def upload(self):
        self.save()
        return self.id

    
