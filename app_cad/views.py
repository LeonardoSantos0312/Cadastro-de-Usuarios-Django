from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    #salvar os dados inseridos na tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.cpf = request.POST.get('cpf')
    novo_usuario.tele = request.POST.get('tele')

    novo_usuario.save()
    #exibir todos os usuarios cadastrados em nova pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    #Retornar os dados para a pagina de listagem de usuarios
    return render(request,'usuarios/usuarios.html',usuarios)