from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView

from aplicaciones.compras.forms import PedidoForm
from aplicaciones.compras.models import Pedido

class PedidosListView(ListView):
    template_name = "op/pedido/pedidos.html"
    model = Pedido
    context_object_name = 'pedidos'
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(referencia__producto__icontains=query)
        else:
            return self.model.objects.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/compra/menu'
        context['listar_url'] = '/compra/pedido'
        context['crear_url'] = '/compra/crearpedido'
        context['titulo'] = 'PEDIDOS'
        context['query'] = self.request.GET.get("query") or ""
        return context

class CrearPedido(CreateView):
    model = Pedido
    template_name = "op/pedido/pedidoForm.html"
    success_url = reverse_lazy('compras:pedido')
    form_class = PedidoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/compra/crearpedido/'
        context['titulo'] = 'INGRESO DE PEDIDOS'
        context['url_anterior'] = '/compra/pedidos'
        context['listar_url'] = '/compra/pedidos'
        context['action'] = 'add'
        return context

    # def post(self,request,*args,**kwargs):
    #     data ={}
    #     try:
    #         action = request.POST['action']
    #         if action == 'add':
    #             form = self.get_form()
    #             data = form.save()
    #         else:
    #             data['error'] = 'No has ingresado ninguna opcion'
    #     except Exception as e:
    #         data['error'] =str(e)
    #     return JsonResponse(data, safe=False)



class ActualizarPedido(UpdateView):
    model = Pedido
    template_name = "op/pedido/pedidoForm.html"
    success_url = reverse_lazy('compras:pedido')
    form_class = PedidoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ACTUALIZAR PEDIDO'
        context['url_anterior'] = '/compra/pedidos'
        context['listar_url'] = '/compra/pedidos'
        return context

class EliminarPedido(DeleteView):
    model = Pedido
    template_name = "op/pedido/eliminarPedido.html"
    success_url = reverse_lazy('compras:pedido')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ELMINAR PEDIDO'
        context['url_anterior'] = '/compra/pedidos'
        context['listar_url'] = '/compra/pedidos'
        return context