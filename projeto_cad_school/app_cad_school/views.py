from django.shortcuts import render
from .models import Usuario
# Create your views here.

def home(request):
    return render(request,"usuarios/login.html")

def informacoes(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get("nome")
    novo_usuario.senha = request.POST.get("senha")
    novo_usuario.save()
    #Exibir todas as notas
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #Retornar os dados para a pagina de listafem de usuarios
    return render(request , 'usuarios/usuarios.html' , usuarios)