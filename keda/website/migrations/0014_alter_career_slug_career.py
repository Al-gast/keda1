# Generated by Django 4.1.6 on 2023-02-02 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_alter_career_slug_career'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='slug_career',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
