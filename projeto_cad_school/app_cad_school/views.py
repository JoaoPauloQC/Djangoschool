from django.shortcuts import render
from .models import Aluno , Materia , Notas
# Create your views here.

def home(request):
    return render(request,"usuarios/login.html")

def error(request):
    return render(request, 'usuarios/erro.html')

def login_action(request):
    nome_got = request.POST.get('nome')
    print(nome_got)
    usuario_logado = Aluno.objects.get( nome = nome_got )
    print(usuario_logado.nome)
    notas = {
        'notas' : Notas.objects.filter(aluno = usuario_logado)
        }
    
    #Retornar os dados para a pagina de listafem de usuarios
    if notas :
        return render(request , 'usuarios/notas.html' , notas)
    else:
        return error()