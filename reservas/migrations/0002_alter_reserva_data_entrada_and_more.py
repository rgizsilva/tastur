# Generated by Django 5.2 on 2025-04-30 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='data_entrada',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='numero_reserva',
            field=models.CharField(default='8be842ddbc', max_length=10, primary_key=True, serialize=False),
        ),
    ]
