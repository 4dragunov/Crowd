from django.db import models
from django.shortcuts import reverse

from django.contrib.auth import get_user_model

from django.utils.text import slugify

from time import time
from datetime import datetime



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
    prize = models.CharField(max_length=20, default=10)
    categories = models.ManyToManyField('Category', related_name='challenges')
    # tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def __str__(self):
        return self.title



    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)



    def get_absolute_url(self):
        return reverse('challenge_detail_url', kwargs={'slug': self.slug})


    def get_update_url(self):
        return reverse('challenge_update_url', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('challenge_delete_url', kwargs={'slug': self.slug})

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