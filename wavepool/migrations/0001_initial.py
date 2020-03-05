# Generated by Django 2.2.11 on 2020-03-05 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('body', models.TextField(max_length=3000)),
                ('source', models.URLField()),
                ('is_cover_story', models.BooleanField(default=False)),
                ('publish_date', models.DateField(default=datetime.date(2020, 3, 5))),
            ],
        ),
    ]
