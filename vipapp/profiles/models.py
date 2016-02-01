# coding: utf-8

from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class Order(models.Model):
    APPTYPE_CHOICES = ()

    RATING_CHOICES = (
        ('M', '3'),
        ('O', '4'),
		('F', '5'),
    )
    STATUS_CHOICES = (
        ('activ', 'Активное'),
        ('moderation', 'Модерация'),
        ('pause', 'Заказ на паузе'),
        ('finished', 'Завершенное'),
        ('foul', 'Оклоненное'),		
        )
    TYPE_CHOICES = (
        ('PayAPp', 'Платное'),
        ('FreeApp', 'Бесплатное')
        )
    PERIODSETUP_CHOICES = (
        ('Hour', 'В час'),
        ('Day', 'В день'),
        )

    app_name = models.CharField(max_length=128)
    id_apps = models.CharField(max_length=128)
    link_redirect = models.CharField(max_length=128)
    rating = models.CharField(max_length=30, choices=RATING_CHOICES)
    order_description = models.TextField(max_length=1000)
    country = CountryField(blank=False) 
    icon = models.ImageField(upload_to="icon/", null=True, blank=True)
    period_setup = models.CharField(max_length=30, default = 'Hour', choices = PERIODSETUP_CHOICES)
    setup_app = models.IntegerField(default = 50)
    app_type = models.CharField(max_length=30, choices = TYPE_CHOICES)
    price = models.IntegerField(default = 10)
    number_performers = models.IntegerField(default = 10)
    agreement = models.BooleanField(default=False)
    user = models.ForeignKey(User,)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='moderation', db_index=True)

    def __unicode__(self):
        return self.app_name


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    created = models.DateTimeField(auto_now=True)
    closed = models.BooleanField(default=False)
    user = models.ForeignKey(User,)

    def __unicode__(self):
        return self.title
