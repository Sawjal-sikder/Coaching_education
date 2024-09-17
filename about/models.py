from django.db import models


# Model for main coaching center information
class AboutCoachingCenter(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='coaching_center_images/')  # Directory for uploaded images
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


# Model for additional details about the coaching center
class AboutCoachingDetails(models.Model):
    accenter = models.ForeignKey(AboutCoachingCenter, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class OurValues(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


# Model for additional details about the coaching center
class OurValuesDetails(models.Model):
    OValues = models.ForeignKey(AboutCoachingCenter, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
