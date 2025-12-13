from django.db import models

class CategoriaIr(models.Model):
	titulo = models.CharField(max_length = 60)
	imagen = models.ImageField(upload_to = 'categorias_ir', null = True)

	def __str__(self):
		return self.titulo

class ArticuloIr(models.Model):
	titulo = models.CharField(max_length = 50)
	descripcion = models.TextField()
	imagen = models.ImageField(upload_to = 'articulos_ir')
	categoria_ir = models.ForeignKey(CategoriaIr, on_delete = models.CASCADE, null = True)

	def __str__(self):
		return self.titulo
	
	def misComentarios(self):
		## select * from comentario where comentario.producto = self
		return self.comentario_set.all()


#generar y comprobar ls migraciones
# py manage.py makemigrations

#para impatar los cambios en la BD
# py manage.py migrate	