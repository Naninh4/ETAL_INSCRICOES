from django.shortcuts import render, redirect
from inscricao.forms import CandidatoForm
from inscricao.models import Candidato
# Create your views here.

def home (request):
    return render(request, 'index.html')
def get_cadastros(request):
    if request.method == 'POST':
        form = CandidatoForm(request.POST) #Armazenando o formulário criado a uma lista
        if form.is_valid():
            print(request.POST)
            alter_form = form.save(commit=False)
            alter_form.mini_cursos = " | ".join(dict(request.POST)['mini_cursos'])

            alter_form.save()

            return redirect("/")
        else:
            form = CandidatoForm

    forms =  CandidatoForm
    candidato = Candidato.objects.all()

    return render(request, "cadastro.html", {"forms": forms, "candidato": candidato})

# def get_post_method(request):

#   if request.method == "POST":

#     form = AlunoForm(request.POST)

#     if form.is_valid():

#       alter_form = form.save(commit=False)
#       alter_form.gender = " | ".join(dict(request.POST)['gender'])
      
#       alter_form.save()
      
#       return redirect("/")

#   forms = AlunoForm
#   aluno = Aluno.objects.all() 

#   return render(request, "get.html", {"forms": forms, "aluno": aluno})