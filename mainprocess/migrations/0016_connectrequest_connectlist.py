# Generated by Django 3.1.2 on 2020-11-05 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainprocess', '0015_remove_connectrequest_connectlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='connectrequest',
            name='connectlist',
            field=models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='mainprocess.profile'),
        ),
    ]