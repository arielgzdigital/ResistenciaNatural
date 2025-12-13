from django.db import models
from django.contrib.auth.models import User
from articulos_ir.models import ArticuloIr


class Comentario(models.Model):
	creado = models.DateTimeField(
		auto_now_add = True)
	modificado = models.DateTimeField(
		auto_now = True)
	texto = models.TextField()
	usuario = models.ForeignKey(User, on_delete = models.CASCADE)
	articulo_ir = models.ForeignKey(ArticuloIr, on_delete = models.CASCADE)

	def __str__(self):
		return self.creado.strftime("%d/%m/%Y %H:%M")

