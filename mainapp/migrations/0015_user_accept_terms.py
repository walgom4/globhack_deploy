# Generated by Django 3.0.6 on 2020-05-31 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_resources_resource_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='accept_terms',
            field=models.BooleanField(default=False),
        ),
    ]
