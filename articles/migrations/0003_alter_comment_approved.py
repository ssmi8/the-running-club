# Generated by Django 3.2.16 on 2022-10-30 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20221028_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=True, verbose_name='Approved'),
        ),
    ]