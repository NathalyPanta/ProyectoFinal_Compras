from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from aplicaciones.compras.forms import RegistroCompraForm
from aplicaciones.compras.models import RegistroCompra


class RegistroCompraListView(ListView):
    template_name = 'op/registro/registrosCompra.html'
    model = RegistroCompra
    context_object_name = 'registroc'
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(producto__icontains=query)
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_anterior'] = '/compra/menu'
        context['listar_url'] = '/compra/registroc'
        context['crear_url'] = '/compra/crearRegistro/'
        context['titulo'] = 'Registro de Compras'
        context['query'] = self.request.GET.get("query") or ""
        return context

class CrearRegistro(CreateView):
    model = RegistroCompra
    template_name = "op/registro/RegistroCompraForm.html"
    success_url = reverse_lazy('compras:registroc')
    form_class = RegistroCompraForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = '/compra/crearRegistro/'
        context['titulo'] = 'REGISTROS'
        context['url_anterior'] = '/compra/registroc'
        context['listar_url'] = '/compra/registroc'
        context['action'] = 'add'
        return context

class ActualizarRegistro(UpdateView):
    model = RegistroCompra
    template_name = "op/registro/RegistroCompraForm.html"
    success_url = reverse_lazy('compras:registroc')
    form_class = RegistroCompraForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ACTUALIZAR REGISTRO'
        context['url_anterior'] = '/compra/registroc'
        context['listar_url'] = '/compra/registroc'
        return context

class EliminarRegistro(DeleteView):
    model = RegistroCompra
    template_name = "op/registro/eliminarRegistro.html"
    success_url = reverse_lazy('compras:registroc')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'ELMINAR REGISTRO'
        context['url_anterior'] = '/compra/registroc'
        context['listar_url'] = '/compra/registroc'
        return context