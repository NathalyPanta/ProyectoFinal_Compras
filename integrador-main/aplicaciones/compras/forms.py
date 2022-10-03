from django.db.models.functions import datetime
from django.forms import ModelForm, DateInput, TextInput
from django import forms
from aplicaciones.compras.models import Proveedor, Pedido, RegistroCompra


class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'

        widgets={
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Nombre del Proveedor'}),
            'ruc': forms.TextInput(attrs={'class': 'form-control','placeholder':'0296537341-001'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'zxcv@correo.com'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control','placeholder':'09xxxxxxxx'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control','placeholder':'"Guayaquil"'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese la Dirección'}),
        }

class PedidoForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['referencia'].widget.attrs['autofocus']=True

    class Meta:
        model = Pedido
        fields = '__all__'
        widgets ={
            'referencia': forms.TextInput(attrs={'class': 'form-control'}),
            'proveedor': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(format=('%d/%m/%Y'),
                                     attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha',
                                            'type': 'date'}),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control'}),
            'subtotal': forms.NumberInput(attrs={
                'readonly':True,
                'class': 'form-control'}),
            'iva': forms.NumberInput(attrs={
                'readonly':True,
                'class': 'form-control'}),
            'total': forms.NumberInput(attrs={
                'readonly':True,
                'class': 'form-control'}),

        }



# class PedidoForm(ModelForm):
#     class Meta:
#         model = Pedido
#         fields = '__all__'
#
#         widgets={
#             'referencia': forms.TextInput(attrs={'class': 'form-control'}),
#             'proveedor': forms.Select(attrs={'class': 'form-control'}),
#             'fecha': forms.DateInput(format=('%d/%m/%Y'),
#                attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha', 'type': 'date'}),
#             'producto': forms.TextInput(attrs={'class': 'form-control'}),
#             'marca': forms.TextInput(attrs={'class': 'form-control'}),
#             'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
#             'precio': forms.TextInput(attrs={'class': 'form-control'}),
#             'subtotal': forms.TextInput(attrs={'class': 'form-control'}),
#             'iva': forms.TextInput(attrs={'class': 'form-control'}),
#             'total': forms.TextInput(attrs={'class': 'form-control'}),
#         }

class RegistroCompraForm(ModelForm):
    class Meta:
        model = RegistroCompra
        fields = '__all__'
        exclude= ['usuario']


        widgets={

            # 'registro': forms.TextInput(attrs={'class': 'form-control'}),
            # 'usuario': forms.Select(attrs={'class': 'form-control'}),
            'fecha_registro': forms.DateInput(format=('%d/%m/%Y'),
               attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha', 'type': 'date'}),
            'referencia': forms.Select(attrs={'class': 'form-control'}),
            'producto': forms.TextInput(attrs={'class': 'form-control'}),
            # 'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
            # 'precio': forms.TextInput(attrs={'class': 'form-control'}),
            # 'subtotal': forms.TextInput(attrs={'class': 'form-control'}),
            # 'iva': forms.TextInput(attrs={'class': 'form-control'}),
            # 'total': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={
                'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control'}),
            'subtotal': forms.NumberInput(attrs={
                'readonly': True,
                'class': 'form-control'}),
            'iva': forms.NumberInput(attrs={
                'readonly': True,
                'class': 'form-control'}),
            'total': forms.NumberInput(attrs={
                'readonly': True,
                'class': 'form-control'}),

        }