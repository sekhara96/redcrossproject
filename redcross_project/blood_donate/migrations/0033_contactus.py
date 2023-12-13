# Generated by Django 4.2.4 on 2023-08-28 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_donate', '0032_remove_donor_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.BigIntegerField()),
                ('city', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('enquirytype', models.CharField(default='', max_length=1000)),
                ('subject', models.CharField(max_length=1000)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]