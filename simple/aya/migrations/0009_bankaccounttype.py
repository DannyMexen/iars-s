# Generated by Django 4.2.2 on 2023-06-19 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aya', '0008_arcariusmexen'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('CU', 'Current'), ('SA', 'Savings')], default='CU')),
            ],
        ),
    ]
