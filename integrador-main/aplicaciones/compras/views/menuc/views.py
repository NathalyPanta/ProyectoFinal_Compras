from django.shortcuts import render
from django.views import View
# Create your views here.
from django.views.generic import TemplateView


# class Inicio(View):
#     def get(self,request,*args,**kwargs):
#         return render(request,'compra.html',{'titulo':"Inicio",'url_anterior':'/'})
#     # def post(self):
#     # def put(self):
#     # def delete(self):

class ComprasMTemplateView(TemplateView):
    template_name = 'compraMenu.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo']="Compras"
        context['url_anterior']="/"
        return context