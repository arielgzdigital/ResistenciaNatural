from django import forms
from .models import ArticuloIr

class FormularioCrearArticuloIr(forms.ModelForm):
	#configurar cada atributo si lo deseo
	#por ejemplo que clase css tiene cada atributo
	class Meta:
		model = ArticuloIr
		fields = ['titulo','descripcion','imagen','categoria_ir']
		
class FormularioModificarArticuloIr(forms.ModelForm):
	class Meta:
		model = ArticuloIr
		fields = ['titulo','descripcion','imagen','categoria_ir']