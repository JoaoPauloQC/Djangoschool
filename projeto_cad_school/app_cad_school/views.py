from django.shortcuts import render
from .models import Aluno , Materia , Notas
# Create your views here.

def home(request):
    return render(request,"usuarios/login.html")

def login_action(request):
    nome_got = request.POST.get('nome')
    usuario_logado = Aluno.objects.filter(nome= nome_got )
    notas = {
        Notas.objects.filter(aluno=usuario_logado.nome)
        }
    #Retornar os dados para a pagina de listafem de usuarios
    return render(request , 'usuarios/notas.html' , notas)