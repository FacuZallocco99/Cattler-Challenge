# Generated by Django 3.2.16 on 2023-02-03 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_troop_troop_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='RFID_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]