# Generated by Django 4.0.2 on 2022-02-28 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tehtavat', '0002_kategoria_tehtava_kategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tehtava',
            name='kategoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='tehtavat.kategoria'),
        ),
    ]
