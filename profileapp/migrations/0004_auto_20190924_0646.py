# Generated by Django 2.2.5 on 2019-09-24 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0003_exam1'),
    ]

    operations = [
        migrations.CreateModel(
            name='exam12',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departments', models.CharField(choices=[('eee', 'eee'), ('ece', 'ece'), ('cse', 'cse'), ('mech', 'mech'), ('civil', 'civil')], max_length=30)),
                ('exam', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('date', models.DateField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='exam1',
        ),
    ]
