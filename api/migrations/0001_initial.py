# Generated by Django 2.1.7 on 2019-06-12 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Verify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='好友用户名')),
                ('sex', models.CharField(max_length=32, verbose_name='用户性别')),
                ('age', models.CharField(max_length=32, verbose_name='用户年龄')),
            ],
        ),
    ]
