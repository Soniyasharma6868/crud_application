# Generated by Django 3.0.1 on 2020-05-22 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerRegModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('repass', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'CustomerReg',
            },
        ),
    ]