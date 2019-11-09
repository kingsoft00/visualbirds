# Generated by Django 2.1.3 on 2019-11-09 21:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bird_identifier', '0003_auto_20191107_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='bird',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bird',
            name='watson_id',
            field=models.IntegerField(default=0),
        ),
    ]
