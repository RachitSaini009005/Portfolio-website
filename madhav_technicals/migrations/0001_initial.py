# Generated by Django 4.1.3 on 2023-06-12 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('Email_id', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('Message', models.CharField(max_length=2000)),
            ],
        ),
    ]
