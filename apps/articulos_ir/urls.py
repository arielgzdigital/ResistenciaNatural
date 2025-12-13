
from django.urls import path
from . import views

app_name = 'articulos_ir'

urlpatterns = [
    path('listar/', views.Listar_Articulos_Ir, name = 'path_listar_articulos_ir'),

    #DETALLE DE UN PRODUCTO CON FUNCION (VBF)
    #path('detalle/<int:pk>', views.Detalle_Articulo_Ir_Funcion, name = 'path_detalle_articulo_ir'),


    #DETALLE DE UN PRODUCTO CON UNA CLASE (VBC)
    path('detalle/<int:pk>', views.Detalle_Articulo_Ir_Clase.as_view(), name = 'path_detalle_articulo_ir'),

    #ABM
    path('crear/', views.Crear_Articulo_Ir_Clase.as_view(),name = 'path_crear_articulos_ir'),
    path('modificar/<int:pk>', views.Modificar_Articulo_Ir_Clase.as_view(),name = 'path_modificar_articulos_ir'),
    path('Eliminar/<int:pk>', views.Eliminar_Articulo_Ir_Clase.as_view(),name = 'path_eliminar_articulos_ir'),

    #CATEGORIAS
    path('categorias/', views.Listar_Categorias_Ir_Funcion, name = 'path_listar_categorias_ir'),
    path('articulosxcategoria/<int:pk>', views.Filtro_Categoria_Ir, name = 'path_filtrados_categoria_ir'),

]
