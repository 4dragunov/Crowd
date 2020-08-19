from django.db import models
from django.shortcuts import reverse, redirect


from django.utils.text import slugify
from django.contrib.auth import get_user_model

from django.contrib.contenttypes.fields import GenericRelation

from time import time
from django.utils import timezone


User = get_user_model()


def gen_slug(s):
    new_slug = (slugify(s, allow_unicode=True))
    return new_slug + '-' + str(int(time()))

class Challenge(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateField(auto_now_add=True)
    date_remaining = models.DateField(auto_now_add=False, blank=True, null=True)
    prize = models.IntegerField(default=1000)
    categories = models.ManyToManyField('Category', related_name='challenges')
    challenge_author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="challenges", null=True)
    image = models.ImageField(blank=True, upload_to='challenge/', null=True)



    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def days_remaning(self):
        days_remaning = self.date_remaining - self.date_pub
        return days_remaning.days


    def get_absolute_url(self):
        return reverse('challenge_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('challenge_update_url', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('challenge_delete_url', kwargs={'slug': self.slug})

class Answer(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.SET_NULL, related_name='answers', null=True)
    title = models.CharField(max_length=150, db_index=True)
    #slug = models.ForeignKey(Challenge.slug, on_delete=models.SET_NULL, related_name='challenge_slug', null=True)
    body = models.TextField(blank=True)
    date_pub = models.DateField(auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="answers", null=True)

    answer_like = models.ManyToManyField(User, related_name='answer_liked', blank=True)
    answer_dislike = models.ManyToManyField(User, related_name='answer_disliked', blank=True)




    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("blog_detail", args=[str(self.pk)])
    def get_absolute_url(self):
        return reverse('answer_create_url', kwargs={'slug': self.slug})



class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail_url', kwargs={'slug': self.slug})


    def get_update_url(self):
        return reverse('category_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('category_delete_url', kwargs={'slug': self.slug})


