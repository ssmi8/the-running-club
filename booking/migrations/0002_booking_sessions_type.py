# Generated by Django 3.2.16 on 2023-02-11 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='sessions_type',
            field=models.CharField(choices=[('B', 'Running group for beginners level'), ('I', 'Running group for intermediate level'), ('A', 'Running group for advanced runners')], default='B', max_length=1),
        ),
    ]
