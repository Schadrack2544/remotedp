# Generated by Django 4.0 on 2021-12-27 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Academic', '0004_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='academic_year',
            new_name='level',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='id',
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_invoice_number',
            field=models.CharField(default='', max_length=255, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='is_paid',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='payment_Order',
            fields=[
                ('txn_id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('payment_invoice_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.payment')),
                ('student_reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.student')),
            ],
        ),
    ]