from django.db import models

# Create your models here.

LISTA_GENERO = [
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino')
]

LISTA_MINICURSOS= [
    ('Introdução a Computação Gráfica', 'Introdução a Computação Gráfica'),
    ('Introdução a construção de jogos', 'Introdução a construção de jogos'),
    ('Minicurso de Realidade Virtual', 'Minicurso de Realidade Virtual'),
    ('Computação nas Nuvens','Computação nas Nuvens'),
] 
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
    genero_candidato = models.CharField(choices=LISTA_GENERO, verbose_name="Sexo:",max_length=50, blank=True)
    curso_candidato = models.CharField(choices=LISTA_CURSO, max_length=50, verbose_name="Curso:")
    mini_cursos = models.CharField( choices=LISTA_MINICURSOS,max_length=100, blank=True, verbose_name="Mini cursos")


