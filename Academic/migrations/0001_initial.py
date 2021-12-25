# Generated by Django 3.2.8 on 2021-11-11 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academic_year',
            fields=[
                ('academic_list', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('academic_comment', models.TextField(max_length=1083)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('college_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('college_name', models.CharField(max_length=100)),
                ('location', models.CharField(default='Nyarugenge', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_credits', models.CharField(default='10', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=100)),
                ('academic_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.academic_year')),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('email', models.EmailField(max_length=255, primary_key=True, serialize=False)),
                ('lecturer_name', models.CharField(max_length=255)),
                ('academic_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.academic_year')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('level_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('level_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(default='S')),
                ('marks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('module_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('module_name', models.CharField(max_length=100)),
                ('credits', models.ForeignKey(default='10', on_delete=django.db.models.deletion.CASCADE, to='Academic.credit')),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.lecturer')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.level')),
                ('module_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.department')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('semester_code', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('semester_name', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_reg', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('profile', models.ImageField(upload_to='student_profile')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('date_of_birth', models.DateField()),
                ('national_id', models.PositiveBigIntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.department')),
                ('year_academic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.academic_year')),
            ],
        ),
        migrations.CreateModel(
            name='Transcript',
            fields=[
                ('transcript_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('credits', models.IntegerField()),
                ('dob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='set_dob', to='Academic.student')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='set_grade', to='Academic.marks')),
                ('level_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='set_level_year', to='Academic.level')),
                ('marks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='set_marks', to='Academic.marks')),
                ('module_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='set_module_id', to='Academic.module')),
                ('student_Fname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='set_student_fname', to='Academic.student')),
                ('student_Lname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='set_student_lname', to='Academic.student')),
                ('student_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='set_student_profile', to='Academic.student')),
                ('student_reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='set_student_reg', to='Academic.student')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('school_name', models.CharField(max_length=100)),
                ('college_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='set_college', to='Academic.college')),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='set_for_module', to='Academic.semester'),
        ),
        migrations.AddField(
            model_name='marks',
            name='module_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='set_module_code', to='Academic.module'),
        ),
        migrations.AddField(
            model_name='marks',
            name='student_reg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='set_student_mark', to='Academic.student'),
        ),
        migrations.AddField(
            model_name='lecturer',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.school'),
        ),
        migrations.AddField(
            model_name='department',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.level'),
        ),
        migrations.AddField(
            model_name='department',
            name='school_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.school'),
        ),
    ]
