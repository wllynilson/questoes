from django.shortcuts import render

# Create your views here.

def teste(request):
    return render(request,'oslive/index.html',{})

def questao(request):
    return render(request,'oslive/')