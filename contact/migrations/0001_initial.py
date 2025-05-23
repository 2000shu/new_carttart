# Generated by Django 5.1.6 on 2025-03-28 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.TextField()),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
