# Generated by Django 2.2.5 on 2020-01-28 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
