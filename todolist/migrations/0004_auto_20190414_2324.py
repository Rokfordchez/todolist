# Generated by Django 2.1.7 on 2019-04-14 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_auto_20190412_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='checkbox',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default='2019-04-14'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default='2019-04-14'),
        ),
    ]
