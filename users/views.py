from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.template import response

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print("Logado")
    else:
        print("Não rolou")

