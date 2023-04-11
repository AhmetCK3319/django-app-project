from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Category(models.Model):
    name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    slug=models.SlugField(null=False,blank=True, unique=True,db_index=True,editable=False)

    def __str__(self):
        return f"{self.name}"
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.name)
        super().save(*args, **kwargs)  



class Blog(models.Model):

    title=models.CharField(max_length=200)
    images=models.ImageField(upload_to='blogs')
    descriptions=RichTextField()
    is_active=models.BooleanField(default=False)
    is_home=models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    slug=models.SlugField(null=False,blank=True, unique=True,db_index=True,editable=False)
    categories=models.ManyToManyField(Category)


    def __str__(self):
        return f"{self.title} "

    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args, **kwargs)    
    
        
