# Generated by Django 4.0.2 on 2022-02-28 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tehtavat', '0003_alter_tehtava_kategoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='tehtava',
            name='tehty',
            field=models.BooleanField(default=False),
        ),
    ]
