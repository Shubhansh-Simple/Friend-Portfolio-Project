# Generated by Django 2.2 on 2021-01-01 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]