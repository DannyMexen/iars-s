# Generated by Django 4.2.2 on 2023-06-19 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aya', '0006_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('contact_first_name', models.CharField(max_length=100)),
                ('contact_last_name', models.CharField(max_length=100)),
                ('contact_phone_number', models.CharField(max_length=13, unique=True)),
                ('contact_email', models.EmailField(max_length=254, unique=True)),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='aya.city')),
            ],
        ),
    ]
