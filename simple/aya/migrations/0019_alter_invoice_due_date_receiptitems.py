# Generated by Django 4.2.2 on 2023-06-19 18:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aya', '0018_alter_arcariusmexen_tpin_alter_invoice_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 19, 18, 14, 42, 561346, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='ReceiptItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_number', models.CharField(max_length=10, unique=True)),
                ('invoice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aya.invoice')),
                ('invoice_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aya.invoiceitem')),
            ],
        ),
    ]
