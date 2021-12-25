# Generated by Django 3.2.8 on 2021-12-21 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Academic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='level',
            field=models.ForeignKey(default='level 1', on_delete=django.db.models.deletion.CASCADE, related_name='level_marks', to='Academic.level'),
        ),
        migrations.AddField(
            model_name='marks',
            name='semester_marks',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='semester_marks', to='Academic.semester'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='grade',
            field=models.CharField(max_length=1),
        ),
    ]