# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-22 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_page_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='enquery_type',
            field=models.CharField(choices=[('general', 'Request For Services'), ('partnership', 'Partnership Queries'), ('media', 'Media Queries'), ('general queries', 'General Queries'), ('feedback', 'Website Feedback'), ('others', 'Others')], max_length=100),
        ),
        migrations.AlterField(
            model_name='menu',
            name='status',
            field=models.CharField(blank=True, default='off', max_length=5),
        ),
    ]
