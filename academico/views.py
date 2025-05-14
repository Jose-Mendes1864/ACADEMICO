
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages

class IndexView(View):

    def get(self, request, *args, **kwargs):
      
        return render(request, 'index.html')
    def post(self, request):
        pass

class CidadesView(View):

    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        print(cidades)
        return render(request, 'cidades.html', {'cidades': cidades})
    def post(self, request):
        pass


class OcupacaoView(View):
    def get(self, request, *args, **kwargs):
        ocupacao = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacao': ocupacao})
    def post(self, request):
        pass

class InstituicaoView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = InstituicaoEnsino.objects.all()
        return render(request, 'instituicao.html', {'instituicoes': instituicoes})
    def post(self, request):
        pass
class AreaSaberView(View):
    def get(self, request, *args, **kwargs):
        areas = AreaSaber.objects.all()
        return render(request, 'area_saber.html', {'areas': areas})
    def post(self, request):
        pass
class CursosView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'cursos.html', {'cursos': cursos})
    def post(self, request):
        pass

class TurmasView(View):
    def get(self, request, *args, **kwargs):
        turmas = Turma.objects.all()
        return render(request, 'turmas.html', {'turmas': turmas})
    def post(self, request):
        pass

class DisciplinasView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplinas.html', {'disciplinas': disciplinas})
    def post(self, request):
        pass

class MatriculasView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.all()
        return render(request, 'matriculas.html', {'matriculas': matriculas})
    def post(self, request):
        pass