# Generated by Django 3.0.6 on 2020-05-30 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20200530_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthregister',
            name='emergency_contact',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
