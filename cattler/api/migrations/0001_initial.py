# Generated by Django 3.2.16 on 2023-02-03 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('lot_number', models.PositiveIntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Troop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('troop_number', models.PositiveIntegerField(unique=True)),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.lot')),
            ],
            options={
                'unique_together': {('troop_number', 'lot')},
            },
        ),
        migrations.CreateModel(
            name='Corral',
            fields=[
                ('corral_number', models.AutoField(primary_key=True, serialize=False)),
                ('troop', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.troop')),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caravan_number', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('RFID_number', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('troop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.troop')),
            ],
        ),
    ]
