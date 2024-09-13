from django.db import models
from embed_video.fields import EmbedVideoField


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=150)
    titleTwo = models.CharField(max_length=150)
    banar = models.ImageField(upload_to='BanarImage/')
    is_active = models.BooleanField(default=True)


class About_coching(models.Model):
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField()

class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)
    discription =models.TextField(null=True,blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Module(models.Model):
    course_title = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, unique=True)
    discription =models.TextField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class videos(models.Model):
   title = models.CharField(max_length=100)
   addDate = models.DateTimeField(auto_now_add=True)
   url = EmbedVideoField()
   is_active = models.BooleanField(default=True)

   def __str__(self):
       return str(self.title)

   class Meta:
       ordering = ['-addDate']

class faq(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.title
class faq_details(models.Model):
    faq_title = models.ForeignKey(faq, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.TextField()
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.question


class studentRegistration(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=11, unique=True)
    def __str__(self):
        return self.last_name