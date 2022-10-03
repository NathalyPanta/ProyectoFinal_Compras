from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView,UpdateView,DeleteView

from aplicaciones.compras.models import Proveedor
from aplicaciones.compras.forms import ProveedorForm


class ProveedorListView(ListView):
    template_name = 'op/prov/proveedores.html'
    model = Proveedor
    context_object_name = 'proveedores'
    paginate_by = 4

    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(nombre__icontains=query)
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/compra/menu'
        context['listar_url']='/compra/proveedor/'
        context['crear_url']= '/compra/crearprov/'
        context['titulo']='Proveedores'
        context['query']=self.request.GET.get("query")or ""
        return context

class CrearProveedor(CreateView):
    template_name = "op/prov/form_Prov.html"
    model = Proveedor
    success_url = reverse_lazy('compras:proveedor')
    form_class = ProveedorForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/compra/crearprov/'
        context['titulo']='INGRESO DE PROVEEDORES'
        context['url_anterior']='/compra/proveedor'
        context['listar_url']='/compra/proveedor/'
        context['action'] = 'add'
        return context

class ActualizarProveedor(UpdateView):
    model = Proveedor
    template_name = 'op/prov/form_Prov.html'
    success_url = reverse_lazy('compras:proveedor')
    form_class = ProveedorForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ACTUALIZAR PROVEEDOR'
        context['url_anterior']='/compra/proveedor'
        context['listar_url']='/compra/proveedor'
        # context['action']='edit'
        return context

class EliminarProveedor(DeleteView):
    model = Proveedor
    template_name = "op/prov/eliminarPro.html"
    success_url = reverse_lazy('compras:proveedor')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ELMINAR PROVEEDOR'
        context['url_anterior'] = '/compra/proveedor'
        context['listar_url'] = '/compra/proveedor'
        return context