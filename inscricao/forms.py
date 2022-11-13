from django import forms
from inscricao.models import Candidato

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
class CandidatoForm(forms.ModelForm):
    genero_candidato = forms.ChoiceField(choices=LISTA_GENERO, widget=forms.RadioSelect())

    mini_cursos = forms.MultipleChoiceField(choices=LISTA_MINICURSOS, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Candidato
        fields = '__all__'
