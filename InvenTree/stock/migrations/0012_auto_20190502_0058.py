# Generated by Django 2.2 on 2019-05-01 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0011_auto_20190502_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockitem',
            name='part',
            field=models.ForeignKey(help_text='Base part', on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='part.Part'),
        ),
    ]
