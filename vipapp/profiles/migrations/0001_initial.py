# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_name', models.CharField(max_length=128)),
                ('id_apps', models.CharField(max_length=128)),
                ('link_redirect', models.CharField(max_length=128)),
                ('rating', models.CharField(max_length=30, choices=[(b'M', b'3'), (b'O', b'4'), (b'F', b'5')])),
                ('order_description', models.TextField(max_length=1000)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('icon', models.ImageField(null=True, upload_to=b'icon/', blank=True)),
                ('period_setup', models.CharField(default=b'Hour', max_length=30, choices=[(b'Hour', b'\xd0\x92 \xd1\x87\xd0\xb0\xd1\x81'), (b'Day', b'\xd0\x92 \xd0\xb4\xd0\xb5\xd0\xbd\xd1\x8c')])),
                ('setup_app', models.IntegerField(default=50)),
                ('app_type', models.CharField(max_length=30, choices=[(b'PayAPp', b'\xd0\x9f\xd0\xbb\xd0\xb0\xd1\x82\xd0\xbd\xd0\xbe\xd0\xb5'), (b'FreeApp', b'\xd0\x91\xd0\xb5\xd1\x81\xd0\xbf\xd0\xbb\xd0\xb0\xd1\x82\xd0\xbd\xd0\xbe\xd0\xb5')])),
                ('price', models.IntegerField(default=10)),
                ('number_performers', models.IntegerField(default=10)),
                ('agreement', models.BooleanField(default=False)),
                ('status', models.CharField(default=b'moderation', max_length=255, db_index=True, choices=[(b'activ', b'\xd0\x90\xd0\xba\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd0\xbe\xd0\xb5'), (b'moderation', b'\xd0\x9c\xd0\xbe\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f'), (b'pause', b'\xd0\x97\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7 \xd0\xbd\xd0\xb0 \xd0\xbf\xd0\xb0\xd1\x83\xd0\xb7\xd0\xb5'), (b'finished', b'\xd0\x97\xd0\xb0\xd0\xb2\xd0\xb5\xd1\x80\xd1\x88\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xb5'), (b'foul', b'\xd0\x9e\xd0\xba\xd0\xbb\xd0\xbe\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xb5')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('closed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
