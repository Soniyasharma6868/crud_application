# Generated by Django 3.0.1 on 2020-05-22 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerregmodel',
            name='Gender',
        ),
        migrations.RemoveField(
            model_name='customerregmodel',
            name='address',
        ),
        migrations.RemoveField(
            model_name='customerregmodel',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customerregmodel',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='customerregmodel',
            name='password',
        ),
        migrations.RemoveField(
            model_name='customerregmodel',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='customerregmodel',
            name='repass',
        ),
    ]
