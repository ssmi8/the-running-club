# Generated by Django 3.2.16 on 2023-02-12 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_comment_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='approved',
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]