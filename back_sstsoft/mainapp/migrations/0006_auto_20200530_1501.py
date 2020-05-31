# Generated by Django 3.0.6 on 2020-05-30 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
        migrations.CreateModel(
            name='healthRegister',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('flu', models.BooleanField(default=False)),
                ('fever', models.BooleanField(default=False)),
                ('cough', models.BooleanField(default=False)),
                ('sore_throat', models.BooleanField(default=False)),
                ('nasal_congestion', models.BooleanField(default=False)),
                ('fatigue', models.BooleanField(default=False)),
                ('difficult_breathe', models.BooleanField(default=False)),
                ('muscle_pain', models.BooleanField(default=False)),
                ('diarrhea', models.BooleanField(default=False)),
                ('threw_up', models.BooleanField(default=False)),
                ('other', models.CharField(blank=True, max_length=1000, null=True)),
                ('temperature', models.DecimalField(decimal_places=2, default=0, max_digits=40)),
                ('photo_temperature', models.ImageField(blank=True, null=True, upload_to='health_register/')),
                ('photo_workspace', models.ImageField(blank=True, null=True, upload_to='health_register/')),
                ('photo_selfie', models.ImageField(blank=True, null=True, upload_to='health_register/')),
                ('user_fk_health', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
