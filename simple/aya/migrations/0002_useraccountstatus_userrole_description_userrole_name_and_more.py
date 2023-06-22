# Generated by Django 4.2.2 on 2023-06-19 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aya', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccountStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('AC', 'Active'), ('IA', 'Inactive'), ('DI', 'Disabled'), ('AR', 'Archived')], default='AC', unique=True)),
                ('description', models.TextField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='userrole',
            name='description',
            field=models.TextField(default='Standard user - core system access privileges.', max_length=300),
        ),
        migrations.AddField(
            model_name='userrole',
            name='name',
            field=models.CharField(choices=[('AD', 'Administrator'), ('ST', 'Standard')], default='ST', unique=True),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_name', models.CharField(max_length=100, unique=True)),
                ('password_hash', models.TextField(max_length=500, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=13, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user_account_status_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='aya.useraccountstatus')),
                ('user_role_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='aya.userrole')),
            ],
        ),
    ]
