# Generated by Django 4.2.4 on 2023-08-31 06:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blood_donate', '0043_donation_process'),
    ]

    operations = [
        migrations.CreateModel(
            name='lastdonatedetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=200)),
                ('patient_name', models.CharField(blank=True, max_length=100, null=True)),
                ('place', models.CharField(max_length=200)),
                ('donation_date', models.DateField(default=django.utils.timezone.now)),
                ('uploade_image', models.ImageField(upload_to='media')),
            ],
        ),
    ]
