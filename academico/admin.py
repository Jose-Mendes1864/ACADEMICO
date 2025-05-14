from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Cidade)
admin.site.register(Ocupacao)
admin.site.register(Pessoa)
admin.site.register(InstituicaoEnsino)
admin.site.register(AreaSaber)
admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(Disciplina)
admin.site.register(Matricula)
admin.site.register(Turno)
admin.site.register(Ocorrencia)
admin.site.register(AvaliacaoTipo)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Periodo)
admin.site.register(CursoDisciplina)


class OcupacaoInline(admin.TabularInline):
    model = Ocupacao
    extra = 1

class InstituicaoInline(admin.TabularInline):
    model = InstituicaoEnsino
    extra = 1

class AreaSaberInline(admin.TabularInline):
    model = AreaSaber
    extra = 1


class CursosInline(admin.TabularInline):
    model = Curso
    extra = 1
class DisciplinaInline(admin.TabularInline):
    model = Disciplina
    extra = 1
class TurmaInline(admin.TabularInline):
    model = Turma
    extra = 1

class FrequenciaInlineAvaliacao(admin.TabularInline):
    model = Avaliacao
    extra = 1

class FrequenciaInlineDisciplina(admin.TabularInline):
    model = Frequencia
    extra = 1

class FrequenciaInlinePessoa(admin.TabularInline):
    model = Frequencia
    extra = 1

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [OcupacaoInline]
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [InstituicaoEnsino]
class CursoAdminOcupacao(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [OcupacaoInline]

class CursoAdminDisciplina(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [DisciplinaInline]

class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [DisciplinaInline]
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [TurmaInline]

class FrequenciaAdminDisciplina(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [FrequenciaInlineDisciplina]
class FrequenciaAdminAvaliacao(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [FrequenciaInlineAvaliacao]
class FrequenciaAdminDisciplina(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    inlines = [FrequenciaInlineDisciplina]

admin.site.register(Pessoa, Ocupacao)
admin.site.register()

