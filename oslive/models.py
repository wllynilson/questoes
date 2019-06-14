from datetime import timezone

from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.forms import forms


class Academico(models.Model):
    CGU = models.CharField(max_length=9, null=True)
    pontuacao = models.IntegerField(null=True)

    class Meta:
        ordering = ['pontuacao']


class Anexo(models.Model):
    IMAGEM = 1
    PDF = 2

    TIPODOANEXO = (
        (IMAGEM, ('Imagem')),
        (PDF, ('Pdf')),
    )

    nome = models.CharField(max_length=200)
    tipoanexo = models.IntegerField(choices=TIPODOANEXO, default=None)
    arquivo = models.FileField(upload_to='documents/')


    def publish(self):
        self.published_date = timezone
        self.save()


    def __str__(self):
        return self.nome



class Questoes(models.Model):
    FACIL = 1
    MEDIA = 2
    DIFICIL = 3

    NIVEL = (
        (FACIL, ('Fácil')),
        (MEDIA, ('Média')),
        (DIFICIL, ('Difícil')),
    )

    A = "A"
    B = "B"
    C = "C"
    D = "D"
    ALTERNATIVAS = (
        (A, 'A'),
        (B, 'B'),
        (C, 'C'),
        (D, 'D'),
    )

    enunciado = models.TextField(max_length=100, null=True)
    alternativaA = models.TextField(max_length=100, null=True)
    alternativaB = models.TextField(max_length=100, null=True)
    alternativaC = models.TextField(max_length=100, null=True)
    alternativaD = models.TextField(max_length=100, null=True)
    nivel = models.IntegerField(choices=NIVEL, default=FACIL)
    anexo = models.ForeignKey(Anexo, on_delete=models.CASCADE)

    class Meta:
        ordering = ['enunciado']

    def publish(self):
        self.published_date = timezone
        self.save()

    def __str__(self):
        return "{}".format(self.enunciado)




class Resposta(models.Model):
    resposta = models.CharField(max_length=5, null=True)
    academico = models.ForeignKey(Academico, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(Questoes, on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone
        self.save()

    def __str__(self):
        return "{}".format(self.resposta)
