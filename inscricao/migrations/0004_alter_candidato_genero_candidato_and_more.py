# Generated by Django 4.1.3 on 2022-11-23 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0003_alter_candidato_genero_candidato_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='genero_candidato',
            field=models.CharField(blank=True, max_length=50, verbose_name='Sexo:'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='mini_cursos',
            field=models.CharField(blank=True, max_length=100, verbose_name='Mini cursos'),
        ),
    ]
