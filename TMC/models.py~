# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Credito(models.Model):
	persona = models.CharField(max_length=200)
	monto_UF = models.IntegerField(default=0)
	plazo = models.IntegerField(default=0)

class TMC(models.Model):
	credito = models.ForeignKey(Credito, on_delete=models.CASCADE)
	TMC = models.IntegerField(default=0)
	fecha_consulta = models.DateTimeField('Fecha consulta')
