# Generated by Django 5.1.2 on 2024-10-13 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=255),
        ),
    ]
