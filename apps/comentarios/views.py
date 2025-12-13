from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from articulos_ir.models import ArticuloIr
from .models import Comentario
from django.contrib.auth.decorators import login_required

@login_required
def comentar(request, pk):
	a = ArticuloIr.objects.get(pk = pk)
	u = request.user

	c = request.POST.get('texto_comentado', None)

	#SQL: insert into comentario value(c,u,p)
	Comentario.objects.create(texto = c, usuario = u, articulo_ir = a)

	return HttpResponseRedirect(reverse_lazy('articulos_ir:path_detalle_articulo_ir', kwargs = {'pk':pk}))

class Eliminar(DeleteView):
	model = Comentario
	template_name = 'comentarios/eliminar.html'
	
	def get_success_url(self):
		return reverse_lazy('articulos_ir:path_detalle_articulo_ir', kwargs={'pk':self.object.articulo_ir.pk})