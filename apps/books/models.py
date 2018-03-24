from __future__ import unicode_literals

from django.db import models
from ..users.models import User


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Author object#{}: {}>".format(
            self.id, self.name)


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Book object#{}: {} by {}>".format(
            self.id, self.title, self.author.name)


class Review(models.Model):
    rating = models.IntegerField()
    content = models.TextField()
    book = models.ForeignKey(Book, related_name="reviews")
    reviewer = models.ForeignKey(User, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Review object#{}: {}>".format(
            self.id, self.rating)