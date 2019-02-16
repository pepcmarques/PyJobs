# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-13 19:40
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0006_auto_20180411_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Job')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Job Applications',
                'verbose_name': 'Job Application',
            },
        ),
        migrations.AlterUniqueTogether(
            name='jobapplication',
            unique_together=set([('user', 'job')]),
        ),
    ]
