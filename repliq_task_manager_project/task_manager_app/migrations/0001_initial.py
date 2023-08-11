# Generated by Django 4.2.4 on 2023-08-11 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('contact_info', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('company_name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_type', models.CharField(max_length=50)),
                ('serial_number', models.CharField(max_length=50)),
                ('condition', models.CharField(max_length=100)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_date', models.DateTimeField(auto_now_add=True)),
                ('condition', models.CharField(max_length=100)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_manager_app.device')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('contact_info', models.CharField(max_length=200)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_manager_app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('condition_at_assignment', models.CharField(max_length=100)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_manager_app.device')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_manager_app.employee')),
            ],
        ),
    ]
