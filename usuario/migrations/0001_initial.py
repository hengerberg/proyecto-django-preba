# Generated by Django 3.2.8 on 2022-04-15 01:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Distribuidora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'distribuidora',
                'verbose_name_plural': 'distribuidoras',
                'db_table': 'distribuidora',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(blank=True, choices=[('m', 'Masculino'), ('f', 'Feminino')], max_length=1, null=True, verbose_name='Genero')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='profiles', verbose_name='Imagen de Perfil')),
                ('telefono', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(message="El número de teléfono debe ingresarse en el formato: '0999999999'. Se permiten hasta 10 dígitos.", regex='^\\+?1?\\d{9,10}$')], verbose_name='Numero de Telefono')),
                ('distribuidora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.distribuidora')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]