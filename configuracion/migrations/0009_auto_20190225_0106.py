# Generated by Django 2.1.7 on 2019-02-25 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0008_institucion'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Institucion',
        ),
        migrations.AddField(
            model_name='evento',
            name='cuenta',
            field=models.CharField(default='22', max_length=50, verbose_name='Cuenta'),
            preserve_default=False,
        ),
    ]
