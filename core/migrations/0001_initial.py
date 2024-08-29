# Generated by Django 5.1 on 2024-08-29 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=200, null=True)),
                ('text', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
