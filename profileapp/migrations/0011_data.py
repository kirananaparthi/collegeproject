# Generated by Django 2.2.5 on 2019-09-25 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0010_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=100)),
            ],
        ),
    ]