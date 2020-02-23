# Generated by Django 2.2.1 on 2020-02-13 15:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_auto_20200213_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='ciudadmodel',
            name='create',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='ciudadmodel',
            name='delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='estadomodel',
            name='create',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='estadomodel',
            name='delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='estcivmodel',
            name='create',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='estcivmodel',
            name='delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='generomodel',
            name='create',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='generomodel',
            name='delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ocupacionmodel',
            name='create',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='ocupacionmodel',
            name='delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='ciudad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.CiudadModel'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.EstadoModel'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='estado_Civ',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.EstCivModel'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.GeneroModel'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='ocupacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.OcupacionModel'),
        ),
        migrations.AlterModelTable(
            name='ciudadmodel',
            table='Ciudad',
        ),
        migrations.AlterModelTable(
            name='estadomodel',
            table='Estado',
        ),
        migrations.AlterModelTable(
            name='estcivmodel',
            table='Estado Civil',
        ),
        migrations.AlterModelTable(
            name='generomodel',
            table='Genero',
        ),
        migrations.AlterModelTable(
            name='ocupacionmodel',
            table='Ocupacion',
        ),
    ]