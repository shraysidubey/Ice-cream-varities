from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    blog_name = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.blog_name