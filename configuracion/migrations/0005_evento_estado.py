# Generated by Django 2.1.7 on 2019-02-24 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0004_auto_20190224_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='estado',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
