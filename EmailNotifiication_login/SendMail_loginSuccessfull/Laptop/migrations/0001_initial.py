# Generated by Django 4.0 on 2021-12-24 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('model_name', models.CharField(max_length=50)),
                ('ram', models.IntegerField()),
                ('rom', models.FloatField()),
                ('processor', models.CharField(max_length=30)),
                ('weight', models.FloatField()),
                ('price', models.FloatField()),
            ],
        ),
    ]