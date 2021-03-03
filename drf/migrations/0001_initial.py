# Generated by Django 2.2 on 2021-03-02 23:43

from django.db import migrations, models
import django.db.models.deletion

from drf.models import Person, Vehicle


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                # BigIntegerField(primary_key=True, default=1, serialize=False)),
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=80, null=False, blank=False, unique=True)),
                ('firstname', models.CharField(max_length=32, null=False, blank=False)),
                ('lastname', models.CharField(max_length=32, null=False, blank=False)),
                ('mobile', models.CharField(max_length=16, null=False, blank=False)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(max_length=64, null=False, blank=False, unique=True, serialize=False)),
                ('rego', models.CharField(max_length=6, null=False, blank=False, unique=True)),
                ('make', models.CharField(max_length=32, null=False, blank=False)),
                ('model', models.CharField(max_length=32, null=False, blank=False)),
                ('year', models.IntegerField(max_length=4, null=False, blank=False))
            ],
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.ForeignKey('Person', on_delete=models.CASCADE, null=False, blank=False)),
                ('vehicle', models.ForeignKey('Vehicle', on_delete=models.CASCADE, null=False, blank=False)),
                ('asking_price', models.IntegerField(max_length=10, null=False)),  # Whole dollars only, no cents.
                ('placed', models.DateField())
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.ForeignKey('Person', on_delete=models.CASCADE, null=False, blank=False)),
                ('vehicle', models.ForeignKey('Vehicle', on_delete=models.CASCADE, null=False, blank=False)),
                ('sale_price', models.IntegerField(max_length=10, null=False)),  # Whole dollars only, no cents.
                ('bought', models.DateField()),
            ],
        ),
    ]
