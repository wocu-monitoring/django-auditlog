# Generated by Django 3.2 on 2022-11-24 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auditlog', '0012_add_logentry_action_access'),
    ]

    operations = [
        migrations.AddField(
            model_name='logentry',
            name='author',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='author'),
        ),
    ]
