from django import forms
from inscricao.models import *


LISTA_GENERO = [
    ('Masculino', 'Masculino'),
    ('Feminino', 'Feminino'),
    ('Não binário', 'Não binário')
]

LISTA_MINICURSOS= [
    ('Introdução a Computação Gráfica', 'Introdução a Computação Gráfica'),
    ('Introdução a construção de jogos', 'Introdução a construção de jogos'),
    ('Minicurso de Realidade Virtual', 'Minicurso de Realidade Virtual'),
    ('Computação nas Nuvens','Computação nas Nuvens'),
] 

class CandidatoForm(forms.ModelForm):
    genero_candidato = forms.ChoiceField(choices=LISTA_GENERO, widget=forms.RadioSelect(), label="Gênero: ")
    nasc_candidato = forms.DateField(widget = forms.TimeInput(attrs={'type': 'date'}), label="Data de Nascimento:")

    mini_cursos = forms.MultipleChoiceField(choices=LISTA_MINICURSOS, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Candidato
        fields = '__all__'
