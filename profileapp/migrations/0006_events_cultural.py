# Generated by Django 2.2.5 on 2019-09-24 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0005_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='cultural',
            field=models.CharField(choices=[('dance', 'dance'), ('sqit', 'sqit'), ('singing', 'singing'), ('speach', 'speach')], default=1, max_length=30),
            preserve_default=False,
        ),
    ]