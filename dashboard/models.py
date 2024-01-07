from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_images')
    def __str__(self):
        return self.user.username
##
def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "category/images/%s.%s"%(instance.id,extension)
##
class InformaionSite(models.Model):
    name = models.CharField(max_length=60 , default='name')
    image_icon = models.ImageField(upload_to='logo/', null=True, blank=True)
    image_footer = models.ImageField(upload_to='logo/', null=True, blank=True)
    title_name =  models.CharField(max_length=150)
    address = models.CharField(max_length=60)
    email = models.EmailField(null=True, blank=True)
    telephone = models.IntegerField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    whatsapp = models.URLField(null=True, blank=True)
    maps = models.CharField(max_length=200, null=True, blank=True)
    pubilished_at = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True, blank=True)

    count_custemor = models.IntegerField()
    compalete_project = models.IntegerField()
    


##

def arabic_slugify(str):
    str = str.replace(" ", "-")
    str = str.replace(",", "-")
    str = str.replace("(", "-")
    str = str.replace(")", "")
    str = str.replace("?", "")
    return str
##
class Post(models.Model):
    user = models.ForeignKey(User, related_name='user_blogs', on_delete=models.CASCADE)
    title  = models.CharField(max_length=60 ,blank=True, null=True)
    image = models.ImageField(upload_to='post/', null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    create_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=60,unique=True, allow_unicode=True, blank=True, null=True)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

##
class Category(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)

    image = models.ImageField(upload_to='category/', null=False, blank=False)
    description = models.TextField(null=True, blank=False)
    create_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=60,unique=True, allow_unicode=True, blank=True, null=True)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            if not self.slug:
                self.slug = arabic_slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        


    def __str__(self):
        return self.name
##
class Project(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category')
    name  = models.CharField(max_length=60 ,blank=False, null=True)
    image = models.ImageField(upload_to='category/', null=False, blank=False)
    location  = models.CharField(max_length=60 ,blank=True, null=True)
    description = models.TextField(null=True, blank=False)
    create_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=60,unique=True, allow_unicode=True, blank=True, null=True)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            if not self.slug:
                self.slug = arabic_slugify(self.name)
        super(Project, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
##
class Image(models.Model):
    image = models.ImageField(upload_to=image_upload)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='project')
    create_date = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.category
    @property
   
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
##
class Pages(models.Model):
    title  = models.CharField(max_length=60, null=False, blank=False)
    image = models.ImageField(upload_to='home/', null=False, blank=False)
    description = models.TextField(null=True, blank=False)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PageAbout(models.Model):
    title_head  = models.CharField(max_length=60, null=False, blank=False)
    title_goal  = models.CharField(max_length=60, null=False, blank=False)
    description = models.TextField(null=True, blank=False)

   # image = models.ImageField(upload_to='services/', null=False, blank=False)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title_head

