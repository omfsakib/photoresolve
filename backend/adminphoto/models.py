from django.db import models

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=200,blank = True, null=True)
    description = models.TextField(max_length=2000, null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    rate = models.FloatField(default=0, null = True,blank = True)
    after = models.ImageField(default="image-placeholder-500x500.jpg",null = True,blank = True)
    button_name = models.CharField(max_length=200,blank = True, null=True)

    def __str__(self):
        return self.name

    
class SubServices(models.Model):
    service =  models.ForeignKey(Services, null=True, on_delete= models.CASCADE)
    name = models.CharField(max_length=200,blank = True, null=True)
    description = models.TextField(max_length=2000, null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    rate = models.FloatField(default=0, null = True,blank = True)
    before = models.ImageField(default="image-placeholder-500x500.jpg",null = True,blank = True)
    after = models.FileField(default="image-placeholder-500x500.jpg",null = True,blank = True)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    thumb = models.ImageField(default="image-placeholder-500x500.jpg",null = True,blank = True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Pricing(models.Model):
    name = models.CharField(max_length=200,blank = True, null=True)
    rate = models.FloatField(default=0, null = True,blank = True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    description = models.TextField(blank=True)
    short_info = models.TextField(blank=True)
    caption = models.CharField(max_length=200,null = True,blank = True)
    phone = models.CharField(max_length=20,null = True,blank = True)
    email = models.EmailField(null = True,blank = True)
    address = models.CharField(max_length=200,null = True,blank = True)
    
    def __str__(self):
        return self.caption
    
class Queries(models.Model):
    name = models.CharField(max_length=200,blank = True, null=True)
    email = models.EmailField(blank = True, null=True)
    description = models.TextField(max_length=2000, null=True,blank=True)
    
    def __str__(self):
        return self.name
    

class Logo(models.Model):
    svg_code = models.TextField()


class Navigation(models.Model):
    name = models.CharField(max_length=100)
    href = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Slide(models.Model):
    text = models.CharField(max_length=200)
    class_name = models.CharField(max_length=50)

    def __str__(self):
        return self.text

class SlideInfo(models.Model):
    caption = models.CharField(max_length=200)
    cover = models.ImageField(null = True,blank = True)

    def __str__(self):
        return self.caption
        

class TermsAndConditions(models.Model):
    terms =  models.TextField(max_length=200000,blank = True, null=True)