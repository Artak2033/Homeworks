# Generated by Django 3.2.4 on 2021-06-11 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp2', '0003_alter_woman_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='man',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]
