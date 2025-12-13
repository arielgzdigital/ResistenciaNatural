from django.shortcuts import render
from .models import ArticuloIr, CategoriaIr

from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import FormularioCrearArticuloIr, FormularioModificarArticuloIr

#PERMISOS
#1
#VAMOS A USAR, PRIMERO ASEGURAR QUE EL USUARIO ESTA LOGUEADO.
#(CON ESTO SEPARO USUARIO VISTANTE Y USUARIO REGISTRADO)

#DEPENDE DE SI LA VISTA ES VBF O VBC
#VBF
from django.contrib.auth.decorators import login_required

#VBC
from django.contrib.auth.mixins import LoginRequiredMixin

#VBF
from 	django.contrib.admin.views.decorators import staff_member_required 
#VBC
from 	django.contrib.auth.mixins import UserPassesTestMixin

def Listar_Articulos_Ir(request):

    #ORM
    #es equivalente a hacer un "select * from producto"
    todos_articulos_ir = ArticuloIr.objects.all().order_by('-id')
    #como resultado la variable todos_articulos_ir es una lista objetos
    #de la clase articuloIr (copiados de la BD)

    #para pasar los datos al template se usa un diccionario
    context = {}
    context['articulos_ir'] = todos_articulos_ir

    # LE PASO LOS RUBROS PARA PODER HACER EL FILTRO EN EL TEMPLATE
    categorias_ir = CategoriaIr.objects.all()
    context['categorias_ir'] = categorias_ir

    return render(request, 'articulos_ir/listar_articulos_ir.html', context)
    #el template cuando recibe el diccionario "contexto"
    #automaticamente lo desempaqueta, es decir en el template
    #tengo directamente una variable que se llama en este caso articulos_ir
    #Ejemplo
    #al template le paso algo asi {'articulos_ir': [obj_loba, objeto_laguna, objeto_museo]}
    #el template: articulos_ir = [obj_loba, objeto_laguna, objeto_museo]

def Detalle_Articulo_Ir_Funcion(request, pk):
    #el Get se usa cuando filtro por la clave,
	#esto es porque siempre el resultado es un SOLO objeto
    articulo_ir = ArticuloIr.objects.get(pk = pk)
    context = {}
    context['articulo_ir'] = articulo_ir
    return render (request,'articulos_ir/detalle_articulo_ir.html', context)

class Detalle_Articulo_Ir_Clase(LoginRequiredMixin, DetailView):
    model = ArticuloIr
    template_name = 'articulos_ir/detalle_articulo_ir.html'
    context_object_name = 'articulo_ir'

class Crear_Articulo_Ir_Clase(UserPassesTestMixin, CreateView):
    model = ArticuloIr
    template_name = 'articulos_ir/crear_articulos_ir.html'
    form_class = FormularioCrearArticuloIr
    success_url = reverse_lazy('articulos_ir:path_listar_articulos_ir')

    def test_func(self):
           if self.request.user.is_staff:
            return True
           else:
               return False

class Modificar_Articulo_Ir_Clase(UpdateView):
    model = ArticuloIr
    template_name = 'articulos_ir/modificar_articulos_ir.html'
    context_object_name = 'articulo_ir'
    form_class = FormularioModificarArticuloIr
    success_url = reverse_lazy('articulos_ir:path_listar_articulos_ir')
    
class Eliminar_Articulo_Ir_Clase(DeleteView):
    model = ArticuloIr
    template_name = 'articulos_ir/eliminar_articulos_ir.html'
    context_object_name = 'articulo_ir'
    success_url = reverse_lazy('articulos_ir:path_listar_articulos_ir')

@login_required
@staff_member_required
def Listar_Categorias_Ir_Funcion(request):
	categorias_ir = CategoriaIr.objects.all()
	context = {}
	context['categorias_ir'] = categorias_ir
	return render(request,'articulos_ir/categorias_ir.html', context)

def Filtro_Categoria_Ir(request,pk):
    c = CategoriaIr.objects.get(pk = pk)

    #Esto es equivalente a.
	# select * from producto where rubro = r
	#siempre retorna una lista    
    a = ArticuloIr.objects.filter(categoria_ir = c).order_by('-id')
    context = {}
    context['articulos_ir'] = a

    categorias_ir = CategoriaIr.objects.all()
    context['categorias_ir'] = categorias_ir

    context['categoria_activa'] = c

    return render(request, 'articulos_ir/listar_articulos_ir.html', context)     


