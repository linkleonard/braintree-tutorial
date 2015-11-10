# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(max_digits=16, decimal_places=2)),
                ('payer', models.ForeignKey(related_name='payments', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
