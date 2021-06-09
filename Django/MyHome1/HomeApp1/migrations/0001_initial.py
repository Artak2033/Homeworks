# Generated by Django 3.2.4 on 2021-06-09 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=20)),
                ('car_color', models.CharField(choices=[('Black', 'BLACK'), ('White', 'WHITE'), ('Red', 'RED'), ('Green', 'GREEN'), ('Blue', 'BLUE')], max_length=20)),
                ('car_year', models.IntegerField(default=1)),
                ('car_hp', models.IntegerField(default=1)),
                ('car_about', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Man',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Name')),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=1)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('adress', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Man',
                'verbose_name_plural': 'Men',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Name')),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
            },
        ),
        migrations.CreateModel(
            name='Woman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Name')),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=1)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('adress', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Woman',
                'verbose_name_plural': 'Women',
            },
        ),
    ]