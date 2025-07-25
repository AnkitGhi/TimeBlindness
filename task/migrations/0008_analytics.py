# Generated by Django 4.2.20 on 2025-04-01 05:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0007_remove_tasksummary_task_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average_time_completion', models.IntegerField()),
                ('no_task_completed', models.IntegerField()),
                ('no_task_remaining', models.IntegerField()),
                ('average_motivation', models.IntegerField()),
                ('average_seatings', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
