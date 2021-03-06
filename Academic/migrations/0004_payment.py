# Generated by Django 4.0 on 2021-12-26 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Academic', '0003_marks_module_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_due', models.IntegerField(default=5000)),
                ('academic_year', models.CharField(max_length=10)),
                ('is_paid', models.BooleanField(default=False)),
                ('student_reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studen_reg_number', to='Academic.student')),
            ],
        ),
    ]
