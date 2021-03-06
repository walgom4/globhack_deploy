# Generated by Django 3.0.6 on 2020-05-30 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_healthregister_emergency_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='healthregister',
            name='emergency_contact',
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='emergency_contact_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='emergency_contact_phone',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='emergency_contact_relationship',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='healthregister',
            name='medical_file',
            field=models.FileField(blank=True, null=True, upload_to='health_register/'),
        ),
    ]
