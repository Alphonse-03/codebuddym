# Generated by Django 3.1.2 on 2020-11-05 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainprocess', '0018_remove_connectrequest_connectlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='connectrequest',
            name='id',
        ),
        migrations.AddField(
            model_name='connectrequest',
            name='idno',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
