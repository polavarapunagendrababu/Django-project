# Generated by Django 3.1.3 on 2020-12-26 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gadgets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exfd',
            name='impf',
            field=models.ImageField(default='profile.jpeg', upload_to='Profile/'),
        ),
        migrations.AlterField(
            model_name='exfd',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
