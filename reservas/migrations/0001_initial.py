# Generated by Django 5.2 on 2025-04-30 01:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('parceiros', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('numero_reserva', models.CharField(default='ae5d3366a2', max_length=10, primary_key=True, serialize=False)),
                ('nome_cliente', models.CharField(max_length=100)),
                ('data_entrada', models.DateField(auto_now_add=True)),
                ('colaborador_responsavel', models.CharField(max_length=100)),
                ('nome_fantasia', models.CharField(max_length=100)),
                ('origem', models.CharField(max_length=100)),
                ('destino', models.CharField(max_length=100)),
                ('data_ida', models.DateField()),
                ('data_volta', models.DateField()),
                ('comentarios_adicionais', models.TextField(blank=True, null=True)),
                ('cnpj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='parceiros.parceiro')),
                ('cpf_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas', to='clientes.cliente')),
            ],
        ),
    ]
