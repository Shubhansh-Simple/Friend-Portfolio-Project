# Generated by Django 2.2 on 2020-12-31 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('top_image', models.ImageField(help_text='Upload top image of the model.', upload_to='images/')),
                ('bottom_image', models.ImageField(help_text='Upload bottom image of the model.', upload_to='images/')),
                ('front_image', models.ImageField(help_text='Upload front image of the model.', upload_to='images/')),
                ('side_image', models.ImageField(help_text='Upload side image of the model.', upload_to='images/')),
                ('isometric_image', models.ImageField(help_text='Upload isometric image of the model.', upload_to='images/')),
                ('project_file', models.FileField(help_text='Upload Your Project file.', upload_to='project_file/')),
            ],
        ),
    ]