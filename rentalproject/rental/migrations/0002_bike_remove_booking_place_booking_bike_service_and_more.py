# Generated by Django 5.1 on 2024-09-13 15:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('available', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bike_type', models.CharField(choices=[('STD', 'Standard'), ('MTN', 'Mountain'), ('RD', 'Road'), ('ELC', 'Electric')], max_length=50)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='booking',
            name='place',
        ),
        migrations.AddField(
            model_name='booking',
            name='bike',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rental.bike'),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_date', models.DateField()),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.bike')),
            ],
        ),
        migrations.DeleteModel(
            name='Place',
        ),
    ]
