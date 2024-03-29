# Generated by Django 5.0.2 on 2024-02-28 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gen', models.CharField(max_length=50, null=True)),
                ('pasword', models.CharField(max_length=50)),
            ],
        ),
    ]
