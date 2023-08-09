# Generated by Django 4.2.2 on 2023-06-19 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aya', '0004_event_remove_log_description_remove_log_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('CE', 'Central'), ('CO', 'Copperbelt'), ('ES', 'Eastern'), ('LP', 'Luapula'), ('LS', 'Lusaka'), ('MU', 'Muchinga'), ('NR', 'Northern'), ('NW', 'North Western'), ('WE', 'Western'), ('SO', 'Southern')], default='CE')),
            ],
        ),
    ]