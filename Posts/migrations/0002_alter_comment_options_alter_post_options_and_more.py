# Generated by Django 4.2.7 on 2024-01-16 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='updated_at',
        ),
    ]
