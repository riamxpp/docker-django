from django.db import models

# Create your models here.
class Empregado(models.Model):
  SEXO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),  
  ]

  matricula = models.IntegerField(primary_key=True)
  nome = models.CharField(max_length=15)
  dataNasc = models.DateField(null=True, blank=True)
  endereco = models.CharField(max_length=30, blank=True)
  sexo = models.CharField(max_length=1, blank=True, choices=SEXO_CHOICES)
  salario = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
  supervisor = models.IntegerField(blank=True)
  depto = models.IntegerField(blank=True)

  supervisor = models.ForeignKey(
    'self',
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='subordinados'
  )



  def __str__(self):
    return self.nome

class Departamento(models.Model):
  nome = models.CharField(max_length=15, unique=True)
  gerente = models.ForeignKey(
    Empregado,
    on_delete=models.PROTECT,
    related_name='gerencia_depto',
  )
  dataInicioGerencia = models.DateField()

  def __str__(self):
    return self.nome

class Projeto(models.Model):
  nome = models.CharField(max_length=45)
  localizacao = models.CharField(max_length=45)
  depart = models.ForeignKey(Departamento, on_delete=models.CASCADE )
  lider = models.ForeignKey(Empregado, on_delete=models.CASCADE )

class Alocacao(models.Model):
  matric = models.ForeignKey(Empregado, on_delete=models.CASCADE )
  codProj = models.ForeignKey(Projeto, on_delete=models.CASCADE )
  horas = models.DecimalField(max_digits=4, decimal_places=2)

class Dependente(models.Model):
  matricula = models.ForeignKey(Empregado, on_delete=models.CASCADE, related_name='dependentes' )
  nome = models.CharField(max_length=45)
  sexo = models.CharField(max_length=1, blank=True, choices=Empregado.SEXO_CHOICES)