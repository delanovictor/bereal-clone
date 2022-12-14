# Generated by Django 4.1 on 2022-10-02 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_person_bio_alter_person_following'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=64, null=True)),
                ('profile_image', models.CharField(blank=True, choices=[('Puppy', 'https://images.pexels.com/photos/39317/chihuahua-dog-puppy-cute-39317.jpeg'), ('Rabbit', 'https://images.pexels.com/photos/4588065/pexels-photo-4588065.jpeg')], max_length=255, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='following',
        ),
        migrations.RemoveField(
            model_name='person',
            name='user',
        ),
    ]
