from django.db import models

# Create your models here.
class RandomImage(models.Model):
     image = models.ImageField(upload_to="media/")

     class Meta:
          varbose_name = "Generated Image"

          