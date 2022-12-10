# Generated by Django 4.1.2 on 2022-12-09 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=100, verbose_name='nombre')),
                ('nombre_cuenta_usuario', models.CharField(max_length=20, verbose_name='nickname')),
                ('correo_usuario', models.CharField(max_length=50, verbose_name='mail')),
                ('contraseña_usuario', models.CharField(max_length=20, verbose_name='contraseña')),
                ('direccion_usuario', models.CharField(max_length=100, null=True, verbose_name='direccion')),
                ('telefono_usuario', models.IntegerField(null=True, verbose_name='telefono')),
            ],
        ),
    ]
