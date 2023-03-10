# Generated by Django 4.1.5 on 2023-01-19 06:29

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_tag_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Career_tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career_tag_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Consult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('bussiness_sector', models.CharField(max_length=200)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=200)),
                ('question', models.TextField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=300)),
                ('employee_image', models.ImageField(upload_to='employee/')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.categories')),
                ('position_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.position')),
            ],
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('career_name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('career_tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.career_tag')),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_name', models.CharField(max_length=300)),
                ('whatsapp_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=200)),
                ('cv', models.FileField(upload_to='')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('career_tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.career_tag')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_header', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image_blog', models.ImageField(upload_to='blog/')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('blog_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.blog_tag')),
            ],
        ),
    ]
