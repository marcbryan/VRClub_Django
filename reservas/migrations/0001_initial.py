# Generated by Django 2.2.5 on 2019-10-16 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planta', models.CharField(max_length=50)),
                ('mida', models.CharField(max_length=50)),
                ('disponibilidad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=1000)),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.Aula')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(verbose_name='fecha para la reserva')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('edad', models.IntegerField(default=0)),
                ('estudios', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva_Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.Material')),
                ('reserva_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.Reserva')),
            ],
        ),
        migrations.AddField(
            model_name='reserva',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.Usuario'),
        ),
    ]
