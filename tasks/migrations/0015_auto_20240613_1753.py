# Generated by Django 3.2.25 on 2024-06-13 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0014_auto_20240613_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='task',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
