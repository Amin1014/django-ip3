from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.db.models import Avg, Max, Min
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
import datetime as dt

class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_tags(self):
        self.save()

    def delete_tags(self):
        self.delete()


class Location(models.Model):
    name = models.CharField(max_length=30)


    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.TextField(max_length=200, null=True, blank=True, default="title")
    project_image = models.ImageField(upload_to='picture/', null=True, blank=True)
    description = models.TextField()
    project_url=models.URLField(max_length=250)

    def average_design(self):
        design_ratings = list(map(lambda x: x.design_rating, self.reviews.all()))
        return (design_ratings)

    def average_usability(self):
        usability_ratings = list(map(lambda x: x.usability_rating, self.reviews.all()))
        return (usability_ratings)

    def average_content(self):
        content_ratings = list(map(lambda x: x.content_rating, self.reviews.all()))
        return (content_ratings)

    def save_project(self):
        self.save()

    @classmethod
    def delete_project_by_id(cls, id):
        projects = cls.objects.filter(pk=id)
        projects.delete()

    @classmethod
    def get_project_by_id(cls, id):
        projects = cls.objects.get(pk=id)
        return projects

    @classmethod
    def search_projects(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

    @classmethod
    def update_project(cls, id):
        projects = cls.objects.filter(id=id).update(id=id)
        return projects

    @classmethod
    def update_description(cls, id):
        projects = cls.objects.filter(id=id).update(id=id)
        return projects

    def __str__(self):
        return self.title


class Profile(models.Model):
    class Meta:
        db_table = 'profile'

    bio = models.TextField(max_length=200, null=True, blank=True, default="bio")
    profile_pic = models.ImageField(upload_to='picture/', null=True, blank=True, default= 0)
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="profile")
    project=models.ForeignKey(Project, null=True,on_delete=models.CASCADE)
    contact=models.IntegerField(default=0)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


    @classmethod
    def search_users(cls, search_term):
        profiles = cls.objects.filter(user__username__icontains=search_term)
        return profiles

    @property
    def image_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url

    def __str__(self):
        return self.user.username


class Image(models.Model):
    image=models.ImageField(upload_to='picture/', )
    name = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="images")
    description=models.TextField()
    location=models.ForeignKey(Location, null=True,on_delete=models.CASCADE)
    tags=models.ManyToManyField(tags, blank=True)
    likes = models.IntegerField(default=0)
    comments= models.TextField(blank=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    @classmethod
    def delete_image_by_id(cls, id):
        pictures = cls.objects.filter(pk=id)
        pictures.delete()

    @classmethod
    def get_image_by_id(cls, id):
        pictures = cls.objects.get(pk=id)
        return pictures

    @classmethod
    def filter_by_tag(cls, tags):
        pictures = cls.objects.filter(tags=tags)
        return pictures

    @classmethod
    def filter_by_location(cls, location):
        pictures = cls.objects.filter(location=location)
        return pictures

    @classmethod
    def search_image(cls, search_term):
        pictures = cls.objects.filter(name__icontains=search_term)
        return pictures

    @classmethod
    def update_image(cls, id):
        pictures=cls.objects.filter(id=id).update(id=id)
        return pictures

    @classmethod
    def update_description(cls, id):
        pictures = cls.objects.filter(id=id).update(id=id)
        return pictures

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='reviews')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="reviews", null=True, blank=True)
    comment = models.TextField()
    design_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    usability_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    content_rating = models.IntegerField(choices=RATING_CHOICES, default=0)

    def save_comment(self):
        self.save()

    def get_comment(self, id):
        comments = Review.objects.filter(image_id =id)
        return comments

    def __str__(self):
        return self.comment

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    value = models.IntegerField(default=True, null=True, blank=True)

    def save_like(self):
        self.save()

    def __str__(self):
        return str(self.user) + ':' + str(self.image) + ':' + str(self.value)

    class Meta:
        unique_together = ("user", "image", "value")