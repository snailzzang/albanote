# Generated by Django 2.1.1 on 2020-01-29 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albalog', '0003_auto_20200129_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='type',
            field=models.CharField(choices=[('manager', '관리자'), ('member', '일반직원')], default='member', max_length=10),
        ),
    ]
