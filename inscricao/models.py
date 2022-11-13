from django.db import models

# Create your models here.


LISTA_CURSO= [
    ('Curso técnico', 'Curso técnico'),
    ('ADS', 'ADS'),
]

class Candidato(models.Model):
    nome_candidato = models.CharField(verbose_name="Nome:", max_length=100)
    cpf_candidato = models.CharField(verbose_name="CPF:", max_length=11)
    nasc_candidato = models.DateField(verbose_name="Data de nascimento: ", )
    email_candidato = models.EmailField(verbose_name="Email:")
    endereco_candidato = models.CharField(max_length=255, verbose_name="Endereço:" )
    genero_candidato = models.CharField(verbose_name="Sexo:",max_length=50, blank=True)
    curso_candidato = models.CharField(choices=LISTA_CURSO, max_length=50, verbose_name="Curso:")
    mini_cursos = models.CharField(max_length=100, blank=True, verbose_name="Mini cursos")


