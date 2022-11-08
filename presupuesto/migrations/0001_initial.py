# Generated by Django 4.1.2 on 2022-11-08 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('itinerario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='presupuesto',
            fields=[
                ('id_presupuesto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_item_presupuesto', models.CharField(max_length=50, verbose_name='nombre item')),
                ('precio_item_presupuesto', models.IntegerField(verbose_name='precio item')),
                ('id_itinerario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itinerario.itinerario')),
            ],
        ),
    ]
