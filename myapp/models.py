from django.db import models

# Create your models here.

class newsletter(models.Model):
    username = models.CharField(max_length=256)
    email = models.EmailField(max_length=56)

    def __str__(self):
        return self.username

class EmsImg(models.Model):
    # etitle = models.CharField(max_length=100)
    image = models.ImageField(upload_to="image/")


class SpaceImg(models.Model):
    # title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="image/")

class AcvImg(models.Model):
    # title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")

class Contact(models.Model):
    yourname = models.CharField(max_length=50)
    subject = models.CharField(max_length=120)
    gmail = models.EmailField(max_length=56)
    mobile = models.CharField(max_length=15, default='')  # Provide a default value
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.yourname

class JobApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    position_applied_for = models.CharField(max_length=50)
    experience = models.CharField(max_length=10)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name